



EL FAMOSO "FIZZ BUZZ"


```
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
```

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
```

EL "LENGUAJE HACKER"


```
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker", para ello debe cambiar las vocales de la siguiente manera
 *  la 'a' se cambia por 4, la 'e' se cambia por 3, la 'i' se cambia por
 *  1, la 'o' se cambia por 0 y la u se mantiene igual. En cuanto a las consonantes
 *  la 'z'se cambia por 2, la 's' se cambia por 5, la 'g' se cambia por 6, la 't' 
 *  se cambia por 7, la 'b' se cambia por 8, la 'p' se cambia por 9, al finalizar 
 *  se debe imprimir el mismo mensaje, pero con las letras indicadas cambiadas por número
 */
```

```python
def transformar_lenguaje_hacker(texto):
    letras = ['a', 'e', 'i', 'o', 'z', 's', 'g', 't', 'b', 'p']
    equivalentes = ['4', '3', '1', '0', '2', '5', '6', '7', '8', '9']
  
    resultado = ""
    for letra in texto:
        if letra in letras:
            resultado += equivalentes[letras.index(letra)]
        else:
            resultado += letra
    return resultado

texto = input("Introduce un texto: ")
texto_hacker = transformar_lenguaje_hacker(texto)
print(texto_hacker)

```

Heterograma, isograma y pangrama



```
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
```

```python
def es_heterograma(texto):
    """
    Devuelve True si el texto es un heterograma, es decir, si no contiene
    ninguna letra repetida.
    """
    letras_vistas = set()
    for letra in texto:
        if letra.isalpha():
            if letra.lower() in letras_vistas:
                return False
            letras_vistas.add(letra.lower())
    return True


def es_isograma(texto):
    """
    Devuelve True si el texto es un isograma, es decir, si no contiene
    ninguna letra repetida (sin importar mayúsculas o minúsculas).
    """
    letras_vistas = set()
    for letra in texto:
        if letra.isalpha():
            if letra.lower() in letras_vistas:
                return False
            letras_vistas.add(letra.lower())
    return True


def es_pangrama(texto):
    """
    Devuelve True si el texto es un pangrama, es decir, si contiene
    todas las letras del alfabeto al menos una vez.
    """
    letras_faltantes = set('abcdefghijklmnopqrstuvwxyz')
    for letra in texto:
        if letra.isalpha():
            letras_faltantes.discard(letra.lower())
    return not letras_faltantes

```




Octal y Hexadecimal


```
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * o Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
```


```python
def convertir_a_base(numero, base):
    """
    Convierte el número decimal dado a la base indicada (8 u 16).
    """
    # Definir símbolos para dígitos en hexadecial
    digitos_hexadecimal = "0123456789ABCDEF"
  
    # Convertir a octal o hexadecimal según la base especificada
    resultado = ""
    cociente = numero
    while cociente > 0:
        resto = cociente % base
        cociente = cociente // base
        if base == 8:
            resultado = str(resto) + resultado
        else:
            resultado = digitos_hexadecimal[resto] + resultado
  
    # Devolver resultado
    return resultado

```


¿ES UN ANAGRAMA?



```
/*
 * Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) 
 * según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando 
 * TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 */
```

```python
def es_anagrama(palabra1, palabra2):
    """
    Función que verifica si dos palabras son anagramas.
    """
    # Primero comprobamos que ambas palabras tengan la misma longitud
    if len(palabra1) != len(palabra2):
        return False
  
    # Convertimos las palabras a listas para poder ordenarlas
    lista1 = list(palabra1.lower())
    lista2 = list(palabra2.lower())
  
    # Ordenamos ambas listas
    lista1.sort()
    lista2.sort()
  
    # Comprobamos si ambas listas son iguales
    if lista1 == lista2:
        return True
    else:
        return False

```
