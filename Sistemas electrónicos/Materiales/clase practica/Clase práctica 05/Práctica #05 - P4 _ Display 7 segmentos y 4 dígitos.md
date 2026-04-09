# **CONTADOR CON UN DISPLAY DE SIETE SEGMENTOS Y 4 DÍGITOS**

<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 05\5461aspng.png" align="left" width="250" style="margin-right: 20px;">

Para conectar el display de 7 segmentos y 4 dígitos 5461AS-1 a una placa Arduino Uno y controlar la velocidad con que aumentan los números usando un potenciómetro, además de usar un botón como reset, sigue el siguiente esquema de conexiones y el código proporcionado.
<br> <!-- Línea en blanco -->
<br> <!-- Línea en blanco -->
<br> <!-- Línea en blanco -->

## **Esquema de conexiones**

### **Display 5461AS-1**:
- A: Pin 2
- B: Pin 3
- C: Pin 4
- D: Pin 5
- E: Pin 6
- F: Pin 7
- G: Pin 8
- DP: Pin 9
- D1: Pin 10
- D2: Pin 11
- D3: Pin 12
- D4: Pin 13

### **Potenciómetro**:
- GND: GND Arduino
- VCC: 5V Arduino
- Signal: Pin A0

### **Botón de reset**:
- Un pin a GND
- Otro pin a Pin 14 (con una resistencia pull-up de 10kΩ al pin 5V)

## **Código Arduino**
```cpp
// Definición de los pines de los segmentos del display de 7 segmentos
const int segmPins[8] = {2, 3, 4, 5, 6, 7, 8, 9};  // a, b, c, d, e, f, g, dp
// Definición de los pines de control de los dígitos
const int pinD[4] = {10, 11, 12, 13};  // D1, D2, D3, D4

// Definición del pin del botón de reset
const int resetButton = 14;
// Definición del pin del potenciómetro
const int ptm = A0;

// Variable que guarda el número actual a mostrar
int num = 0;

// Matriz que guarda los valores de los segmentos para cada número del 0 al 9
const byte numeros[10] = {
  0b00111111, // 0
  0b00000110, // 1
  0b01011011, // 2
  0b01001111, // 3
  0b01100110, // 4
  0b01101101, // 5
  0b01111101, // 6
  0b00000111, // 7
  0b01111111, // 8
  0b01101111  // 9
};

void setup() {
  // Configuración de los pines de los segmentos como salidas
  for (int i = 0; i < 8; i++) {
    pinMode(segmPins[i], OUTPUT);
    digitalWrite(segmPins[i], LOW);
  }
  // Configuración de los pines de los dígitos como salidas
  for (int i = 0; i < 4; i++) {
    pinMode(pinD[i], OUTPUT);
    digitalWrite(pinD[i], HIGH);
  }
  // Configuración del pin del botón de reset como entrada con resistencia pull-up
  pinMode(resetButton, INPUT_PULLUP);
}

void loop() {
  // Si el botón de reset es presionado, reiniciar el número a 0
  if (digitalRead(resetButton) == LOW) {
    num = 0;
  }

  // Leer el valor del potenciómetro y mapearlo a un rango de 100 a 1000 ms
  int delayTime = map(analogRead(ptm), 0, 1023, 100, 1000);

  // Mostrar cada dígito del número en el display
  for (int i = 0; i < 4; i++) {
    int digito = (num / (int)pow(10, i)) % 10; // Extraer el dígito correspondiente
    displaydigito(digito, i); // Mostrar el dígito en la posición correspondiente
    delay(5);  // Pequeño retraso para prevenir parpadeo
  }

  delay(delayTime); // Retraso basado en el valor del potenciómetro
  num++; // Incrementar el número
  if (num > 9999) num = 0; // Reiniciar el número si supera 9999
}

void displaydigito(int digito, int posicion) {
  // Obtener el byte que representa los segmentos encendidos para el dígito
  byte segmento = numeros[digito];
  // Encender/apagar cada segmento según el byte correspondiente
  for (int i = 0; i < 8; i++) {
    digitalWrite(segmPins[i], segmento & (1 << i));
  }
  // Encender el dígito correspondiente (activar el transistor o controlador de dígito)
  digitalWrite(pinD[posicion], LOW);
  delay(2); // Pequeño retraso para asegurar que el dígito se muestra
  // Apagar el dígito (desactivar el transistor o controlador de dígito)
  digitalWrite(pinD[posicion], HIGH);
}
```

## **Notas sobre el esquema y el código**

### **Esquema de conexiones**:
- Los pines del segmento están conectados a los pines digitales del Arduino.
- Los pines del dígito están conectados a otros pines digitales del Arduino y se controlan para encender el dígito correspondiente.
- El potenciómetro está conectado al pin analógico A0 para leer el valor y ajustar la velocidad de incremento del número.
- El botón de reset está conectado al pin digital 14 con una resistencia pull-up interna.

### **Código**:
- El código configura los pines como salidas y los inicializa.
- En el loop principal, el valor del potenciómetro se lee para determinar la velocidad de incremento.
- Se actualiza y muestra el número en el display, incrementándolo hasta un máximo de 9999.
- El botón de reset restablece el número a 0 cuando se presiona.

#### **Definición de pines y variables**:
- **segmPins**: Define los pines que controlan los segmentos del display de 7 segmentos.
- **pinD**: Define los pines que controlan los dígitos del display.
- **resetButton**: Define el pin del botón de reset.
- **ptm**: Define el pin del potenciómetro.
- **num**: Variable que guarda el número actual a mostrar en el display.
- **numeros**: Matriz que guarda los valores binarios que representan los segmentos encendidos para cada dígito del 0 al 9.

#### **Función setup()**:
- Configura los pines de los segmentos y dígitos como salidas.
- Inicializa todos los segmentos y dígitos apagados.
- Configura el pin del botón de reset como entrada con resistencia pull-up.

#### **Función loop()**:
- Verifica si el botón de reset ha sido presionado para reiniciar el contador.
- Lee el valor del potenciómetro y lo convierte en un tiempo de retardo.
- Muestra el número actual en el display, actualizando cada dígito.
- Incrementa el número y lo reinicia a 0 si supera 9999.

#### **Función displaydigito()**:
- Toma un dígito y una posición, y enciende los segmentos adecuados para mostrar el dígito en la posición indicada.
- Utiliza un pequeño retardo para asegurar que el dígito se muestra correctamente antes de pasar al siguiente dígito.


[enlace en línea](https://www.tinkercad.com/things/kYKOS14DgBW-practica-05-p4-display-7-segmentos-y-4-digitos)