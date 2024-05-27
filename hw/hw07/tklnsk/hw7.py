#Task 1
def largest_number():
    """This function returns the largest number between n1 and n2"""
    n1 = int(input("Enter your first number: "))
    n2 = int(input("Enter your second number: "))
    if n1 > n2:
        return n1
    else:
        return n2
result = largest_number()
print(f"The largest number is: {result}")

#Task 2

import math
def area_of_rectangle(length, width):
    return length * width
def area_of_triangle(base, height):
    return 1 / 2 * base * height
def area_of_circle(radius):
    return math.pi * radius ** 2

def main():
    print("What do you want to calculate?")
    print("a. Area of rectangle \n"
          "b. Area of triangle \n"
          "c. Area of circle \n"
          )
    user = input("Enter a, b or c \n ")

    if user == "a":
        height = float(input("Enter the height: \n "))
        length = float(input("Enter the length: \n "))
        area = area_of_rectangle(length, height)
        print("Area of rectangle", area)

    elif user == "b":
        height = float(input("Enter the height: \n "))
        width = float(input("Enter the width: \n "))
        area = area_of_triangle(height, width)
        print("Area of triangle", area)

    elif user == "c":
        radius = float(input(" Enter the radius: \n "))
        print("Area of circle", round(area_of_circle(radius), 2))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

#Task 3
def count_letters(word):
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1
    return count
word = str(input("Enter a word: "))
print(count_letters(word))

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    if max_distance >= distance_to_pump:
        return True
    else:
        return False
# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
# Counting sheep...
def count_sheeps(sheep):
    count = 0
    for sheep in sheep:
        if sheep == True or sheep is None:
            count += 1
    return count
