squares = [a ** 2 for a in range(1,11)]
print(squares)

# matriz transpuesta
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [[row[i]for row in matriz] for i in range(len(matriz[0]))]
print(matriz)
print(transposed)


"""Doble de los Números
Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension."""
listNumber = [1, 2, 3, 4, 5]
doble = [x * 2 for x in listNumber]
print(doble)

"""Filtrar y Transformar en un Solo Paso
Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas."""
listWord = ["sol", "mar", "montaña", "rio", "estrella"]
upperCase = [str.upper() for str in listWord if len(str)>3]
print(upperCase)

"""Crear un Diccionario con List Comprehension
Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension."""
key = ["nombre", "edad", "ocupación"]
values = ["Juan", 30, "Ingeniero"]
diccionario = {key[i]: values[i] for i in range(len(key))}
print(diccionario)

"""Extraer Información de una Lista de Diccionarios
Dada una lista de diccionarios que representan personas:"""
peoples = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}]

filter = [people["nombre"] for people in peoples if people["ciudad"] == "Madrid" and people["edad"] > 30]
print(filter)

"""List Comprehension con un else
Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están."""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newNumbers = [x * 2 if x % 2 == 0 else x for x in numbers]
print(newNumbers)