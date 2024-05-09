login = "First"
user = input("Enter your login: ")
while user == login:
    print("User authorised")
    break
while user != login:
    print("Error")
    break