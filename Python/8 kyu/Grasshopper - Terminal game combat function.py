"""
DESCRIPTION:
Create a combat function that takes the player's current health and the amount of damage recieved,
and returns the player's new health. Health can't be less than 0.
"""


def combat(health, damage):
    return health - damage if health - damage > 0 else 0