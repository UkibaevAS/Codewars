"""
Create an OR function, without use of the 'or' keyword, that takes an list of boolean values and runs OR
against all of them.

Assume there will be between 1 and 6 variables, and return None (python) / nil (ruby) for an empty list.
"""


def alt_or(lst):
    return any(lst) if len(lst) > 0 else None