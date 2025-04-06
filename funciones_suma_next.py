print('*** Función sum y next')

lista = [1,2,3,4,5]

# Suma todos los elementos
resultado = sum(lista)
print(f'El resultado de la suma es: {resultado}')

# Con valor inicial
resultado = sum(lista, 20)
print(f'Resultado de la suma con valor inicial: {resultado}')

# La función next
iterador = iter(lista)

# Obtenemos del próximo elemento del iterador usando la función next
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')