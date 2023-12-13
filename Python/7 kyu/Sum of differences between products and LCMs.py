"""
In this kata you need to create a function that takes a 2D array/list of non-negative integer pairs and returns
the sum of all the "saving" that you can have getting the LCM of each couple of number compared to their simple product.

For example, if you are given:

[[15,18], [4,5], [12,60]]
Their product would be:

[270, 20, 720]
While their respective LCM would be:

[90, 20, 60]
Thus the result should be:

(270-90)+(20-20)+(720-60)==840
This is a kata that I made, among other things, to let some of my trainees familiarize with the euclidean algorithm,
a really neat tool to have on your belt ;)
"""


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return b
    elif a > b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)


def sum_differences_between_products_and_LCMs(pairs):
    res = []
    for i in pairs:
        z = abs(i[0] * i[1])
        if z == 0:
            res.append(0)
        else:
            res.append(i[0] * i[1] - z / gcd(i[0], i[1]))
    return int(sum(res))