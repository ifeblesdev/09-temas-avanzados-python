# Manejo de cadenas

# Dividir una cadena split()
cadena = 'Hola mundo'
palabras = cadena.split('m')
print(palabras)

# Buscar con find
posicion = cadena.find('mundo')
print(f'Posicón de la cadena mundo: {posicion}')

# Reemplazar con replace
nueva_cadena = cadena.replace('mundo', 'Amigo')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

# Multiplicación de cadenas
cadena = 'Hola '
resultado_multiplicacion_cadenas = cadena * 3
print(f'Resultado multiplicacion de cadenas: {resultado_multiplicacion_cadenas}')

# Strip es para limpiar una cadena
cadena = '....Hola Mundo....'
cadena_limpia = cadena.strip('.')
print(f'Cadena limpia de caracteres: {cadena_limpia}')