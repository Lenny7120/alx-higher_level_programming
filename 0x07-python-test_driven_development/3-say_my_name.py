#!/usr/bin/python3
"""This module has a function that prints a name

"""

def say_my_name(first_name, last_name=""):
    """
    This function prints name ( <first name> <last name>)
    Args:
        first_name: first name to be printed
        last_name: last name to be printed
    Raises:
          TypeError: when first name and last name are not strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
