class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


