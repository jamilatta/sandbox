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

                doc = {'parts': [str(part) for part in case.parts.all()],
                       'total_parts': int(case.parts.all().count()),
                       'client': [str(part) for part in case.parts.all() if part.is_advogated],
                       'value': case.public_value,
                       'descriptors': [str(subject) for subject in case.descriptors.all()],
                       'status': "Inativo" if case.closing_date else "Ativo",
                       'currency': case.currency.currency_name if case.currency else 'Unknown',
                       'type_operation': case.type_operation.operation_name if case.type_operation else 'Unknown'}

                es_conn.index(index='relevcases', doc_type='relevcase', body=doc)

    except Exception as e:
        print e.message
