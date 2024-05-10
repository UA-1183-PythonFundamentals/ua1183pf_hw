class A:
    def printA(self):
        print("A")
    def printB(self):
        print("B")
    def printC(self):
        print("C")

class B(A):
    def printA(self):
        print("BA")
    def printB(self):
        print("<B>")

class C(A):
    def printA(self):
        print("CA")
    def printC(self):
        print("<C>")
class D(B, C):
    pass

d = D()

d.printA()

print(D.__mro__)

class D(C, B):
    pass

print(D.__mro__)