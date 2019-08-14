#!/usr/bin/python
# File Name : template_matcher.py
# Purpose :
# Creation Date : 10-09-2012
# Last Modified : Thu 11 Oct 2012 04:33:50 PM MDT
# Created By : Nathan Gilbert
#
import sys
import utils

def useARKPOS(f):
    return utils.readInPOSTags(f)

def token2tag(token):
    tokentag = token.split("/")
    return tuple(tokentag)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <template_file> <tagged_tweets>" % (sys.argv[0])
        sys.exit(1)

    templates = []
    with open(sys.argv[1], 'r') as template_file:
        templates.extend(template_file.readlines())

    template_map = {}
    for t in templates:
        tokens = t.split(":")
        template_map[tokens[0].strip()] = []
    tagged_tweets = useARKPOS(sys.argv[2])

    templates = {}
    for tt in tagged_tweets:
        output_line = []
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

                    if t1 in template_map.keys():
                    #    template_map[t1].append("{0} {1} {2}".format(prev[0],
                    #        tups[i][0], following[0]))
                        output_line.append("9001:1")

                    if t2 in template_map.keys():
                        output_line.append("9002:1")
                    #    template_map[t2].append("{0} {1} {2}".format(prev[0],
                    #        tups[i][0], following[0]))
                    if t3 in template_map.keys():
                        output_line.append("9003:1")
                    #    template_map[t3].append("{0} {1} {2}".format(prev[0],
                    #        tups[i][0], following[0]))
                    if t4 in template_map.keys():
                        output_line.append("9004:1")
                    if t5 in template_map.keys():
                        output_line.append("9005:1")
                    if t6 in template_map.keys():
                        output_line.append("9006:1")
        print ' '.join(output_line)
    #for key in template_map.keys():
    #    print key
    #    print template_map[key]
