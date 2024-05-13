import re

password = str(input("Enter a password: "))

if len(password) < 6 or len(password) > 16:
    print("Password must be between 6 and 16 characters.")
    exit()

if not re.search("[a-z]", password):
    print("Password is invalid: It must contain at least one lowercase letter.")
    exit()

if not re.search("[A-Z]", password):
    print("Password is invalid: It must contain at least one uppercase letter.")
    exit()

if not re.search("[0-9]", password):
    print("Password is invalid: It must contain at least one digit.")
    exit()

if not re.search("[!@#$]", password):
    print("Password is invalid: It must contain at least one of the characters '@', '#', or '$'.")
    exit()

print("Password is valid")