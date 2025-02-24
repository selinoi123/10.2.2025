import time
from webbrowser import Error

import pytest
from pyexpat import ExpatError

import calculator

def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"


def test_calculator_minus_small():
    # Arrange
    a: int = 10
    b: int = 10
    expected: int = 0

    # Act
    actual: int = calculator.minus(a, b)

    # Assert
    assert expected == actual, "small numbers minus"

def test_calculator_multiply_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 1.0

    # Act
    actual: float = calculator.multiply(a, b)

    # Assert
    assert expected == actual, "small numbers multiply"

def test_calculator_div_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 100

    # Act
    actual: float = calculator.divide(a, b)

    # Assert
    assert expected == actual, "small numbers div"

# False positive
def test_calculator_div_by_zero1():
    # Arrange
    a: int = 10
    b: float = 0

    # Act
    try:
        # next line should raise an error
        calculator.divide(a, b)

        # if we got here it's incorrect
        # the test should fail!
        # since we expected ZeroDivisionError
        # to occur
        assert False, "should raise ZeroDivisionError"

    except ZeroDivisionError as e:
        # this is the good scenario
        # an error has occurred
        # test should pass successfully
        assert True


# False positive
def test_calculator_div_by_zero2():
    # Arrange
    a: int = 10
    b: float = 0

    with pytest.raises(Exception) as ex:
        calculator.divide(a, b)

def test_check_error_happned():
    with pytest.raises(IndexError) as ex:
        calculator.make_error()

# sending input value to a functions during test
# extra feature , *bonus
def test_calculator_hello(monkeypatch):

    # black box
    monkeypatch.setattr('builtins.input', lambda _: "danny1")

    expected = "hello danny"
    result = calculator.say_hello()

    assert expected == result

def test_calculator_power():
    # Arrange
    a: int = 2
    b: int = 4
    expected: int = 16

    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "numbers power"


def test_calculator_power_2():
    # Arrange
    a: int = 3
    b: int = 2
    expected: int = 9

    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "numbers power"


def test_calculator_sqrt():
    a = 25
    expected = 5

    # Act
    actual = calculator.sqrt(a)

    # Assert
    assert expected == actual, "Expected sqrt 25 to equal 5"

def test_calculator_sqrt_negative():
    with pytest.raises(ValueError):
        calculator.sqrt(-5)

def test_calculator_factorial():
    a = 4
    expected = 24

    # Act
    actual = calculator.factorial(a)

    # Assert
    assert expected == actual, "Expected factorial 4 to  24"

def test_calculator_factorial_negative():
    with pytest.raises(ValueError):
        calculator.factorial(-1)

def test_calculator_factorial_2():
    a = 5
    expected = 120

    # Act
    actual = calculator.factorial(a)

    # Assert
    assert expected == actual, "Expected factorial 5 to  120"

def test_calculator_factorial_negative_2():
    with pytest.raises(ValueError):
        calculator.factorial(-3)