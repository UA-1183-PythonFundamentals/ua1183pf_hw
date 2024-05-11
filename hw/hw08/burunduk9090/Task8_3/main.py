from calculate_area import *

user_choice = input("Enter your choice [circle, rectangle, triangle] or 'exit' to exit: ")

while user_choice != "exit":

    if user_choice.lower() == "circle":
        area_data = int(input("Enter radius: "))

        print(area_circle(area_data))
    elif user_choice.lower() == "rectangle":
        area_data_width = int(input("Enter width: "))
        area_data_height = int(input("Enter height: "))

        print(area_rectangle(area_data_width, area_data_height))
    elif user_choice.lower() == "triangle":
        area_data_height = int(input("Enter height: "))
        area_data_base = int(input("Enter base: "))

        print(area_triangle(area_data_base, area_data_height))

    user_choice = input("Enter your choice [cirlce, rectangle, triangle] or 'exit' to exit: ")
