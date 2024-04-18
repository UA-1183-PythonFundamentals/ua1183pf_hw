# x = 10
# y = 12
# print(f"{x}  {x=} {sum([1,2,3,4])} {sum([1,2,3,4])=}")

# print()
# print(f"{x=} {y=} x==y is {x==y}")
# print(f"x={x}x {y=} x!=y is {x!=y}")
# print(f"{x=} {y=} x>y is {x>y}")
# print(f"{x=} {y=} x<y is {x<y}")
# print(f"{x=} {y=} x>=y is {x>=y}")
# print(f"{x=} {y=} x<=y is {x<=y}")

# x = 12
# y = 12
# print(f"{x=} {y=} x==y is {x==y}")
# print(f"x={x}x {y=} x!=y is {x!=y}")
# print(f"{x=} {y=} x>y is {x>y}")
# print(f"{x=} {y=} x<y is {x<y}")
# print(f"{x=} {y=} x>=y is {x>=y}")
# print(f"{x=} {y=} x<=y is {x<=y}")

# x = 1
# y = 0
# print(x, not x)
# print(y, not y)

# a , b = True, True
# print(f"A and B => {a and b}", f"A or B => {a or b}")
# a , b = True, False
# print(f"A and B => {a and b}", f"A or B => {a or b}")
# a , b = False, True
# print(f"A and B => {a and b}", f"A or B => {a or b}")
# a , b = False, False
# print(f"A and B => {a and b}", f"A or B => {a or b}")

# print(True and True and False or True)
# print(True and 1 and "abc")


# is_false = [False, 0, 0.0, None, "", (), [], {}]
# print([1,2] and "123" and 0.0001)
# print([] and "22" and 0.0001)

# a = [1,2,3]
# b = [1,2,3]
# c = a
# print(a is b)
# print(a == b)
# print(a is c)
# print(a is not b)

# a = [1,2,3,4,5,6, (11,12, 13),]
# b = "programmer"
# print(5 in a)
# print(11 in a)
# print((11,12) in a)
# print(() in a)

# print("rog" in b)
# print("m" in b)
# print("m" not in  b)
# print("Xm" not in  b)


# score = int(input("score: "))
# if score > 8:
#     print("You have passed the exam")
#     print(f"{score}>8")

# print("Exam was finished.")

# temperature = float(input('What is the temperature? '))
# if temperature > 30:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')
# print('Get some exercise outside.')


# age = int(input('age: '))
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')

# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')
# if age < 12:
#     print('kid')

# if age < 18:
#     print('teenager')

# if age < 50:
#     print('adult')
# else:
#     print('you are not old')
# b = int(input("number "))
# t = "isTrue" if b else "isFalse"
# t = b ? "isTrue" : "isFalse"
# print(t)
# t = None
# if b:
#     t = "isTrue"
# else:
#     t = "isFalse"
# print(t)

# t = 12+5 if b else sum((1,2,3,4,5))
# print(t)
# status = int(input('HTTP status code: '))

# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
# if status == 400:
#     print("Bad request")
# elif status == 401:
#     print("Unauthorized")
# elif status ==  403:
#     print("Forbidden")
# elif status ==  404:
#     print("Not found")
# else:
#     print("Other error")


# match status:
#     case 400:
#         print("Bad request")
#     case 401 | 403 as s:
#         print(f'{s} is authentication error')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")




# values = ("load", "http://test.ua")
# values = ("save", "http://test.ua", "test.txt")
# values = ("save", "http://test.ua", "out_1.txt","out_2.txt","out_3.txt")



# match values:
#     case "load", link:
#         print(f"load {link=}")
#     case "save", link, filename:
#         print(f"save {link=} in {filename}")
#     case "save", link, *filenames:
#         print(f"save {link=} in")
#         for filename in filenames:
#             print("\t", link, filename)
#     case _:
#         print("default:", values)


l = [
    ("load", "http://test.ua"),
    ("save", "http://test.ua", "test.txt"),
    ("save", "http://test.ua", "out_1.txt","out_2.txt","out_3.txt")]

for val in l:

    match val:
        case "load", link:
            print(f"load {link=}")
        case "save", link, filename:
            print(f"save {link=} in {filename}")
        case "save", link, *filenames:
            print(f"save {link=} in")
            for filename in filenames:
                print("\t", link, filename)
        case _:
            print("default:", values)