#6.1
even_2 = []
odd_3 = []
not_2_3 = []
for num in range(1, 11):
    if num % 2 == 0:
        even_2.append(num)
    elif num % 3 == 0:
        odd_3.append(num)
    else:
        not_2_3.append(num)
print("even numbers that are divisible by 2: ", even_2)
print("odd numbers, which are divisible by 3: ", odd_3)
print("numbers that are not divisible by 2 and 3: ", not_2_3)

#6.2
a = "First"
user = input("Enter your login: ")
while user == a:
    print("Welcome!")
    break
while user != a:
    print("Error! Try again!")
    break
