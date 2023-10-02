import csv

# Nombre del archivo CSV
archivo_csv = "datos.csv"

# Nombre de la columna de edades
columna_edades = "edad"

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

edades = []

try:
    with open(archivo_csv, newline='') as csvfile:
        # Crear un objeto lector de CSV
        lector_csv = csv.DictReader(csvfile)

        for fila in lector_csv:
            if columna_edades in fila:
                edad = int(fila[columna_edades])
                edades.append(edad)

    promedio = calcular_promedio(edades)

    print(f"El promedio de las edades en la columna '{columna_edades}' es: {promedio:.2f}")
    
#MSG
except FileNotFoundError:
    print(f"El archivo '{archivo_csv}' no se encontró.")
except ValueError:
    print("Se encontró un valor no numérico en la columna de edades.")
except ZeroDivisionError:
    print("No se encontraron edades para calcular el promedio.")
