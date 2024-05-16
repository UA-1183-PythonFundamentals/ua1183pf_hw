# d = {}

# try:
#     print(d["a"])
# except:
#     print("error")
#     d["a"] = None

# print("test", d)

# d = {
#     "a": 10
# }
# # try:
# #     pass
# # except:
# #     pass
# # finally:
# #     print("a")

# run = True
# while run:
#     try:
#         code = input("enter code: ")
#         if code =="exit":
#             run = False
#         a = eval(code)
#     except KeyError:
#         print("KeyError")
#     except ArithmeticError as err:
#         print("ArithmeticError",f"{type(err)} {err}")
#     except (ValueError, TypeError) as err:
#         print(err)
#     except:
#         print("Error")
#     else:
#         print(a)
#     finally:
#         print("finally")


# print("end")


# rez = None
# def div(a, b):
#     global rez
#     try:
#         rez = a/b
#         return rez
#     except ZeroDivisionError:
#         return float('inf')
#     finally:
#         return "Text"   

# print(div(10, 5))
# print(rez)
# # print(div(10, 0))

# import time
# try:
#     response = request.post(url, 40)
#     if response.status ==200:
#         save()
#     time.sleep(5) 
# except:
#     print("")

# def div(a, b):
#     if b == 1:
#         raise ValueError("b is 0")
#     return a/b
# try:
#     div(5, 0)
#     div(5, 0)
# except Exception as err:
    
#     print(type(err), err)
# def div(a, b):
#     if b == 1:
#         raise 10
#     return a/b
# try:
#     div(5, 1)
#     div(5, 0)
# except Exception as err:
    
#     print(type(err), err)


from mylogs import logging
from model import User, UserException
import time
words = ["a", "b", "c", 1, 2]
import random
users = []
while len(users) < 5:
    try:
        user = User(random.choice(words), random.choice(words), random.choice(words))
    except UserException as err:
        logging.error(err)
        time.sleep(random.randint(0, 2))
    else:
        users.append(user)

print(users)




