'''There is an array with some numbers. All numbers are equal except for one.
Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
This is the first kata in series:
    Find the unique number (this kata)
    Find the unique string
    Find The Unique'''


#First solution
def find_uniq(arr):
    res = sorted(arr)
    return res[-1] if res[0] == res[1] else res[0]

#Second solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr[:3].count(b) > 1 else b

#Third solution
def find_uniq(arr):
    return max(arr) if arr.count(min(arr)) > 1 else min(arr)
