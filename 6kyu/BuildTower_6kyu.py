
'''Build Tower by the following given argument:
number of floors (integer and always greater than 0).
Tower block is represented as *

    Python: return a list;
Have fun!

for example, a tower of 3 floors looks like below
[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]'''



#First Solution
def tower_builder(n_floors):
    length = n_floors * 2 - 1
    return ['{:^{}}'.format('*' * a, length) for a in range(1, length + 1 , 2)]


#Second solution
def tower_builder(n_floors):
    res = []
    x = 1
    v = 1
    while v < n_floors+1:
        res.append(((n_floors-v) * ' ') + (x * '*') + ((n_floors-v) * ' '))
        x += 2
        v += 1
    if n_floors > len(res):
        res.append(((n_floors * 2) - 1) * '*')
    return res
