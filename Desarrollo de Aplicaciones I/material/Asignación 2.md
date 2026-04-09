### **Indicaciones Iniciales**

---

Se le proporcionará cinco algoritmos en seudocódigo escritos para pseint, usted debe usarlos para crear un prograrma adecuado para correr en python.

### **Ejercicios**

---

1. Crear un algoritmo que muestre el nombre del cliente y  la compra de llantas,  si la cantidad de llantas comprados es menor de 12, al precio de las llantas compradas se le hará un descuento del 20%, sabiendo que el costo de la llanta es 250 soles por unidad, y si el número de llantas compradas es mayor de 12, el precio de llanta se reduce a 220 por unidad y el descuento será de 25%.Ingresar por teclado 3 números enteros y mostrar  el menor de los 3 números ingresados y la suma de dichos número

```pseint
Algoritmo compra_llantas
    Escribir "Ingrese el nombre del comprador"
    Leer nombre
    Escribir "Ingresar el número de llantas a comprar"
    Leer nllantas
  
    Si nllantas < 12 Entonces
        psd<-nllantas*250
        des<-psd*0.20
        ptotal<-psd-des
        Escribir "Ha comprado menos de una docena de llantas"
        Escribir "El total sin descuento es: " psd
        Escribir "El descuento es: " des
        Escribir nombre " pagará " ptotal
    Sino
        psd<-nllantas*220
        des<-psd*0.25
        ptotal<-psd-des
        Escribir "Ha comprado más de una docena de llantas"
        Escribir "El total sin descuento es: " psd
        Escribir "El descuento es: " des
        Escribir nombre " pagará " ptotal
    Finsi
FinAlgoritmo

```

2. Desarrolle un algoritmo que permita leer un valor entero positivo N y determinar si es primo o no.

```pseint
Algoritmo NumeroPrimo
    Definir N, i, contador Como Entero
  
    Escribir "Ingrese un número entero positivo: "
    Leer N
  
    Si N < 2 Entonces
        Escribir N, " no es un número primo"
    Sino
        contador <- 0
  
        Para i <- 2 Hasta (N - 1) Con Paso 1 Hacer
            Si N % i = 0 Entonces
                contador <- contador + 1
            FinSi
        FinPara
  
        Si contador = 0 Entonces
            Escribir N, " es un número primo"
        Sino
            Escribir N, " no es un número primo"
        FinSi
    FinSi
FinAlgoritmo
```

3. Diseñar un algoritmo que solicite números al usuario hasta que el usuario ingrese el número 0. El algoritmo deberá imprimir la suma de todos los números ingresado

```pseint
Proceso SumaNumeros
    Definir numero, suma Como Entero

    suma <- 0
    numero <- 1

    Mientras numero <> 0 Hacer
        Escribir "Ingrese un número: "
        Leer numero
        suma <- suma + numero
    Fin Mientras

    Escribir "La suma de los números ingresados es: ", suma
FinProceso
```

4. Diseñar un algoritmo que solicite números al usuario hasta que la suma de los números ingresados sea mayor a 100. El algoritmo deberá imprimir la cantidad de números que se ingresaron.

```pseint
Proceso SumaHasta100
    Definir numero, suma, cantidad Como Entero

    suma <- 0
    cantidad <- 0

    Mientras suma <= 100 Hacer
        Escribir "Ingrese un número: "
        Leer numero
        suma <- suma + numero
        cantidad <- cantidad + 1
    Fin Mientras

    Escribir "Se ingresaron ", cantidad, " números para sumar más de 100."
FinProceso
```

5. Escribe un algoritmo que pida al usuario un número N e imprima los primeros N números de la serie de Fibonacc

```pseint
Algoritmo fibonacci

  Definir N, i, a, b, c Como Entero
  a = 0
  b = 1

  Escribir "Ingrese un número entero positivo:"
  Leer N

  Escribir a
  Escribir b

  Para i = 3 hasta N hacer
    c = a + b
    Escribir c
    a = b
    b = c
  FinPara

FinAlgoritmo
```

### **Puntaje**

---

Cada programa en python tendrá un puntaje de dos, para un total de 10 puntos totales en el trabajo

### **Criterios de Evaluación**

---

+ Funcionamiento correcto del programa *60% (1.2 puntos por cada programa)*
+ Respetar los convencionalismos en programación *20% (0.4 puntos por cada programa)*
+ Claridad y sencillez en la solución *20% (0.4 puntos por cada programa)*
