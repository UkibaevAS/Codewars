"""
Spoonerize... with numbers... numberize?... numboonerize?... noonerize? ...anyway!
If you don't yet know what a spoonerism is and haven't yet tried my spoonerism kata, please do check it out first.

You will create a function which takes an array of two positive integers, spoonerizes them, and returns
the positive difference between them as a single number or 0 if the numbers are equal:

[123, 456] = 423 - 156 = 267
Your code must test that all array items are numbers and return "invalid array" if it finds that either item
is not a number. The provided array will always contain 2 elements.

When the inputs are valid, they will always be integers, no floats will be passed. However, you must take into
account that the numbers will be of varying magnitude, between and within test cases.
"""


def noonerize(numbers):
    a, b = numbers
    if isinstance(a, int) and isinstance(b, int):
        x = str(numbers[0])
        y = str(numbers[-1])
        if len(x) > 1 and len(y) > 1:
            x1 = y[0] + x[1:]
            y1 = x[0] + y[1:]
        elif len(x) == 1:
            x1 = y[0]
            y1 = x[0] + y[1:]
        else:
            x1 = y[0] + x[1:]
            y1 = x[0]
        return abs(int(x1) - int(y1))
    else:
        return "invalid array"