# **CONTADOR CON UN DISPLAY DE SIETE SEGMENTOS Y 4 DÍGITOS**

<img src="5461aspng.png" align="left" width="250" style="margin-right: 20px;">

Para conectar el display de 7 segmentos y 4 dígitos 5461AS-1 a una placa Arduino Uno y controlar la velocidad con que aumentan los números usando un potenciómetro, además de usar un botón como reset, sigue el siguiente esquema de conexiones y el código proporcionado.

## **Explicación del código**

Este programa implementa un contador de 0 a 9999 en un display de 4 dígitos (5461AS-1). La velocidad de conteo se ajusta con un potenciómetro y un botón de reset permite reiniciar el contador. Utiliza multiplexación por dígitos para mostrar diferentes valores en cada posición.

### **1. Declaración de pines y variables**

```cpp
const int segmPins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
const int pinD[4] = {10, 11, 12, 13};
const int resetButton = 14;
const int ptm = A0;

int num = 0;

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
```

- `segmPins[8]`: Pines para los segmentos A-G y DP (punto decimal).
- `pinD[4]`: Pines de control de los 4 dígitos (cátodos comunes). Se activan con LOW.
- `resetButton = 14;`: Pin para el botón de reset (pull-up interna).
- `ptm = A0;`: Pin analógico para el potenciómetro.
- `numeros[10]`: Arreglo de 10 bytes, cada uno codifica con bits qué segmentos encender para cada dígito (0-9). El prefijo `0b` indica que son números binarios.

### **2. Configuración `setup()`**

```cpp
void setup() {
  for (int i = 0; i < 8; i++) {
    pinMode(segmPins[i], OUTPUT);
    digitalWrite(segmPins[i], LOW);
  }
  for (int i = 0; i < 4; i++) {
    pinMode(pinD[i], OUTPUT);
    digitalWrite(pinD[i], HIGH);
  }
  pinMode(resetButton, INPUT_PULLUP);
}
```

- Configura todos los pines de segmentos como salidas y los apaga (LOW).
- Configura los pines de dígitos como salidas y los desactiva (HIGH para ánodo común o cátodo con transistor).
- Configura el botón de reset como entrada con resistencia pull-up interna (pin 14 = A0 como digital).

### **3. Bucle `loop()`**

```cpp
void loop() {
  if (digitalRead(resetButton) == LOW) {
    num = 0;
  }

  int delayTime = map(analogRead(ptm), 0, 1023, 100, 1000);

  for (int i = 0; i < 4; i++) {
    int digito = (num / (int)pow(10, i)) % 10;
    displaydigito(digito, i);
    delay(5);
  }

  delay(delayTime);
  num++;
  if (num > 9999) num = 0;
}
```

- `digitalRead(resetButton) == LOW`: Si se presiona el botón (LOW por pull-up), reinicia `num` a 0.
- `delayTime = map(analogRead(ptm), 0, 1023, 100, 1000)`: Convierte el valor del potenciómetro en un retardo entre 100 y 1000 ms que controla la velocidad de conteo.
- El bucle `for` recorre las 4 posiciones del display:
  - `(num / (int)pow(10, i)) % 10`: Extrae el dígito correspondiente (unidades, decenas, centenas, millares).
  - `displaydigito(digito, i)`: Muestra el dígito en la posición correspondiente.
  - `delay(5)`: Pequeña pausa entre dígitos para evitar parpadeo.
- `num++`: Incrementa el contador.
- `if (num > 9999) num = 0`: Reinicia al superar 9999.

### **4. Función `displaydigito()`**

```cpp
void displaydigito(int digito, int posicion) {
  byte segmento = numeros[digito];
  for (int i = 0; i < 8; i++) {
    digitalWrite(segmPins[i], segmento & (1 << i));
  }
  digitalWrite(pinD[posicion], LOW);
  delay(2);
  digitalWrite(pinD[posicion], HIGH);
}
```

