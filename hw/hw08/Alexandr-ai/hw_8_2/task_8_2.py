import re

def is_valid_password(password):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"
    
    if re.match(pattern, password):
        return True
    else:
        return False

password = input("Enter your password: ")



# if is_valid_password(password) is True:
#     print("Good valid password")
# else:
#     print("Not valid password")

print("Good valid password") if is_valid_password(password) else print("Not valid password")
