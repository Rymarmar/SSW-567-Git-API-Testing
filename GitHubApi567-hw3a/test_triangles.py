# test_github_api.py  (HW03a_Mocking branch)
# Benedict Martinez – SSW 567 – HW 03b
# Tests are fully mocked: no real HTTP requests are made.
# I pledge my honor that I have abided by the Stevens Honor System
# Changed name of file to test_triangles.py

"""Unit tests for triangles.py (HW03c)."""
# pylint: disable=missing-function-docstring
import pytest
from triangles import classify_triangle

# --- invalid types ---
@pytest.mark.parametrize("a,b,c", [("3", 3, 3), (None, 3, 3)])
def test_invalid_type_raises(a, b, c):
    with pytest.raises(TypeError):
        classify_triangle(a, b, c)

# --- non-positive sides ---
@pytest.mark.parametrize("a,b,c", [(0,1,1), (-1,2,2), (3,-4,5)])
def test_non_positive_raises(a, b, c):
    with pytest.raises(ValueError):
        classify_triangle(a, b, c)

# --- triangle inequality fails ---
@pytest.mark.parametrize("a,b,c", [(1,2,3), (2,3,5), (10,1,1)])
def test_not_a_triangle(a, b, c):
    assert classify_triangle(a, b, c) == "Not a triangle"

# --- valid classes ---
def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

@pytest.mark.parametrize("sides", [(2,2,3), (2,3,2), (3,2,2)])
def test_isosceles_any_order(sides):
    assert classify_triangle(*sides) == "Isosceles"

@pytest.mark.parametrize("sides", [(3,4,6), (4,6,3), (6,3,4)])
def test_scalene_any_order(sides):
    assert classify_triangle(*sides) == "Scalene"

def test_float_boundary_not_triangle():
    assert classify_triangle(1.0, 2.0, 3.0) == "Not a triangle"
