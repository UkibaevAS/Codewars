"""
DESCRIPTION:
My friend wants a new band name for her band. She like bands that use the formula: "The" + a noun with
the first letter capitalized, for example:

"dolphin" -> "The Dolphin"

However, when a noun STARTS and ENDS with the same letter, she likes to repeat the noun twice and connect
them together with the first and last letter, combined into one word (WITHOUT "The" in front), like this:

"alaska" -> "Alaskalaska"

Complete the function that takes a noun as a string, and returns her preferred band name written as a string.
"""


def band_name_generator(name):
    return f'The {name.capitalize()}' if name[0] != name[-1] else f'{name.capitalize()}{name[1:]}'