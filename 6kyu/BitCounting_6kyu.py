'''Write a function that takes an integer as input, and returns the number of bits 
that are equal to one in the binary representation of that number. You can guarantee 
that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should 
return 5 in this case'''


#Fist solution
def count_bits(n):
    return bin(n).count('1')

#Second solution
def count_bits(n):
    binar = bin(n)[2:]
    x = 0
    return sum(x + 1 if int(i) > 0 else x for i in binar)

#Third solution
def count_bits(n):
    binar = bin(n)[2:]
    x = 0
    for i in binar:
        if int(i) > 0:
            x += 1
    return x
