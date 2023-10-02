#Ejercicio 2 - Lectura de Archivos. Crea un programa que lea un archivo de texto llamado "datos.txt"
#y muestre su contenido en pantalla.

try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo 'datos.txt' no se encontró.")
