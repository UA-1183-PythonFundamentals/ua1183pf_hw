# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# II. Find The Distance Between Two Points
import math
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

# III. No yelling!
def filter_words(st):
    words = st.split()
    formatted_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    return ' '.join(formatted_words)

#IV. Convert a Number to a String
def number_to_string(num):
    return str(num)
# V. Reversing Words in a String
def reverse(st):
    return ' '.join(st.strip().split()[::-1])

# VI. Reverse List Order
def reverse_list(l):
    return l[::-1]

# VII. Multiples of 3 or 5
def solution(n):
    if n < 0:
        return 0
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = fuel_left * mpg
    if max_distance >= distance_to_pump:
        return True
    else:
        return False
# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
# XI. Counting sheep
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count += 1
    return count


# XII. Is this my tail?
def correct_tail(body, tail):
    last_letter = body[-1]
    return last_letter == tail
