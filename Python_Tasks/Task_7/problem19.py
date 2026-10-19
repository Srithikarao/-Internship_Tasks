# problem 19 : Weighted Uniform Strings
# hackerrank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weights = set()
    previous = ''
    count = 0
    for char in s:
        if char == previous:
            count += 1
        else:
            count = 1
        weight = (ord(char) - ord('a') + 1) * count
        weights.add(weight)
        previous = char
    result = []
    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
