import pytest
import math
from triangle import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(1, 1, 1) == "equilateral"

def test_scalene_triangle():
    assert classify_triangle(1, 2, 3) == "scalene"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 4) == "isosceles"
    assert classify_triangle(3, 4, 3) == "isosceles"
    assert classify_triangle(4, 3, 3) == "isosceles"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "right scalene"

def test_invalid_triangle():
    assert classify_triangle(0,0,0) == "invalid triangle"
    assert classify_triangle(0,0,1) == "invalid triangle"
    assert classify_triangle(0,1,1) == "invalid triangle"
    assert classify_triangle(1,0,1) == "invalid triangle"
    assert classify_triangle(0,1,0) == "invalid triangle"


