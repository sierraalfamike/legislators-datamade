#!/usr/bin/env python

import csv
import datetime
import sys
import getopt
import os

def main(args):
    # set default input file as legislators.csv in current directory
    pathToInputFile = os.path.join(os.getcwd(), "legislators.csv")

    # parse CLI arguments
    helpMessage = "\nflags:\n -i, --inputfile <inputfile>\n"
    try:
        opts, args = getopt.getopt(args,"hi:",["inputfile="])
    except getopt.GetoptError:
        print(helpMessage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(helpMessage)
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            pathToInputFile = arg

    # check for input file access
    try:
        open(pathToInputFile, "r")
    except IOError:
        print("Error: input file: \"" + pathToInputFile + "\" not found and \"legislators.csv\" not found in current directory.")
        sys.exit(1)

    # parse and extract data from input file to dictionaries
    entries45 = []
    entriesRepSocial = []
    with open(pathToInputFile, "r") as inputFile:
        inputFileReader = csv.DictReader(inputFile)
        for entry in inputFileReader:
            # calculate time since birthdate
            timedelta = datetime.datetime.today() - datetime.datetime.strptime(entry["birthdate"], '%Y-%m-%d')
            if entry["party"] == "D" and timedelta.days/365 < 45:
                entries45.append(entry)
            if entry["party"] == "R" and entry["twitter_id"] != "" and entry["youtube_url"] != "":
                entriesRepSocial.append(entry)

    # write dictionaries to output files
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    pathToOutputEntries45 = r".\sc_DataMade_45young_"+timestamp+r".csv"
    pathToOutputEntriesRepSocial = r".\sc_DataMade_RepSocial_"+timestamp+r".csv"
    with open(pathToOutputEntries45, "w", newline='') as outputEntries45:
        outputEntries45writer = csv.DictWriter(outputEntries45, fieldnames=entries45[0].keys())
        outputEntries45writer.writeheader()
        outputEntries45writer.writerows(entries45)

    with open(pathToOutputEntriesRepSocial, "w", newline='') as outputEntriesRepSocial:
        outputEntriesRepSocialwriter = csv.DictWriter(outputEntriesRepSocial, fieldnames=entriesRepSocial[0].keys())
        outputEntriesRepSocialwriter.writeheader()
        outputEntriesRepSocialwriter.writerows(entriesRepSocial)

if __name__ == "__main__":
    main(sys.argv[1:])
