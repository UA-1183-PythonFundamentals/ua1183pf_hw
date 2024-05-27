class Polygon:
  def __init__(self, points):
    self.points = points

  def get_area(self):
    raise NotImplementedError("Subclasses must implement get_area()")


class Rectangle(Polygon):
  def __init__(self, width, height):
    super().__init__([
      (0, 0),  # Bottom left corner
      (width, 0),  # Bottom right corner
      (width, height),  # Top right corner
      (0, height)  # Top left corner
    ])
    self.width = width
    self.height = height

  def get_area(self):
    return self.width * self.height

# Example usage
rectangle = Rectangle(5, 3)
area = rectangle.get_area()
print(f"Area of the rectangle: {area}")