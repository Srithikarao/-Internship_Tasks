# problem 17: Separate the Numbers
# hackerrank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

import math
import os
import random
import re
import sys


def separateNumbers(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        first = s[:i]
        num = int(first)
        if first[0] == '0':
            continue
        expected = ""
        while len(expected) < length:
            expected += str(num)
            num += 1
        if expected == s:
            print("YES", first)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
