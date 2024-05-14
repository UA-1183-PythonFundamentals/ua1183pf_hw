class Employee:
    """Class include all employees and counter."""
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
        
    def print_employee_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        
    @classmethod
    def get_total_employees(self):
        return self.total_employees
    

print("Information about class Employee:")
print(f"Base classes: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
    
emp1 = Employee("John", 50000)
emp2 = Employee("Alice", 60000)
emp3 = Employee("Bob", 55000)

emp1.print_employee_info()
emp2.print_employee_info()
emp3.print_employee_info()

print("\nTotal number of employees:", Employee.get_total_employees())