#https://www.hackerrank.com/challenges/a-very-big-sum

def aVeryBigSum(ar):
    return sum(ar)
# OR
def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum+=i
    return sum
