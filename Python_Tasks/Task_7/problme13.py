# problem 13 : Sherlock and the Valid String
# hackerrank: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    freq = Counter(s)
    values = list(freq.values())
    counts = Counter(values)
    if len(counts) == 1:
        return "YES"
    if len(counts) > 2:
        return "NO"
    first, second = counts.keys()
    if (counts[first] == 1 and (first - 1 == second or first == 1)):
        return "YES"
    if (counts[second] == 1 and (second - 1 == first or second == 1)):
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

