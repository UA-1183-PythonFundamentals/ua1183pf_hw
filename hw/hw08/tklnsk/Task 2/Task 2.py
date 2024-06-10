import re
def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.search('[$#@]', password):
        return False
    else:
        return True

def main ():
    password = input('Enter the password: ')
    if is_valid_password(password):
        print('Password is valid')
    else:
        print('Password is invalid')

if __name__ == '__main__':
    main()