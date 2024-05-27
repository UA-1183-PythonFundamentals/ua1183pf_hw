# Create a class Human, everyone has a name, create a method in the class that displays a welcome message to each person. 
# Create a class method in the class that returns information that it is a species of "Homosapiens". 
# And in the class create a static method that returns an arbitrary message. 

class Human:
    species = "Homosapiens"
    
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        return f"Welcome, {self.name}!"
    
    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}."
    
    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message"

user1 = Human("Hanna")
print(user1.welcome_message())
print(user1.get_species())
print(user1.arbitrary_message())

