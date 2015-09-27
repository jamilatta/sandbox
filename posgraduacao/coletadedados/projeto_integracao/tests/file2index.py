# coding: utf-8

import time
import json

from SolrAPI import Solr

DATA_FILE = "data/dados_2011.txt"


def main():

    solr = Solr('http://localhost:8080/solr/nem', timeout=30)

    solr.delete('*:*')
    data_list = []

    for count, line in enumerate(open(DATA_FILE)):

        d = {'id': line[0:12], 'text': line[536: 545]}
        data_list.append(d)
        print count

        if len(data_list) == 10000:
            print "Sending..."
            solr.update(json.dumps(data_list), headers={'Content-Type': 'text/json'})
            print "Commiting..."
            solr.commit()
            #Clean data_list
            data_list = []

    solr.optimize()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print "Duration: %s" % str(end-start)

