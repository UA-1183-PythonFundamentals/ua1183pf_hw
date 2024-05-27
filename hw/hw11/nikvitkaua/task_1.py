class CustomErr(Exception):
    pass
    
def process_age(age:int):
    try:
        if age < 0:
            raise CustomErr("Age can't be negative")
        elif age % 2 == 0:
            print('Even')
        else:
            print('Odd')
    except CustomErr as err:
        print(err)
        
def main():
    user_age = int(input("Enter your age: "))
    process_age(user_age)
    
main()