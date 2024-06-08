# Write a Python program to check the validity of a password (input from users)

def validate_password(password):

    if len(password) < 6 or len(password) > 16:
        return False
    
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for char in password:
    
        if 'a' <= char <= 'z':
            has_lowercase = True
        elif 'A' <= char <= 'Z':
            has_uppercase = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in "$#@*&!)()":
            has_special = True
    
    if has_lowercase and has_uppercase and has_digit and has_special:
        return True
    else:
        return False

password = input("Enter a password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid")
