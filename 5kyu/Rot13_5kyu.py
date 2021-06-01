'''ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should
be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.'''


#First solution
def rot13(message):
    return ''.join(chr((65 if char.isupper() else 97) + ((ord(char) - (65 if char.isupper() else 97)) + 13) % 26) if char.isalpha() else char for char in message)


#Second solution
def rot13(message):
    res = []
    for char in message:
        if char not in map(chr, range(97, 123)) and char not in map(chr, range(65, 91)):
            res.append(char)
        else:
            if char.islower() and ord(char) + 13 > 122:
                res.append(chr(((ord(char) + 13) - 122) + 96))
            elif char.isupper() and ord(char) + 13 > 90:
                res.append(chr(((ord(char) + 13) - 90) + 64))
            else:
                res.append(chr((ord(char))+13))
    return ''.join(res)
