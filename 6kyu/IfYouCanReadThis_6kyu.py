'''Task:
You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

Input:
If, you can read?

Output:
India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

Note:
    There are preloaded dictionary you can use, named NATO
    The set of used punctuation is ,.!?.
    Punctuation should be kept in your return string, but spaces should not.
    Xray should not have a dash within.
    Every word and punctuation mark should be seperated by a space ' '.
    There should be no trailing whitespace'''


#First solution
def to_nato(words):
    result = []
    dictionary = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 
        'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 
        'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 
        'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 
        'Y': 'Yankee', 'Z': 'Zulu'}

    words = list(map(str, words.upper().replace(' ', '')))
    for a in words:
        if a in dictionary:
            result.append(dictionary[a])
        else:
            result.append(a)
    return ' '.join(result)

#Second solution


def to_nato(words):
    result = []
    dictionary = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 
        'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 
        'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 
        'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 
        'Y': 'Yankee', 'Z': 'Zulu', '?': '?', ',': ',', '.': '.', '!': '!'}

    words = list(map(str, words.upper().replace(' ', '')))
    for a in words:
        for keys, values in dictionary.items():
            if a == keys:
                result.append(values)
    return ' '.join(result)
