# problem 15 : Game of Thrones - I
# hackerank: https://www.hackerrank.com/challenges/game-of-thrones/problem

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
