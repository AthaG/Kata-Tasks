'''Complete the function scramble(str1, str2) that returns true if a portion 
of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used(a-z). No punctuation or digits will 
    be included.
    Performance needs to be considered

Input strings s1 and s2 are null terminated.

Examples

scramble('rkqodlw', 'world') == > True
scramble('cedewaraaossoqqyt', 'codewars') == > True
scramble('katas', 'steak') == > False'''


#First solution
def scramble(s1, s2):
    return all(s1.count(char) >= s2.count(char) for char in set(s2))


#Second solution
def scramble(s1, s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True


#Third solution
def scramble(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    cnt = 0
    for char in s1:
        if char == s2[cnt]:
            cnt += 1
            if cnt == len(s2):
                return True
    return False