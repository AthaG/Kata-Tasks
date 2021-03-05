'''Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3])  # returns [1, 1, 2, 1, 3, 0, 0]'''

#First solution
def move_zeros(array):
    return sorted(array, key=lambda x: not isinstance(x, bool) and x == 0)

#Second solution
def move_zeros(array):
    result = [i for i in array if isinstance(i, bool) or i != 0]
    return result + (len(array)-len(result)) * [0]

#Third solution
def move_zeros(array):
    result = []
    zeros = 0
    for i in array:
        if repr(i) == '0' or repr(i) == '0.0':
            zeros += 1
        else:
            result.append(i)
    return result + zeros * [0]
