'''A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is,
False if not. Ignore numbers and punctuation.'''


#First solution
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))


#Second solution
import string

def is_pangram(s):
    s = s.lower()
    res = list(string.ascii_lowercase)
    for i in s:
        if i in res:
            res.remove(i)
    return not res
