'''The internet is a very confounding place for some adults. Tom has just joined an online forum and is trying to fit in with all the teens and tweens. 
It seems like they're speaking in another language! Help Tom fit in by translating his well-formatted English into n00b language.

The following rules should be observed:

    "to" and "too" should be replaced by the number 2, even if they are only part of a word(E.g. today=2day).
    Likewise, "for" and "fore" should be replaced by the number 4.
    Any remaining double o's should be replaced with zeros(E.g. noob=n00b).
    "be", "are", "you", "please", "people", "really", "have", and "know" should be changed to "b", "r", "u", "plz", "ppl", "rly", "haz", and "no" respectively
    (even if they are only part of the word).
    When replacing words, always maintain case of the first letter unless another rule forces the word to all caps.
    The letter "s" should always be replaced by a "z", maintaining case.
    "LOL" must be added to the beginning of any input string starting with a "w" or "W".
    "OMG" must be added to the beginning(after LOL, if applicable,) of a string 32 characters1 or longer.
    All evenly numbered words2 must be in ALL CAPS(Example: Cake is very delicious. becomes Cake IZ very DELICIOUZ).
    If the input string starts with "h" or "H", the entire output string should be in ALL CAPS.
    Periods(.), commas(, ), and apostrophes(') are to be removed.
    3A question mark(?) should have more question marks added to it, equal to the number of words2 in the sentence(Example: Are you a foo? has 4 words, so it would be converted to r U a F00????).
    3Similarly, exclamation points(!) should be replaced by a series of alternating exclamation points and the number 1, equal to the number of words2 in the sentence
    (Example: You are a foo! becomes u R a F00!1!1).

1 Characters should be counted After: any word conversions, adding additional words, and removing punctuation. Excluding: All punctuation and any 1's added after exclamation marks(!). Character count includes spaces.

2 For the sake of this kata, "words" are simply a space-delimited substring, regardless of its characters. Since the output may have a different number of words than the input, 
words should be counted based on the output string.

Example: whoa, you are my 123 < 3 becomes LOL WHOA u R my 123 < 3 = 7 words.

3 The incoming string will be punctuated properly, so punctuation does not need to be validated.'''

#First solution. REGEX (right approach)
import re

dict = {"[\.,']": "", "too?": "2", "fore?": "4", "oo": "00", "be": "b",
        "are": "r", "you": "u", "please": "plz", "people": "ppl",
        "really": "rly", "have": "haz", "know": "no", "s": "z"}


def n00bify(text):
    for word in dict:
        text = re.sub(word, dict[word], text, flags=re.IGNORECASE)

    if text[0] in "hH":
        text = text.upper()

    if text[0] in "wW":
        text = "LOL " + text

    if len(re.sub("[\?!]*", "", text)) >= 32:
        text = re.sub("\A(LOL |)", "\g<1>OMG ", text)

    text = " ".join(w.upper() if i % 2 != 0 else w for i,
                    w in enumerate(text.split()))

    text = re.sub("(\?|!)", "\g<1>" * len(text.split()),
                  text).replace("!!", "!1")

    return text


#Second solution.(It works but is not the best approach)
def n00bify(text):
    mydict = {ord('.'): None, ord(','): None, ord('\''): None,
              ord('s'): ord('z'), ord('S'): ord('Z')}
    text = text.translate(mydict)
    sub = text.split(' ')

    a = ['FORE', 'Too', 'You', 'you', 'to', 'too', 'for', 'fore',
         'be', 'are', 'pleaze', 'people', 'really', 'have', 'know']
    b = ['4', '2', 'u', 'u', '2', '2', '4', '4',
         'b', 'r', 'plz', 'ppl', 'rly', 'haz', 'no']

    for i, c in enumerate(sub):
        for k, j in enumerate(a):
            if j in c:
                sub[i] = c.replace(a[k], b[k])

    for i, c in enumerate(sub):
        if 'oo' in c:
            sub[i] = c.replace('oo', '00')
        if 'Oo' in c:
            sub[i] = c.replace('Oo', '00')
        if 'Be' in c:
            sub[i] = c.replace('Be', 'b')

    if 'h' == sub[0][0] or 'H' == sub[0][0]:
        for i, c in enumerate(sub):
            sub[i] = c.replace(c, c.upper())
    if 'w' == sub[0][0] or 'W' == sub[0][0]:
        sub[:0] = ['LOL']

    x = 1
    for i, c in enumerate(sub):
        if '!' in sub[i]:
            while x < len(sub):
                sub[i] = (
                    (''.join(((sub[i][:(c.index('!')+x)]) + '1' + (sub[i][(c.index('!')+x):])))))
                x += 1
                if x < len(sub):
                    sub[i] = (
                        (''.join(((sub[i][:(c.index('!')+x)]) + '!' + (sub[i][(c.index('!')+x):])))))
                    x += 1

    count = 0
    for i in sub:
        count += len(i)
        if '1' in i:
            countone = i.count('1')
            count = count - countone
    if sub[0] == 'LOL':
        count -= 3
        if count + (len(sub)-1) >= 32:
            sub.insert(1, 'OMG')
    if count + (len(sub)-1) >= 32 and sub[0] != 'LOL' and sub[0] != 'After':
        sub[:0] = ['OMG']

    for i, c in enumerate(sub):
        if i % 2 == 1:
            sub[i] = c.replace(c, c.upper())

    for i, c in enumerate(sub):
        if '?' in c:
            sub[i] = ((''.join(((sub[i][:c.index('?')]) +
                                ((len(sub)-1) * '?') + (sub[i][(c.index('?')):])))))

    for i, c in enumerate(sub):
        x = c.count('!') + c.count('1')
        if '!' in c and x != len(sub):
            while x < len(sub):
                if c.count('!') > c.count('1'):
                    sub[i] = (
                        (''.join(((sub[i][:(c.index('!')+x)]) + '1' + (sub[i][(c.index('!')+x):])))))
                else:
                    sub[i] = (
                        (''.join(((sub[i][:(c.index('1')+x)]) + '!' + (sub[i][(c.index('1')+x):])))))
                x += 1

    return ' '.join(sub)
