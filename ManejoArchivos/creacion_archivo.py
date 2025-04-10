# Crear un archivo 

nombre_archivo = "mi_archivo.txt"

# Abrir el archivo en modo escritura (esto creará el archivo si no existe)
archivo = open(nombre_archivo, "w")
archivo.write("Hola, como estás?\n")
archivo.write("Estoy agregando información al archivo.\n")
archivo.close()

print(f'Se creó el archivo {nombre_archivo} y se escribió información en él.')

# Otra forma con el objeto with
with open(nombre_archivo, "w") as archivo:
    archivo.write("Hola, como estás?\n")
    archivo.write("Estoy agregando información al archivo.\n")
    archivo.write("Se utiliza el objeto with.\n")

print(f'Se creó el archivo {nombre_archivo} y se escribió información en él.')    





