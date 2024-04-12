#!/usr/bin/python3

class Square():
    """A class to represent a square."""

    # Class variables for width and height
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize the square with optional width and height."""
        # Set instance variables based on keyword arguments
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.width * self.height

    def PerimeterOfMySquare(self):
        """Calculate the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return a string representation of the square."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    # Create an instance of the Square class with given width and height
    s = Square(width=12, height=9)
    # Print the string representation of the square
    print(s)
    # Print the area of the square
    print(s.area_of_my_square())
    # Print the perimeter of the square
    print(s.PerimeterOfMySquare())
