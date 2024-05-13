class Human:
  """Class description people"""
  def __init__(self, name):
    self.name = name
      
  def greetings(self):
    print(f"Hello, {self.name}!")

  @classmethod
  def human_homo(self):
    return "This is a species of Homosapiens."
  
  @staticmethod
  def some_message():
    return "Some string"


mykyta = Human('Mykyta')
mykyta.greetings()

print(Human.human_homo())
print(Human.some_message())