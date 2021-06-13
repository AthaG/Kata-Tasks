'''Given three arrays of integers, return the sum of elements that are common in all 
three arrays.

For example:
common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays

More examples in the test cases.
Good luck!'''


#First solution
from collections import Counter

def common(a, b, c):
    return sum((Counter(a) & Counter(b) & Counter(c)).elements())

#Second solution
def common(a, b, c):
    a.sort()
    b.sort()
    c.sort()
    d, e, f = 0, 0, 0
    count = 0
    while d < len(a) and e < len(b) and f < len(c):
        if a[d] == b[e] == c[f]:
            count += a[d]
            d += 1
            e += 1
            f += 1
        elif a[d] < b[e]:
            d += 1
        elif b[e] < c[f]:
            e += 1
        else:
            f += 1
    return count
