# Fibonacci
# 0 1 1 2 3 5 8 13 21 34 55 

def fibonacci(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a+b 

for num in fibonacci(100):
    print(num)
