# Fibonacci numbers module fibo.py
def fib(n): # write Fibonacci series up to n
    a, b = 1, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
        print()
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b =1, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    print(f"{__name__=}")