'''Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.'''


#First solution
def find_it(seq):
    count = 0
    for i in seq:
        count ^= i
    return count

#Second solution
def find_it(seq):
    bin = dict()

    for i in seq:
        if i not in bin:
            bin[i] = 0
        bin[i] += 1

    for k, v in bin.items():
        if v % 2 == 1:
            return k

#Third solution
def find_it(seq):
    return max([i for i in seq if seq.count(i) % 2 == 1])
