# https://www.hackerrank.com/challenges/cloudy-day

def maximumPeople(p, x, y, r):
    if len(y) == 1 or len(y) == 0:
        return sum(p) # if there is 1 cloud they can remove it and if it's 0 cloud nothing to remove.
    else:
        sunnyPeople = sum(p)
        for l in range(len(x)): # len(x) or len(p) no of towns
            count = 0
            for c in range(len(y)): # len(y) no of clouds
                if y[c] - r[c] <= x[l] <= y[c] + r[c]:
                    if count == 0:
                        sunnyPeople -= p[l]
                        count+=1
                    break             
        return sunnyPeople

print(maximumPeople([10,100], [5,100], [4], [1]))

#four arrays representing the populations of each town(p),
#locations of the towns(x), locations of the clouds(y),
#and the extents of coverage of the clouds(r).