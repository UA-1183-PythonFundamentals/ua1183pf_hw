
# def decorator(func):
#     def inner(*args, **qwargs):
#         print("<"*10)
#         func(*args, **qwargs)
#         print(">"*10)
#     return inner


# def add(a,b):
#     print(f"{a}+{b}={a+b}")
# add = decorator(add)


# @decorator
# def mul(a,b,c):
#     print(f"{a}*{b}*{c}={a*b*c}")


# add(2,4)
# mul(2,4,3)
# add(2,4)
# mul(2,4,3)
# add(2,4)
# mul(2,4,3)

# ///////////////////////////////////////////////////////

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner


# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner

# @percent
# @star
# def add(a,b):
#     print(f"{a}+{b}={a+b}")

# @star
# @percent
# def mul(a,b,c):
#     print(f"{a}*{b}*{c}={a*b*c}")


# add(2,4)
# mul(2,4,3)
# /////////////////////////////////////////////////////////////////////////////


# def ramka(symbol, count):
#     def decorator(func):
#         def inner(*args, **kwargs):
#             print(symbol * count)
#             func(*args, **kwargs)
#             print(symbol * count)
#         return inner
#     return decorator



# @ramka("-", 20)
# @ramka("<>", 3)
# @ramka("*", 10)
# def add(a,b):
#     print(f"{a}+{b}={a+b}")





