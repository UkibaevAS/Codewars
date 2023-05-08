"""
Sami is practicing her aim with her bow and is shooting some balloons in the air. On each balloon,
they have different numbers written on them which represent their size. She would like to pop the balloon
highest in the air that also has the most balloons of the same size present. If there is a tie, then she
will instead pop the balloon of the size highest in the air. Do you think you can output which balloon
she pops on each shot?

You will be provided an array of the balloons as integers (the integers representing the sizes) in lowest
to highest order in the air. You will also be given an integer pops, which will be the number of pops
that Sami will execute.

Constraints
0 < pops <= number of elements in balloons

10 <= number of elements in balloons <= 500

1 <= balloon size <= 1000

Example
pops = 4
balloons = [5, 7, 5, 7, 4, 5]

pop #1: 5
pop #2: 7
pop #3: 5
pop #4: 4

return: [5, 7, 5, 4]
Explanation
For pop #1, we return 5 because it is the most frequent, the list now becomes {5, 7, 5, 7, 4}.
In pop #2, we return 7, since 5 and 7 are the most frequent, but 7 is the highest, so we pop 7.
The list now becomes {5, 7, 5, 4}. In pop #3, we pop 5 since it’s the most frequent.
The list now becomes {5, 7, 4}. In pop #4, we pop 4 since all balloons now have the same count (here: 1),
but the balloon of size 4 is the highest in the air.
"""

from collections import Counter


def freq_stack(pops, balloons):
    res_list = []
    balloons.reverse()

    for _ in range(pops):
        count_max = 0
        num_max = 0
        cnt = dict(Counter(balloons))
        for num, count in cnt.items():

            if count > count_max:
                count_max = count
                num_max = num
                index = balloons.index(num)

        res_list.append(balloons.pop(index))
    return res_list
