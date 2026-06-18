# **Intensidad LED - Ciclo FOR**

<img src="tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Explicación del código**

Este programa utiliza un bucle `for` para aumentar y disminuir gradualmente la intensidad de un LED mediante PWM (modulación por ancho de pulso). El LED realiza un efecto de "respiración" al incrementar y reducir su brillo de forma continua.

### **1. Declaración de variables globales**

```cpp
int led_pwm = 3, brillo = 0;
```

- `int led_pwm = 3;`: Define el pin 3 para la salida PWM del LED. El pin 3 tiene capacidad PWM (~).
- `int brillo = 0;`: Variable que almacenará el valor de brillo actual, de 0 (apagado) a 255 (máximo brillo).

### **2. Configuración `setup()`**

```cpp
void setup()
{
  pinMode(led_pwm, OUTPUT);
}
```

- `pinMode(led_pwm, OUTPUT);`: Configura el pin 3 como salida para poder usar `analogWrite()`.

### **3. Bucle `loop()`**

```cpp
void loop()
{
  for(brillo = 0; brillo < 256; brillo++)
  {
    analogWrite(led_pwm, brillo);
    delay(30);
  }
  for(brillo = 255; brillo >= 0; brillo--)
  {
    analogWrite(led_pwm, brillo);
    delay(30);
  }
}
```

- `for(brillo = 0; brillo < 256; brillo++)`: Bucle ascendente que incrementa `brillo` de 0 a 255. En cada iteración:
  - `analogWrite(led_pwm, brillo);`: Establece el ciclo de trabajo PWM según el valor de `brillo`. 0 es 0% (apagado), 255 es 100% (máximo brillo).
  - `delay(30);`: Pausa de 30 ms para que el cambio sea perceptible visualmente.
- `for(brillo = 255; brillo >= 0; brillo--)`: Bucle descendente que reduce `brillo` de 255 a 0, generando el efecto inverso.
- La alternancia entre ambos bucles produce un efecto de aumento y disminución continua del brillo.

### **Código completo para copiar y pegar**

```cpp
// Intensidad LED - Ciclo FOR

int led_pwm = 3, brillo = 0;

void setup()
{
  pinMode(led_pwm, OUTPUT);
}

void loop()
{
  for(brillo = 0; brillo < 256; brillo++)
  {
    analogWrite(led_pwm, brillo);
    delay(30);
  }
  for(brillo = 255; brillo >= 0; brillo--)
  {
    analogWrite(led_pwm, brillo);
    delay(30);
  }
}
```

### **Enlace al simulador**

[Código en Tinkercad](https://www.tinkercad.com/things/aP2QLXK1Coa-practica-04-p1-intensidad-led-ciclo-for)

---

## **Preguntas teóricas**

1. ¿Qué significa PWM y cómo funciona en Arduino? ¿Qué pines tienen capacidad PWM?
2. ¿Cuál es el rango de valores que acepta `analogWrite()` y qué corresponde cada extremo?
3. ¿Por qué el bucle `for` usa `brillo < 256` en lugar de `brillo <= 255`? ¿Cuántas iteraciones tiene ese bucle?
4. ¿Qué sucedería si se eliminan los `delay(30)` dentro de los bucles? ¿Se notaría el cambio de intensidad?
5. ¿Qué diferencia hay entre `analogWrite()` y `digitalWrite()`? ¿En qué situaciones se usa cada uno?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Cambia el `delay(30)` a `delay(5)` y luego a `delay(100)`. Prueba ambos valores.
*Pregunta:* ¿Cómo afecta el delay a la velocidad del efecto de respiración? ¿Con qué valor se ve más suave?

### **Ejercicio 2**
Modifica el bucle ascendente para que vaya de 0 a 255 en pasos de 5 (`brillo += 5`) y el descendente en pasos de 5 (`brillo -= 5`).
*Pregunta:* ¿Cómo cambia el efecto visual? ¿Se nota una transición más abrupta?

### **Ejercicio 3**
Agrega un segundo LED en el pin 5 que haga el efecto inverso: mientras el primer LED aumenta su brillo, el segundo disminuye.
*Pregunta:* ¿Cómo sincronizas ambos LEDs? Describe el patrón visual resultante.

### **Ejercicio 4**
Reemplaza el valor fijo 30 del delay por una variable que también varíe con un bucle `for`, de modo que la velocidad de transición también cambie cíclicamente.
*Pregunta:* ¿El efecto es más interesante? ¿Cómo se comporta la velocidad a lo largo del tiempo?

### **Ejercicio 5**
Usando un solo `for` y una bandera (`bool subiendo`), reescribe el programa para que funcione con un solo bucle que cambie de dirección cuando llegue a los extremos.
*Pregunta:* ¿Qué ventaja tiene este enfoque frente a usar dos bucles `for` separados?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
