#!/usr/bin/env python
from tclient import TClient

client = TClient()

terms = ['somatic', 'embryogenesis']

print "Get tweets... searching by %s" % terms

client.get_tweets(terms, 100000000)

client.save('twitterarchive/repo/somatic_embryogenesis.txt')

print "Done!"
