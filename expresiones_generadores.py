print('*** Expresiones generadores ***')

generador = (x**2 for x in range(10) if x % 2 == 0)

for cuadrador_pares in generador:
    print(cuadrador_pares)
