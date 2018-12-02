#!/usr/bin/env python2

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        break # This is one way to get ride of the top line with headers.
    d = {}
    for line in reader:
        #l = re.split(
        #    r'"\t? ?"',
        #    line)
        #l[0] = re.sub(r'^"', '', l[0])
        #l[-1] = re.sub(r'"\r\n$', '', l[-1])
        #id = l[0]
        #body = re.sub(
        #    r'\t|\r|\n|\.|,|!|\?|:|;|"|\(|\)|<|>|\[|\]|#|$|=|-|/',
        #    ' ',
        #    l[4]).strip()
        #words = re.split(r' ', body)
        words = re.split(
            '\s*[,.!?:;"()<>\[\]#$=\-/\s]+\s*',
            line[4].lstrip().lower() + ' '
        )
        for w in words:
            #d.setdefault(w, []).append(id)
            print w, '\t', line[0]
    return d

if '__main__' == __name__:
    mapper()
