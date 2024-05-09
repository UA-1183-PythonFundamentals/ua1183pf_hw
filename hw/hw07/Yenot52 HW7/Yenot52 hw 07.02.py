def calculate_rectangle_area(length, width):
  """This function calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  return length * width

def calculate_triangle_area(base, height):
  """This function calculates the area of a triangle.

  Args:
    base: The base of the triangle.
    height: The height of the triangle.

  Returns:
    The area of the triangle.
  """
  return 0.5 * base * height

def calculate_circle_area(radius):
  """This function calculates the area of a circle.

  Args:
    radius: The radius of the circle.

  Returns:
    The area of the circle.
  """
  return radius * radius * 3.141592654

def main():
  """This function prompts the user to enter the shape they want to calculate the area of. """
  
shape = input("Enter the shape you want to calculate the area of: ")

if shape == "rectangle":
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))
  area = calculate_rectangle_area(length, width)
  print("The area of the rectangle is:", area)

elif shape == "triangle":
  base = float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  area = calculate_triangle_area(base, height)
  print("The area of the triangle is:", area)

elif shape == "circle":
  radius = float(input("Enter the radius of the circle: "))  
  area = calculate_circle_area(radius)
  print("The area of the circle is:", area)

else:
  print("Invalid shape.")