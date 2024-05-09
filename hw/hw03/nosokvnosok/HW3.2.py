# Введення та демонстрація значення
print("Write your four-digit natural number: ")
num = input()
print(f"Your four-digit natural number is {num}, type of your number is {type(num)}")

# Переведення у list
num = list(num)
print(f"Your four-digit natural number as the list is {num}, type of this object is {type(num)}")

# Переведення у int кожного значення з list
num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])
num[3] = int(num[3])

# Знаходження добутка усіх окремих елементів
product = num[0] * num[1] * num[2] * num[3]
print(f"The product of the digits of this number is {product}, type of product is {type(product)}")

# Розвертання числа як str і переведення у int
revStr = f"{num[3]}{num[2]}{num[1]}{num[0]}"
revInt = int(revStr)
print(f"Your four-digit reversed natural number is {revInt}, type of this object is {type(revInt)}")

sortNum = sorted(num)
sortStr = f"{sortNum[0]}{sortNum[1]}{sortNum[2]}{sortNum[3]}"
sortInt = int(sortStr)
print(f"Your four-digit sorted natural number is {sortInt}, type of this object is {type(sortInt)}")
