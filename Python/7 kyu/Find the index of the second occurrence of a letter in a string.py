"""
In this kata, you need to write a function that takes a string and a letter as input and then returns the index
of the second occurrence of that letter in the string. If there is no such letter in the string, then the function
should return -1. If the letter occurs only once in the string, then -1 should also be returned.

Examples:

second_symbol('Hello world!!!','l') --> 3
second_symbol('Hello world!!!', 'A') --> -1
"""


def second_symbol(s, symbol):
    if s.count(symbol) < 2:
        return -1
    else:
        x = 0
        for i in range(len(s)):
            if s[i] == symbol:
                x += 1
            if x == 2:
                return i