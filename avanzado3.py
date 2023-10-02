#Escritura de Archivos JSON. Crea un programa que tome un diccionario y lo escriba en
#un archivo JSON llamado "datos.json".

import json

mi_diccionario = {
    "nombre": "Alyssa",
    "edad": 32,
    "ciudad": "Woodlands"
}
nombre_archivo = "datos.json"

with open(nombre_archivo, "w") as archivo:
    json.dump(mi_diccionario, archivo)

print(f"El diccionario se ha escrito en el archivo {nombre_archivo}")
