'''The rgb function is incomplete. Complete it so that passing in RGB decimal values
will result in a hexadecimal representation being returned. Valid decimal values for
RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest
valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not
work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3'''

#First solution (best)
def rgb(r, g, b):
    limits = lambda x: min(255, max(x, 0))
    return ('{:02X}' * 3).format(limits(r), limits(g), limits(b))

#Second solution
def rgb(r, g, b):
    lis = [r, g, b]
    for i, num in enumerate(lis):
        if num < 0:
            lis[i] = 0
        elif num > 255:
            lis[i] = 255

    for i, num in enumerate(lis):
        if num < 9:
            lis[i] = hex(num).replace('x', '')
        else:
            lis[i] = hex(num).replace('0x', '')
    return ''.join(i.upper() for i in lis)
