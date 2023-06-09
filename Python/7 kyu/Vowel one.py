"""
DESCRIPTION:
vowelOne
Write a function that takes a string and outputs a strings of 1's and 0's where vowels
become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.

Examples:

vowelOne "abceios" -- "1001110"

vowelOne "aeiou, abc" -- "1111100100"
"""


def vowel_one(s):
    x = ''
    for i in s.upper():
        if i in ['A', 'E', 'I', 'O', 'U']: #, 'Y'
            x += str(1)
        else:
            x += str(0)
    return x