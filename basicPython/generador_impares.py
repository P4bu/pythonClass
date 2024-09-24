# generador de impares 

def generador_impares(n):
    for i in range(1, n + 1, 2):
        yield i

# Usar el generador
impares = generador_impares(10)

for num in impares:
    print(num)

