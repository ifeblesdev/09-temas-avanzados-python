print('*** Abrir archivo en modo exclusivo ***')

nombre_archivo = "mi_archivo.txt"
try:
    with open(nombre_archivo, "x") as archivo:
        archivo.write("Escrituro en modo exclusivo\n")
        archivo.write("Espero te sea útil.\n")
        print(f'Se creó el archivo {nombre_archivo} y se escribió información en él.')
except FileExistsError as e:
    print(f'El archivo {nombre_archivo} ya existe. Detalle error {e}')