clasificacion = [(x, " es par") if x % 2 == 0 else "impar" for x in range(10)]
print(clasificacion)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
plana= [x for fila in matriz for x in fila]
print(plana)

cuadrado = lambda x: x**2
variable = 3
print(f'El cuadrado de {variable} es:', cuadrado(variable))