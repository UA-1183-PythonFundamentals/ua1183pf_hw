import re


def valid_password(password):
    has_lower_char = len(re.findall("[a-z]", password))
    has_upper_char = len(re.findall("[A-Z]", password))
    has_nums = len(re.findall("[0-9]", password))
    has_special_char = len(re.findall('[$, #, @]', password))
    password_length = len(password)

    if (has_lower_char > 0 and has_upper_char > 0 and
            has_nums > 0 and has_special_char > 0 and
            6 < password_length < 17):
        return True
    else:
        return False


password = input("Enter a password: ")
if valid_password(password):
    print("Valid password")
else:
    print("Invalid password")
