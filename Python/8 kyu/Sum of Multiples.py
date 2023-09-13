"""
Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"
"""


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    elif n == m or n > m:
        return 0
    else:
        res = []
        for i in range(n, m):
            if i != 0:
                if i % n == 0:
                    res.append(i)
        return 'INVALID' if sum(res) <= 0 else sum(res)