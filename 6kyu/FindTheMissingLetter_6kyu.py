'''#Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input 
and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter 
be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:
['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"

(Use the English alphabet with 26 letters!)
Have fun coding it and please don't forget to vote and rank this kata!'''


def find_missing_letter(chars):
    res = list(range(ord(chars[0]), ord(chars[-1])))
    for c in res:
        if chr(c) not in chars:
            return chr(c)
