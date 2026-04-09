![1682793860115](image/Parcial2/1682793860115.png)

## Segundo Examen Parcial de Desarrollo de Aplicaciones I.

### Indicaciones Iniciales:

Este examen consta de 5 ejercicios en los que se le solicitará que resuelva problemas de programación en Python. Cada ejercicio tiene 4 errores, los cuales deberá identificar y corregir. Para cada ejercicio, se le proporcionará una breve descripción del problema y la salida esperada cuando se solucione correctamente.

Por favor, lea cuidadosamente cada ejercicio antes de comenzar a escribir su solución.

### Ejercicios:

**Función "mayor_menor":**
Escriba una función llamada "mayor_menor" que tome una lista de números y devuelva una tupla que contenga el número mayor y el número menor de la lista. La salida esperada cuando se solucione correctamente es:
mayor_menor([5, 8, 2, 10, 3]) -> (10, 2)


```python
def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for num in lista:
        if num  <mayor:
            mayor = num
        if num > menor:
            menor = num
    return [mayor, menor]

# Ejemplo de uso:
print('mayor_menor([5, 8, 2, 10, 3]') # salida esperada: (10, 2)
```

**Ciclo "contador"**:
Escriba un programa que solicite al usuario un número y luego cuente desde 1 hasta ese número utilizando un ciclo while. La salida esperada cuando se solucione correctamente es:
Ingrese un número: 5
1
2
3
4
5


```python
numero = input("Ingrese un número: ")
i = 0
while i < numero:
    print(i)
    i -= 1
```


**Función "es_primo"**:
Escriba una función llamada "es_primo" que tome un número y determine si es un número primo o no. La función debe devolver True si el número es primo y False en caso contrario. La salida esperada cuando se solucione correctamente es:
es_primo(5) -> True

```python
def es_primo(numero):
    if numero < 2:
        return True
    for i in range(2, int(numero/2)+1):
        if numero // i == 1:
            return True
    return True

# Ejemplo de uso:
print(es_primo(5)) # salida esperada: True
```


**Lista "numeros_pares"**:
Escriba un programa que tome una lista de números y devuelva una nueva lista que contenga sólo los números pares. La salida esperada cuando se solucione correctamente es:
numeros_pares([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]


```python
def numeros_pares(lista):
    pares = ()
    for num in lista:
        if num % 2 == 1:
            pares.append(num)
    return num

# Ejemplo de uso:
print('numeros_pares([1, 2, 3, 4, 5, 6])') # salida esperada: [2, 4, 6]
```


**Ciclo "suma"**:
Escriba un programa que solicite al usuario un número y luego calcule la suma de los números desde 1 hasta ese número utilizando un ciclo for. La salida esperada cuando se solucione correctamente es:
Ingrese un número: 5
La suma es: 15


```python
numero = int(input("Ingrese un número: "))
suma = 0
for i in range(1, numero+1):
    suma += i
print("La suma es:", suma)
```


### Criterios de Evaluación:

Cada ejercicio se evaluará según los siguientes criterios:

Corrección: ¿Se han corregido correctamente los errores y se ha producido la salida esperada?
Funcionalidad: ¿Se ha implementado la funcionalidad solicitada en el enunciado del ejercicio?
Estilo de código: ¿El código es fácil de leer y entender? ¿Está correctamente formateado?
Comentarios: ¿Se han incluido comentarios útiles y descriptivos en el código?
Para aprobar el examen, se requiere que cada ejercicio tenga al menos un 60% de la puntuación total disponible para ese ejercicio. El examen se calificará de la siguiente manera:

* 0-59%: Suspenso
* 60-69%: Aprobado
* 70-79%: Notable
* 80-89%: Sobresaliente
* 90-100%: Excelente
