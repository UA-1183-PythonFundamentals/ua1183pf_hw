class Employee:
  employee_count = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.employee_count += 1  # Increment counter on object creation

  def get_info(self):
    print(f"Name: {self.name}")
    print(f"Salary: ${self.salary:.2f}")

  @classmethod
  def print_total_employees(cls):
    print(f"Total Employees: {cls.employee_count}")

# Create some employee objects
emp1 = Employee("Ivan", 50000)
emp2 = Employee("Anastasia", 65000)

# Print information about each employee
emp1.get_info()
emp2.get_info()

# Print total number of employees
Employee.print_total_employees()