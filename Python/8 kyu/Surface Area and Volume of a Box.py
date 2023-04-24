"""
Write a function that returns the total surface area and volume of a box as an array: [area, volume]
"""


def get_size(w,h,d):
    x =  w * h * d
    y = (w * h + h * d + w * d) * 2
    return [y, x]