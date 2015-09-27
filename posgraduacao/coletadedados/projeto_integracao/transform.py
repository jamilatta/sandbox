# coding: utf-8

import time
import json

from itertools import izip

"""
 File to read two files line by line simultaneously.

 This script read ENEM dados_2011.txt and questions_2011.txt and output something like this:

    300005366935;330.70;323.70;483.30;486.90;460.00;A;B;D
"""

DATA_FILE = "data/dados_2011.txt"
QUESTIONS_FILE = "data/questions_2011.txt"


def main():
    with open(DATA_FILE) as dados, open(QUESTIONS_FILE) as questions:
        for d, q in izip(dados, questions):

            NU_INS = d[0:12].strip()
            NU_NT_CN = d[536:545].strip()
            NU_NT_CH = d[545:554].strip()
            NU_NT_LC = d[554:563].strip()
            NU_NT_MT = d[563:572].strip()
            NU_NOTA_REDACAO = d[996:1005].strip()
            # Em que escola cursou o ensino médio
            Q33 = q[47:48].strip()
            # Até quando sua pai estudou
            Q02 = q[15:16].strip()
            # Até quando sua mãe estudou
            Q03 = q[15:16].strip()

            if NU_NT_CN != '.' and NU_NT_CH != '.' and NU_NT_LC != '.' and NU_NT_MT != '.' and NU_NOTA_REDACAO != '0.00':
                print ';'.join([
                            d[0:12].strip(),
                            NU_NT_CN,
                            NU_NT_CH,
                            NU_NT_LC,
                            NU_NT_MT,
                            NU_NOTA_REDACAO,
                            Q33,
                            Q02,
                            Q03])

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print "Duration: %s" % str(end-start)
