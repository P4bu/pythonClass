def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    return (a / b)

def calculator():
    while True:
        print("Ingrese una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        option = int(input("Ingrese su opcion (1,2,3,4,5) => "))

        if option == 5:
            print("Saliendo de la calculadora!")
            break
        if option in [1,2,3,4]:
            num1 = float(input("Ingrese el primer numero => "))
            num2 = float(input("Ingrese el segundo numero => "))

        if option == 1:
            print("La suma es: ", add(num1, num2))

        if option == 2:
            print("La resta es: ", subtract(num1, num2))            

        if option == 3:
            print("La Multiplicacion es: ", multiply(num1, num2))    

        if option == 4:
            if num2 != 0:
                print("La division es: ", divide(num1, num2))   
            else: 
                print("Error, no puedes dividir por 0")     

calculator()
