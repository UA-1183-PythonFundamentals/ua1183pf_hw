class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)  # A rectangle has 4 sides
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage:
rectangle = Rectangle(10, 20)
print(f"Area of rectangle: {rectangle.area()}")
