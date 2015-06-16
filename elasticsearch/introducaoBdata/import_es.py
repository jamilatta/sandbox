#!/usr/bin/python
# coding: utf-8

import sys, os, csv

from elasticsearch import Elasticsearch


if len(sys.argv) == 1:
    print "Type the import file name, example: python import_es.py c:/data.csv"
else:

    filename = sys.argv[1]

    es_conn = Elasticsearch('http://localhost:9200')

    try:
        # Create a csv file
        with open(filename, 'r') as fpcsv:
            fp = csv.reader(fpcsv, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

            print "Processing, please take a while...."

            for row in fp:

                doc = {'parts': row[0],
                       'total_parts': int(len(row[0].split('##'))),
                       'client': row[1],
                       'value': row[2],
                       'descriptors': row[3].split('##') ,
                       'status': row[4],
                       'currency': row[5],
                       'type_operation': row[6]}

                es_conn.index(index='relevcases', doc_type='relevcase', body=doc)

    except Exception as e:
        print e.message
