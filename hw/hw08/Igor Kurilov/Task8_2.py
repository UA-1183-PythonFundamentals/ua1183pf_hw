import re

def is_valid_password(password):
    # Check if password length is between 6 and 16 characters
    if len(password) < 6 or len(password) > 16:
        return False
    
    # Check if password contains at least 1 lowercase letter
    if not re.search("[a-z]", password):
        return False
    
    # Check if password contains at least 1 uppercase letter
    if not re.search("[A-Z]", password):
        return False
    
    # Check if password contains at least 1 digit
    if not re.search("[0-9]", password):
        return False
    
    # Check if password contains at least 1 special character from [$#@]
    if not re.search("[$#@]", password):
        return False
    
    # If all conditions are met, return True
    return True

# Test the function
password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password. Password must contain at least 1 lowercase letter, 1 uppercase letter, 1 digit, 1 special character from [$#@], and have a length between 6 and 16 characters.")
