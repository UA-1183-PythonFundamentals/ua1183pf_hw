n = int(input("Enter a number: "))

a = 0 
b = 1
while a <= n:
    print(a, end=" ")
    a = b 
    b = a+b
    
# def enter_fibonacci(n):
#     a, b = 0, 1
#     while a <= n:
#         print(a, end=" ") 
#         a, b = b, a + b    

# enter_fibonacci(n)


    
