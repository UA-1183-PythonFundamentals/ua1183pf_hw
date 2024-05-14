import math


def area_rectangle(height, width):
    return height * width


def area_triangle(height, base):
    return height * base * 1 / 2


def area_circle(radius):
    return math.pi * pow(radius, 2)
