"""
DESCRIPTION:
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
Notes:

If either input is an empty string, consider it as zero.

Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)
"""


def sum_str(a, b):
    if len(a) == 0 and  len(b) == 0:
        return '0'
    elif len(a) != 0 and  len(b) == 0:
        return a
    elif len(a) == 0 and  len(b) != 0:
        return b
    return str(int(a) + int(b))