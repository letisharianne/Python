# Fibonacci series
def fib(n):
    a, b = 1, 0
    while a <= n:
        print(a, end=' ')
        a, b = b, a+b

fib(1000)
# 