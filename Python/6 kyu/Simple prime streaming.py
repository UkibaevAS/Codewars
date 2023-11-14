"""
Consider a sequence made up of the consecutive prime numbers. This infinite sequence would start with:

"2357111317192329313741434753596167717379..."
You will be given two numbers: a and b, and your task will be to return b elements starting from index a
in this sequence.

For example:
solve(10,5) == `19232` Because these are 5 elements from index 10 in the sequence.
Tests go up to about index 20000.
"""


def create_lst_prime_num(num=45000) -> str:
    a = list(range(num + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= num:
        if a[i] != 0:
            lst.append(str(a[i]))
            for j in range(i, num + 1, i):
                a[j] = 0
        i += 1
    return ''.join(lst)

def solve(a, b):
    return create_lst_prime_num()[a: a + b]