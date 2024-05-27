def rectangle(a, b):
    return a * b
def triangle(c, d):
    return 0.5 * c * d
def circle(r):
    return 3.14 * r ** 2

mauinfunc = input("Enter the type of figure you want to calculate area of:")

if mauinfunc == "rectangle":
    a = int(input("Enter the length:"))
    b = int(input("Enter the width:"))
    print("Your result: ", rectangle(a, b))
elif mauinfunc == "triangle":
    c = int(input("Enter the base: "))
    d = int(input("Enter the height: "))
    print("Your result:", triangle(b, c))
elif mauinfunc == "circle":
    r = int(input("Enter the radius: "))
    print("Your result", circle(r))