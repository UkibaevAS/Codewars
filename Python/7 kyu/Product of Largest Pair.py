"""
Rick wants a faster way to get the product of the largest pair in an array. Your task is to create a performant
solution to find the product of the largest two integers in a unique array of positive numbers.
All inputs will be valid.
Passing [2, 6, 3] should return 18, the product of [6, 3].

Disclaimer: only accepts solutions that are faster than his, which has a running time O(nlogn).

max_product([2, 1, 5, 0, 4, 3])              # => 20
max_product([7, 8, 9])                       # => 72
max_product([33, 231, 454, 11, 9, 99, 57])   # => 104874
"""


def max_product(a):
    n1 = 0
    n2 = 0
    for i in a:
        if i > n2:
            n2, n1 = i, n2
        elif i > n1:
            n1 = i
    return n2 * n1