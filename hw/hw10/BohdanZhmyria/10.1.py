class Polygon:
    def __init__(self, length):
        self.length = length

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def display(self):
        print(f"The area of the rectangle is {self.length * self.width}")

area_rectangle = Rectangle(23, 32)

area_rectangle.display()