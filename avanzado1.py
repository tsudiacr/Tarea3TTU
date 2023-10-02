#Matrices y Funciones. Define una función que tome dos matrices como entrada y devuelva su suma como una nueva matriz.
def suma_de_matrices(matriz1, matriz2):
    # Verificar si las matrices tienen las mismas dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None  # Las matrices no tienen las mismas dimensiones, no se pueden sumar

    filas = len(matriz1)
    columnas = len(matriz1[0])

    matriz_suma = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_suma[i][j] = matriz1[i][j] + matriz2[i][j]

    return matriz_suma

matriz1 = [[1, 5, 3], [4, 5, 6], [7, 8, 2]]
matriz2 = [[9, 2, 7], [6, 7, 4], [3, 2, 1]]

resultado = suma_de_matrices(matriz1, matriz2)

if resultado is not None:
    for fila in resultado:
        print(fila)
else:
    print("Las matrices no tienen las mismas dimensiones, no se pueden sumar.")
