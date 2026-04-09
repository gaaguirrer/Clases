### **Indicaciones Iniciales**

---

Se le proporcionará cinco algoritmos en seudocódigo escritos para pseint, usted debe usarlos para crear un prograrma adecuado para correr en python.

### **Ejercicios**

---

1. Ingresar por teclado 3 números enteros y mostrar  el menor de los 3 números ingresados y la suma de dichos números.

```pseint
Algoritmo numero_menor_y_suma
    Escribir "Ingrese el primer valor "
    Leer num1
    Escribir "Ingrese el segundo valor "
    Leer num2
    Escribir "Ingrese el tercer valor "
    Leer num3
    suma <- num1 + num2 + num3
    Si num1 < num2 & num1 < num3 Entonces
        Escribir "El numero menor es : " num1
        Escribir "La suma de los numeros es : " suma
    SiNo
        Si num2 < num1 & num2 < num3 Entonces
            Escribir "El numero menor es : " num2
            Escribir "La suma de los numeros es : " suma
        SiNo 
            Escribir "El numero menor es : " num3
            Escribir "La suma de los numeros es : " suma
        FinSi
    FinSi
FinAlgoritmo
```

2. A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. si la cantidad de horas trabajadas es mayor a 40 horas. la tarifa se incrementa en un 50% para las horas extras. calcular el salario del trabajador dadas las horas trabajadas y la tarifa.

```pseint
Algoritmo salario_trabajador
    Escribir "Ingrese las horas trabajadas"
    Leer horas_trabajadas
    Escribir "Ingrese la tarifa por hora trabajada"
    Leer tarifa
  
    Si horas_trabajadas <= 40 Entonces
        salario <- horas_trabajadas * tarifa
        Escribir "Salario normal " salario
    SiNo
        tarifa_extra <- tarifa + 0.50 * tarifa
        horas_extras <- horas_trabajadas - 40
        Escribir "Horas extras trabajadas " horas_extras
        salario <- horas_extras * tarifa_extra + 40 *tarifa
        Escribir "Valor de la tarifa extra " tarifa_extra
        Escribir salario
    FinSi
FinAlgoritmo
```

3. Ingresar por teclado dos valores numéricos y mostrar cual es el mayor o si son iguales, mostrar el residuo de la división de dichos números

```pseint
Algoritmo mayoroigual
   Escribir "Ingrese el primer numero "
   Leer n1
   Escribir "Ingrese el segundo numero "
   Leer n2
   Si n1 > n2 Entonces
      Escribir "El numero mayor es : " n1
   SiNo
      Si n2 > n1 Entonces
         Escribir "El numero mayor es : " n2
      SiNo
         Escribir "Los numeros son iguales " 
      FinSi
   FinSi
   res<- n1%n2
   Escribir "El residuo de la division es " res
FinAlgoritmo
```

4. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%

```pseint
Algoritmo pagocamisas
    Escribir "Ingresar la cantidad de camisas a comprar"
    Leer nc
    Escribir "Ingrese el precio de la camisa"
    Leer pc
    Si nc >= 3 Entonces
        costo<-nc*pc 
        Escribir "El costo de las camisas es " costo
        des<-costo*0.20
        Escribir "El descuento es " des
        pt<-costo-des
        Escribir "El costo total a pagar es " pt
    SiNo
        costo<-nc*pc 
        Escribir "El costo de las camisas es " costo
        des<-costo*0.10
        Escribir "El descuento es " des
        pt<-costo-des
        Escribir "El costo total a pagar es " pt
    FinSi
FinAlgoritmo
```

5. Un cliente va a comprar una moto y se percata que si lo compraba el día martes tiene un descuento del 12%, luego si lo compra el día sábado tiene un descuento del 18% y si es feriado un 25%, mostrar cuanto pagara en cada opción.

```pseint
Algoritmo compramoto
dia <- " "
precio <- 0
Escribir "Ingrese el costo de la moto"
Leer precio
Escribir "Ingrese el dia de la compra"
Leer dia
Si dia = "martes" Entonces
    des <- precio * 0.12
    Escribir "El descuento es: " des
    pago <- precio - des
    Escribir "El pago total de la moto es: " pago
SiNo
    Si dia = "sabado" Entonces
        des <- precio * 0.18
        Escribir "El descuento es: " des
        pago <- precio - des
        Escribir "El pago total de la moto es: " pago
    SiNo
        des <- precio * 0.25
        Escribir "El descuento es: " des
        pago <- precio - des
        Escribir "El pago total de la moto es: " pago
    FinSi
FinSi
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
