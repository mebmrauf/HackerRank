# https://www.hackerrank.com/challenges/staircase

def staircase(n):
    for i in range(n):
        print(f"{' '*(n-1-i)}{'#'*(1+i)}")