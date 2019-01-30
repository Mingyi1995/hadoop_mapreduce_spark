#!/usr/bin/python

import sys
import csv


class Mapper():
    # mapper class initialization
    def __init__(self):
        self.iteration = 0
        self.currentCountry = None
        self.previousCountry = None
        self.currentFx = None
        self.percentChange = None
        self.currentKey = None
        self.fxMap = []
        #self.f = filename


    def map(self):
        # mapping from reading

        file = sys.stdin
        for line in file:
            if line.startswith("Date"):
                continue
            else:
                words = line.strip().split(',')
                if len(words) != 3 or len(words[2]) == 0:
                    continue
                else:
                    self.currentCountry = words[1]
                    self.currentFx = float(words[2])

                    if self.currentCountry != self.previousCountry:
                        self.previousCountry = self.currentCountry
                        self.previousFx = self.currentFx
                        self.previousLine = line
                        continue

                    elif self.currentCountry == self.previousCountry:
                        self.percentChange = ((self.currentFx - self.previousFx) / self.previousFx) * 100.00
                        self.currentKey = (self.currentCountry, self.percentChange)
                        self.fxMap.append(self.currentKey)

                    self.previousCountry = self.currentCountry
                    self.previousFx = self.currentFx
                    self.previousLine = line

        for i in sorted(self.fxMap):
            print("%s - %.2f%%" % (i[0], i[1]))


if __name__ == '__main__':
    mp = Mapper()
    mp.map()
