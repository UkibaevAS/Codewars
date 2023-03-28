"""
DESCRIPTION:
Create a function that takes a string as a parameter and does the following, in this order:

Replaces every letter with the letter following it in the alphabet (see note below)
Makes any vowels capital
Makes any consonants lower case
Note:

the alphabet should wrap around, so Z becomes A
in this kata, y isn't considered as a vowel.
So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)
"""


def changer(s):
    vowel = 'aeoiu'
    text = ''
    for sym in s.lower():
        if sym.isalpha():
            new_sym = chr(ord(sym) + 1)
            if ord(new_sym) <= 122:
                if new_sym in vowel:
                    text += new_sym.upper()
                else:
                    text += new_sym
            else:
                new_sym = chr(ord(new_sym) - 26)
                if new_sym in vowel:
                    text += new_sym.upper()
                else:
                    text += new_sym

        else:
            text += sym
    return text