'''Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.'''


#First solution
def get_count(input_str):
    return sum(1 for i in input_str if i in 'aeiou')

#Second solution
def get_count(input_str):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in input_str:
        if i in vowels:
            num_vowels += 1
    return num_vowels
