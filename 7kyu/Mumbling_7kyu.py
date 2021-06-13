'''This time no story, no theory. The examples below show you how to write function 
accum:

Examples:
    accum("abcd") -> "A-Bb-Ccc-Dddd"
    accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.'''


#First solution
def accum(s):
    return '-'.join((c * (i+1)).capitalize() for i, c in enumerate(s))

#Second solution
def accum(s):
    s = list(s)
    x = 0
    for i in s:
        s[x] = (i * (x+1)).title()
        x += 1
    return '-'.join(s)
