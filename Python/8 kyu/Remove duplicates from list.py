"""
DESCRIPTION:
Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same.
"""


def distinct(seq):
    sorted_seq = []
    [sorted_seq.append(i) for i in seq if i not in sorted_seq]
    return sorted_seq