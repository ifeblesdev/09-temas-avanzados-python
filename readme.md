# ⚙️ Temas Avanzados en Python

Este documento resume algunos conceptos avanzados de Python que te ayudarán a escribir código más eficiente, limpio y profesional.

---

## 🔁 Generadores

Los **generadores** son funciones que devuelven iteradores utilizando la palabra clave `yield`. Permiten generar elementos uno a uno, de forma perezosa (*lazy*), lo que los hace ideales para manejar grandes volúmenes de datos sin consumir mucha memoria.

```python
def contador(n):
    for i in range(n):
        yield i
```

---

## 🎁 Decoradores

Los **decoradores** son funciones que envuelven otras funciones para extender su comportamiento sin modificarlas directamente. Son útiles para tareas como logging, autenticación, validación de permisos, entre otros.

```python
def mi_decorador(func):
    def wrapper():
        print("Antes")
        func()
        print("Después")
    return wrapper
```

---

## 🔍 Funciones Lambda

Una **lambda** es una función anónima, definida en una sola línea. Se usa comúnmente para operaciones rápidas o como funciones de apoyo en `map()`, `filter()` o `sorted()`.

```python
cuadrado = lambda x: x * x
```

---

## 🧮 Reduce

La función **`reduce()`** aplica una operación acumulativa a los elementos de un iterable, reduciéndolos a un solo valor. Es parte del módulo `functools`.

```python
from functools import reduce

suma = reduce(lambda x, y: x + y, [1, 2, 3, 4])  # Resultado: 10
```

---

## 🔢 Sorted

La función **`sorted()`** ordena cualquier iterable y acepta argumentos como `key` y `reverse` para una ordenación personalizada.

```python
nombres = ["Carlos", "ana", "Bea"]
ordenados = sorted(nombres, key=str.lower)  # ['ana', 'Bea', 'Carlos']
```

---

## 📚 Recursos adicionales

- [Documentación oficial de Python](https://docs.python.org/3/)
- [PEP 8 – Guía de estilo para código Python](https://peps.python.org/pep-0008/)
- [functools – Higher-order functions](https://docs.python.org/3/library/functools.html)
- [itertools – Itertools mágicas](https://docs.python.org/3/library/itertools.html)

---

✨ ¡Sigue explorando Python y lleva tu código al siguiente nivel!
