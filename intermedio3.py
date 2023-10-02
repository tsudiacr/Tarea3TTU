#Ejercicio 3 - Integración de Múltiples Funciones. Combina las funciones que has creado en ejercicios anteriores para leer datos de un archivo, realizar transformaciones y escribir los resultados en un nuevo archivo.

import json

# Función para convertir un diccionario en cadena JSON
def convertir_diccionario_a_json(diccionario):
    if isinstance(diccionario, dict):
        cadena_json = json.dumps(diccionario)
        return cadena_json
    else:
        return None

# Ejercicio 1 - Función para transformar cadenas a mayúsculas o dejar diccionarios intactos
def convertir_a_mayusculas_o_dejar_intacto(lista_de_cadenas):
    if isinstance(lista_de_cadenas, list):
        # Verificar si la lista contiene diccionarios o cadenas
        if all(isinstance(item, dict) for item in lista_de_cadenas):
            # Si todos los elementos son diccionarios, dejar la lista intacta
            return lista_de_cadenas
        elif all(isinstance(item, str) for item in lista_de_cadenas):
            # Si todos los elementos son cadenas, convertir a mayúsculas
            cadenas_en_mayusculas = [cadena.upper() for cadena in lista_de_cadenas]
            return cadenas_en_mayusculas
    return None

lista_original = ["feliz", "fin", "de", "semana", "larga"]
lista_transformada = convertir_a_mayusculas_o_dejar_intacto(lista_original)

if lista_transformada:
    print(lista_transformada)
else:
    print("No es una lista válida.")

# Ejercicio 2 - Función para ordenar una lista de diccionarios por una clave específica
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

# Ejercicio 3 - Función que integra las funciones anteriores
def procesar_archivo_entrada(archivo_entrada, archivo_salida, clave_ordenamiento=None):
    try:
        with open(archivo_entrada, "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no se encontró.")
        return

    datos_transformados = convertir_a_mayusculas_o_dejar_intacto(datos)

    if clave_ordenamiento:
        datos_transformados = ordenar_lista_de_diccionarios(datos_transformados, clave_ordenamiento)

    with open(archivo_salida, "w") as archivo:
        for resultado in datos_transformados:
            archivo.write(str(resultado) + "\n")

    print(f"Resultados escritos en '{archivo_salida}'")

archivo_entrada = "entrada.json"
archivo_salida = "resultados.txt"
clave_ordenamiento = "nombre"

procesar_archivo_entrada(archivo_entrada, archivo_salida, clave_ordenamiento)
