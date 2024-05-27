class Polygon:
    def __init__(self, sides):
        self.sides = sides


    def __str__(self):
        return f"A polygon with {len(self.sides)} sides."


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])

    def square(self):
        return self.sides[0] * self.sides[1]


rectangle = Rectangle(33, 3)
print(rectangle)
print("Square:", rectangle.square())


#Task 2
class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is a static method."


name = Human(input("Name is "))
print(name.greet())
print(Human.species())
print(Human.arbitrary_message())


#Task3

class Employee:
    # Class variable to keep track of the total number of employees
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)


