#!/usr/bin/env python3

import sys

thisCount = 0
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()
    thisCount += 1
    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", thisCount)
        oldKey = thisKey;
        thisCount = 0

    oldKey = thisKey

if oldKey != None:
    print(oldKey, "\t", thisCount)

