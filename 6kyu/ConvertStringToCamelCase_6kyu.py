'''Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized only if 
the original word was capitalized (known as Upper Camel Case, also often referred 
to as Pascal case).
Examples:
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"'''


#First solution
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('-', '').replace('_', '')

#Second solution
def to_camel_case(text):
    first = text[:1]
    rest = text.title()
    return first + rest[1:].replace('-', '').replace('_', '')
