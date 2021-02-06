#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0;
    neg = 0;
    zer = 0;
    total = 0;
    for x in arr:
        total += 1
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zer += 1
    print(str(round(pos / total, 6)))
    print(str(round(neg / total, 6)))
    print(str(round(zer / total, 6)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
