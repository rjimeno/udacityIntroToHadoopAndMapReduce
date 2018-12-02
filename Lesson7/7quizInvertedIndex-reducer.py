#!/usr/bin/env python2

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    d = {}
    for line in reader:
        print line
        word, node = line
        d.setdefault(word, []).append(node)
    for w in d:
        print w, '\t', '\t'.join(d[w])
    return d

if '__main__' == __name__:
    d = reducer()
