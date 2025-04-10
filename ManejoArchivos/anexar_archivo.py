print('*** Anexar información a un archivo ***')

nombre_archivo = "mi_archivo.txt"

with open(nombre_archivo, "a") as archivo:
    archivo.write("Escribiendo en modo anexar\n")
    archivo.write("Espero te sea útil.\n")
    print(f'Se anexó información al archivo {nombre_archivo}.')
