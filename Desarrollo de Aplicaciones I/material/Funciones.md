# Funciones en Python

En Python, una función es un bloque de código que se puede reutilizar para realizar una tarea específica. Las funciones en Python se definen utilizando la palabra clave `def` seguida del nombre de la función y los parámetros de entrada entre paréntesis.

## Sintaxis

La sintaxis básica de una función en Python es la siguiente:

```python
def nombre_funcion(parametros):
    """Docstring - Descripción de la función"""
    # Código de la función
    return valor_de_retorno

```

Donde:

* `def`: Palabra clave que indica que se está definiendo una función.
* `nombre_funcion`: Nombre de la función.
* `parametros`: Son los argumentos que recibe la función, separados por comas y encerrados entre paréntesis. Pueden ser opcionales, por lo que se pueden dejar en blanco.
* `"""Docstring - Descripción de la función"""`: Es la descripción de la función, su documentación. Es opcional, pero es una buena práctica incluirlo.
* `return`: Indica el valor que se va a retornar al finalizar la ejecución de la función. Es opcional, y si no se especifica, la función retorna `None`.

## Ejemplo

Veamos un ejemplo de una función sencilla que recibe dos números y devuelve la suma de ellos:

```python
def sumar(a, b):
    """Esta función devuelve la suma de dos números"""
    return a + b

```

Para llamar a la función, simplemente se utiliza su nombre y se le pasan los argumentos correspondientes:

```python
resultado = sumar(2, 3)
print(resultado)  # 5

```

En este caso, la función `sumar` toma dos parámetros, `a` y `b`, y retorna la suma de ambos.

## Argumentos

Los argumentos son los valores que se pasan a una función cuando se llama. Las funciones pueden tener argumentos opcionales y argumentos con valores por defecto.

### Argumentos posicionales

Los argumentos posicionales son aquellos que se pasan en el orden en que se definen en la función. Por ejemplo:

```python
def imprimir_nombre(nombre, apellido):
    print(nombre, apellido)

imprimir_nombre('Juan', 'Pérez')

```

En este caso, se están pasando dos argumentos posicionales, `'Juan'` y `'Pérez'`, que corresponden a los parámetros `nombre` y `apellido`, respectivamente.

### Argumentos con valor por defecto

Los argumentos con valor por defecto son aquellos que tienen un valor asignado por defecto. Si no se especifica un valor para ese argumento al llamar a la función, se utilizará el valor por defecto. Por ejemplo:

```python
def imprimir_nombre(nombre, apellido, saludo='Hola'):
    print(saludo, nombre, apellido)

imprimir_nombre('Juan', 'Pérez')

```

En este caso, se está especificando un valor por defecto para el argumento `saludo`. Si al llamar a la función no se especifica el valor de `saludo`, se utilizará el valor por defecto `'Hola'`.

### Argumentos opcionales

Los argumentos opcionales son aquellos que no son necesarios para llamar a la función. Por ejemplo:

```python
def imprimir_nombre(nombre, apellido, saludo=None):
    if saludo:
        print(saludo, nombre, apellido)
    else:
	print(nombre, apellido)

```



`None` es un valor especial en Python que se utiliza para indicar la ausencia de valor. En otras palabras, `None` es una forma de representar la falta de un valor significativo en una variable o expresión.

En términos técnicos, `None` es un objeto único en Python que se utiliza para representar la ausencia de valor. Se puede pensar en `None` como un tipo de dato en sí mismo, similar a los tipos de datos básicos como `int` y `str`.

`None` es comúnmente utilizado en Python para indicar que una variable no tiene valor asignado o que una función no devuelve ningún valor. Por ejemplo, si se define una función que no devuelve nada, se puede utilizar la sentencia `return None` para indicar explícitamente que la función no devuelve un valor.

```python
def funcion_que_no_devuelve_nada():
    print("Esta función no devuelve nada")
    return None

```

También es común utilizar `None` como un valor por defecto para los argumentos de las funciones, indicando que si el argumento no es proporcionado al llamar la función, se utilizará el valor por defecto `None`.

```python
def funcion_con_argumento_opcional(argumento=None):
    if argumento is None:
        print("El argumento no fue proporcionado")
    else:
        print("El argumento es:", argumento)

```

En resumen, `None` es un valor especial en Python que se utiliza para indicar la ausencia de valor y es comúnmente utilizado para indicar que una variable no tiene valor asignado o que una función no devuelve ningún valor.


Aparte de usar el valor `None` como valor por defecto de un argumento para crear argumentos opcionales, también se pueden usar otros valores como valores por defecto, como números, cadenas de texto o incluso otros objetos.

Por ejemplo, se puede definir una función que acepte un argumento opcional `mensaje` que tenga un valor por defecto de `"Hola"`:

```python
def saludar(nombre, mensaje="Hola"):
    print(mensaje, nombre)

saludar("Juan")           # Imprime: Hola Juan
saludar("Ana", "Adiós")   # Imprime: Adiós Ana

```


