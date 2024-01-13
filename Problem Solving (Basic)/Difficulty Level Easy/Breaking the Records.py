# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

def breakingRecords(scores):
    minCount, maxCount, minR, maxR = 0, 0, scores[0], scores[0]
    for i in scores[1:]:
        if i > maxR:
            maxCount+=1
            maxR = i
        elif i < minR:
            minCount += 1
            minR = i
    return [maxCount, minCount]