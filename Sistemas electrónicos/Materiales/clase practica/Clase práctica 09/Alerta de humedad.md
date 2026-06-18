# **Alerta de humedad con Sensor de Humedad de Suelo y Zumbador**

<img src="tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Explicación del código**

Este programa lee un sensor de humedad de suelo y activa un zumbador cuando la humedad cae por debajo del 30%. Es útil para sistemas de riego automatizado que alertan cuando la tierra está seca.

### **1. Declaración de pines y variables**

```cpp
const int sensorPin = A0;
const int sensorVCC = A2;
const int buzzerPin = 3;

int lectura = 0;
int humedadPorcentaje = 0;
```

- `sensorPin = A0`: Pin de señal del sensor de humedad.
- `sensorVCC = A2`: Pin que alimenta el sensor (se usa como salida digital para controlar la alimentación).
- `buzzerPin = 3`: Pin para el zumbador activo.
- `lectura`: Almacena el valor analógico crudo del sensor (0-1023).
- `humedadPorcentaje`: Almacena el porcentaje de humedad calculado.

### **2. Configuración `setup()`**

```cpp
void setup()
{
  Serial.begin(9600);
  pinMode(sensorVCC, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  digitalWrite(sensorVCC, HIGH);
}
```

- Inicia la comunicación serie para visualizar los valores del sensor.
- Configura el pin de alimentación del sensor como salida y lo enciende (HIGH).
- Configura el pin del zumbador como salida.

### **3. Bucle `loop()`**

```cpp
void loop()
{
  lectura = analogRead(sensorPin);
  humedadPorcentaje = map(lectura, 1023, 0, 0, 100);

  Serial.print("Lectura: ");
  Serial.print(lectura);
  Serial.print("\t Humedad: ");
  Serial.print(humedadPorcentaje);
  Serial.println(" %");

  if (humedadPorcentaje < 30)
  {
    tone(buzzerPin, 1000);
  }
  else
  {
    noTone(buzzerPin);
  }

  delay(500);
}
```

- `analogRead(sensorPin)`: Lee el valor analógico del sensor (0-1023).
- `map(lectura, 1023, 0, 0, 100)`: Convierte el valor leído a porcentaje. Los valores se invierten (suelo seco da lecturas altas, suelo húmedo da lecturas bajas).
- `tone(buzzerPin, 1000)`: Activa el zumbador con una frecuencia de 1000 Hz cuando la humedad es menor al 30%.
- `noTone(buzzerPin)`: Apaga el zumbador cuando la humedad es suficiente.
- `delay(500)`: Pausa de 500 ms entre lecturas.

### **Código completo para copiar y pegar**

```cpp
// Alerta de humedad con Sensor de Humedad de Suelo

const int sensorPin = A0;
const int sensorVCC = A2;
const int buzzerPin = 3;

int lectura = 0;
int humedadPorcentaje = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(sensorVCC, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  digitalWrite(sensorVCC, HIGH);
}

void loop()
{
  lectura = analogRead(sensorPin);
  humedadPorcentaje = map(lectura, 1023, 0, 0, 100);

  Serial.print("Lectura: ");
  Serial.print(lectura);
  Serial.print("\t Humedad: ");
  Serial.print(humedadPorcentaje);
  Serial.println(" %");

  if (humedadPorcentaje < 30)
  {
    tone(buzzerPin, 1000);
  }
  else
  {
    noTone(buzzerPin);
  }

  delay(500);
}
```

---

## **Preguntas teóricas**

1. ¿Por qué se usa `map(lectura, 1023, 0, 0, 100)` con los valores mínimo y máximo invertidos? ¿Qué representa cada extremo?
2. ¿Qué diferencia hay entre un zumbador activo y uno pasivo? ¿Con cuál funciona `tone()`?
3. ¿Por qué se alimenta el sensor desde un pin digital (A2) en lugar de conectarlo directamente a 5V?
4. ¿Qué función cumple `tone()` y cuáles son sus parámetros? ¿Cómo se apaga el tono?
5. ¿Cómo se determinan los valores máximo y mínimo del sensor de humedad? ¿Qué experimentos harías para encontrarlos?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Cambia el umbral de activación del zumbador al 50% en lugar del 30%.
*Pregunta:* ¿El zumbador se activa con mayor o menor humedad? ¿Cómo afecta esto a un sistema de riego?

### **Ejercicio 2**
Agrega un LED en el pin 4 que se encienda cuando la humedad sea menor al 30% (misma condición que el zumbador).
*Pregunta:* ¿La alerta visual y sonora funcionan simultáneamente? ¿Cuál es más útil en cada contexto?

### **Ejercicio 3**
Cambia la frecuencia del zumbador según el nivel de humedad: usa 500 Hz para humedad entre 20-30%, 1000 Hz para 10-20%, y 2000 Hz para menos de 10%.
*Pregunta:* ¿Cómo implementaste los diferentes tonos? ¿Usaste `if-else if` anidados?

### **Ejercicio 4**
Agrega un segundo umbral: activa un LED verde en el pin 5 cuando la humedad sea mayor al 70% (suelo húmedo).
*Pregunta:* ¿Cómo combinaste las condiciones para tener 3 estados (seco, normal, húmedo)?

### **Ejercicio 5**
Muestra el porcentaje de humedad en una pantalla LCD 16×2 conectada en los pines 7-12.
*Pregunta:* ¿Qué librería necesitas? ¿Cómo distribuyes la información en las dos filas?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
