'''Write a class that, when given a string, will return an uppercase string with each letter shifted 
forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5)  # creates a CipherHelper with a shift of five
c.encode('Codewars')  # returns 'HTIJBFWX'
c.decode('BFKKQJX')  # returns 'WAFFLES'

If something in the string is not in the alphabet(e.g. punctuation, spaces), simply leave it as is .
The shift will always be in range of[1, 26].'''


class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        self.st = st
        res = []
        for char in self.st:
            char = char.upper()
            if char not in map(chr, range(65, 91)):
                res.append(char)
            else:
                num = ord(char)
                if num + self.shift <= 90:
                    char = chr(num + self.shift)
                else:
                    char = chr((num - 91) + 65 + self.shift)
                res.append(char)
        return ''.join(res)

    def decode(self, st):
        self.st = st
        res = []
        for char in self.st:
            char = char.upper()
            if char not in map(chr, range(65, 91)):
                res.append(char)
            else:
                num = ord(char)
                if num - self.shift < 65:
                    char = chr(91 - (65 - (num - self.shift)))
                else:
                    char = chr(num - self.shift)
                res.append(char)
        return ''.join(res)
