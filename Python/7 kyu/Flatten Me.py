"""
DESCRIPTION:
In this kata, your task is to create a function that takes a single list as an argument and returns a flattened list.
The input list will have a maximum of one level of nesting (list(s) inside of a list).

# no nesting
[1, 2, 3]

# one level of nesting
[1, [2, 3]]
Examples
>>> flatten_me(['!', '?'])
['!', '?']

>>> flatten_me([1, [2, 3], 4])
[1, 2, 3, 4]

>>> flatten_me([['a', 'b'], 'c', ['d']])
['a', 'b', 'c', 'd']

>>> flatten_me([[True, False], ['!'], ['?'], [71, '@']])
[True, False, '!', '?', 71, '@']
"""


def flatten_me(lst):
    res = []
    for obj in lst:
        res += flatten_me(obj) if isinstance(obj, list) else [obj]

    return res