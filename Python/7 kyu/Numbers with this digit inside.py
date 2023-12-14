"""
You have to search all numbers from inclusive 1 to inclusive a given number x, that have the given digit d in it.
The value of d will always be 0 - 9.
The value of x will always be greater than 0.

You have to return as an array

the count of these numbers,
their sum
and their product.

For example:
x = 11
d = 1
->
Numbers: 1, 10, 11
Return: [3, 22, 110]

If there are no numbers, which include the digit, return [0,0,0].
"""


def numbers_with_digit_inside(x, d):
    res = [i for i in range(1, x + 1) if str(d) in str(i)]
    if res:
        lenght, summ = len(res), sum(res)
        x = res[0]
        for i in res[1:]:
            x *= i
        return [lenght, summ, x]
    return [0, 0, 0]