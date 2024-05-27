# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# Find The Distance Between Two Points
import math
def distance(x1, y1, x2, y2):
    # Your code here
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
# No yelling!
def filter_words(st):
    words = st.split()
    formatted_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    return ' '.join(formatted_words)
# Convert a Number to a String
def number_to_string(num):
    return str(num)
# Reversing Words in a String
def reverse(st):
    result = st.split()
    return ' '.join(result[::-1])
# Reverse List Order
def reverse_list(l):
    l = l[::-1]
    return l
# Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    s = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s
# Counting sheep...
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count
# Is this my tail?
def correct_tail(body, tail):
    sub = body[-len(tail):]
    if sub == tail:
        return True
    else:
        return False