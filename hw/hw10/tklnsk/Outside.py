#Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
#Color-ghost
import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

#Basic-subclasses-Adam-and-Eve
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]



#Classy-classes
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.info=f"{self.name}s age is {self.age}"

#Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 14)
#Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name[0].isupper():
        raise ValueError("Invalid class name. The name must start with an uppercase letter.")

    if not new_name.isalnum():
        raise ValueError("Invalid class name. The name must contain only letters and digits.")

    if new_name[0].isdigit():
        raise ValueError("Invalid class name. The name cannot start with a digit.")

    cls.__name__ = new_name