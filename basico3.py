#Ejercicio 3 - Diccionarios y Funciones. Define una función que tome un diccionario como entrada y
# devuelva la clave con el valor máximo.

def clave_maxima(diccionario):
    if not diccionario:
        return None
    max_valor = max(diccionario.values())
    for clave, valor in diccionario.items():
        if valor == max_valor:
            return clave

# Ejemplo de uso:
mi_diccionario = {"a": 50, "b": 7, "c": 77}
resultado = clave_maxima(mi_diccionario)
print("La clave con el valor máximo es:", resultado)
