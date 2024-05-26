class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        raise NotImplementedError("Area calculation not implemented for generic polygons")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
        self.length = length
        self.width = width

    @classmethod
    def from_input(cls):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return cls(length, width)

    def area(self):
        return self.length * self.width

rectangle = Rectangle.from_input()
print("Perimeter:", rectangle.perimeter())
print("Area:", rectangle.area())