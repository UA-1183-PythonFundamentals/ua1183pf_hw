#1.  Ball-super-ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#2. Color-ghost
import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

#3. Basic-subclasses-Adam-and-Eve
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

#4. Classy-classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

    @property
    def getInfo(self):
        return self.info

#5. Building Spheres
import math

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

#6. Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Error")
    cls.__name__ = new_name
