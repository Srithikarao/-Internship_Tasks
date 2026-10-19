# problem 9 : Beautiful Binary String
# hackerrank: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    blist = list(b)
    count = 0
    i = 0    
    while i < len(blist) - 2:
        if blist[i] == '0' and blist[i+1] == '1' and blist[i+2] == '0':
            count += 1
            blist[i+2] = '1'
            i += 3
        else:
            i += 1       
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