En este caso, se está definiendo la función `saludar` que tiene un argumento opcional `mensaje` que tiene un valor por defecto de `"Hola"`. Si se llama a la función sin especificar un valor para `mensaje`, se utilizará el valor por defecto `"Hola"`. Si se especifica un valor para `mensaje`, ese valor será utilizado en lugar del valor por defecto.

También es posible tener varios argumentos opcionales en una misma función. En este caso, los argumentos opcionales se definen en la lista de argumentos después de los argumentos posicionales y se les puede asignar valores por defecto. Por ejemplo:


```python
def imprimir_datos(nombre, apellido, edad=None, ciudad=""):
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    if edad is not None:
        print("Edad:", edad)
    if ciudad != "":
        print("Ciudad:", ciudad)

imprimir_datos("Juan", "Pérez")             # Imprime: Nombre: Juan, Apellido: Pérez
imprimir_datos("María", "González", 25)     # Imprime: Nombre: María, Apellido: González, Edad: 25
imprimir_datos("Pedro", "Martínez", ciudad="Madrid")   # Imprime: Nombre: Pedro, Apellido: Martínez, Ciudad: Madrid

```

En este ejemplo, se está definiendo una función llamada `imprimir_datos` que acepta cuatro argumentos, dos argumentos posicionales (`nombre` y `apellido`) y dos argumentos opcionales (`edad` y `ciudad`). La edad se asigna por defecto al valor `None` mientras que la ciudad se asigna a una cadena vacía. La función imprime los datos proporcionados según los argumentos recibidos, pero solo imprime los argumentos opcionales si se proporcionan.


## Return

La sentencia `return` se utiliza para devolver un valor de la función. Una vez que se ejecuta una sentencia `return`, la ejecución de la función se detiene y el valor se devuelve al lugar donde se llamó la función.

Por ejemplo:

```python
def sumar(a, b):
    return a + b

resultado = sumar(2, 3)
print(resultado)  # Imprime: 5

```


En este caso, la función `sumar` devuelve la suma de `a` y `b` utilizando la sentencia `return`.

## Pass

La sentencia `pass` se utiliza como marcador de posición cuando se está definiendo una función y se necesita especificar la estructura básica de la función sin escribir el código real.

Por ejemplo:

```python
def funcion_sin_implementar():
    pass

```


En este caso, se está definiendo una función `funcion_sin_implementar` que no hace nada. La sentencia `pass` se utiliza para evitar errores de sintaxis al definir una función vacía.

## Listas como parámetros


En Python, se pueden pasar listas como parámetros de una función. Esto es útil cuando se necesita realizar una operación en una lista y se quiere que esa operación sea realizada por una función. En esta sección, presentaré algunos ejemplos de cómo se pueden utilizar las listas como parámetros de una función.

1. Funciones para sumar los elementos de una lista

La función `sum()` se utiliza para sumar los elementos de una lista. Por ejemplo:

```python
def sumar_elementos(lista):
    suma = sum(lista)
    return suma

numeros = [1, 2, 3, 4]
resultado = sumar_elementos(numeros)
print(resultado)   # Imprime: 10

```


2. Funciones para ordenar una lista

La función `sort()` se utiliza para ordenar una lista en orden ascendente. Por ejemplo:

```python
def ordenar_lista(lista):
    lista.sort()
    return lista

numeros = [4, 2, 3, 1]
resultado = ordenar_lista(numeros)
print(resultado)   # Imprime: [1, 2, 3, 4]

```


## Parámetro *args

En Python, el parámetro `*args` se utiliza para pasar un número variable de argumentos a una función. El parámetro `*args` permite que una función acepte cualquier número de argumentos posicionales, los cuales se tratan como una tupla dentro de la función.

Aquí hay un ejemplo sencillo que muestra cómo usar `*args` en una función:

```python
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

resultado = sumar_numeros(1, 2, 3)
print(resultado)   # Imprime: 6

```


En este ejemplo, la función `sumar_numeros()` acepta cualquier número de argumentos. Los argumentos se pasan a la función separados por comas, y la función los trata como una tupla llamada `args`. Dentro de la función, se usa un bucle para sumar los valores de la tupla `args`.

El parámetro `*args` también se puede usar en combinación con otros argumentos. Aquí hay un ejemplo que muestra cómo usar `*args` junto con un argumento normal:

```python
def multiplicar_numeros(factor, *args):
    producto = 1
    for numero in args:
        producto *= numero
    return producto * factor

resultado = multiplicar_numeros(2, 1, 2, 3)
print(resultado)   # Imprime: 12

```


En este ejemplo, la función `multiplicar_numeros()` acepta un argumento normal llamado `factor` y cualquier número de argumentos posicionales. Dentro de la función, se usa un bucle para multiplicar los valores de la tupla `args`. Finalmente, el producto se multiplica por el valor del argumento `factor`.

El parámetro `*args` es muy útil cuando se trabaja con funciones que pueden aceptar diferentes números de argumentos. Permite escribir funciones más flexibles y reutilizables.
