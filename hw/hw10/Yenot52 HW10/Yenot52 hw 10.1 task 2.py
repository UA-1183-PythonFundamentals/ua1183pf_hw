class Human:
  species = "Homosapiens"  

  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Welcome, {self.name}!")

  @classmethod
  def get_species(cls):
    return f"Human is a species of {cls.species}."

  @staticmethod
  def random_message():
    messages = [
      "It's a beautiful day!",
      "Hello from the world of humans!",
      "Let's learn some Python!",
    ]
    import random
    return random.choice(messages)


# Example usage
person1 = Human("Anastasia")
person1.greet()  # Output: Welcome, Anastasia!

print(Human.get_species())  # Output: Homosapiens (using class method)

print(Human.random_message())  # Output: (one of the random messages)
