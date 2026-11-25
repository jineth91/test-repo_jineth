import pytest

from calculator import add, subtract, multiply, divide, is_prime, fibonacci


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (-1, 1, 0), (0.5, 0.25, 0.75)])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize("n, expected", [(0, False), (1, False), (2, True), (17, True), (21, False), (97, True)])
def test_is_prime(n, expected):
    assert is_prime(n) is expected


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)
