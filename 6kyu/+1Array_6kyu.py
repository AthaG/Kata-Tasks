'''Given an array of integers of any length, return an array that has 1 added to the 
value represented by the array.
    the array can't be empty
    only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples:
    For example the array [2, 3, 9] equals 239, adding one would return the array 
    [2, 4, 0].

    [4, 3, 2, 5] would return [4, 3, 2, 6]'''


def up_array(arr):
    if len(arr) == 0:
        return None
    for i, a in enumerate(arr):
        if arr[0] == 0 and len(arr) > 1:
            arr.remove(0)
        elif a < 0 or a >= 10:
            return None
    arr = ''.join(map(str, arr))
    arr = int(arr)+1
    return list(map(int, str(arr)))
