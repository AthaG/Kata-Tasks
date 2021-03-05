'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool')  # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !'''

#First solution
def pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

#Second solution
def pig_it(text):
    splited = text.split()
    return ' '.join(f'{i[1:]}{i[0]}ay' if i.isalpha() else i for i in splited)