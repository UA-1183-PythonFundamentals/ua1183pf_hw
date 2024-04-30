
'''#1 task
l = [1, 2, 3]
print(type(l[0]))

for i in l:
    i = float(i)
    print(type(i), i)

#2 task
l = [0, 1]
n = int(input('input n number: '))

#while len(l) < 10:
while l[-1] <= n:
    
    la = l[-2] + l[-1]
    if la <= n:
        l.append(la)
    else:
        break
    
print(l)'''


#3 task
n = int(input('input n number: '))
print(range(1, n))
fact = 1
for i in range(1, n+1):
    fact *= i

print('Factorial result :', fact)

    

