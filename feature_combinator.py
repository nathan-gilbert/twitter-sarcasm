#!/usr/bin/python
# File Name : feature_combinator.py
# Purpose : Takes 2 features, where each line corresponds to a tweet and
# combines them...
# Creation Date : 09-19-2012
# Last Modified : Wed 19 Sep 2012 11:02:48 AM MDT
# Created By : Nathan Gilbert
#
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <first-feature-file> <second-feature-file>" % (sys.argv[0])
        sys.exit(1)

    feat1 = []
    with open(sys.argv[1], 'r') as feat1file:
        feat1.extend(feat1file.readlines())

    feat2 = []
    with open(sys.argv[2], 'r') as feat2file:
        feat2.extend(feat2file.readlines())

    if len(feat1) != len(feat2):
        sys.err.write("Error: files different lengths.")
        sys.exit(1)

    length = len(feat1)
    for i in range(0, length):
        print "{0} {1}".format(feat1[i].strip(), feat2[i].strip())

