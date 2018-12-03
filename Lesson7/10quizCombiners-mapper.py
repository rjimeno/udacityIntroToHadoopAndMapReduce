#!/usr/bin/env python2

import sys
import csv
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        date = line[0]
        amount = line[4]
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print weekday, '\t', amount

if '__main__' == __name__:
    mapper()