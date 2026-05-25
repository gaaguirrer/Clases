# **LED con Pulsador - IF**

<img src="tkc2.png" align="left" width="350" style="margin-right: 20px;">

## **Explicación del código**

Este programa es el famoso "LED con Pulsador". Su objetivo es ejecutar una secuencia de encendido/apagado de tres LEDs (Verde, Amarillo y Rojo) **solo cuando se presiona un pulsador**. Se usa una estructura condicional `if` para leer el estado del pulsador y ejecutar la secuencia si se ha presionado. Es una introducción a la lectura de entradas digitales y al control del flujo del programa.

### **1. Declaración de variables globales**

```c++
const int led_rojo = 7;
const int led_amarillo = 8;
const int led_verde = 9;
const int pulsador = 10;
int tiempo = 500;
```

- `const int led_rojo = 7;`: Define el pin para el LED rojo como el pin digital 7. El uso de `const` evita que el valor se modifique accidentalmente en el programa.
- `const int led_amarillo = 8;`: Define el pin para el LED amarillo como el pin digital 8.
- `const int led_verde = 9;`: Define el pin para el LED verde como el pin digital 9.
- `const int pulsador = 10;`: Define el pin para el pulsador como el pin digital 10. Este pin se configurará como entrada para leer el estado del pulsador.
- `int tiempo = 500;`: Declara una variable llamada `tiempo` que almacena la duración de los delays (500 ms). Esto permite cambiar la velocidad de la secuencia modificando un solo número.

### **2. Configuración `setup()`**

```c++
void setup() {
  pinMode(led_rojo, OUTPUT);
  pinMode(led_amarillo, OUTPUT);
  pinMode(led_verde, OUTPUT);
  pinMode(pulsador, INPUT);
}
```

- Los pines de los LEDs se configuran como `OUTPUT` para poder controlarlos.
- El pin del pulsador se configura como `INPUT`. Esto significa que Arduino leerá el estado del pin (HIGH o LOW). Es necesario conectar el pulsador de manera que entregue HIGH cuando es presionado (conectándolo a VCC, generalmente 5V, y usando una resistencia "pull-down" para que lea LOW cuando no se presiona).

### **3. Bucle `loop()` con estructura `if`**

```c++
void loop() {
  if (digitalRead(pulsador) == HIGH) {
    digitalWrite(led_verde, HIGH);
    delay(tiempo);
    digitalWrite(led_amarillo, HIGH);
    delay(tiempo);
    digitalWrite(led_rojo, HIGH);
    delay(tiempo);
    digitalWrite(led_rojo, LOW);
    delay(tiempo);
    digitalWrite(led_amarillo, LOW);
    delay(tiempo);
    digitalWrite(led_verde, LOW);
    delay(tiempo);
  }
}
```

- `if (digitalRead(pulsador) == HIGH)`: Esta es la condición. La función `digitalRead(pulsador)` lee el estado del pin del pulsador. Si es `HIGH` (normalmente significa que el pulsador está presionado), las instrucciones dentro de las llaves `{ ... }` se ejecutarán. Si no, el programa simplemente las saltará y el bucle `loop` se repetirá hasta que se presione el pulsador.

#### **Secuencia de Encendido y Apagado:**

Dentro del `if`, el programa ejecuta la siguiente secuencia cuando se presiona el pulsador:

1.  **Verde ON:** `digitalWrite(led_verde, HIGH);` → Espera 0.5 segundos.
2.  **Amarillo ON:** `digitalWrite(led_amarillo, HIGH);` → Espera 0.5 segundos.
3.  **Rojo ON:** `digitalWrite(led_rojo, HIGH);` → Espera 0.5 segundos.
4.  **Rojo OFF:** `digitalWrite(led_rojo, LOW);` → Espera 0.5 segundos.
5.  **Amarillo OFF:** `digitalWrite(led_amarillo, LOW);` → Espera 0.5 segundos.
6.  **Verde OFF:** `digitalWrite(led_verde, LOW);` → Espera 0.5 segundos.

