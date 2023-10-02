# Ejercicio 1 - Listas y Funciones. Escribe una función que tome una lista de números como entrada y
# devuelva la suma de todos los números en la lista.


def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

num_lista = [1, 2, 3, 4, 5]
resultado = suma_lista(num_lista)
print("La suma de la lista es:", resultado)
