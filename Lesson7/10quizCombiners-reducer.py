#!/usr/bin/env python2

import sys

totalDay = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
count = [0, 0, 0, 0, 0, 0, 0]

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWeekDay = int(data_mapped[0])
    thisSale = float(data_mapped[1])

    totalDay[thisWeekDay] += float(thisSale)
    count[thisWeekDay] += 1
    #print >> sys.stderr, thisWeekDay, ': ', count[thisWeekDay]
for d in range(0, 6):
    print d, "\t", int(totalDay[d] / count[d])

