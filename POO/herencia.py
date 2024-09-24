class Vehiculo:
    def __init__(self, marca, modelo, precio):
        #Encapsulacion
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True
    
    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} ha sido vendido.")
        else:
            print(f"El vehículo {self.marca} no está disponible.")
    #Abstracion
    def estado(self):
        return self.disponible 
    #Abstracion
    def get_precio(self):
        return self.precio

    def inicio_motor(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase (hija).")

    def detener_motor(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase (hija).")
#Herencia
class Auto(Vehiculo):
    #Polimorfismo
    def inicio_motor(self):
        if not self.disponible:
            return f"El motor del vehículo {self.marca} está en marcha."
        else:
            return f"El vehículo {self.marca} no está disponible."
            
    def detener_motor(self):
        if not self.disponible:
            return f"El motor del vehículo {self.marca} se ha detenido."
        else:
            return f"El vehículo {self.marca} no está disponible."

class Bicicleta(Vehiculo):
    def inicio_motor(self):
        if not self.disponible:
            return f"La bicicleta {self.marca} está en marcha."
        else:
            return f"La bicicleta {self.marca} no está disponible."
            
    def detener_motor(self):
        if not self.disponible:
            return f"La bicicleta {self.marca} se ha detenido."
        else:
            return f"La bicicleta {self.marca} no está disponible."

class Camion(Vehiculo):
    def inicio_motor(self):
        if not self.disponible:
            return f"El camión {self.marca} está en marcha."
        else:
            return f"El camión {self.marca} no está disponible."
            
    def detener_motor(self):
        if not self.disponible:
            return f"El camión {self.marca} se ha detenido."
        else:
            return f"El camión {self.marca} no está disponible."

class Comprador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.estado():  
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f"Lo siento, {vehiculo.marca} no está disponible.")

    def preguntar_vehiculo(self, vehiculo: Vehiculo):
        disponibilidad = "Disponible" if vehiculo.estado() else "No disponible"  # Cambiar a estado()
        print(f"El {vehiculo.marca} está {disponibilidad} y cuesta {vehiculo.get_precio()}.")

class Tienda:
    def __init__(self):
        self.inventario = []  
        self.compradores = [] 

    def add_vehiculo(self, vehiculo: Vehiculo):
        self.inventario.append(vehiculo)   
        print(f"El {vehiculo.marca} ha sido agregado al catálogo.")

    def add_comprador(self, comprador: Comprador):
        self.compradores.append(comprador) 
        print(f"El cliente ha sido añadido.")

    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponibles en la tienda:")
        for vehiculo in self.inventario:
            if vehiculo.estado():  
                print(f"- {vehiculo.marca} por {vehiculo.get_precio()}.") 

# Datos
car1 = Auto("Toyota", "Corolla", 20000)
bike1 = Bicicleta("Yamaha", "MT-07", 7000)
truck1 = Camion("Volvo", "FH16", 80000)

customer1 = Comprador("Carlos")

tienda = Tienda()
tienda.add_vehiculo(car1)
tienda.add_vehiculo(bike1)
tienda.add_vehiculo(truck1)

# Mostrar vehículos disponibles
tienda.mostrar_vehiculos_disponibles()

# Cliente consultar un vehículo
customer1.preguntar_vehiculo(car1)

# Cliente comprar un vehículo
customer1.comprar_vehiculo(car1)

# Mostrar vehículos disponibles
tienda.mostrar_vehiculos_disponibles()
