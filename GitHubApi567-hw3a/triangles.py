# Benedict Martinez – SSW 567 – HW 03a
# I pledge my honor that I have abided by the Stevens Honor System
# Changed name of file to triangles.py

"""Triangle classification module for HW03c."""
from typing import Union

Number = Union[int, float]

def classify_triangle(a: Number, b: Number, c: Number) -> str:
    """Return 'Equilateral', 'Isosceles', 'Scalene', or 'Not a triangle'."""
    # Type & value checks
    for side in (a, b, c):
        if not isinstance(side, (int, float)):
            raise TypeError("Sides must be int or float")
        if side <= 0:
            raise ValueError("Sides must be > 0")

    # Triangle inequality
    if not (a + b > c and b + c > a and c + a > b):
        return "Not a triangle"

    # Classes
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"
