# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, dear!"
    else:
        return "Hello, " + name
    

# Find The Distance Between Two Points
import math


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)


# No yelling!
def filter_words(sentence):
    words = sentence.split()  
    words[0] = words[0].capitalize()  
    filtered_sentence = ' '.join(words)   
    return filtered_sentence
 

# Convert a Number to a String
def number_to_string(number):
    return str(number)


# Reversing Words in a String
def reverse_list(lst):
    return lst[::-1]


# Reverse List Order
def reverse_list(lst):
    return list(reversed(lst))


# Multiples of 3 or 5
def sum_of_multiples(n):
    if n < 0:
        return 0

    total = 0
    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total


# Will you make it?
def can_reach_pump(distance_to_pump, remaining_fuel):
    max_distance = remaining_fuel * 25
    return max_distance >= distance_to_pump


# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


#  Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
# Counting sheep
def count_sheeps(array):
    count = 0
    for sheep in array:
        if sheep == True: 
            count += 1
    return count


# Is this my tail?
def correct_tail(body, tail):
    last_char = body[-1]
    
    if last_char == tail:
        return True
    else:
        return False