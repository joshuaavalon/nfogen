# Nfo Gen
[![Release](https://img.shields.io/github/release/joshuaavalon/nfogen.svg?style=flat-square&colorB=brightgreen)](https://github.com/joshuaavalon/nfogen/releases)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/joshuaavalon/nfogen/blob/master/LICENSE)

Nfo Gen is a script to generate nfo file(s). It is designed to be used by plex agent [XBMCnfoTVImporter](https://github.com/gboudreau/XBMCnfoTVImporter.bundle).

## Usage
```bash
$ python nfogen.py <show name> [arguments]
```

## Arguments
| Short | Long             | Argument(s)      | Example        | Description                                          |
|-------|------------------|------------------|----------------|------------------------------------------------------|
|`-o`   |`--output`        | output directory |`-o dir/`       | Output directory of the nfo(s) (default: current)    |
|`-s`   |`--season`        | season number    |`-s 1`          | Season number of the nfo(s) (default: 1)             |
|`-D`   |`--date`          | start date       |`-D 2017-01-01` | Start date of the nfo file(s) (default: today)       |
|`-m`   |`--mpaa`          | mpaa             |`-m TV-14`      | Common mpaa of all the generate nfo(s)               |
|`-d`   |`--directors`     | directors        |`-d Alex Mary`  | Common director(s) of all the generate nfo(s)        |
|`-w`   |`--writers`       | writers          |`-w Alex Mary`  | Common writer(s) of all the generate nfo(s)          |
|`-i`   |`--increment`     | days             |`-i 7`          | Number of day(s) between each episode (default: 7)   |
|`-S`   |`--start_episode` | start episode    |`-S 1`          | Episode number of the start (inclusive) (default: 1) |
|`-E`   |`--end_episode`   | end episode      |`-E 12`         | Episode number of the end (inclusive) (default: 12)  |
|`-v`   |`--version`       | N/A              |`-v`            | Show the version of the program                      |
|`-h`   |`--help`          | N/A              |`-h`            | Show help of the program                             |
