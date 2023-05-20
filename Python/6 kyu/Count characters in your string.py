"""
The main idea is to count all the occurring characters in a string. If you have a string like aba,
then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(s):
    res = {}
    for i in s:
        if i.isalpha():
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
    return res