class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def print_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Example usage:
employee1 = Employee("John", 50000)
employee2 = Employee("Jane", 60000)

employee1.employee_info()
employee2.employee_info()
Employee.print_total_employees()

# Display class information
print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
