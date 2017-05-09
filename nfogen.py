import argparse
from datetime import datetime, date, timedelta
from typing import List
from xml import etree
from xml.etree.ElementTree import Element, SubElement, ElementTree, Comment, ProcessingInstruction, _escape_cdata, \
    _escape_attrib, QName

from os import path

"""
Only print metavar once
"""


class HelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ", ".join(action.option_strings) + " " + args_string


def valid_date(date_str: str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: {0}".format(date_str)
        raise argparse.ArgumentTypeError(msg)


def valid_dir(path_str: str):
    if path_str == "" or path.isdir(path_str):
        return path_str
    raise TypeError("{0} is not a directory".format(path_str))


def main():
    args = parse_args()
    if args.start_episode > args.end_episode:
        raise ValueError("Start episode number cannot be greater than end episode number")
    start_date = args.date  # type: date
    for episode_num in range(args.start_episode, args.end_episode + 1):
        index = episode_num - args.start_episode  # type: int
        aired = start_date + timedelta(days=args.increment * index)  # type: date
        root = generate_xml(episode_num=episode_num, aired=aired, directors=args.directors,
                            writers=args.writers, mpaa=args.mpaa)  # type: Element
        file_name = "{0} - s{1:02d}e{2:02d}.nfo".format(args.name, args.season, episode_num)  # type: str
        tree = ElementTree(element=root)  # type: ElementTree
        tree.write(path.join(args.output, file_name), encoding="utf-8", short_empty_elements=False)


def parse_args():
    parser = argparse.ArgumentParser(prog="Nfo Gen", description="Nfo Gen is a script to generate nfo file(s).",
                                     formatter_class=HelpFormatter)
    parser.add_argument("name", type=str)
    parser.add_argument("-o", "--output", type=valid_dir, default="", metavar="<output directory>",
                        help="Output directory of the nfo(s) (default: current)")
    parser.add_argument("-s", "--season", type=int, default=1, metavar="<season number>",
                        help="Season number of the nfo(s) (default: %(default)s)")
    parser.add_argument("-D", "--date", type=valid_date, default=date.today(), metavar="<start date>",
                        help="Start date of the nfo file(s) (default: %(default)s)")
    parser.add_argument("-m", "--mpaa", type=str, default="", metavar="<mpaa>",
                        help="Common mpaa of all the generate nfo(s)")
    parser.add_argument("-d", "--directors", type=str, nargs="+", metavar="<director(s) name>",
                        help="Common director(s) of all the generate nfo(s)")
    parser.add_argument("-w", "--writers", type=str, nargs="+", metavar="<writer(s) name>",
                        help="Common writer(s) of all the generate nfo(s)")
    parser.add_argument("-i", "--increment", type=int, default=7, metavar="<number of day(s)>",
                        help="Number of day(s) between each episode (default: %(default)s)")
    parser.add_argument("-S", "--start_episode", type=int, default=1, metavar="<start episode>",
                        help="Episode number of the start (inclusive) (default: %(default)s)")
    parser.add_argument("-E", "--end_episode", type=int, default=12, metavar="<end episode>",
                        help="Episode number of the end (inclusive) (default: %(default)s)")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.1")
    return parser.parse_args()


def generate_xml(episode_num: int, aired: date, directors: List[str], writers: List[str], mpaa: str) -> Element:
    if writers is None:
        writers = []
    if directors is None:
        directors = []
    root = Element("episodedetails")
    SubElement(root, "title").text = ""
    SubElement(root, "episode").text = str(episode_num)
    SubElement(root, "aired").text = aired.strftime("%Y-%m-%d")
    SubElement(root, "mpaa").text = mpaa
    SubElement(root, "plot").text = ""
    SubElement(root, "director").text = "/".join(directors)
    SubElement(root, "credits").text = "/".join(writers)
    SubElement(root, "rating").text = ""
    return root


"""
HACK
"""


def _serialize_xml(write, elem, qnames, namespaces, short_empty_elements, addintend="  ", intend="", newl="\n",
                   **kwargs):
    tag = elem.tag
    text = elem.text
    if tag is Comment:
        write(intend + "<!--%s-->" % text)
    elif tag is ProcessingInstruction:
        write(intend + "<?%s?>" % text)
    else:
        tag = qnames[tag]
        if tag is None:
            if text:
                write(_escape_cdata(text))
            for e in elem:
                _serialize_xml(write, e, qnames, None, addintend=addintend, intend=addintend + intend, newl=newl,
                               short_empty_elements=short_empty_elements)
        else:
            write(intend + "<" + tag)
            items = list(elem.items())
            if items or namespaces:
                if namespaces:
                    for v, k in sorted(namespaces.items(),
                                       key=lambda x: x[1]):  # sort on prefix
                        if k:
                            k = ":" + k
                        write(" xmlns%s=\"%s\"" % (
                            k,
                            _escape_attrib(v)
                        ))
                for k, v in sorted(items):  # lexical order
                    if isinstance(k, QName):
                        k = k.text
                    if isinstance(v, QName):
                        v = qnames[v.text]
                    else:
                        v = _escape_attrib(v)
                    write(" %s=\"%s\"" % (qnames[k], v))
            if text or len(elem) or not short_empty_elements:
                write(">")
                if text is not None:
                    write(_escape_cdata(text))
                else:
                    write(newl)
                for e in elem:
                    _serialize_xml(write, e, qnames, None, addintend=addintend, intend=addintend + intend, newl=newl,
                                   short_empty_elements=short_empty_elements)
                write("</" + tag + ">" + newl)
            else:
                write(" />" + newl)
    if elem.tail:
        write(_escape_cdata(elem.tail))


etree.ElementTree._serialize_xml = _serialize_xml
etree.ElementTree._serialize["xml"] = _serialize_xml
if __name__ == "__main__":
    main()
