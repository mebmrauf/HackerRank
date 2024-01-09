# https://www.hackerrank.com/challenges/mini-max-sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    lst = []
    for i in range(5):
        xum = sum(arr[:i]) + sum(arr[i+1:])
        lst.append(xum)
    print(min(lst), max(lst))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)