#Transformación de Datos con Funciones. Define una función que tome una lista de cadenas y devuelva una nueva lista con las cadenas en mayúsculas.

def convertir_a_mayusculas(lista_de_cadenas):
    cadenas_en_mayusculas = [cadena.upper() for cadena in lista_de_cadenas]
    return cadenas_en_mayusculas

lista_original = ["feliz", "fin", "de", "semana", "larga"]
lista_en_mayusculas = convertir_a_mayusculas(lista_original)
print(lista_en_mayusculas)
