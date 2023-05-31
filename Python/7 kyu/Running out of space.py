"""
Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an
array showing the space decreasing.
For example, running this function on the array ['i', 'have','no','space'] would produce
['i','ihave','ihaveno','ihavenospace']


"""


def spacey(array):
    res = []
    for i in array:
        if len(res) != 0:
            res.append(res[-1] + i)
        else:
            res.append(i)
    return res