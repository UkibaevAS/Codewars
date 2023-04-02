"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in
a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(*args):
    res = ''
    for i in args:
        if i < 0:
            i = 0
        elif i > 255:
            i = 255
        if len(hex(i)[2:]) > 1:
            res += hex(i)[2:].upper()
        else:
            res += f'0{hex(i)[2:]}'.upper()
    return res