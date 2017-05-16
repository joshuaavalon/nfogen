# Nfo Gen
[![Release](https://img.shields.io/github/release/joshuaavalon/nfogen.svg?style=flat-square&colorB=brightgreen)](https://github.com/joshuaavalon/nfogen/releases)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/joshuaavalon/nfogen/blob/master/LICENSE)

* [Overview](#overview)
* [Usage](#usage)
* [Arguments](#arguments)
   * [Template String](#template-string)

## Overview
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
|`-D`   |`--date`          | start date       |`-D 2017-01-01` | Start date of the nfo file(s) (default: None)        |
|`-m`   |`--mpaa`          | mpaa             |`-m TV-14`      | Common mpaa of all the generate nfo(s)               |
|`-d`   |`--directors`     | directors        |`-d Alex Mary`  | Common director(s) of all the generate nfo(s)        |
|`-w`   |`--writers`       | writers          |`-w Alex Mary`  | Common writer(s) of all the generate nfo(s)          |
|`-i`   |`--increment`     | days             |`-i 7`          | Number of day(s) between each episode (default: 7)   |
|`-S`   |`--start_episode` | start episode    |`-S 1`          | Episode number of the start (inclusive) (default: 1) |
|`-E`   |`--end_episode`   | end episode      |`-E 12`         | Episode number of the end (inclusive) (default: 12)  |
|`-r`   |`--rating`        | rating           |`-r 1.0`        | Common rating(s) of all the generate nfo(s)          |
|`-t`   |`--title`         | title*           |`-t Ep1`        | Common title(s) of all the generate nfo(s)           |
|`-v`   |`--version`       | N/A              |`-v`            | Show the version of the program                      |
|`-h`   |`--help`          | N/A              |`-h`            | Show help of the program                             |

\* Support template string

### Template String
Template string allow using variable in the string for different nfos.

| Variable  | Description                                       |
|-----------|---------------------------------------------------|
| %INDEX%   | Current index in loop. Start from 0.              |
| %EPISODE% | Current episode number.                           |
| %DATE%    | Aired date of current episode. Format: yyyy-mm-dd |
