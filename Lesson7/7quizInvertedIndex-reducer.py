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
        size = len(d[w])
        s = set(d[w])
        l = list(s)
        l.sort()
        print w, '\t', size, '\t', '\t'.join(l)

if '__main__' == __name__:
    reducer()
