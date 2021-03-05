'''The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.'''

#First solution
def max_sequence(arr):
    result = counts = 0
    for i in arr:
        counts += i
        if counts < 0:
            counts = 0
        elif result < counts:
            result = counts
    return result

#Second solution
def max_sequence(arr):
    result = 0
    count = 0
    for i in arr:
        count += i
        if count < 0:
            count = 0
        if result < count:
            result = count
    return result
