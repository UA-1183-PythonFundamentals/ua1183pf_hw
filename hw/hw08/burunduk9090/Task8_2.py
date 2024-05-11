import re

pattern = r'^(?=.*\d)(?=.*[a-zA-Z])(?=.*[#@$]).{6,16}$'
while True:
    password = input("enter your password: ")

    if re.search(pattern, password):
        print("password is valid.")
    else:
        print("password is invalid.")
