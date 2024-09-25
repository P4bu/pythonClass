

with open('manejoArchivos/cuento.txt', 'r') as file:
    lineas = file.readline()
    print(len(lineas))

# Otra forma
conteo = 0
with open('manejoArchivos/cuento.txt', 'r') as file:
    for line in file:
        conteo += 1
print(conteo)    