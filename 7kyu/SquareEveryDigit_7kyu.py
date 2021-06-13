'''Welcome. In this kata, you are asked to square every digit of a number and 
concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 
is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer'''


#First solution
def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))

#Second solution
def square_digits(num):
    num = [int(i)**2 for i in str(num)]
    return int(''.join(str(i) for i in num))
