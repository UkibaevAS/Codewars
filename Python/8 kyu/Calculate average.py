"""
DESCRIPTION:
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.
"""


def find_average(numbers):
    count = summ = 0
    for i in range(len(numbers)):
        summ += numbers[i]
        count += 1
    if summ / count != 0:return summ / count
    else:return 0