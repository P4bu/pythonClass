# generador de pares
def generador_pares(n):
    for i in range(0, n + 1, 2):
        yield i

pares = generador_pares(10)

for num_par in pares:
    print(num_par)
