#!/usr/bin/env python2

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    d = {}
    for line in reader:
        word, node = line
        d.setdefault(word, []).append(node)
    for w in d:
        d[w].sort()
        print w, '\t', len(d[w]), '\t', '\t'.join(d[w])

if '__main__' == __name__:
    reducer()
