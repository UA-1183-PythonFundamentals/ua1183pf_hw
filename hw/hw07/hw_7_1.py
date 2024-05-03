import math


#Task 1
def biger_number(a, b):
    '''This function return biger value'''

    return a if a >= b else b
    
a = int(input('Input your first number :'))
b = int(input('Input your second number :'))

if type(a) is int and type(b) is int:
    result = biger_number(int(a), int(b))
    print(result)
else:
    "value must be a number"




#Task 2
def rectangle_area(c, d):
    '''This function return area of rectangle'''
    if type(c) is int and type(d) is int:
        return c * d
    else:
        return "value must be a number"
    

def triangle_area(a, h):
    '''This function return area of triangle'''
    if type(a) is int and type(h) is int:
        return (1 / 2 * (a * h))
    else:
        return "value must be a number"
    

def circle_area(r):
    '''This function return area of circle'''
    if type(r) is int:
        return math.pi * r ** 2
    else:
        return "value must be a number"
    
c = int(input('If you want calculate area of rectangle input first number > 0 :'))
d = int(input('If you want calculate area of rectangle input second number > 0 :'))
t = int(input('If you want calculate area of triangle input number > 0 :'))
h = int(input('If you want calculate area of triangle input hight number > 0 :')) 
r = int(input('If you want calculate area of triangle input radius number > 0 :')) 



if type(c) is int and type(d) is int and int(c) > 0 and int(d) > 0:
    rectangle_area = rectangle_area(a, b)
    print('rectangle area is:', rectangle_area)


if type(t) is int and type(h) is int and int(t) > 0 and int(h) > 0:
    triangle_area = triangle_area(t, h)
    print('triangle area is:', triangle_area)

if type(r) is int and int(r) > 0:
    circle_area = circle_area(r)
    print('circle area is:', circle_area)