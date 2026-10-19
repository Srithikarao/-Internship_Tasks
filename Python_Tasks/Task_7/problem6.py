# problem 6 : Pangrams
# hackerrank : https://www.hackerrank.com/challenges/pangrams/problem
import math
import os
import random
import re
import sys


def pangrams(s):
    unique_letters = set(c.lower() for c in s if c.isalpha())
    if len(unique_letters) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()

