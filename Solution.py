#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonal1 = []
    diagonal2 = []
    i = 0
    for x in arr:
        diagonal1.append(x[i])
        i += 1
    i = len(arr[0]) - 1
    for x in arr:
        diagonal2.append(x[i])
        i -= 1
    return abs(sum(diagonal1) - sum(diagonal2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
