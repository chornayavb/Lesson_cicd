# test_functions.py
import pytest
from main import *


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False


def test_is_odd():
    assert is_odd(3) is True
    assert is_odd(10) is False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_is_palindrome():
    assert is_palindrome("level") is True
    assert is_palindrome("world") is False


def test_max_of_list():
    assert max_of_list([1, 2, 3]) == 3
    assert max_of_list([-1, -5, -3]) == -1
    with pytest.raises(ValueError):
        max_of_list([])

