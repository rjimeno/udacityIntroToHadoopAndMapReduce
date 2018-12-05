#!/usr/bin/env python2

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"',
                        quoting=csv.QUOTE_ALL)
    #output = [None, None, None, None,
    #          None, None, None, None,
    #          None, None, None, None, None]
    output = []
    for line in reader:
        if 6 == len(line):
            output[9:13] = line[1:5]
        elif 10 == len(line):
            output[0:10] = line[0:10]
        else:
            continue
        writer.writerow(output)

        if output and output[0] != line[0]:
            output[0] = line[0]
            continue


if '__main__' == __name__:
    reducer()
