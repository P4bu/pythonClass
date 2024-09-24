numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers)
print(numbers[2])

information = {"nombre": "Pablo", 
               "apellido": "Barra", 
               "altura": 1.70,
               "edad": 33}
print(information)
del information["edad"]
print(information)

clave = information.keys()
print(clave)

values = information.values()
print(values)

pairs = information.items()
print(pairs)

contacts = {"Pablo" :{ 
               "apellido": "Barra", 
               "altura": 1.70,
               "edad": 33},
            "Tana": {
                    "apellido": "Corral", 
                    "altura": 1.60,
                    "edad": 31}}
print(contacts)
print(contacts["Pablo"])