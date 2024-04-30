# """
# doc module"""
# def my_print():
#     # """mdjvn;dsf
#     # jvbosdfjvb
#     # vbsdfho
#     # """
#     print(">"*10)
#     print("\tmy name")
#     print("<"*10)

# # my_print()
# # my_print()
# # my_print()
# # my_print()
# # my_print()
# # my_print()
# # my_print()
# # print(my_print)
# # f = my_print
# # f()

# res = sum([1,2,3,4,5,6])
# print(res)

# s = sum

# def sum(obj):
#     result = type(obj)
#     return result

# res = sum([1,2,3,4,5,6])
# print(res)



# sum = s
# res = sum([1,2,3,4,5,6])
# print(res)
# # help(sum)
# # help(my_print)

# print(sum.__doc__)
# print(my_print.__doc__)

# def my_f(name):
#     print(f"my name is {name}")

# my_f("Liubomyr")
# my_f("Andry")

# r = my_f("test")
# print(r)

# def my_f(name):
#     result = f"my name is {name}"
#     print(result)
#     return result*2
    

# my_f("Liubomyr")
# my_f("Andry")

# r = my_f("test")
# print(r)

# def my_sum(a, b):
#     print(f"{a}+{b}=", end="")
#     result = a+b
#     print(result)
#     return result
#     print("test")

# my_sum(1, 5)

# def is_prime(n):
#     for i in range(2, n-1):
#         print(f"{n}%{i}=> {n%i}")
#         if n%i == 0:
#             return False
#     return True

# print(is_prime(9))
# print(is_prime(26))
# print(is_prime(17))

# name = "Test"
# def print_info(name, age):
#     print(f"my name is {name}. age: {age}")

# # print_info() #TypeError: print_info() missing 2 required positional arguments: 'name' and 'age'
# #print_info("anna") #TypeError: print_info() missing 1 required positional argument: 'age'
# print_info("Liubomyr", 38)
# # print_info("Liubomyr", 38, "test") #TypeError: print_info() takes 2 positional arguments but 3 were given
# print(name)


# def print_info(name, age=18, sex="Men"):
#     print(f"my name is {name}. age: {age}. sex:{sex}")

# print_info("Liubomyr", 38)
# print_info("Anna", 18, "Women")
# print_info("Oleh")


# # def f(a, b=1, c):pass#SyntaxError: parameter without a default follows parameter with a default
# def f():pass
# print_info({1,2},[1,2,3],  f)

# type Vector = list[float]


# def scale(scalar: float, vector: Vector) -> Vector:
#     """"""
#     return str([scalar * int(num) for num in vector]) + "aaa"


# # passes type checking; a list of floats qualifies as a Vector.
# scale("dsfds", [1, 2, 3])
# new_vector = scale("2.0", [1.0, -4.2, 5.4])
# print(new_vector)



# def print_info(name, age=18, sex="Men"):
#     print(f"my name is {name}. age: {age}. sex:{sex}")

# print_info( "Women", "Anna", 18)

# print_info(sex="Women", age=99, name="Pavlo")
# # print_info(sex="Women", 99, name="Pavlo") #SyntaxError: positional argument follows keyword argument

# def greet(*names):
#     print(type(names), names)

# greet(1,2,"test", None, ["a", "b", ""])

# print

# def f(a, b, c, *args, d=10, e=55, **kwargs):
#     print(f"{a=} {b=} {c=} {args=} {d=} {e=} {kwargs=}")

# f(1,2,3)
# f(1,2,3,4,5,6,7,8,9,0, x=11, dz=22, m=[1,2,3], gg=59, d=9999)


# def print_info(name, age=18, sex="Men"):
#     print(f"my name is {name}. age: {age}. sex:{sex}")

# l = ["Anna", 28, "Women"]

# print_info(l[0], l[1], l[2])
# print_info(*l)

# d = {
#     "sex": "50/50",
#     "age": 378,
#     "name": "Pavlo"
# }
# print_info(d["name"], d["age"], d["sex"])
# print_info(age=d["age"], sex=d["sex"], name=d["name"])
# print_info(**d)

# d = {
#     "sex": "50/50",
#     "age": 378,
#     "name": "Pavlo",
#     "city": "Lviv"
# }
# # print_info(**d) #TypeError: print_info() got an unexpected keyword argument 'city'


# a = 1
# def f():
#     print(dir())

# print(dir())

# f()


# x = "global"

# def f():
#     y = "local"
#     print(x)
#     print(y)

# f()

# print(x)
# print(y)




# x = "global"

# def f():
#     x = "local"
#     print(x)

# f()
# print(x)



# x = "global"

# def f():
#     print(x) #UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#     x = "local"
#     print(x)

# f()
# print(x)


# x = "global"

# def f():
#     global x
#     print(x) #UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
#     x = "local"
#     print(x)

# f()
# print(x)

# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         print("inner", x)
#     inner()
#     print("outer", x)

# outer()
# y = "global"
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         global y
#         x = "nonlocal"
#         print("inner", x)
#     inner()
#     print("outer", x)

# outer()


# def get_funcks():
#     l = [ ]
#     def sum(a,b):
#         nonlocal l
#         l.append(f"{a}+{b}={a+b}")
#         return a+b
#     def div(a,b):
#         nonlocal l
#         l.append(f"{a}/{b}={a/b}")
#         return a/b
#     def my_print():
#         nonlocal l 
#         print(l)
#     return sum, div, my_print

# s, d, p = get_funcks()
# # s(1,2)
# p()
# s(1,2)
# d(8, 9)
# d(11, 99)
# p()
# 5! = 1*2*3*4*5
# import sys
# sys.setrecursionlimit(2000)
# def fuctorial(n):


#     if n <=0:
#         return 1
#     print(f"{n}*fuctorial({n-1})")
#     return n*fuctorial(n-1)

# f = fuctorial(5)
# print(f)
lambda a, b: a*b
def mm(a,b):
    return a*b


l = [1,2, "3", "abc", 2.5]
l.sort(key=lambda x: x if type(x) in [int, float] else len(x))
print(l)
