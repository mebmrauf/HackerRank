# https://www.hackerrank.com/challenges/apple-and-orange

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [apple+a for apple in apples]
    oranges = [orange+b for orange in oranges]
    apples = [apple for apple in apples if s<=apple<=t]
    oranges = [orange for orange in oranges if s<=orange<=t]
    print(f"{len(apples)}\n{len(oranges)}")