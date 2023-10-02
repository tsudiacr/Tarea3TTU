# Ejercicio 4 - Escritura de Archivos. Crea un programa que escriba una lista de nombres en un
# archivo llamado "nombres.txt", un nombre por línea.

nombres = ["Diana", "Melvin", "Alyssa", "Federico"]

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")
