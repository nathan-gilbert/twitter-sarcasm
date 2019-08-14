#!/usr/bin/python
# File Name : negative_word_feature_generator.py
# Purpose :
# Creation Date : 09-19-2012
# Last Modified : Wed 19 Sep 2012 11:10:19 AM MDT
# Created By : Nathan Gilbert
#
import sys

import utils

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <tweetlist>" % (sys.argv[0])
        sys.exit(1)

    FEAT_NAME = "neg_word"

    #the negative words 
    negative_word_lists = [
            "word_lists/negative_adjectives.txt",
            "word_lists/negative_feeling_words.txt",
            "word_lists/negative_financial_words.txt",
            "word_lists/negative_seeds.txt",
            "word_lists/negative_words.txt"
            ]

    negative_phrases = []
    for wl in negative_word_lists:
        with open(wl, 'r') as nwl:
            for line in nwl:
                if line.startswith("#"):
                    continue
                line = line.strip()
                if line not in negative_phrases:
                    negative_phrases.append(line)

    tok = utils.Tokenizer()
    with open(sys.argv[1], 'r') as tweetList:
        for line in tweetList:
            line=line.strip()

            #print line
            tokens = tok.tokenize(line)
            new_line  = ' '.join(tokens)
            negative_count = 0
            for phrase in negative_phrases:
                if new_line.find(phrase) > -1:
                    negative_count += 1

            if negative_count > 0:
                print "{0}:{1}".format(FEAT_NAME, negative_count)
            else:
                print "  "
