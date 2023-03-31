"""
DESCRIPTION:
When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"
"""


def position(alphabet):
    return f"Position of alphabet: {ord(alphabet.upper()) - 64}"