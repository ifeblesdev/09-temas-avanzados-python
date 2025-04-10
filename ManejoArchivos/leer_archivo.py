print('*** Leer archivo con Python ***')
nombre_archivo = "mi_archivo.txt"

# Leer un archivo usando el método readline()
with open(nombre_archivo, "r") as archivo:
    # Leer las líneas del archivo
    # print(archivo.readlines())
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())

print('-'*50)
# Leer un archivo usando el método read()
print('Leyendo el contenido del archivo con el método read()')
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()
    print(contenido)