"""
Given an array of integers, return the smallest common factors of all integers in the array.

When i say Smallest Common Factor i mean the smallest number above 1 that can divide
all numbers in the array without a remainder.

scf([200, 30, 18, 8, 64, 34]) //=> 2
scf([21, 45, 51, 27, 33]) //=> 3
scf([133, 147, 427, 266]) //=> 7
If there are no common factors above 1, return 1 (technically 1 is always a common factor).
"""


def scf(arr):
    if len(arr) > 0:
        for i in range(2, min(arr) + 1):
            if all(True if x % i == 0 else False for x in arr):
                return i
    return 1
