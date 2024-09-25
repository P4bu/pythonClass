#Leer un archivo linea por linea
""" with open('manejoArchivos/cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip()) # Eliminar saltos de lineas 
"""

#Leer todas las lineas en un lista
""" with open('manejoArchivos/cuento.txt', 'r') as file:
    for lineas in file:
        lineas = file.readline()
        print(lineas) 
"""

#Añadir texto a : append
""" with open('manejoArchivos/cuento.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")
"""

#Sobreescribir el texto w : borra todo por el texto
with open('manejoArchivos/cuento.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")