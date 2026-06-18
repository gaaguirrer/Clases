# **JUEGO DE LA SERPIENTE**

<img src="1588AS-LED-Matrix.png" align="left" width="250" style="margin-right: 20px;">

Para crear el juego de la serpiente con la matriz LED de 8×8 y el módulo joystick en una placa Arduino UNO, se presenta el esquema de conexión y el código en Arduino.

## **Explicación del código**

Este programa implementa el clásico juego "Snake" en una matriz LED de 8×8. La serpiente se controla con un joystick, crece al comer manzanas, y la velocidad aumenta progresivamente. El juego termina si la serpiente choca contra un borde o contra sí misma.

### **1. Definiciones y pines**

```cpp
#define FILAS 8
#define COLUMNAS 8

const int pinesColumnas[COLUMNAS] = {3, 10, 11, 6, 13, 5, 1, 0};
const int pinesFilas[FILAS] = {7, 2, A0, 4, 8, A1, 9, 12};

#define JOYSTICK_X A2
#define JOYSTICK_Y A3
#define JOYSTICK_SW A4
```

- Se definen las constantes `FILAS` y `COLUMNAS` para la matriz LED de 8×8.
- `pinesColumnas[]` y `pinesFilas[]`: Pines de conexión de la matriz.
- `JOYSTICK_X`, `JOYSTICK_Y`, `JOYSTICK_SW`: Pines para el joystick.

### **2. Variables globales**

```cpp
int direccion = 0; // 0: Derecha, 1: Abajo, 2: Izquierda, 3: Arriba
int velocidad = 500;

int serpienteX[64] = {4, 3, 2};
int serpienteY[64] = {4, 4, 4};
int longitudSerpiente = 3;

int manzanaX = 0;
int manzanaY = 0;
```

- `direccion`: Almacena la dirección actual del movimiento.
- `velocidad`: Tiempo entre movimientos (ms). Comienza en 500 ms.
- `serpienteX[]` y `serpienteY[]`: Coordenadas de cada segmento de la serpiente. La cabeza está en el índice 0.
- `longitudSerpiente`: Número de segmentos actuales de la serpiente.
- `manzanaX`, `manzanaY`: Coordenadas de la manzana.

### **3. Configuración `setup()`**

```cpp
void setup() {
  Serial.begin(9600);
  pinMode(JOYSTICK_SW, INPUT_PULLUP);

  for (int i = 0; i < COLUMNAS; i++) {
    pinMode(pinesColumnas[i], OUTPUT);
  }
  for (int i = 0; i < FILAS; i++) {
    pinMode(pinesFilas[i], OUTPUT);
  }

  randomSeed(analogRead(0));
  generarManzana();
}
```

- Configura los pines de la matriz como salidas y el botón del joystick como entrada pull-up.
- `randomSeed(analogRead(0))`: Inicializa el generador de números aleatorios con una semilla basada en ruido analógico.
- `generarManzana()`: Coloca la primera manzana en una posición aleatoria.

### **4. Bucle `loop()`**

```cpp
void loop() {
  leerJoystick();
  moverSerpiente();
  mostrarMatriz();
  delay(velocidad);
}
```

- `leerJoystick()`: Lee los ejes X/Y del joystick y actualiza la dirección.
- `moverSerpiente()`: Calcula la nueva posición de la cabeza, verifica colisiones, mueve el cuerpo y comprueba si comió la manzana.
- `mostrarMatriz()`: Actualiza la matriz LED con las posiciones de la serpiente y la manzana.
- `delay(velocidad)`: Controla la velocidad del juego.

### **5. Funciones auxiliares principales**

**`leerJoystick()`:** Lee los valores analógicos de los ejes y determina la dirección según umbrales (X < 300: izquierda, X > 700: derecha, Y < 300: arriba, Y > 700: abajo).

**`moverSerpiente()`:** Actualiza la cabeza según la dirección. Verifica colisiones contra bordes y contra el propio cuerpo. Si come la manzana, aumenta la longitud y reduce `velocidad` (mínimo 100 ms). Si choca, llama a `gameOver()`.

**`generarManzana():** Genera coordenadas aleatorias para la manzana, asegurando que no aparezca sobre la serpiente.

**`mostrarMatriz():** Recorre la matriz y enciende los LEDs correspondientes a la serpiente y la manzana, usando multiplexación con un pequeño retardo (`delayMicroseconds(100)`).

### **Código completo para copiar y pegar**

