#!/usr/bin/env python
from tclient import TClient

client = TClient()

terms = ['scielo', 'redescielo', 'SciELO', 'scielo brasil']

print "Get tweets... searching by %s" % terms

client.get_tweets(terms, 100000000)

client.save('twitterarchive/repo/scielo.txt')

print "Done!"
