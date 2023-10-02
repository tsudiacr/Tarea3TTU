#Ejercicio 5 - Transformación de Datos. Dada una lista de números, crea una nueva lista que
#contenga el cuadrado de cada número en la lista original.

def cuadrados_lista(lista):
    cuadrados = [numero ** 2 for numero in lista]
    return cuadrados

numeros = [1, 2, 3, 4, 5]
resultado = cuadrados_lista(numeros)
print("Lista de cuadrados:", resultado)
