print('*** Decoradores en Python ***')

def decorador(func):
    def wrapper(*args, **kwargs):
        print('Antes de llamar a la función saludar')
        resultado = func(*args, **kwargs)
        print('Luego de llamar a la función saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Ignacio')

