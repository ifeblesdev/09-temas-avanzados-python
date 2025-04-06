print('*** Generadores en Python ***')

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador +=1

# Creamos un generador
var_generador = generador(5)

# Iteramos sobre el generador
for valor in var_generador:
    print(valor)
