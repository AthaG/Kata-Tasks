'''Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the 
last two names, which should be separated by an ampersand.

Example:
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    # returns 'Bart, Lisa & Maggie'

    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    # returns 'Bart & Lisa'

    namelist([ {'name': 'Bart'} ])
    # returns 'Bart'

    namelist([])
    # returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'. '''


def namelist(names):
    list = []
    for item in names:
        name = item.pop('name')
        list.append(name)
    for i in range(len(list)):
        list.insert((i + 1) + i, ', ')
    if list == []:
        return ''.join(list)
    elif len(list) == 2:
        del list[-1]
        return ''.join(list)
    else:
        del list[-1]
        del list[-2]
        list.insert(-1, ' & ')
        string = ''.join(list)
    return string
