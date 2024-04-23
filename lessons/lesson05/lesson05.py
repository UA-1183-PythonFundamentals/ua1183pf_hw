l = [1,2,3,"qwerty", "test", 125.5]
# print(">>>")
# print("\t", l[0])
# print("<<<")
# print(">>>")
# print("\t", l[1])
# print("<<<")
# for element in l:
#     print(">>>")
#     print("\t", element)
#     print("<<<")
# i = 0
# while i < len(l):
#     print(">>>")
#     print("\t", l[i])
#     print("<<<")
#     i += 1
# correct_age = False
# while not correct_age:
#     age = input("enter age: ")
#     if age.isdigit():
#         age = int(age)
#         if 0 < age < 100:
#             correct_age = True
#         else:
#             print(f"age must be 0 > age > 100, current {age}")
#     else:
#         print("age is not digit")

# print(f"my age {age}")
# l = [1,2,3,"qwerty", "test", 125.5]

# while l:
#     element = l.pop()
#     print(f"pop {element} in {l}")

# for i in 152:
#     pass

# r = list(range(10))
# print(r)

# r = tuple(range(-5, 10))
# print(r)

# r = " ".join(map(str, range(-10, 10, 3)))
# print(r)
# int
# matrix = None
# N = 2
# # for i in range(N):
# #     row = []
# #     for j in range(N):
# #         e = input(f"a[{i}][{j}]=")
# #         row.append(e)
# #     matrix.append(row)
# i = 0
# while i <N:
#     row = []
#     j=0
#     while j < N:
#         e = input(f"a[{i}][{j}]=")
#         row.append(e)
#         j += 1
#     if matrix is None:
#         matrix = []
#     matrix.append(row)
#     i += 1

# for i in range(N):
#     for j in range(N):
#         print(matrix[i][j], end="\t")
#     print()

# n = int(input("n(n>1): "))
# i = 1
# l = []
# while i < n:
#     r = []
#     for j in range(1, i):
#         if i % j:
#             r.append( i % j)
#     if len(r)== i-2:
#         l.append(i)
#     i +=1

# # print(l)

# while i < n:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         l.append(i)
#     i +=1

# print(l)


# for i in range(5):
#     print(i, end="")
#     if i%2:
#         print( )
#         continue
#     print( " x**2=", i*i)
# else:
#     print("end for")
# print("======")

# for i in range(5):
#     pass
#     print(i, end="")
#     li = []
#     if i%2:
#         print( )
#         break
#     print( " x**2=", i*i)
# else:
#     print("end for")
# print("======")

# for i in range(5): pass



for i in range(101):
    if i % 2 != 0:
        number = i
        print(number)