"""
DESCRIPTION:
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""


def remove_exclamation_marks(s):
    out_str = ''
    for sym in s:
        if sym != '!':
            out_str += sym
    return out_str