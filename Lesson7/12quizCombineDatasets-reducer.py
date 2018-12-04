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
    output = [None, None, None, None,
              None, None, None, None,
              None, None, None, None, None]
    for line in reader:
        if 10 == line[1]:
            output[9] = line[1]
            output[10] = line[2]
            output[11] = line[3]
            output[12] = line[4]
        elif 20 == line[1]:
            output[0:9] = line[0:9]
        else:
            continue
        writer.writerow(output)


if '__main__' == __name__:
    reducer()
