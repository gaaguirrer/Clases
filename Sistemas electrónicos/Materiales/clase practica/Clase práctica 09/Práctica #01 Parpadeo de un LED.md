# **Parpadeo de un LED**

<img src="tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Explicación del código**

Este programa enciende y apaga un LED conectado al pin 13 de forma continua, con un intervalo de 1 segundo. Es el programa equivalente al "Hello World" en Arduino y sirve para verificar que la placa y el LED funcionan correctamente.

### **1. Configuración `setup()`**

```cpp
void setup()
{
  pinMode(13, OUTPUT);
}
```

- `pinMode(13, OUTPUT);`: Configura el pin digital 13 como salida. El pin 13 tiene un LED incorporado en la mayoría de las placas Arduino, por lo que no requiere componentes externos.

### **2. Bucle `loop()`**

```cpp
void loop()
{
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

- `digitalWrite(13, HIGH);`: Establece el pin 13 a 5 V, encendiendo el LED.
- `delay(1000);`: Detiene la ejecución durante 1000 milisegundos (1 segundo) mientras el LED permanece encendido.
- `digitalWrite(13, LOW);`: Establece el pin 13 a 0 V, apagando el LED.
- `delay(1000);`: Mantiene el LED apagado durante 1 segundo antes de repetir el ciclo.
- El bucle se repite infinitamente, generando un parpadeo constante de 1 Hz (un ciclo por segundo).

### **Código completo para copiar y pegar**

```cpp
// Parpadeo de un LED

void setup()
{
  pinMode(13, OUTPUT);
}

void loop()
{
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

---

## **Preguntas teóricas**

1. ¿Qué hace la función `pinMode()` y por qué es necesario llamarla en `setup()`?
2. ¿Qué diferencia hay entre `digitalWrite(pin, HIGH)` y `digitalWrite(pin, LOW)`?
3. ¿Cuánto dura un ciclo completo de parpadeo (encendido + apagado)? ¿Cuál es la frecuencia en Hz?
4. ¿Qué sucede si se conecta un LED externo al pin 13 sin resistencia? ¿Por qué?
5. ¿Qué pasaría si se elimina el `delay(1000)` después de apagar el LED?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Cambia el tiempo de parpadeo a 200 ms encendido y 200 ms apagado.
*Pregunta:* ¿Cómo se percibe el parpadeo? ¿Se ve más rápido?

### **Ejercicio 2**
Cambia los tiempos para que el LED esté encendido 200 ms y apagado 800 ms.
*Pregunta:* ¿Qué efecto visual se produce? ¿Parece un "destello" breve?

### **Ejercicio 3**
Conecta un LED externo en el pin 12 con una resistencia de 220 Ω. Haz que ambos LEDs (interno y externo) parpadeen alternadamente (uno se enciende mientras el otro se apaga).
*Pregunta:* ¿Cómo sincronizaste ambos LEDs? ¿Usaste variables para los pines?

### **Ejercicio 4**
Haz que el LED parpadee 3 veces rápido (200 ms) y luego permanezca apagado 2 segundos, repitiendo el patrón.
*Pregunta:* ¿Cómo implementaste el patrón? ¿Usaste un bucle `for` para las 3 repeticiones?

### **Ejercicio 5**
Reemplaza los valores fijos de delay por variables constantes (`const int`) y explica por qué es una buena práctica.
*Pregunta:* ¿Qué ventajas tiene usar constantes con nombres descriptivos en lugar de números literales?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
