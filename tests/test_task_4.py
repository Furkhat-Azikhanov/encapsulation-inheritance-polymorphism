import math

import pytest

from tasks import Circle, Rectangle, Triangle


def test_circle():
    c = Circle(1)
    assert round(c.area(), 2) == round(math.pi * 1**2, 2)
    assert round(c.perimeter(), 2) == round(2 * math.pi * 1, 2)

def test_rectangle():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14

def test_triangle():
    t = Triangle(3, 4, 5)
    assert round(t.area(), 2) == 6.0
    assert t.perimeter() == 12

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 1, 5)  # невозможно построить треугольник
