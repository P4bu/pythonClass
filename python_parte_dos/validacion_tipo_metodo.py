def divide(a: int, b: int) -> float:
    if not isinstance(a, int) or not isinstance(b,int):
        raise TypeError('Ambos numeros deben ser enteros o flotantes')
    if b == 0:
        raise ZeroDivisionError('El divisor no puede ser 0')
    
    return a / b

result = divide(10,0)

# Ejemplo de uso
try:
    res = divide(10, '2')
    print(res)
except TypeError as e:
    print(f'Error: {e}')    