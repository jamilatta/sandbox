#!/usr/bin/env python
from tclient import TClient

c = TClient()

terms = ['scielo', 'redescielo', 'SciELO', 'scielo brasil']

print "Get tweets... searching by %s" % terms

c.get_tweets(terms, 10000)

c.save('twitterarchive/repo/scielo.txt')

print "Done!"
