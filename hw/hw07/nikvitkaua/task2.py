# Task 2
def get_area_of_rectangle(height, width):
    """
    Function get 2 params (width and height) and return area of rectangle

    :param height: type float or int and value height of rectangle
    :param width: type float or int and value width of rectangle
    :return: area of rectangle
    """
    return height * width


def get_area_of_triangle(base, height):
    """
    Get 2 values base and height and return area of rectangle

    :param base: type float or int
    :param height: type float or int
    :return: area of rectangle
    """
    return (base * height) / 2


def get_area_of_circle(radius):
    """
    Function take radius and return area of circle

    :param radius: int or float and value radius of circle
    :return: area of circle
    """
    PI = 3.14

    return PI * radius**2