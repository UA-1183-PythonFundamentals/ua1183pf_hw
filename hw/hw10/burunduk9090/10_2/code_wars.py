# I. Ball-super-ball
# class Ball(object):
#     def __init__(self, ball_type='regular'):
#         self.ball_type = ball_type

# II. Color-ghost
# from random import randint
#
# color = ['white', 'yellow', 'purple', 'red']
#
#
# class Ghost():
#     def __init__(self):
#         self.index = randint(0, len(color)-1)
#         self.color = color[self.index]


# III. Basic-subclasses-Adam-and-Eve
# class Human():
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass
# a, b = Man(), Woman()
# def God():
#     return [a, b]

# IV. Classy-classes
# class Person():
#     def __init__(self, name, age):
#         self.name = str(name)
#         self.age = int(age)
#         self.info = f"{self.name}s age is {self.age}"

# #V. Building Spheres
# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         return 4 / 3 * math.pi * pow(self.radius, 3)
#
#     def get_surface_area(self):
#         return 4 * math.pi * pow(self.radius, 2)
#
#     def get_density(self):
#         return self.mass / self.get_volume()

# VI. Dynamic Classes
# import re
#
# pattern = r'^[A-Z][A-Za-z0-9]*$'
#
#
# def change_name_class(cls, name):
#     if not re.match(pattern, name):
#         raise ValueError(f"Invalid class name: '{name}'")
#
#     cls.__name__ = name
#     return cls
#
