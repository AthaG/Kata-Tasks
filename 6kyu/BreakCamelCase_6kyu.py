'''Complete the solution so that the function will break up camel casing, using a 
space between words.
Example:
    "camelCasing"  =>  "camel Casing"
    "identifier"   =>  "identifier"
    ""             =>  ""'''


def solution(s):
    res = []
    for char in s:
        if char.isupper():
            res.append(' ' + char)
        else:
            res.append(char)
    return ''.join(res)
