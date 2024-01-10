# https://www.hackerrank.com/challenges/plus-minus

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