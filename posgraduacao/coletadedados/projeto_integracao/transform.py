# coding: utf-8

import time
import json

from itertools import izip

DATA_FILE = "data/dados_2011.txt"
QUESTIONS_FILE = "data/questions_2011.txt"

"""
 File to read two files line by line simultaneously
"""


def main():
    with open(DATA_FILE) as dados, open(QUESTIONS_FILE) as questions:
        for d, q in izip(dados, questions):
            print ';'.join([
                        d[0:12],
                        d[536:545],
                        d[545:554],
                        d[554:563],
                        d[563:572],
                        d[996:1005],
                        q[47:48],
                        q[15:16],
                        q[16:17]])

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print "Duration: %s" % str(end-start)
