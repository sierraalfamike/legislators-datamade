# Intro
 
This is part one of the code challenge for DataMade. The task is to use a [csv file](http://unitedstates.sunlightfoundation.com/legislators/legislators.csv) and output the following information:
1. First spreadsheet: All Democrats who are younger than 45 years old
2. Second spreadsheet: All Republicans who have Twitter accounts and YouTube channels

# Usage

The task is done with a simple Python script named `datamade_01.py`. It can be run like a typical Python script:

## On Windows
```
> python.exe .\datamade_01.py -h

flags:
 -i, --inputfile <inputfile>

```
## On Linux/BSD/*nix
```
> ./datamade_01.py -h

flags:
 -i, --inputfile <inputfile>

```

The script will look for a `legislator.csv` file in the current directory and, if specified, it will use a file specified with the `-i` or `--inputfile` flags.

# Approach of the script
The script parses each line of the csv file into a `dict` for convenience, using the first line as the field names. After that, it's a matter of checking for the conditions as specified. The results are stored in a couple of  `list` objects and written out to the filesystem at the end.