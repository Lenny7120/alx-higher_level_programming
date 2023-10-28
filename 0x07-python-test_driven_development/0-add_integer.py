#!/usr/bin/python3
"""
This module contains a function that add two(2) integers

"""

def add_integer(a, b=98):
    """This function adds two numbers
    Args:
         a : first number to be added
         b : second number to be added
    Returns: sum of the two numbers.
    Raises : TypeError if either of the arguments are not integers or float

    """ 
    if  not isinstance (a, int) and not isinstance (a, float):
        raise TypeError("a must be an integer")
    if not isinstance (b, int) and not isinstance (a, float):
        raise TypeError("b must be an integer")

    return  int(a) + int(b)
