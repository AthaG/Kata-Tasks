'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.'''


#First solution
def find_short(s):
    return len(min(s.split(), key=len))

#Second solution
def find_short(s):
    l = [len(c) for i, c in enumerate(s.split(' '))]
    return min(l)  # l: shortest word length
