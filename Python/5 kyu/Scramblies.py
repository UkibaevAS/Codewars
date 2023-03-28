"""
DESCRIPTION:
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be
rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""


def scramble(s1, s2):
    s = ''
    for sym in s2.lower():
        if sym not in s:
            s += sym
            if s2.count(sym) > s1.lower().count(sym):return False
    return True