# problem 19: Company Logo
# hackerrank: https://www.hackerrank.com/challenges/most-commons/problem
import math
import os
import random
import re
import sys
from collections import Counter
if __name__ == '__main__':
    s = input()
    chars = Counter(s).items()
    for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
        print(char, n)
