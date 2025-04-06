nombres = ['Juan', 'Maria', 'Pedro', 'Ana']
edades = [30,25,35]
ciudades = ['Madrid','Barcelona','Sevilla']

# Combinar los elementos de las listas usando la función zip
personas = zip(nombres, edades, ciudades)

# Iterar sobre el resultado de la función zip. Zip toma en cuenta la lista mas pequeña

for persona in personas:
    print(persona)