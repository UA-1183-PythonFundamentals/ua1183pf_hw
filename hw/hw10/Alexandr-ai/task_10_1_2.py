class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "Static method"
    
