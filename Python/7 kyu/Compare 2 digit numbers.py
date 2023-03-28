"""
DESCRIPTION:
You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.

Example:

compare(13,14)=50%;
compare(23,22)=50%;
compare(15,51)=100%;
compare(12,34)=0%.
"""


def compare(a, b) -> str:
    num = 0
    if str(a) == str(b) or str(a) == str(b)[:: -1]:
        return f'100%'
    for i in str(a):
        for index in range(len(str(b))):
            if i == str(b)[index]:
                num += 50
    return f'{50}%' if num != 0 else f'{0}%'