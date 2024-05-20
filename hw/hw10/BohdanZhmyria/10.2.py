class Human:
    def __init__(self, name):
        self.name = name
    def welcome_message(self):
        print("Welcome " + self.name + "!")

    @classmethod
    def species(cls):
        print("This is a species of Homosapiens")

    @staticmethod
    def static_method():
        print("This is a static method")

human1 = Human("Bohdan")
human1.welcome_message()
Human.species()
Human.static_method()
