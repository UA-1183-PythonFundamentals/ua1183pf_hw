# Write a Python program to check the validity of a password (input from users)

def validate_password(password):

    # Check if password length is between 6 and 16 characters
    if len(password) < 6 or len(password) > 16:
        return False
    
    # Initialize flags to track if password meets each condition
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    
    # Check each character in the password
    for char in password:
        # Check if character is a lowercase letter
        if 'a' <= char <= 'z':
            has_lowercase = True
        # Check if character is an uppercase letter
        elif 'A' <= char <= 'Z':
            has_uppercase = True
        # Check if character is a digit
        elif '0' <= char <= '9':
            has_digit = True
        # Check if character is one of the special characters
        elif char in "$#@":
            has_special = True
    
    # Check if all conditions are met
    if has_lowercase and has_uppercase and has_digit and has_special:
        return True
    else:
        return False

# Test the function
password = input("Enter a password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid")
