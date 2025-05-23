import pytest
from tasks import GradeBook

def test_add_and_get_average():
    gb = GradeBook()
    gb.add_grade("Alice", 5)
    gb.add_grade("Alice", 4)
    assert gb.get_average("Alice") == 4.5

def test_all_averages():
    gb = GradeBook()
    gb.add_grade("Bob", 3)
    gb.add_grade("Bob", 4)
    gb.add_grade("Alice", 5)
    avg = gb.get_all_averages()
    assert avg["Bob"] == 3.5
    assert avg["Alice"] == 5

def test_invalid_grade():
    gb = GradeBook()
    with pytest.raises(ValueError):
        gb.add_grade("Charlie", 6)
