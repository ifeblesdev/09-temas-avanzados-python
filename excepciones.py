print('*** Manejo de excepciones ***')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')
        resultado = numerador / denominador
        print(f'Resultado de la división: {resultado}')
        
    # except ZeroDivisionError:
    #     print(f'Error: No se puede dividir entre zero')
    # except TypeError:
    #     print(f'Error: Los operandos deben ser numéricos')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
    else:
        print(f'No ocurrión nigún error')
    finally:
        print(f'Terminamos de procesar la excepción')


# Ejemplo de uso
dividir(10,2)
dividir(10,0)
dividir(10,'0')

