# class Car:
#     """this class car """
#     def print(self):
#         print(self)


# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# print(type(Car))
# print(type(car_1))
# car_1.print()
# car_2.print()
# car_3.print()

# class Car:
#     """this class car """
#     cm = [1,2,3]
#     ci = 17
#     def __init__(self, im, ii):
#         self.im = im
#         self.ii = ii
#     def print(self):
#         print(self)


# car_1 = Car([99], 17)
# car_2 = Car([88], 8)

# print(Car.cm, Car.ci)
# # print(Car.ii)#AttributeError: type object 'Car' has no attribute 'ii'. Did you mean: 'ci'?
# print(car_1.cm, car_1.ci, car_1.im, car_1.ii)
# print(car_2.cm, car_2.ci, car_2.im, car_2.ii)
# car_1.cm.append(55)
# car_1.im.append(55)
# print(car_1.cm, car_1.ci, car_1.im, car_1.ii)
# print(car_2.cm, car_2.ci, car_2.im, car_2.ii)

# print(dir(Car))
# print(dir(car_1))
# print(Car.__dict__)
# print(car_1.__dict__)
# car_1.print()
# # Car.print()#TypeError: Car.print() missing 1 required positional argument: 'self'
# Car.print(car_1)

# f = Car.print
# f("sss")

# def my_print(obj, text):
#     print(obj, text)

# my_print(car_1, "test_1")
# Car.print2 = my_print
# Car.print2(car_1, "tets_2")
# car_1.print2("test_3")
# import random

# class Car:
#     """this class car"""

#     def __init__(self, marka, color, max_speed):
#         self.marka = marka
#         self.color = color
#         self.max_speed = max_speed
#         self.current_speed = 0
#     # def __del__(self):
#     #     print("delete", self)

#     def __str__(self):
#         return f"car: {self.marka} {self.color} {self.current_speed} {self.max_speed}"
#     def __repr__(self):
#         return f"CAR<{self.marka} {self.color} {self.current_speed}>"
#     def __add__(self, other):
#         marka = random.choice([self.marka, other.marka])
#         color = random.choice([self.color, other.color])
#         max_speed = random.choice([self.max_speed, other.max_speed])
#         return Car(marka, color, max_speed)
    
#     def set_speed(self, speed):
#         if speed < 0:
#             self.current_speed = 0
#         elif speed > self.max_speed:
#             self.current_speed = self.max_speed
#         else:
#             self.current_speed = speed

#     def accelerate(self):
#         print("accelerate", self)
#         self.set_speed(self.current_speed + 5)

#     def barke(self):
#         if self.current_speed<5:
#             self.current_speed = 0
#         else:
#             self.current_speed -= 5
#     def __lt__(self, other):
#         return self.current_speed < other.current_speed


# car_1 = Car("BMW", "silver", 250)
# car_2 = Car("LAZ", "red", 120)
# print(car_1.marka, car_1.color, car_1.current_speed, car_1.max_speed)
# print(car_2)
# print(car_1)

# print(car_1.__dict__)
# print(car_2.__dict__)
# car_1.set_speed(300)
# print(car_1)

# car_1.set_speed(0)
# car_3 = Car("alfa romeo", "blue", 350)
# cars = [car_1, car_2, car_3]
# print(cars)
# # run = True
# # while run:

# #     index = random.randint(0, len(cars)-1)
# #     cars[index].accelerate()

# #     for car in cars:
# #         if car.current_speed == car.max_speed:
# #             print("win", car)
# #             run = False
# #             break
#     # else:
#     #     print(cars)


# print(cars)
# cars.sort()
# print(cars)
# print(car_1 + car_2)

# class Truck(Car):
#     def __init__(self, marka, color, max_speed, max_weight):
#         super().__init__(marka, color, max_speed)
#         self.max_weight = max_weight
#     def __str__(self):
#         return "truck"+super().__str__()[3:] + f" max_weight: {self.max_weight}"
#     def __repr__(self):
#         return f"Truck({self.marka}, {self.max_weight})"
#     def accelerate(self):
#         print("accelerate Truck", self)
#         self.set_speed(self.current_speed + 2)

# tr_1 = Truck("BMW", "silver", 140, 350)
# tr_2 = Truck("LAZ", "red", 130, 350)


# print(tr_1)
# print([tr_1, tr_2])

# cars.append(tr_1)
# cars.append(tr_2)
# run = True
# while run:

#     index = random.randint(0, len(cars)-1)
#     cars[index].accelerate()

#     for car in cars:
#         if car.current_speed == car.max_speed:
#             print("win", car)
#             run = False
#             break
#     # else:
#     #     print(cars)




from mclass import A

    