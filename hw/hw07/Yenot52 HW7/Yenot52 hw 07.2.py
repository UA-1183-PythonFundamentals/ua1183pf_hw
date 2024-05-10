# I. Jenny's secret message

def greet(name):
    if name == "Johnny":  
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

print(greet("Jenny")) 
print(greet("Johnny"))  

# II. Find The Distance Between Two Points

from math import sqrt
def distance(x1, y1, x2, y2):
    return round(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)), 2)

#III. No yelling!

def filter_words(text):
    pass
    words = text.split()
    text = " ".join(words)
    return text.capitalize()

#IV. Convert a Number to a String

def number_to_string(num):
    return str(num)

#V. Reversing Words in a String

def reverse(st):
    st = st.split()
    reversed_st = st[::-1]
    result = ""
    for word in reversed_st:
        result += " " + word
    return result.strip()

#VI. Reverse List Order

def reverse_list(l):
    l.reverse()
    return l 

#VII. Multiples of 3 or 5

def solution(number):
    sum = 0
    for i in range(number):
        if(i % 3) == 0 or (i % 5) == 0:
            sum += i 
    return sum 
  
#VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= (mpg * fuel_left)

#IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return name + " plays banjo"
    return name + " does not play banjo"

#X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    if bool(boolean):
        return "Yes"
    else:
        return "No"
    
#XI. Counting sheep

def count_sheeps(sheep):
    return sum([1 for s in sheep if s])

#XII. Is this my tail?

def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False