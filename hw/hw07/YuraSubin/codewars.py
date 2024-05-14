#Task 1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

#Task 2
from math import sqrt
def distance(x1, y1, x2, y2):
    return round(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)), 2)

#Task 3
def filter_words(st):
    st = " ".join(st.split())
    return st.capitalize()

#Task 4

def number_to_string(num):
    # Return a string of the number here!
    return str(num)

#Task 5

def reverse(st):
    words = st.strip().split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string

#Task 6

def reverse_list(l):
    return l[::-1]

#Task 7

def solution(number):
    if number < 0:
        return 0

    sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum += num

    return sum
#Task 8

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    distance1 = mpg * fuel_left
    return distance1 >= distance_to_pump

#Task 9

def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
#Task 10

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

#Task 11

def count_sheeps(sheep):
    return sum(1 for s in sheep if s)
#Task 12

def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False