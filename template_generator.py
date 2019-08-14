#!/usr/bin/python
# File Name : template_generator.py
# Purpose : Generate a list of templates for sarcastic tweets.
# Creation Date : 10-09-2012
# Last Modified : Thu 11 Oct 2012 04:18:21 PM MDT
# Created By : Nathan Gilbert
#
import sys
import operator

import utils

def useARKPOS(f):
    return utils.readInPOSTags(f)


def useRitterPOS():
    pass

def token2tag(token):
    tokentag = token.split("/")
    return tuple(tokentag)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <tagged_tweets>" % (sys.argv[0])
        sys.exit(1)

    #get pos tags
    tagged_tweets = useARKPOS(sys.argv[1])

    #look at all the sarcastic tweets, select all patterns that can be
    #generated via these tweets
    #how are patterns generated? 
    # a. 1 lexical component, 1 POS tag, 1 variable 
    # => <I> <V> <X>
    # => <X> <love> <N>
    # => <I> <X> <school>
    templates = {}
    for tt in tagged_tweets:
        #print "Working on tweet: {0}".format(num)
        #print tt
        tt_tokens = tt.split()
        #print tt_tokens
        tups = [token2tag(token) for token in tt_tokens]
        #print tups

        #generate the three different kinds of template
        #find where the verbs are
        for i in range(len(tups)):
            if tups[i][1] == "V":
                if i > 0:
                    prev = tups[i-1]
                else:
                    continue

                n=i+1
                if n < len(tups) and tups[n][1] == "N":
                    following = tups[i+1]

                    t1 = "<{0}> <V> <N>".format(prev[0])
                    t2 = "<{0}> <V> <{1}>".format(prev[1], following[0])
                    t3 = "<{0}> <{1}> <{2}>".format(prev[1], tups[i][0], following[0])
                    t4 = "<{0}> <{1}> <{2}>".format(prev[1], tups[i][0],
                            following[0])
                    t5 = "<{0}> <{1}> <{2}>".format(prev[0], tups[i][1],
                            following[0])
                    t6 = "<{0}> <{1}> <{2}>".format(prev[0], tups[i][1],
                            following[1])

                    templates[t1] = templates.get(t1, 0) + 1
                    templates[t2] = templates.get(t2, 0) + 1
                    templates[t3] = templates.get(t3, 0) + 1
                    templates[t4] = templates.get(t4, 0) + 1
                    templates[t5] = templates.get(t5, 0) + 1
                    templates[t6] = templates.get(t6, 0) + 1
                    #new template? <X> <V> <D>* <A>* <N>+ 

    sorted_templates = sorted(templates.iteritems(),
            key=operator.itemgetter(1), reverse=True)

    for st in sorted_templates:
        print "{0} : {1}".format(st[0], st[1])
