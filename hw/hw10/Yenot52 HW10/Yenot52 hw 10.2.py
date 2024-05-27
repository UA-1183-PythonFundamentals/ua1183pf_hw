# I. Ball-super-ball

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# II. Color-ghost

import random 

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow" , "purple" , "red"])

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"



# III. Basic-subclasses-Adam-and-Eve

class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Man(Human):
    def __init__(self, name):
        super().__init__(name, "male")
        self.role = "man"

class Woman(Human):
    def __init__(self, name):
        super().__init__(name, "female")
        self.role = "woman"

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

adam_and_eve = God()


# IV. Classy-classes

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.info=f"{self.name}s age is {self.age}"


# V. Building Spheres

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
        volume = (4/3) * math.pi * self.radius ** 3
        return round(volume, 5)
    
    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)
    
    def get_density(self):
        if self.radius == 0:
            return "Undefined"
        else:
            density = self.mass / self.get_volume()
            return round(density, 5)
    
    
#VI. Dynamic Classes

import re

def class_name_changer(cls, new_name):
    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError("Invalid class name. Class names must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name