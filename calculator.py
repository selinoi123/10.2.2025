import math
import sqlite3

def add(a, b):
    return a + b  # + 0.1 # 0.99999999999


# 0.4444444444 + 0.66666666666
# 0.999999999999
# 1.0

def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def make_error():
    raise IndexError()

def create_table(query):
    # check if table exists
    raise sqlite3.IntegrityError

def say_hello():
    name = input("enter name? ")
    return f"hello {name}"

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    sum = 1
    for i in range(1, a + 1):
        sum = sum * i

    return sum