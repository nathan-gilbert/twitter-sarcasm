#!/usr/bin/python
# File Name : convert_annots.py
# Purpose :
# Creation Date : 09-18-2012
# Last Modified : Tue 18 Sep 2012 02:13:17 PM MDT
# Created By : Nathan Gilbert
#
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <first-argument>" % (sys.argv[0])
        sys.exit(1)


    with open(sys.argv[1], 'r') as inFile:
        for line in inFile:
            line=line.strip()

            if line.startswith("NOT_"):
                print "-1"
            else:
                print "+1"
