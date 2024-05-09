# Task 2
user_num = int(input("Enter your num: "))
result = [0, 1]

i = 0
while i < user_num:
    fibonacci = result[i] + result[i + 1]

    if fibonacci >= user_num:
        break

    result.append(fibonacci)
    i += 1

print(result)
