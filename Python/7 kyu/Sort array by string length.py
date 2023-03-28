"""
DESCRIPTION:
Write a function that takes an array of strings as an argument and returns a sorted array containing the
same strings, ordered from shortest to longest.

For example, if this array were passed as an argument:

["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:

["Eyes", "Glasses", "Monocles", "Telescopes"]

All of the strings in the array passed to your function will be different lengths, so you will not have
to decide how to order multiple strings of the same length.
"""


def sort_by_length(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr