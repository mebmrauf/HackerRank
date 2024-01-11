# https://www.hackerrank.com/challenges/kangaroo

def kangaroo(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return "YES"
    elif v1 != v2 and (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    else:
        return "NO"

# (x2 - x1) % (v1 - v2) == 0
# it ensures they will land on the same position after the same number of jumps.   
# (x2 - x1) / (v1 - v2) >= 0 ;
# it ensures that the kangaroo with the higher starting position is not moving in the opposite direction 
# and makes sure they will meet in the positive direction on the number line.