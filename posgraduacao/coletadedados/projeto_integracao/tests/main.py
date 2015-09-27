# coding: utf-8

import time
import json

DATA_FILE = "data/dados_2011.txt"
QUESTIONS_FILE = "data/questions_2011.txt"


def main():

    for line in open(QUESTIONS_FILE):
        print line[0:12]

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print "Duration: %s" % str(end-start)