```cpp
// JUEGO DE LA SERPIENTE

#define FILAS 8
#define COLUMNAS 8

const int pinesColumnas[COLUMNAS] = {3, 10, 11, 6, 13, 5, 1, 0};
const int pinesFilas[FILAS] = {7, 2, A0, 4, 8, A1, 9, 12};

#define JOYSTICK_X A2
#define JOYSTICK_Y A3
#define JOYSTICK_SW A4

int direccion = 0;
int velocidad = 500;

int serpienteX[64] = {4, 3, 2};
int serpienteY[64] = {4, 4, 4};
int longitudSerpiente = 3;

int manzanaX = 0;
int manzanaY = 0;

void setup() {
  Serial.begin(9600);
  pinMode(JOYSTICK_SW, INPUT_PULLUP);

  for (int i = 0; i < COLUMNAS; i++) {
    pinMode(pinesColumnas[i], OUTPUT);
  }
  for (int i = 0; i < FILAS; i++) {
    pinMode(pinesFilas[i], OUTPUT);
  }

  randomSeed(analogRead(0));
  generarManzana();
}

void loop() {
  leerJoystick();
  moverSerpiente();
  mostrarMatriz();
  delay(velocidad);
}

void leerJoystick() {
  int x = analogRead(JOYSTICK_X);
  int y = analogRead(JOYSTICK_Y);

  if (x < 300) {
    direccion = 2;
  } else if (x > 700) {
    direccion = 0;
  } else if (y < 300) {
    direccion = 3;
  } else if (y > 700) {
    direccion = 1;
  }
}

void moverSerpiente() {
  int nuevaX = serpienteX[0];
  int nuevaY = serpienteY[0];

  switch (direccion) {
    case 0: nuevaX++; break;
    case 1: nuevaY++; break;
    case 2: nuevaX--; break;
    case 3: nuevaY--; break;
  }

  if (nuevaX < 0 || nuevaX >= COLUMNAS || nuevaY < 0 || nuevaY >= FILAS) {
    gameOver();
  }

  for (int i = 0; i < longitudSerpiente; i++) {
    if (serpienteX[i] == nuevaX && serpienteY[i] == nuevaY) {
      gameOver();
    }
  }

  for (int i = longitudSerpiente; i > 0; i--) {
    serpienteX[i] = serpienteX[i - 1];
    serpienteY[i] = serpienteY[i - 1];
  }

  serpienteX[0] = nuevaX;
  serpienteY[0] = nuevaY;

  if (nuevaX == manzanaX && nuevaY == manzanaY) {
    longitudSerpiente++;
    velocidad = max(100, velocidad - 50);
    generarManzana();
  }
}

void generarManzana() {
  bool manzanaValida = false;
  while (!manzanaValida) {
    manzanaX = random(0, COLUMNAS);
    manzanaY = random(0, FILAS);
    manzanaValida = true;
    for (int i = 0; i < longitudSerpiente; i++) {
      if (serpienteX[i] == manzanaX && serpienteY[i] == manzanaY) {
        manzanaValida = false;
        break;
      }
    }
  }
}

void mostrarMatriz() {
  for (int i = 0; i < FILAS; i++) {
    digitalWrite(pinesFilas[i], LOW);
  }

  for (int i = 0; i < FILAS; i++) {
    for (int j = 0; j < COLUMNAS; j++) {
      if (haySerpiente(j, i) || hayManzana(j, i)) {
        digitalWrite(pinesColumnas[j], LOW);
      } else {
        digitalWrite(pinesColumnas[j], HIGH);
      }
    }
    digitalWrite(pinesFilas[i], HIGH);
    delayMicroseconds(100);
    digitalWrite(pinesFilas[i], LOW);
  }
}

bool haySerpiente(int x, int y) {
  for (int i = 0; i < longitudSerpiente; i++) {
    if (serpienteX[i] == x && serpienteY[i] == y) {
      return true;
    }
  }
  return false;
}

bool hayManzana(int x, int y) {
  return (manzanaX == x && manzanaY == y);
}

void gameOver() {
  while (1);
}
```

### **Enlace al simulador**

[Código en Tinkercad]()

---

## **Preguntas teóricas**

1. ¿Cómo funciona la multiplexación en la función `mostrarMatriz()`? ¿Por qué se usa `delayMicroseconds(100)`?
2. Explica cómo se actualiza la posición del cuerpo de la serpiente en `moverSerpiente()`. ¿Por qué se recorre el arreglo de atrás hacia adelante?
3. ¿Qué función cumple `randomSeed(analogRead(0))`? ¿Qué pasaría si se omite?
4. ¿Cómo se evita que la serpiente pueda moverse en dirección opuesta a la actual (ej. de derecha a izquierda inmediatamente)?
5. ¿Qué ocurre en `gameOver()`? ¿Cómo se podría mejorar para mostrar un mensaje o reiniciar con un botón?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Modifica la función `gameOver()` para que, en lugar de un bucle infinito, reinicie el juego automáticamente después de 3 segundos.
*Pregunta:* ¿Cómo reinicias todas las variables a su estado inicial? ¿Usaste una función `reiniciarJuego()`?

### **Ejercicio 2**
Agrega un mecanismo para evitar que la serpiente pueda girar 180° sobre sí misma (ej. si va a la derecha, no pueda ir inmediatamente a la izquierda).
*Pregunta:* ¿Qué condición agregaste en `leerJoystick()`? ¿Usaste una variable `direccionAnterior`?

### **Ejercicio 3**
Haz que la velocidad inicial sea 300 ms en lugar de 500 ms, y que cada manzana reduzca 30 ms en lugar de 50 ms.
*Pregunta:* ¿Cómo cambia la dificultad del juego? ¿Se nota la progresión más gradual?

### **Ejercicio 4**
Agrega marcador de puntuación: muestra la longitud de la serpiente en el Monitor Serie cada vez que come una manzana.
*Pregunta:* ¿Dónde agregaste el `Serial.println()`? ¿La puntuación es correcta?

### **Ejercicio 5**
Reemplaza el control por joystick por control por botones: 4 botones en los pines 5, 6, 7, 8 para las 4 direcciones.
*Pregunta:* ¿Cómo adaptaste `leerJoystick()` para leer botones en lugar de valores analógicos? ¿Usaste `digitalRead()`?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
