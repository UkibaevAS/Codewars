"""
DESCRIPTION:
The function is not returning the correct values. Can you figure out why?

Example (Input --> Output ):

3 --> "Earth"
"""


def get_planet_name(id):
    name = {1: "Mercury",
            2: "Venus",
            3: "Earth",
            4: "Mars",
            5: "Jupiter",
            6: "Saturn",
            7: "Uranus",
            8: "Neptune"}
    return name[id]