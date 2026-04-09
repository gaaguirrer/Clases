# **Sensor de temperatura y humedad (DHT11 y DHT22)**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 08\tkc1.png" align="left" width="250" style="margin-right: 20px;">
El DHT11 y el DHT22 son sensores de temperatura y humedad ampliamente utilizados en proyectos de electrónica y domótica. Aunque ambos sensores tienen funciones similares y la misma interfaz de comunicación (un solo cable de datos), existen diferencias clave entre ellos en cuanto a precisión, rango de medición y velocidad de muestreo. A continuación, se detallan las características de ambos sensores:

### **DHT11**:
- Rango de Temperatura: 0 a 50 °C
- Precisión de Temperatura: ±2 °C
- Rango de Humedad: 20-90% RH
- Precisión de Humedad: ±5% RH
- Frecuencia de Muestreo: 1 muestra por segundo (1 Hz)
- Durabilidad: Vida útil moderada
- Costo: Bajo

### **DHT22**:
- Rango de Temperatura: -40 a 80 °C
- Precisión de Temperatura: ±0.5 °C
- Rango de Humedad: 0-100% RH
- Precisión de Humedad: ±2-5% RH
- Frecuencia de Muestreo: 0.5 Hz (una muestra cada 2 segundos)
- Durabilidad: Vida útil más larga
- Costo: Moderadamente más alto que el DHT11

## **Interfaz y Código**
Ambos sensores utilizan un protocolo de comunicación digital de un solo hilo, y se pueden conectar de manera similar a microcontroladores como Arduino, ESP8266 o ESP32. A menudo, la misma biblioteca de software puede utilizarse para ambos sensores, aunque es necesario tener en cuenta los tiempos de muestreo y las diferencias en precisión al interpretar los datos.

A continuación, se presenta un ejemplo de código para Arduino utilizando la biblioteca DHT de Adafruit, que es compatible con ambos sensores. Este código muestra cómo inicializar y leer datos tanto del DHT11 como del DHT22.

## **Código Arduino**

```cpp
#include "DHT.h"

// Definir el pin al que está conectado el sensor
#define DHTPIN 2     

// Definir el tipo de sensor
//#define DHTTYPE DHT11   // Descomentar esta línea si se usa el DHT11
#define DHTTYPE DHT22   // Descomentar esta línea si se usa el DHT22

// Inicializar el sensor DHT
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Inicializar la comunicación serie para la depuración
  Serial.begin(9600);
  Serial.println("DHTxx test!");

  // Inicializar el sensor DHT
  dht.begin();
}

void loop() {
  // Esperar unos segundos entre mediciones
  delay(2000);

  // Leer la humedad
  float h = dht.readHumidity();
  // Leer la temperatura en grados Celsius (por defecto)
  float t = dht.readTemperature();
  // Leer la temperatura en grados Fahrenheit
  float f = dht.readTemperature(true);

  // Verificar si alguna lectura ha fallado y salir temprano (para intentarlo de nuevo)
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Falla al leer el sensor de calor!");
    return;
  }

  // Calcular el índice de calor en grados Fahrenheit
  float hif = dht.computeHeatIndex(f, h);
  // Calcular el índice de calor en grados Celsius
  float hic = dht.computeHeatIndex(t, h, false);

  // Mostrar los resultados
  // Imprimir la humedad
  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t"); // \t agrega una tabulación para una mejor legibilidad

  // Imprimir la temperatura en grados Celsius
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.print(" *C "); // *C indica grados Celsius

  // Imprimir la temperatura en grados Fahrenheit
  Serial.print(f);
  Serial.print(" *F\t"); // \t agrega una tabulación para una mejor legibilidad

  // Imprimir el índice de calor en grados Celsius
  Serial.print("Índice de calor: ");
  Serial.print(hic);
  Serial.print(" *C "); // *C indica grados Celsius

  // Imprimir el índice de calor en grados Fahrenheit
  Serial.print(hif);
  Serial.println(" *F"); // \n indica una nueva línea

  // Nota: El índice de calor (heat index) se calcula en función de la temperatura y la humedad,
  // proporcionando una medida de cómo se siente realmente la temperatura en función de la humedad.
}


```
[enlace en línea](https://www.tinkercad.com/things/254aJdmC3zK-practica-08-p1-sensor-de-temperatura-y-humedad-dht11-y-22)
