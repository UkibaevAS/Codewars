"""
Write a function that takes a list of at least four elements as an argument and returns
a list of the middle two or three elements in reverse order.
"""


def reverse_middle(lst):
    k = len(lst) // 2
    if len(lst) % 2 == 0:
        res = lst[k - 1: k + 1]
        res.reverse()

    else:
        res = lst[k - 1: k + 2]
        res.reverse()
    return res
