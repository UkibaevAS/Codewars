"""
Create a function that returns the total of a meal including tip and tax. You should not tip on the tax.

You will be given the subtotal, the tax as a percentage and the tip as a percentage.
Please round your result to two decimal places.
"""


def calculate_total(subtotal, tax, tip):
    sum_tax = subtotal * tax / 100
    sum_tip = subtotal * tip / 100
    return round(subtotal + sum_tax + sum_tip, 2)