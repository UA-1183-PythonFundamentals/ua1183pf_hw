# # I. Jenny's secret message:
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)
#
# II. Find The Distance Between Two Points
# from math import sqrt
# def distance(x1, y1, x2, y2):
#     return round(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)), 2)
#
# III. No yelling!
# def filter_words(st):
#     st = " ".join(st.split())
#     return st.capitalize()
#
# IV. Convert a Number to a String
# def number_to_string(num):
#     return str(num)
#
# V. Reversing Words in a String
# def reverse(st):
#     st = st.split()
#     st.reverse()
#     b = " ".join(st)
#     return b
#
# VI. Reverse List Order
# def reverse_list(l):
#     l = list(l)
#     l.reverse()
#     return l
#
# VII. Multiples of 3 or 5
# def solution(number):
#     sum = 0
#     if number < 0:
#         return 0
#     else:
#         for i in range(number):
#             if i % 3 == 0 or i % 5 == 0:
#                 sum = sum + i
#         return sum
#
# VIII. Will you make it?
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if mpg*fuel_left >= distance_to_pump:
#         return True
#     else:
#         return False
#
# IX. Are You Playing Banjo?
# def are_you_playing_banjo(name):
#     if name.lower()[0] == 'r':
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"
#
# X. Convert boolean values to strings 'Yes' or 'No’
# def bool_to_word(boolean):
#     return 'Yes' if boolean else 'No'
#
# XI. Counting sheep
# def count_sheeps(sheep):
#     count = 0
#     for i in range(len(sheep)):
#         if sheep[i]:
#             count += 1
#         else:
#             continue
#     return count

# # XII. Is this my tail?
# def correct_tail(body, tail):
#     sub = body[-1]
#     sub_1 = tail[0]
#     if sub == sub_1:
#         return True
#     else:
#         return False
