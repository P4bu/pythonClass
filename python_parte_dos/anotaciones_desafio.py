# Lista de empleados
empleados = [

    {"nombre": "Alan Brito",
     "edad": 30,
     "sueldo": 30000
     },
    {"nombre": "Luis Perez",
     "edad": 25,
     "sueldo": 10000
     },
    {"nombre": "Elza Payo",
     "edad": 20,
     "sueldo": 20000
     },
     {"nombre": "Elba Lazo",
     "edad": 20,
     "sueldo": 50000
     }
]

# Funcion para crear la nueva lista con el filtro de los sueldos
def lista_empleados(empleados: list, limite: int = 30000) -> list:
    lista = [empleado for empleado in empleados if empleado['sueldo'] >= limite]
    return lista

# Motrar el resultado
print(lista_empleados(empleados))
# print(lista_empleados(empleados, limite=20000))