# 1
class Ball:
    # your code goes here
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# 2
from random import choice

class Ghost(object):
    colors = ["red", "white", "yellow", "purple"]
    
    def __init__(self):
        self.color = choice(self.colors)
        
        
# 3
def God():
    return Human.create()

class Human:
    def create():
        adam = Man()
        eve = Woman()
        return [adam, eve]
    pass
        
class Man(Human):
    pass

class Woman(Human):
    pass


# 4
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.info=f"{self.name}s age is {self.age}"
        

# 5
from math import pi

class Sphere(object):
    """This class include formulas for sphere

    Args:
        object (_type_): _description_
    """
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        V = 4 / 3 * pi * self.radius**3
        return round(V, 5)
    
    def get_surface_area(self):
        P = 4 * pi * self.radius**2
        return round(P, 5)
    
    def get_density(self):
        V = self.get_volume()
        D = self.mass / V
        return round(D, 5)
    
# 6
def class_name_changer(cls, new_name):
    if not new_name[0].isupper():
        raise ValueError("Invalid class name. The name must start with an uppercase letter.")

    if not new_name.isalnum():
        raise ValueError("Invalid class name. The name must contain only letters and digits.")

    if new_name[0].isdigit():
        raise ValueError("Invalid class name. The name cannot start with a digit.")

    cls.__name__ = new_name
    
