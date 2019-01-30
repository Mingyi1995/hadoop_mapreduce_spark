#!/usr/bin/python

import sys
import csv
# initialize the iteration
iteration = 0
# nullify all the values
currentCountry = None
previousCountry = None
currentFx = None
percentChange = None
currentKey = None

fxMap = []

with open(sys.argv[1], 'r') as file:
    for line in file:
        if line.startswith("Date"):
            continue
        else:
            words = line.strip().split(',')
            if len(words) != 3 or len(words[2]) == 0:
                continue
            else:
                currentCountry = words[1]
                currentFx = float(words[2])

                if currentCountry != previousCountry:
                    previousCountry = currentCountry
                    previousFx = currentFx
                    previousLine = line
                    continue

                elif currentCountry == previousCountry:
                    percentChange = ((currentFx - previousFx) / previousFx) * 100.00
                    currentKey = (currentCountry, percentChange)
                    fxMap.append(currentKey)

                previousCountry = currentCountry
                previousFx = currentFx
                previousLine = line

    for i in sorted(fxMap):
        print("%-20s - %f" % (i[0], i[1]))
