def area_of_rectangle(width, height):
    """
    Обчислює площу прямокутника.
    
    Параметри:
    width (float): Ширина прямокутника.
    height (float): Висота прямокутника.
    
    Повертає:
    float: Площа прямокутника.
    """
    return width * height

def area_of_triangle(base, height):
    """
    Обчислює площу трикутника.
    
    Параметри:
    base (float): Довжина основи трикутника.
    height (float): Висота трикутника.
    
    Повертає:
    float: Площа трикутника.
    """
    return 0.5 * base * height

def area_of_circle(radius):
    """
    Обчислює площу кола.
    
    Параметри:
    radius (float): Радіус кола.
    
    Повертає:
    float: Площа кола.
    """
    pi = 3.14
    return pi * radius ** 2