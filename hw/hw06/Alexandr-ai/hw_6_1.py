


#Task 1
n = range(1, 10)
print(n)
even = []
odd = []
not_divisible = []

for i in n:
    if  i%2 == 0:
        even.append(i)
        #print(even)
    elif i%3 == 0 and i%2 == 1:
        odd.append(i)
        #print(odd)
    elif i%2 !=2 and i%3 != 3:
        not_divisible.append(i)
        #print(not_divisible)

print('even' , even)
print('odd' , odd)
print('not_divisible' , not_divisible)


#Task 2


while True:
    login = input('Input your login please :')

    if login == "First":
        print("Greating !!!")
        break
    else:
        print("Sorry, can you inpunt correct login")
