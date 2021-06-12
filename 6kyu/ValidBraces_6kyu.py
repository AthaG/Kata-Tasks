'''Write a function that takes a string of braces, and determines if the order of the 
braces is valid. It should return true if the string is valid, and false if it's 
invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: 
brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and 
curly braces: ()[]{}.
What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
Examples:
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False'''


#First solution
def validBraces(string):
    y = 0
    for i, c in enumerate(string):
        if c == '(' and string[i+1::2].find(')') >= 0:
            y += 1
        if c == '[' and string[i+1::2].find(']') >= 0:
            y += 1
        if c == '{' and string[i+1::2].find('}') >= 0:
            y += 1
    return y == len(string)/2

#Second solution
def validBraces(string):
    y = 0
    for i, c in enumerate(string):
        if c == '(' and string[i+1::2].find(')') >= 0:
            y += 1
        if c == '[' and string[i+1::2].find(']') >= 0:
            y += 1
        if c == '{' and string[i+1::2].find('}') >= 0:
            y += 1
    return True if y == len(string)/2 else False
