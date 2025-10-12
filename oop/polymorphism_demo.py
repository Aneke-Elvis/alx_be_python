# polymorphism_demo.py
# Demonstrates polymorphism and method overriding in Python

import math

# -------------------------------
# Base Class: Shape
# -------------------------------
class Shape:
    """A generic base class for all shapes."""

    def area(self):
        """
        Placeholder method to be overridden by subclasses.
        Raises an error if not implemented by a derived class.
        """
        raise NotImplementedError("Subclass must implement this method")


# -------------------------------
# Derived Class: Rectangle
# -------------------------------
class Rectangle(Shape):
    """Represents a rectangle shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Returns the area of the rectangle (length × width)."""
        return self.length * self.width


# -------------------------------
# Derived Class: Circle
# -------------------------------
class Circle(Shape):
    """Represents a circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns the area of the circle (π × radius²)."""
        return math.pi * (self.radius ** 2)
