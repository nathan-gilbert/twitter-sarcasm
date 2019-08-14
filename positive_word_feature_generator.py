#!/usr/bin/python
# File Name : positive_word_feature_generator.py
# Purpose :
# Creation Date : 09-19-2012
# Last Modified : Wed 19 Sep 2012 01:20:59 PM MDT
# Created By : Nathan Gilbert
#
import sys

import utils

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <tweetlist>" % (sys.argv[0])
        sys.exit(1)

    FEAT_NAME = "pos_word"

    #the positive words 
    positive_word_lists = [
            "word_lists/positive_phrases.txt",
            ]

    positive_phrases = []
    for wl in positive_word_lists:
        with open(wl, 'r') as nwl:
            for line in nwl:
                if line.startswith("#"):
                    continue
                line = line.strip()
                if line not in positive_phrases:
                    positive_phrases.append(line)

    tok = utils.Tokenizer()
    with open(sys.argv[1], 'r') as tweetList:
        for line in tweetList:
            line=line.strip()

            #print line
            tokens = tok.tokenize(line)
            new_line  = ' '.join(tokens)
            positive_count = 0
            for phrase in positive_phrases:
                if new_line.find(phrase) > -1:
                    positive_count += 1

            if positive_count > 0:
                print "{0}:{1}".format(FEAT_NAME, positive_count)
            else:
                print "  "
