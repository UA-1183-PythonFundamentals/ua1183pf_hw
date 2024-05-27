class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

print(Rectangle(5, 5).area())

