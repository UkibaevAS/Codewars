"""
Write a function insert_dash(num) / insertDash(num) / InsertDash(int num) that will insert dashes ('-')
between each two odd digits in num. For example: if num is 454793 the output should be 4547-9-3.
Don't count zero as an odd digit.

Note that the number will always be non-negative (>= 0).
"""


def insert_dash(num):
    num = str(num)
    res = num[0]
    for i in range(1, len(num)):
        if int(num[i - 1]) % 2 != 0 and int(num[i]) % 2 != 0:
            res += '-' + num[i]
        else:
            res += num[i]
    return res