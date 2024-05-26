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



empl1 = Employee("Alice", 50000)
empl2 = Employee("Bob", 60000)

Employee.display_total_employees()

empl1.display_info()
empl2.display_info()