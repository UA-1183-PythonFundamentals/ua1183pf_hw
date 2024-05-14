#1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#2
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

#3
def filter_words(st):
    return " ".join((st[0].upper() + st[1:].lower()).split())

#4
def number_to_string(num):
    return str(num)

#5
def reverse(st):
    s = st.split()
    return ' '.join(s[::-1])

#6
def reverse_list(list):
  list.reverse()
  return list

#7
def solution(number):
    sum = 0
    for i in range(number):
        if(i % 3) == 0 or (i % 5) == 0:
            sum += i 
    return sum 

#8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left*mpg >= distance_to_pump

#9
def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    
#10
def bool_to_word(bool):
    if bool:
        return 'Yes'
    else:
        return 'No'
    
#11
def count_sheeps(sheep):
    return sum([1 for s in sheep if s])

#12
def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False