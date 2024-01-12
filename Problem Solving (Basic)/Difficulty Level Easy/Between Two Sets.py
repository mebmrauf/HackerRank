# https://www.hackerrank.com/challenges/between-two-sets

def getTotalX(a, b):
    min_b = min(b)

    lcm_a = 1
    for num in a:
        lcm_a = lcm(lcm_a, num)

    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = gcd(gcd_b, num)

    count = 0
    current_multiple = lcm_a

    while current_multiple <= min_b:
        if gcd_b % current_multiple == 0:
            count += 1
        current_multiple += lcm_a

    return count
    
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)