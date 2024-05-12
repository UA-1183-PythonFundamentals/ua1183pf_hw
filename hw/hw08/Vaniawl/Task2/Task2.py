import re
def validate_password(password):
    if not 6 <= len(password) <= 16:
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.search('[!@_.,#$]', password):
        return False
    return True
def main():
    password = input('Enter password: ')
    if validate_password(password):
        print('Password is valid')
    else:
        print('Password is invalid')

if __name__ == '__main__':
    main()
