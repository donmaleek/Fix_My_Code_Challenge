#!/usr/bin/python3

class Square:
    
    side_length = 0
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """Calculate the area of the square."""
        return self.side_length * self.side_length

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.side_length

    def __str__(self):
        """String representation of the square."""
        return f"Square(side_length={self.side_length})"

if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())

