# **Uso del Joystick**

<img src="tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Explicación del código**

Este programa lee la posición de un joystick analógico en sus ejes X e Y, así como el estado de su botón pulsador. Los valores se muestran en el Monitor Serie para verificar el funcionamiento del joystick.

### **1. Declaración de pines y variables**

```cpp
const int JOY_X = A0;
const int JOY_Y = A1;
const int JOY_SW = 2;

int valorX = 0;
int valorY = 0;
bool boton = false;
```

- `JOY_X = A0;`: Pin analógico para el eje X (VRX del joystick).
- `JOY_Y = A1;`: Pin analógico para el eje Y (VRY del joystick).
- `JOY_SW = 2;`: Pin digital para el botón pulsador (SW del joystick). Normalmente está en HIGH y se pone LOW al presionar.
- `valorX`, `valorY`: Almacenan las lecturas analógicas (0-1023).
- `boton`: Almacena el estado del botón (true = presionado).

### **2. Configuración `setup()`**

```cpp
void setup()
{
  Serial.begin(9600);
  pinMode(JOY_SW, INPUT_PULLUP);
}
```

- `Serial.begin(9600);`: Inicia la comunicación serie para mostrar valores.
- `pinMode(JOY_SW, INPUT_PULLUP);`: Configura el pin del botón como entrada con resistencia pull-up interna, evitando usar una resistencia externa.

### **3. Bucle `loop()`**

```cpp
void loop()
{
  valorX = analogRead(JOY_X);
  valorY = analogRead(JOY_Y);
  boton = !digitalRead(JOY_SW);

  Serial.print("X: ");
  Serial.print(valorX);
  Serial.print("\t Y: ");
  Serial.print(valorY);
  Serial.print("\t BOTON: ");
  Serial.println(boton ? "PRESIONADO" : "LIBRE");

  delay(100);
}
```

- `analogRead(JOY_X/Y)`: Lee el valor analógico de cada eje (0-1023). En reposo (centro), el valor es aproximadamente 512.
- `!digitalRead(JOY_SW)`: Lee el botón y lo invierte. Con pull-up, al presionar se lee LOW, por lo que `!` lo convierte a `true`.
- `Serial.print()`: Muestra los valores en el Monitor Serie.
- `boton ? "PRESIONADO" : "LIBRE"`: Operador ternario que selecciona el texto según el estado del botón.
- `delay(100)`: Pausa para evitar saturar el Monitor Serie.

### **Código completo para copiar y pegar**

```cpp
// Uso del Joystick

const int JOY_X = A0;
const int JOY_Y = A1;
const int JOY_SW = 2;

int valorX = 0;
int valorY = 0;
bool boton = false;

void setup()
{
  Serial.begin(9600);
  pinMode(JOY_SW, INPUT_PULLUP);
}

void loop()
{
  valorX = analogRead(JOY_X);
  valorY = analogRead(JOY_Y);
  boton = !digitalRead(JOY_SW);

  Serial.print("X: ");
  Serial.print(valorX);
  Serial.print("\t Y: ");
  Serial.print(valorY);
  Serial.print("\t BOTON: ");
  Serial.println(boton ? "PRESIONADO" : "LIBRE");

  delay(100);
}
```

---

## **Preguntas teóricas**

1. ¿Qué valores esperas leer en los ejes X e Y cuando el joystick está en reposo (centro)? ¿Por qué?
2. ¿Qué es una resistencia pull-up y por qué se usa `INPUT_PULLUP` en lugar de una resistencia externa?
3. ¿Qué rango de valores devuelve `analogRead()`? ¿Cuántos volts representa cada unidad?
4. ¿Qué función cumple el operador ternario `? :`? ¿Cómo se escribe la misma lógica con `if-else`?
5. ¿Qué pasaría si se elimina el `delay(100)` del `loop()`? ¿El Monitor Serie se saturaría?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Modifica el código para que encienda un LED en el pin 13 cuando el joystick se mueva hacia la derecha (X > 700).
*Pregunta:* ¿Qué condición usaste? ¿El LED se enciende consistentemente al mover el joystick a la derecha?

### **Ejercicio 2**
Agrega detección de las 4 direcciones (arriba, abajo, izquierda, derecha) usando los umbrales X < 300, X > 700, Y < 300, Y > 700. Muestra la dirección en el Monitor Serie.
*Pregunta:* ¿Hubo direcciones que se activaron sin querer al soltar el joystick? ¿Cómo agregarías histéresis?

### **Ejercicio 3**
Controla la intensidad de un LED PWM en el pin 9 usando el eje X del joystick. Mapea el valor X (0-1023) al rango PWM (0-255) con `map()`.
*Pregunta:* ¿El brillo del LED sigue suavemente el movimiento del joystick?

### **Ejercicio 4**
Haz que el botón del joystick funcione como un interruptor (toggle): cada vez que se presiona, un LED en el pin 13 cambia de estado (encendido/apagado) y se mantiene.
*Pregunta:* ¿Cómo implementaste el cambio de estado? ¿Usaste una variable `bool` para recordar el estado anterior?

### **Ejercicio 5**
Usa el joystick para controlar la posición de un servo. El eje X controla el ángulo (0-180° mediante `map()`) y el botón reinicia el servo a 90°.
*Pregunta:* ¿Cómo integrar el joystick y el servo en un solo programa? ¿Usaste la biblioteca `<Servo.h>`?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
