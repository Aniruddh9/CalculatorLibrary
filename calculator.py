"""
    Calculator library containing basic calculator operations
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiplication(first_term, second_term):
   return first_term * second_term


def division(first_term, second_term):
    try:
        return first_term / second_term
    except ZeroDivisionError:
        print("Division by zero is not allowed")

