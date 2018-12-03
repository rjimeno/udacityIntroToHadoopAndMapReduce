#!/usr/bin/env python2

import sys
import csv
from datetime import datetime

def mapper():
    totalDay = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0}
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        date = line[0]
        amount = float(line[4])
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        totalDay[weekday] += amount
    for d in sorted(totalDay.keys()):
        print d, "\t", totalDay[d]

if '__main__' == __name__:
    mapper()