- `numeros[digito]`: Obtiene el byte de configuración de segmentos para el dígito.
- `segmento & (1 << i)`: Operación bitwise que extrae cada bit del byte para determinar si el segmento `i` debe encenderse.
- `digitalWrite(pinD[posicion], LOW)`: Activa el dígito correspondiente.
- `delay(2)`: Mantiene el dígito encendido 2 ms.
- `digitalWrite(pinD[posicion], HIGH)`: Apaga el dígito antes de pasar al siguiente.

### **Código completo para copiar y pegar**

```cpp
// Contador con Display 7 segmentos y 4 dígitos (5461AS-1)

const int segmPins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
const int pinD[4] = {10, 11, 12, 13};
const int resetButton = 14;
const int ptm = A0;

int num = 0;

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
  for (int i = 0; i < 8; i++) {
    pinMode(segmPins[i], OUTPUT);
    digitalWrite(segmPins[i], LOW);
  }
  for (int i = 0; i < 4; i++) {
    pinMode(pinD[i], OUTPUT);
    digitalWrite(pinD[i], HIGH);
  }
  pinMode(resetButton, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(resetButton) == LOW) {
    num = 0;
  }

  int delayTime = map(analogRead(ptm), 0, 1023, 100, 1000);

  for (int i = 0; i < 4; i++) {
    int digito = (num / (int)pow(10, i)) % 10;
    displaydigito(digito, i);
    delay(5);
  }

  delay(delayTime);
  num++;
  if (num > 9999) num = 0;
}

void displaydigito(int digito, int posicion) {
  byte segmento = numeros[digito];
  for (int i = 0; i < 8; i++) {
    digitalWrite(segmPins[i], segmento & (1 << i));
  }
  digitalWrite(pinD[posicion], LOW);
  delay(2);
  digitalWrite(pinD[posicion], HIGH);
}
```

### **Enlace al simulador**

[Código en Tinkercad](https://www.tinkercad.com/things/kYKOS14DgBW-practica-05-p4-display-7-segmentos-y-4-digitos)

---

## **Preguntas teóricas**

1. ¿Qué es la multiplexación y por qué es necesaria en un display de 4 dígitos?
2. Explica la expresión `(num / (int)pow(10, i)) % 10`. ¿Cómo extrae cada dígito individual?
3. ¿Qué hace el operador `& (1 << i)` en la función `displaydigito()`? ¿Cómo se relaciona con los bits del byte?
4. ¿Por qué se usa `INPUT_PULLUP` para el botón de reset? ¿Qué nivel lógico tiene cuando está presionado?
5. ¿Qué función cumple `delay(2)` dentro de `displaydigito()`? ¿Qué pasaría si se omite?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Cambia el rango del `map()` para que el potenciómetro controle la velocidad entre 50 ms y 2000 ms.
*Pregunta:* ¿Cómo afecta el rango más amplio a la experiencia de control? ¿El contador puede ir muy lento?

### **Ejercicio 2**
Modifica el programa para que el contador cuente hacia atrás (de 9999 a 0) en lugar de hacia adelante.
*Pregunta:* ¿Qué cambios hiciste en el `loop()`? ¿El botón de reset sigue funcionando?

### **Ejercicio 3**
Agrega un segundo botón en el pin 15 que, al presionarlo, pause/reanude el contador (sin reiniciarlo).
*Pregunta:* ¿Cómo implementaste la pausa? ¿Usaste una bandera `bool pausa`?

### **Ejercicio 4**
Haz que el punto decimal (DP) del primer dígito parpadee a 500 ms como indicador visual de que el sistema está funcionando.
*Pregunta:* ¿Qué segmento adicional debes controlar? ¿Cómo intercalas el parpadeo sin usar `delay()`?

### **Ejercicio 5**
Reemplaza el uso de `pow(10, i)` por una división iterativa manual para evitar la biblioteca matemática.
*Pregunta:* ¿Cómo extraes cada dígito sin usar `pow()`? ¿El código ocupa menos memoria?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
