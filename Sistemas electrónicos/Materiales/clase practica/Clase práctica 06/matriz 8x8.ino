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

