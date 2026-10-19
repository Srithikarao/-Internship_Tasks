# problem 12: Making Anagrams
# hackerrank: https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys

def makingAnagrams(s1, s2):
    count = 0
    for char in "abcdefghijklmnopqrstuvwxyz":
        count += abs(s1.count(char) - s2.count(char))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
