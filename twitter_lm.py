#!/usr/bin/python
# File Name : twitter_lm.py
# Purpose : Develop language models of twitter data. 
# Creation Date : 05-04-2012
# Last Modified : Wed 10 Oct 2012 01:58:17 PM MDT
# Created By : Nathan Gilbert
#
import sys
import nltk
import nltk.data
import glob

import utils
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.corpus import PlaintextCorpusReader
from ngram import NgramModel

def process_tweets(tweets):
    uni,bi,tri = [],[],[]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <corpus-root> <tweets-file>" % (sys.argv[0])
        sys.exit(1)

    corpus_root = sys.argv[1]
    estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
    ignored_words = nltk.corpus.stopwords.words('english')

    pos_movie_reviews = PlaintextCorpusReader(corpus_root+"/pos", ".*\.txt")
    neg_movie_reviews = PlaintextCorpusReader(corpus_root+"/neg", ".*\.txt")

    print "Corpora built."

    pos_unigram_lm = NgramModel(1, pos_movie_reviews.words(), estimator)
    print "Positive unigram model complete."
    pos_bigram_lm = NgramModel(2, pos_movie_reviews.words(), estimator)
    print "Positive bigram model complete."
    #pos_trigram_lm = NgramModel(3, pos_movie_reviews.words(), estimator)


    neg_unigram_lm = NgramModel(1, neg_movie_reviews.words(), estimator)
    print "Negative unigram model complete."
    neg_bigram_lm = NgramModel(2, neg_movie_reviews.words(), estimator)
    print "Negative bigram model complete."
    #neg_trigram_lm = NgramModel(3, neg_movie_reviews.words(), estimator)

    #read in the tweets
    tweets = []
    tokenizer = utils.Tokenizer()

    neg_review_higher = 0
    pos_review_higher = 0
    with open(sys.argv[2], 'r') as tweets_file:
        tweets.extend(tweets_file.readlines())
        for tweet in tweets:
            tokens = tokenizer.tokenize(tweet)
            pu = pos_unigram_lm.perplexity(tokens)
            nu = neg_unigram_lm.perplexity(tokens)

            pb = pos_bigram_lm.perplexity(tokens)
            nb = neg_bigram_lm.perplexity(tokens)

            #pt = pos_trigram_lm.perplexity(tokens)
            #nt = neg_trigram_lm.perplexity(tokens)

            #print pu, nu, pb, nb, pt, nt
            #print pu, nu

            line = ""
            if pu > nu:
                pos_review_higher += 1
                line += "9002:1"
            else:
                line += "9003:1"
                neg_review_higher += 1

            if pb > nb:
                line += " 9004:1"
            else:
                line += " 9005:1"

            print line
    #print "Positive reviews with higher perplexity: {0}".format(pos_review_higher)
    #print "Negative reviews with higher perplexity: {0}".format(neg_review_higher)
