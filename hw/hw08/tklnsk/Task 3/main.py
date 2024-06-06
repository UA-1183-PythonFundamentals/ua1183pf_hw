from calculations import rectangle_area, triangle_area, circle_area
def main():
    print("What would you like to calculate?")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

def choice():

    choice = input("Enter your choice: ")
    if choice == "1":
        print("Enter the values of sides:")
        a = float(input())
        b = float(input())
        print(f"Area of Rectangle is: {rectangle_area(a, b)}")
    elif choice == "2":
        print("Enter the values of sides:")
        h = float(input())
        a = float(input())
        print (f"Area of Triangle is: {triangle_area(h, a)}")
    elif choice == "3":
        print("Enter the values of sides:")
        r = float(input())
        print(f"Area of Circle is: {circle_area(r)}")
    else:
        print("Wrong number. Try again.")



choice()
