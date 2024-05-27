class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species_info(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

# Example usage:
person = Human("Alice")
person.welcome_message()
print(Human.species_info())
print(Human.arbitrary_message())
