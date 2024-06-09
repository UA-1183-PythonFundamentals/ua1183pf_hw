class Employee:
    total_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
    def print_total_employees(self):
        print(f"Total Employees: {self.total_employees}")
    def show_info(self):
        print(f"Name: {self.name}. Salary: {self.salary}")

    emp1 = Employee("John", 5000)
    emp2 = Employee("Mary", 3400)
    emp3 = Employee("Juliet", 5000)
    emp1.show_info()
    emp2.show_info()
    emp3.show_info()

    emp1.print_total_employees()
