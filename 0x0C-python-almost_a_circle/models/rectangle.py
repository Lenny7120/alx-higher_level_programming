#!/usr/bin/python3
"""This module contains a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x
    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """Sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Defines the area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """Print the rectangle with '#' characters, considering x and y offsets."""
        for _ in range(self.y):
            print(" ")  # Print empty lines for y offset
            for _ in range(self.x):
                print(" ")
        """Print the rectangle with '#' characters."""
        for _ in range(self.height):
            print("#" * self.width)
    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    def update(self, *args):
        """Update attributes with the provided arguments."""
        if len(args) > 0:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
