def greet(name, last_name = "No tiene apellido"):
    print("Hola", name, last_name)

greet("Pablo", "Barra")    
greet("Dani")
greet(last_name="Barra", name="Pablo")