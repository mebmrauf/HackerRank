# https://www.hackerrank.com/challenges/simple-array-sum

def simpleArraySum(ar):
    return sum(ar)
# OR
def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum+=i
    return sum