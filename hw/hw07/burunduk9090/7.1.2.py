def area_of_circle(radius):
    area = 3.14 * radius * radius
    return f"Area of circle is {area}"


def area_of_rectangle(width, height):
    area = width * height * 2
    return f"Area of rectangle is {area}"


def area_of_triangle(height, base):
    area = 1 / 2 * base * height
    return f"Area of triangle is {area}"


user_choice = input("Enter your choice [circle, rectangle, triangle] or 'exit' to exit: ")

while user_choice != "exit":

    if user_choice.lower() == "circle":
        area_data = int(input("Enter radius: "))
        print(area_of_circle(area_data))
    elif user_choice.lower() == "rectangle":
        area_data_width = int(input("Enter width: "))
        area_data_height = int(input("Enter height: "))
        print(area_of_rectangle(area_data_width, area_data_height))
    elif user_choice.lower() == "triangle":
        area_data_height = int(input("Enter height: "))
        area_data_base = int(input("Enter base: "))
        print(area_of_triangle(area_data_base, area_data_height))

    user_choice = input("Enter your choice [cirlce, rectangle, triangle] or 'exit' to exit: ")
