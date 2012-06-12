#!/usr/bin/env python

import os
import sys
import shutil

def convert_to_utf8(filename):
    encodings = ('windows-1253', 'iso-8859-1', 'macgreek')

    try:
        f = open(filename, 'r').read()
    except Exception:
        sys.exit(1)

    for enc in encodings:
        try:
            data = f.decode(enc)
            break
        except Exception:
            if enc == encodings[-1]:
                sys.exit(1)
            continue

    fpath = os.path.abspath(filename)
    newfilename = fpath + '.bak'
    shutil.copy(filename, newfilename)

    f = open(filename, 'w')
    try:
        f.write(data.encode('utf-8'))
    except Exception, e:
        print e
    finally:
        f.close()

if __name__ == '__main__':
    convert_to_utf8(sys.argv[1])

