import random

# tamaño del tablero
TAMANO_TABLERO = 5
NUM_BARCO = 3

# iniciar el tablero
tablero = [["~"] * TAMANO_TABLERO for _ in range(TAMANO_TABLERO)]

# Colocar barcos aleatorios
barcos_colocados = 0
while barcos_colocados < NUM_BARCO:
    fila = random.randint(0, TAMANO_TABLERO - 1)
    col = random.randint(0, TAMANO_TABLERO - 1)
    if tablero[fila][col] == "~":
        tablero[fila][col] = "B"
        barcos_colocados += 1

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    print("  " + " ".join(str(i) for i in range(TAMANO_TABLERO)))
    for i, fila in enumerate(tablero):
        print(i, " ".join(fila))

# Juego
def jugar():
    intentos = 0
    barcos_hundidos = 0

    while barcos_hundidos < NUM_BARCO:
        mostrar_tablero(tablero)
        fila = int(input("Ingresa la fila (0-4): "))
        col = int(input("Ingresa la columna (0-4): "))
        
        if tablero[fila][col] == "B":
            print("¡Tocado!")
            tablero[fila][col] = "X"
            barcos_hundidos += 1
        elif tablero[fila][col] == "~":
            print("Agua.")
            tablero[fila][col] = "O"
        else:
            print("Ya has intentado aquí.")
        
        intentos += 1

    print(f"Ganaste! Hundiste todos los barcos en {intentos} intentos.")

# Iniciar el juego
if __name__ == "__main__":
    jugar()
