# 1. Ball-super-ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")

print("Ball 1 type:", ball1.ball_type)   
print("Ball 2 type:", ball2.ball_type)   

# 2. Ghost objects are instantiated without any arguments.
import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost = Ghost()
print("Ghost color:", ghost.color)

# 3. According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def create():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

adam, eve = create()

print("Adam name:", adam.name)
print("Eve name:", eve.name)

# 4. complete this Class, the Person class has been created. You must fill in the Constructor method to accept a name as string and an 
# age as number, complete the get Info property and getInfo method/Info getter which should return johns age is 34
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}'s age is {self.age}"

john = Person("John", 34)
print(john.info)  

# 5. Now that we have a Block let's move on to something slightly more complex: a Sphere.
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
        density = self.mass / self.get_volume()
        return round(density, 5)

ball = Sphere(2, 50)
print("Radius:", ball.get_radius())
print("Mass:", ball.get_mass())
print("Volume:", ball.get_volume())
print("Surface Area:", ball.get_surface_area())
print("Density:", ball.get_density())

# 6. Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
def change_class_name(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    cls.__name__ = new_name

class MyClass:
    pass

change_class_name(MyClass, "UsefulClass")
change_class_name(MyClass, "SecondUsefulClass")

print(MyClass.__name__)  


