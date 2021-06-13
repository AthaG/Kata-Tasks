'''An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an
isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case'''


#First solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))

#Second solution
def is_isogram(string):
    return len(set(string.lower())) == len(string.lower())

#Third solution
def is_isogram(string):
    return len([string.count(i) for i in string.lower()]) == len(set(string.lower()))
