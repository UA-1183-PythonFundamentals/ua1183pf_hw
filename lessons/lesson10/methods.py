# class A:
#     def f1(self):
#         print(type(self), self)

#     @classmethod
#     def f2(cls):
#         print(type(cls), cls)

#     @staticmethod
#     def f3(self):
#         print(type(self), self)


# a = A()
# a.f1()
# # A.f1()#TypeError: A.f1() missing 1 required positional argument: 'self'

# a.f2()
# A.f2()

# a.f3("aa")
# A.f3("AA")


# class Model:
#     @classmethod
#     def pp(cls):
#         cls.objects
#     @classmethod
#     def select_all(cls):
#         sql = f"SELECT * FROM {cls.TABLE_NAME}"
#         print(sql)
#     def p(self):
#         print(self.objects)
# class User1(Model):
#     TABLE_NAME = "User"
#     objects = []
#     def __init__(self) -> None:
#         self.objects.append("User1")

# class User2(Model):
#     TABLE_NAME = "test"
#     objects = []
#     def __init__(self) -> None:
#         self.objects.append("User2")


# a = User1()
# User1()
# b = User2()
# User1()
# User1()
# User2()

# print(User1.objects)
# print(User2.objects)
# a.p()

# b.p()
# User1.pp()
# User2.pp()
# User1.select_all()
# User2.select_all()


class A:
    def __init__(self) -> None:
        self.a = 1
        self._a = 2
        self.__a = 3
        def f(a,b):
            print(a, b)
        self.f = f
    def p(self):
        print(self.a)
        print(self._a)
        print(self.__a)
class J(A):
    def __init__(self) -> None:
        super().__init__()
        def f():
            print("a, b")
        self.g = f
a = A()
print(a.a)
print(a._a)
print(a._A__a)
a.p()
a.f(1,2)

j = J()
j.f(1,2)
j.g()

# lambda a: a**2

# def f(a):
#     return a**2