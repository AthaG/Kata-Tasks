'''Given a positive number n > 1 find the prime factor decomposition of n. 
The result will be a string with the following form:

"(p1**n1)(p2**n2)...(pk**nk)"

where a ** b means a to the power of b

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"'''


def primeFactors(n):
    numList = []
    i = 2
    while i <= n:
        if n % i == 0:
            numList.append(i)
            n /= i
        else:
            i += 1
    result = ''
    i = 0
    while i < len(numList):
        repeat = numList.count(numList[i])
        if repeat > 1:
            result += f'({numList[i]}**{repeat})'
            i += repeat
        else:
            result += f'({numList[i]})'
            i += repeat
    return result
