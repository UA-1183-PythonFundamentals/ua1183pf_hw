#Task 1
def greet(name):
#     return "Hello, {name}!".format(name=name)

    if name == "Johnny":

        return "Hello, my love!"

    else:

        return "Hello, {name}!".format(name=name)
    
#Task 2
def distance(x1, y1, x2, y2):
    # Your code here
    dx = (x2 - x1) ** 2
    dy = (y2 - y1) ** 2 
    d= dx + dy
    b = d ** 0.5
    b = round(b, 2)
    
    return b

#Task 3
def filter_words(st):
    pass
    words = st.split()
    st = " ".join(words)
    return st.capitalize()


#Task 4
def number_to_string(num):
    # Return a string of the number here!
    return str(num)


#Task 5
def reverse(st):
    # Your Code Here
    words = st.strip().split()
    words.reverse()
    st = " ".join(words)
    
    return st


#Task 6 
def reverse_list(l):
    'return a list with the reverse order of l'
    r = list(reversed(l))
    return r

#Task 7
def solution(number):
#     pass
    if number <= 0:
        return 0
    
    multiples = filter(lambda x: x % 3 == 0 or x % 5 == 0, range(number))
    return sum(multiples)

#Task 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    return True if distance_to_pump <= mpg * fuel_left else False

#Task 9
def are_you_playing_banjo(name):
    # Implement me!
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
#Task 10
def bool_to_word(boolean):
    # TODO
    return "Yes" if boolean else "No"

#Task 11
def count_sheeps(sheep):
  # TODO May the force be with you
    #pass
    return sheep.count(True)

#Task 12
def correct_tail(body, tail):
                       
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False