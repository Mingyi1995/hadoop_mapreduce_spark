#!/usr/bin/python

from operator import itemgetter
import sys

class Reducer():

    def __init__(self):
        self.dic = {}

    def reduce(self):
        prev_key, prev_value, count = None, None, 1

        for line in sys.stdin:
            key, value = line.split('- ', 1)
            key = key.strip()

            if prev_key == key:
                if prev_value == value:
                    count += 1
                if prev_value != value:
                    prev_value = value
                    print(key, value, count)
                    count = 1
            else:
                prev_key = key


if __name__ == '__main__':

    rd = Reducer()
    rd.reduce()
