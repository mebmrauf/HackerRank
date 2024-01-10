# https://www.hackerrank.com/challenges/diagonal-difference

def diagonalDifference(arr):
    pSum, sSum = 0, 0
    for i in range(len(arr)):
        pSum += arr[i][i]
        sSum += arr[i][len(arr)-1-i]
    return abs(pSum-sSum)