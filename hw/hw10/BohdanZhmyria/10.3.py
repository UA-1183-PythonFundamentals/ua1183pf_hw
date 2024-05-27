class Employee:
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    @classmethod
    def displayCount(cls):
        print(Employee.count)
    def displayEmployee(self):
        print(self.name, self.salary)

emp1 = (Employee('Bob', 1500))
emp2 = (Employee('Rob', 2000))
emp1.displayEmployee()
emp2.displayEmployee()
print(Employee.count)

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)