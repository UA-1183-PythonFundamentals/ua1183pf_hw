
#Task 10.1.1
class Polygon:
    def __init__(self, length, hight):
        self.length = length
        self.hight = hight


class Rectangle(Polygon):
    def __init__(self, length, hight):
        super().__init__(length, hight)

    def square(self):
        return self.length * self.hight
    