La combinación produce una onda de iluminación y apagado secuencial que simula un efecto tipo "carrusel".

### **Código completo para copiar y pegar**

```c++
// LED con Pulsador - IF
// Resistencias de 220 ohm en serie con cada LED

const int led_rojo = 7;
const int led_amarillo = 8;
const int led_verde = 9;
const int pulsador = 10;
int tiempo = 500;

void setup() {
  pinMode(led_rojo, OUTPUT);
  pinMode(led_amarillo, OUTPUT);
  pinMode(led_verde, OUTPUT);
  pinMode(pulsador, INPUT);
}

void loop() {
  if (digitalRead(pulsador) == HIGH) {
    digitalWrite(led_verde, HIGH);
    delay(tiempo);
    digitalWrite(led_amarillo, HIGH);
    delay(tiempo);
    digitalWrite(led_rojo, HIGH);
    delay(tiempo);
    digitalWrite(led_rojo, LOW);
    delay(tiempo);
    digitalWrite(led_amarillo, LOW);
    delay(tiempo);
    digitalWrite(led_verde, LOW);
    delay(tiempo);
  }
}
```

### **Enlace al simulador**

[Código en Tinkercad](https://www.tinkercad.com/things/dcOymPvmek8-practica-03-p2-led-con-pulsador-if)

---

## **Preguntas teóricas**

1. ¿Por qué el pin del pulsador se configura como `INPUT` y los pines de los LED como `OUTPUT`? ¿Qué función cumple la función `digitalRead()`?
2. En el contexto de un pulsador, ¿qué significa "PULL-DOWN" y "PULL-UP"? ¿Por qué es necesario y cómo se implementaría en el código para un pulsador que conecta a tierra?
3. Explica el propósito de la estructura condicional `if` y cómo funciona junto con `digitalRead()` para controlar la ejecución de la secuencia de luces.
4. Si se cambia la variable `tiempo` a 100 ms, ¿cómo cambiará la secuencia de los LEDs? Describe el efecto visual y su duración total.
5. ¿Qué sucede si se omite la línea `pinMode(pulsador, INPUT);` en el `setup()`? ¿El comportamiento del circuito sería el mismo? Justifica tu respuesta.

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Para cada ejercicio, copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Modifica el programa para que los LEDs se enciendan en orden inverso (Rojo, Amarillo, Verde) en lugar de verde, amarillo, rojo.
*Pregunta:* ¿Observas alguna diferencia en la secuencia respecto al original? ¿Es más fácil identificar el cambio?

### **Ejercicio 2**
Añade un cuarto LED Azul en el pin 6. Modifica el código para que después del LED verde, el LED azul también se encienda y luego se apague, integrando al azul en la secuencia final.
*Pregunta:* ¿Cómo afecta esto a la duración total de la secuencia? ¿Qué patrón de luces ves?

### **Ejercicio 3**
Cambia la lógica del pulsador para que el programa ejecute la secuencia cuando **no** se presione el pulsador y no haga nada cuando se presione. (Pista: Cambia la condición dentro del `if`).
*Pregunta:* ¿Cómo se comporta el circuito ahora? ¿Por qué este comportamiento podría ser útil en algún proyecto?

### **Ejercicio 4**
Elimina la línea `digitalWrite(led_rojo, LOW);`, `digitalWrite(led_amarillo, LOW);` y `digitalWrite(led_verde, LOW);` y sus respectivos `delay(tiempo)`. Deja solo la parte del encendido.
*Pregunta:* ¿Qué ocurre con los LEDs después de que la secuencia de encendido termina? ¿El programa regresa a su estado inicial? Explica qué ves.

### **Ejercicio 5**
Agrega un `delay(tiempo);` adicional **al final** de la secuencia dentro del `if` (justo antes de cerrar las llaves).
*Pregunta:* ¿Qué cambia en la respuesta del LED cuando se presiona el pulsador? ¿Hay algún efecto de "colapso" o retardo antes de que el sistema pueda responder nuevamente?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*