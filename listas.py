to_do = ["Dirigirnos al Hotel", 
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1, 2, 3, 4, "5"]
print(numbers)
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(type(mix))
print(len(mix))
print("Primer elemento ", mix[0])
print("Segundo elemento ", mix[1])
print("Ultimo elemento ", mix[-1])

string = "hola mundo"
print("Primera letra ", string[0])

print(mix[0:2]) # buena practica dejarlo vacio desde 0 [:2]
print(mix)
mix.append(False)
mix.append(["a", "b"])
print(mix)   
mix.insert(1,["a", "b"]) # se inserta en un lugar (position, value)

# Index cual es la posicion y primera aparicion de un elemento
print(mix.index(["a", "b"]))


numbers = [1, 200, 3, 4, 90.5, 100]
print("Mayor ", max(numbers))
print("Menor ", min(numbers))

del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
# del numbers elimina toda la lista
