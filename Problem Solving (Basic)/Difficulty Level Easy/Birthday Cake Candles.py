# https://www.hackerrank.com/challenges/birthday-cake-candles

def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)