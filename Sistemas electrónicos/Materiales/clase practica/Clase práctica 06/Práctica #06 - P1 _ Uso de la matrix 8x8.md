# **Uso de la matrix 8x8**
<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 06\1588AS-LED-Matrix.png" align="left" width="350" style="margin-right: 20px;">

## **Conexiones**


| Pin    | Ubicación        | Conector |
|--------|------------------|----------|
| Pin 0  | Columna 8        | C8       |
| Pin 1  | Columna 7        | C7       |
| Pin 2  | Fila 2           | R2       |
| Pin 3  | Columna 1        | C1       |
| Pin 4  | Fila 4           | R4       |
| Pin 5  | Columna 6        | C6       |
| Pin 6  | Columna 4        | C4       |
| Pin 7  | Fila 1           | R1       |
| Pin 8  | Fila 5           | R5       |
| Pin 9  | Fila 7           | R7       |
| Pin 10 | Columna 2        | C2       |
| Pin 11 | Columna 3        | C3       |
| Pin 12 | Fila 8           | R8       |
| Pin 13 | Columna 5        | C5       |
| Pin A0 | Fila 5           | R5       |
| Pin A1 | Fila 7           | R7       |

<img src="C:\one\OneDrive - UNP Universidad Nacional Politécnica\Clases\Materias\Sistemas electrónicos\Materiales\clase practica\Clase práctica 06\Matriz 8x8_bb.jpg" align="center" width="550" style="margin-right: 20px;">


En cada fila se conecta una resistencia de 330 ohms
<br> <!-- Línea en blanco -->

## **Código Arduino**


```cpp
// Definición de pines para las columnas
const int colPins[8] = {0, 1, 3, 10, 11, 6, 13, 5};
// Definición de pines para las filas
const int rowPins[8] = {7, 2, 4, 8, A0, 9, A1, 12};

void setup() {
  // Configuramos los pines de las columnas como salidas
  for (int i = 0; i < 8; i++) {
    pinMode(colPins[i], OUTPUT);
    digitalWrite(colPins[i], HIGH); // Apagamos todas las columnas
  }

  // Configuramos los pines de las filas como salidas
  for (int i = 0; i < 8; i++) {
    pinMode(rowPins[i], OUTPUT);
    digitalWrite(rowPins[i], LOW); // Apagamos todas las filas
  }
}

void loop() {
  // Encendemos cada LED uno por uno
  for (int row = 0; row < 8; row++) {
    for (int col = 0; col < 8; col++) {
      lightLed(row, col);
      delay(100); // Esperamos 100 milisegundos
      clearLed(row, col);
    }
  }
}

// Función para encender un LED específico
void lightLed(int row, int col) {
  digitalWrite(colPins[col], LOW);  // Encendemos la columna
  digitalWrite(rowPins[row], HIGH); // Encendemos la fila
}

// Función para apagar un LED específico
void clearLed(int row, int col) {
  digitalWrite(colPins[col], HIGH); // Apagamos la columna
  digitalWrite(rowPins[row], LOW);  // Apagamos la fila
}

```
[enlace en línea]()
