#1. Jenny's secret message
def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"

#2. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5), 2)

#3. No yelling!
def filter_words(st):
    words = st.split()
    words1 = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    words1 = ' '.join(words1)
    return words1

#4. Convert a Number to a String
def number_to_string(num):
    return str(num)

#5. Reversing Words in a String
def reverse(st):
    result = st.split()
    return ' '.join(result[::-1])

#6. Reverse List Order
def reverse_list(l):
    return l[::-1]

#7. Multiples of 3 or 5
def solution(number):
    def solution(number):
        total_sum = 0
        for number in range(1, number):
            if number % 3 == 0 or number % 5 == 0:
                total_sum += number
        return total_sum

#8. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance1 = mpg * fuel_left
    return distance1 >= distance_to_pump

#9. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#10. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"

#11. Counting sheep
def count_sheeps(sheep):
    count = 0
    for present in sheep:
        if present:
            count += 1
    return count

#12. Is this my tail?
def correct_tail(body, tail):
    sub = body[len(body)-len(tail):]
    if sub == tail:
        return True
    else:
        return False
