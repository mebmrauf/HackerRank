# https://www.hackerrank.com/challenges/compare-the-triplets

def compareTriplets(a, b):
    aliceSum, bobSum = 0, 0
    for i in range(3):
        if a[i] > b[i]:
            aliceSum += 1
        elif b[i] > a[i]:
            bobSum += 1
    return [aliceSum, bobSum]