#!/usr/bin/python
# File Name : baseline_feature_generator.py
# Purpose :
# Creation Date : 09-18-2012
# Last Modified : Tue 02 Oct 2012 04:53:17 PM MDT
# Created By : Nathan Gilbert
#
import sys
import utils
import operator

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <tweets> <outfile>" % (sys.argv[0])
        sys.exit(1)

    unigrams = {}
    tok = utils.Tokenizer(preserve_case=False)
    with open(sys.argv[1], 'r') as inFile:
        for tweet in inFile:
            #each line is a tweet
            tweet = tweet.strip()

            #split the words
            tokens = tok.tokenize(tweet)

            #print tokens
            for t in tokens:
                unigrams[t] = unigrams.get(t, 0) + 1

    #print len(unigrams.keys())
    features = map(lambda x : x[0], sorted(unigrams.iteritems(), key=operator.itemgetter(1), reverse=True))

    data_set = []
    with open(sys.argv[1], 'r') as inFile:
        for tweet in inFile:
            tweet = tweet.strip()
            tokens = tok.tokenize(tweet)

            values = {}
            for t in tokens:
                feature = features.index(t) + 1
                values[str(feature)] = values.get(str(feature), 0) + 1

            ff = ""
            for key in values.keys():
                ff += "{0}:{1} ".format(key, values[key])
            data_set.append(ff)
            #print values

    with open(sys.argv[2], 'w') as outFile:
        for line in data_set:
            outFile.write(line+'\n')

