class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.precio = precio
        self.modelo = modelo
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehiculo {self.marca} vendido -> Precio: $ {self.precio}")
        else:
            print(f"El vehiculo {self.marca} no esta disponibles")

    def comprar(self):
        self.disponible = True
        print(f"Vehiculo {self.marca} comprado")

    def estado(self):
        return self.disponible

    def get_precio(self):
        return self.precio    
        

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.usuario_list_vehiculos = []

    def comprar_vehiculo(self, vehiculo):
        if vehiculo.disponible:
            vehiculo.vender()
            self.usuario_list_vehiculos.append(vehiculo)
            print(f"Agrege un vehiculo a la coleccion")
        else:
            print(f"El vehiculo {self.marca} no esta disponibles")

    def vender_vehiculo(self, vehiculo):
        if vehiculo in self.usuario_list_vehiculos:
            vehiculo.comprar()
            self.usuario_list_vehiculos.remove(vehiculo)
        else:
            print(f"No tengo vehiculos en la coleccion")

class Tienda:
    def __init__(self):
        self.vehiculos = []
        self.usuarios = []

    def add_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Se agrego {vehiculo.marca} al catalogo")

    def add_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Se registro {usuario.nombre} a la tienda")

    def mostrar_vehiculos_disponibles(self):
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                print(f"Disponibles: {vehiculo.marca} Precio -> $ {vehiculo.precio}")        


# Datos de prueba
vehiculo1 = Vehiculo("Toyota", "Celica", 2000)
vehiculo2 = Vehiculo("Porche", "Carrera", 40000)
vehiculo3 = Vehiculo("Toyota", "Corolla", 20000)
vehiculo4 = Vehiculo("Honda", "Civic", 22000)
vehiculo5 = Vehiculo("Ford", "Mustang", 30000)

usuario1 = Usuario("Pablo", 1)
usuario2 = Usuario("Juanito", 2)

tienda = Tienda()
tienda.add_usuario(usuario1)
tienda.add_usuario(usuario2)

tienda.add_vehiculo(vehiculo1)
tienda.add_vehiculo(vehiculo2)
tienda.mostrar_vehiculos_disponibles()

usuario1.comprar_vehiculo(vehiculo1)

print("Estado actual de la tienda con la venta del vehiculo")
tienda.mostrar_vehiculos_disponibles()

usuario1.vender_vehiculo(vehiculo1)

print("Estado actual de la tienda con la compra del vehiculo")
tienda.mostrar_vehiculos_disponibles()
