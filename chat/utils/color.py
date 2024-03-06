import random
import string


colors = [
    "#FF5733",
    "#FFC300",
    "#FFAFBD",
    "#FF7373",
    "#C70039",
    "#900C3F",
    "#9AECDB",
    "#00B4D8",
    "#48CAE4",
    "#00C49A",
    "#8338EC",
    "#3A86FF",
    "#6D6875",
    "#FFD700",
    "#FF9100",
    "#FF6B6B",
    "#235347",
    "#b9b3fc",
]


def generate_random_color():
    # Generate a random hexadecimal color code from color options
    return random.choice(colors)
