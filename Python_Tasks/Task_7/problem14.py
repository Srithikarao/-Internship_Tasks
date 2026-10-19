# priblem 14 : Anagram
# hackerrank: https://www.hackerrank.com/challenges/anagram/problem

import math
import os
import random
import re
import sys

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    count = 0
    for char in s1:
        if char in s2:
            s2 = s2.replace(char, '', 1)
        else:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
