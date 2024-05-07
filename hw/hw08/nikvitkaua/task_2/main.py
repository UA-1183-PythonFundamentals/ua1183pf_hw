import re

def is_valid_password(password):
    has_lower_char = len(re.findall("[a-z]", password))
    has_upper_char = len(re.findall("[A-Z]", password))
    has_nums = len(re.findall("[0-9]", password))
    has_special_char = len(re.findall('[$, #, @]', password))
    password_length = len(password)

    if has_lower_char > 0 and has_upper_char > 0 and has_nums > 0 and has_special_char > 0 and password_length > 6 and password_length < 17:
        return True
    else:
        return False