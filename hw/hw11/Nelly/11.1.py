# Write a program that prompts the user to enter their age, and then displays a message stating whether 
# the age is even or odd. The program must provide the ability to enter a negative number, and in this 
# case generate an exception. The master code should call a function that processes the information entered

def process_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    if age % 2 == 0:
        return "Ваш вік парний."
    else:
        return "Ваш вік непарний."

def main():
    try:
        age = int(input("Будь ласка, введіть свій вік: "))
        message = process_age(age)
        print(message)
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()


    