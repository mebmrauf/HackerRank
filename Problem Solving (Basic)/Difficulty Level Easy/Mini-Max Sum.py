# https://www.hackerrank.com/challenges/mini-max-sum

def miniMaxSum(arr):
    lst = []
    for i in range(5):
        xum = sum(arr[:i]) + sum(arr[i+1:])
        lst.append(xum)
    print(min(lst), max(lst))