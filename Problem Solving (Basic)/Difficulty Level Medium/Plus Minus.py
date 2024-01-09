# https://www.hackerrank.com/challenges/plus-minus

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pSum, nSum, zSum = 0, 0, 0
    for i in arr:
        if i > 0:
            pSum += 1
        elif i < 0:
            nSum += 1
        else:
            zSum += 1
    pRat, nRat, zRat = round(pSum/len(arr), 6), round(nSum/len(arr), 6), round(zSum/len(arr), 6)
    print(f"{pRat}\n{nRat}\n{zRat}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)