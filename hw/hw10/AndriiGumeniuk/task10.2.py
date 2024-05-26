class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is a static method."


name = Human(input("Name is "))
print(name.greet())
print(Human.species())
print(Human.arbitrary_message())