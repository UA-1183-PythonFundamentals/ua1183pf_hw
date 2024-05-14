class Human:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Hello, " + self.name)

    def print_species(self):
        print(f'{self.name}: Homosapiens')

    @staticmethod
    def print_message():
        print('Python Fundamentals')


a = Human("Bob")

a.print_name()
a.print_species()
a.print_message()
