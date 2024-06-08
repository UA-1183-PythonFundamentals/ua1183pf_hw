#task 1
class Ball(object):
    # your code goes here
    def __init__ (self, ball_type="regular"):
        self.ball_type = ball_type


#task 2
import random

class Ghost(object):
    pass
    def __init__(self):
        self.colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(self.colors)


#task 3
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
    #code
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

#Test 4
class Person:
    def __init__(self, name,age):
        self.age = age
        self.name = name
        self.info=f"{self.name}s age is {self.age}"
        
    def getInfo(self):
        return self.info
    

#Task 5

import math
class Sphere(object):
    #pass
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius (self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius**3
        return round(volume, 5)
    
    
    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)
    
    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)
    

    #Test 6
    def class_name_changer(cls, new_name):
        pass
        if not new_name[0].isupper() or not new_name.isalnum():
            raise ValueError("Invalid class name format")

        cls.__name__ = new_name