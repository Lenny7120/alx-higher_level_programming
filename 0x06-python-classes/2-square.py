#!/usr/bin/python3
"""
This module defines a  class called square

"""

class Square:
    """
    Defines a class called square

    """
    def __init__(self, size=0):
        """
        Initializes an instance
        Args: 
             size:  represent the size of the square
        Raises: 
              TypeError: if size not an integer
              ValueError: if size is less than zero

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

