# https://www.hackerrank.com/challenges/divisible-sum-pairs

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in ar[i+1:]:
            if (ar[i]+j)%k == 0:
                count+=1
    return count