# Fibonacci
# 0 1 1 2 3 5 8 13 21 34 55 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = 6
print(fibonacci(number))    