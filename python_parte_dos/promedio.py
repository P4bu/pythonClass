def calculate_average(numbers):
    """
    Calcula el promedio de una lista de numeros
    Parametros:
    numbers (list): una lista puede ser numeros enteros o flotantes

    retorna: 
    float: el promedio de los numeros en la lista
    """

    return sum(numbers) / len(numbers)

# Imprimiendo el resultado de la funcion 
print(calculate_average([1, 2, 3, 4, 5]))