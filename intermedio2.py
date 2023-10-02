#Ejercicio 2 - Manejo de Estructuras de Datos Anidadas. Escribe una función que tome una lista de
#diccionarios y devuelva la lista ordenada por el valor de una clave específica en los diccionarios.

def ordenar_lista_de_diccionarios(lista, clave):
    lista_ordenada = sorted(lista, key=lambda x: x.get(clave, 0))
    return lista_ordenada

lista_de_diccionarios = [
    {"nombre": "Melvin", "edad": 30},
    {"nombre": "Alyssa", "edad": 32},
    {"nombre": "Sofia", "edad": 34},
    {"nombre": "Diana", "edad": 33}
]

clave_orden = "edad"

resultado = ordenar_lista_de_diccionarios(lista_de_diccionarios, clave_orden)

# Imprimir la lista ordenada
for elemento in resultado:
    print(elemento)
