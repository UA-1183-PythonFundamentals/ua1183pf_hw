# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    d = (x2 - x1)**2 + (y2 - y1)**2
    return round(math.sqrt(d), 2)


# No yelling!
def filter_words(st):
    st = st.lower().split()

    result = " ".join(st).capitalize()
    return result


# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# Reversing Words in a String
def reverse(st):
    result = st.split()
    return ' '.join(result[::-1])


# Reverse List Order
def reverse_list(l):
    return l[::-1]


# Multiples of 3 or 5
def solution(number):
    i = 0
    result = 0

    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            result += i
        i += 1

    return result


# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False


# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"


# Counting sheep...
def count_sheeps(sheep):
    result = 0

    for s in sheep:
        if s == True:
            result += 1
        else:
            result += 0

    return result


# Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False