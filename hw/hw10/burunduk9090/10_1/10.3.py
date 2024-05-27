class Employee:
    """ Represents the employee object """

    counter = 0
    all_info = ''

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
        Employee.all_info += f'Name: {self.name}\t\t\tSalary: {self.salary}\n'

    def print_info(self):
        print("Name:", self.name)
        print('Salary:', self.salary)

    @classmethod
    def count_employee(cls):
        print("Employee Count:", Employee.counter)

    @classmethod
    def print_all_info(cls):
        print("All Info:")
        print(cls.all_info)


print("Base:", Employee.__base__)
print("Dict:", Employee.__dict__)
print("Name:", Employee.__name__)
print("Module:", Employee.__module__)
print("Doc:", Employee.__doc__)
