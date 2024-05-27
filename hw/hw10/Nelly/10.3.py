  
# Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.

class Employee:
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
    
    def display_employee_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
    
    @classmethod
    def display_total_employees(cls):
        print("Total Employees:", cls.total_employees)