
"""
Vector Addition Using Operator Overloading.

Demonstrates how to overload the + operator
using the __add__() method in Python OOP.
"""


class Vector:
    """Represent a two-dimensional vector."""

    def __init__(self, x, y):
        """Initialize the vector with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two Vector objects and return a new Vector."""
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        """Return a readable string representation of the vector."""
        return f"Vector({self.x}, {self.y})"


def main():
    """Create two vectors and demonstrate vector addition."""

    # Create Vector objects
    v1 = Vector(2, 3)
    v2 = Vector(4, 1)

    # Add vectors using the + operator
    result = v1 + v2

    # Display the result
    print(result)


if __name__ == "__main__":
    main()