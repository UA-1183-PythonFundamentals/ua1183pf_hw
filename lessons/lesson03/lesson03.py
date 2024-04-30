# print("a")

# print(object)

# a = 13
# print(a, id(a),type(a))
# a = 14
# print(a, id(a),type(a))
# a = (1,2,3)
# print(a, id(a),type(a))
# # a[1] = 15 #error
# a = [1,2,3]
# print(a, id(a),type(a))
# a[1] = 100
# print(a, id(a),type(a))
# a.append(11)
# print(a, id(a),type(a))
# print(a, id(a),type(a) is list)
# print(a, id(a),type(a) == "<class 'list'>")
# print("test1");print("test1");print("test1"); 
# for i in range(5):
#     for j in range(5):
#         print(i, j)
#         print(j+i)
#     print(">"*10)


# a = [12,3,7]
# b = (1,2,3)
# c = "asdg"
# d = 15
# f = [a,b,c,d]
# a.append(["a", "b"])
# print(f)

# PI = 3.14
# print(PI)

# PI += 1
# print(PI)

# from math import pi
# print(pi)

# a = 10
# print(a,type(a))
# a = 0b10
# print(a, type(a))

# a = 0o10
# print(a, type(a))

# a = 0x10
# print(a, type(a))

# for i in range(20):
#     print(f"{i}\t{bin(i)[2:]}\t{oct(i)[2:]}\t{hex(i)[2:]}")
#     # print(f"{i}\t{bin(i)}\t{oct(i)}\t{hex(i)}")

# a = 100000
# print(a, type(a))

# a = 100_000_000
# print(a, type(a))

# a = 100000
# print(a, type(a))

# a = 100_000.001
# print(a, type(a))

# a = 0.0
# print(a, type(a))
# a = 0.
# print(a, type(a))
# a = .0
# print(a, type(a))
# e = 10
# a = 15e3
# print(a, type(a))
# a = 15e-3
# print(a, type(a))
# a = 1.5e-3
# print(a, type(a))


# t = True

# f = False

# a = ""



# def f(n):
#     if n>0:
#         return n
    
# print(f(1))
# print(f(-1))


# s = "0123abc0123"
# print(s, len(s))
# l = list(s)
# print(l, len(s))
# print(l[5])
# s = "asadfadsasdadsasdasdadsaAsdadsaf"
# print(set(s))

# for i in range(255):
#     print(f"{i} - {chr(i)}")

# for i in s:
#     print(f"{i} - {ord(i)}")

# d = {
#     "key": "value",
#     1: 12,
#     234: "aaa"
# }
# print(d)
# print(d[234])
# # print(d[233]) # error
# print(d.get(233))
# d = {}
# print(type(d))
# d = set()
# print(type(d))



# a = int("34")
# print(a) 
# a = int("34", 16)
# print(a) 

# a= float("333")
# print(a)
# a= float(22)
# print(a)
# c = eval("3 + 5 + 6")
# print(c)
# s = str(a)
# print(s, type(s))


# s = "hy 'andry'"
# print(s)
# s = 'hy \'andry\''
# print(s)



# name = input("name: ")
# age = float(input("age: "))
# template = "Hello, %s! age: %.4f %s"
# result = template % (name, age, name)
# print(result)

# template = "Hello, {}! age: {}"
# result = template.format(name, age)
# print(result)
# template = "Hello, {n}! age: {k} {n}"
# result = template.format(n=name, k=age)
# print(result)


# result = f"Hello, {name.upper() }! age: {333.3 -float(age) } {name}"
# print(result)


str = 'programiz'
print(list(enumerate(str)))
print('str = ', str)
print(str[0])
print(str[-1], str[-2])

print(str[0:4])
print(str[2:-2])
print(str[:-2])
print(str[3:])
print(str[::2])
print(str[::-1])
str = list('programiz')
print(list(enumerate(str)))
print('str = ', str)
print(str[0])
print(str[-1], str[-2])

print(str[0:4])
print(str[2:-2])
print(str[:-2])
print(str[3:])
print(str[::2])
print(str[::-1])
strin = 'programiz'
