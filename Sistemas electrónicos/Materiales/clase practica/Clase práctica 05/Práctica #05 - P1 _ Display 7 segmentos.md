# **Display 7 segmentos**

<img src="tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Explicación del código**

Este programa controla un display de 7 segmentos (ánodo común) usando un potenciómetro para seleccionar el dígito a mostrar (del 0 al 7). Los segmentos se controlan mediante `digitalWrite()` sobre cada pin.

### **1. Declaración de variables y constantes**

```cpp
#define PTM A0
const int B = 1, A = 2, F = 3, G = 4, E = 5, D = 6, C = 7;
int i = 0, lectura = 0, opt = 0;
```

- `#define PTM A0`: Define la macro `PTM` para referirse al pin analógico A0. Es una alternativa a `const int` que no ocupa memoria RAM.
- `const int B = 1, A = 2, ..., C = 7;`: Constantes que asignan los pines digitales 1 al 7 a los segmentos del display.
  - La asignación no sigue el orden alfabético de los segmentos; depende del conexionado físico.
- `int i = 0;`: Variable de control para bucles.
- `int lectura = 0;`: Almacena el valor leído del potenciómetro.
- `int opt = 0;`: Almacena el número de dígito a mostrar después del mapeo.

### **2. Configuración `setup()`**

```cpp
void setup()
{
  for (i = 1; i < 8; i++){
    pinMode(i, OUTPUT);
  }
}
```

- Un bucle `for` configura los pines 1 al 7 como salidas. Esto evita escribir 7 líneas de `pinMode`.
- **Nota:** El pin 0 no se usa porque corresponde a la comunicación serie (RX).

### **3. Bucle `loop()`**

```cpp
void loop()
{
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);

  lectura = analogRead(PTM);
  opt = map(lectura, 0, 1023, 0, 7);

  switch(opt){
    case 1: 
      digitalWrite(A, LOW);  digitalWrite(B, HIGH);
      digitalWrite(C, HIGH); digitalWrite(D, LOW);
      digitalWrite(E, LOW);  digitalWrite(F, LOW);
      digitalWrite(G, LOW);
    break;
    // ... otros casos ...
    default: 
      digitalWrite(A, HIGH); digitalWrite(B, HIGH);
      digitalWrite(C, HIGH); digitalWrite(D, HIGH);
      digitalWrite(E, HIGH); digitalWrite(F, HIGH);
      digitalWrite(G, LOW);  // Cero
    break;
  }
}
```

- Primero se apagan todos los segmentos escribiendo `LOW` en cada pin. Esto evita arrastrar estado del ciclo anterior.
- `analogRead(PTM)`: Lee el potenciómetro (0-1023).
- `map(lectura, 0, 1023, 0, 7)`: Convierte el valor al rango 0-7 para seleccionar un dígito.
- `switch(opt)`: Según el valor, se encienden los segmentos correspondientes:
  - **case 1:** B y C encendidos → muestra "1".
  - **case 2:** A, B, D, E, G encendidos → muestra "2".
  - ... hasta **case 7:** A, B, C encendidos → muestra "7".
  - **default:** A, B, C, D, E, F encendidos → muestra "0".

### **Código completo para copiar y pegar**

```cpp
// Display 7 segmentos

#define PTM A0
const int B = 1, A = 2, F = 3, G = 4, E = 5, D = 6, C = 7;
int i = 0, lectura = 0, opt = 0;

void setup()
{
  for (i = 1; i < 8; i++){
    pinMode(i, OUTPUT);
  }
}

void loop()
{
  digitalWrite(A, LOW);  digitalWrite(B, LOW);
  digitalWrite(C, LOW);  digitalWrite(D, LOW);
  digitalWrite(E, LOW);  digitalWrite(F, LOW);
  digitalWrite(G, LOW);

  lectura = analogRead(PTM);
  opt = map(lectura, 0, 1023, 0, 7);

  switch(opt){
    case 1:
      digitalWrite(A, LOW);  digitalWrite(B, HIGH);
      digitalWrite(C, HIGH); digitalWrite(D, LOW);
      digitalWrite(E, LOW);  digitalWrite(F, LOW);
      digitalWrite(G, LOW);
    break;
    case 2:
      digitalWrite(A, HIGH); digitalWrite(B, HIGH);
      digitalWrite(C, LOW);  digitalWrite(D, HIGH);
      digitalWrite(E, HIGH); digitalWrite(F, LOW);
      digitalWrite(G, HIGH);
    break;
    case 3:
      digitalWrite(A, HIGH); digitalWrite(B, HIGH);
      digitalWrite(C, HIGH); digitalWrite(D, HIGH);
      digitalWrite(E, LOW);  digitalWrite(F, LOW);
      digitalWrite(G, HIGH);
    break;
    case 4:
      digitalWrite(A, LOW);  digitalWrite(B, HIGH);
      digitalWrite(C, HIGH); digitalWrite(D, LOW);
      digitalWrite(E, LOW);  digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
    break;
    case 5:
      digitalWrite(A, HIGH); digitalWrite(B, LOW);
      digitalWrite(C, HIGH); digitalWrite(D, HIGH);
      digitalWrite(E, LOW);  digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
    break;
    case 6:
      digitalWrite(A, LOW);  digitalWrite(B, LOW);
      digitalWrite(C, HIGH); digitalWrite(D, HIGH);
      digitalWrite(E, HIGH); digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
    break;
    case 7:
      digitalWrite(A, HIGH); digitalWrite(B, HIGH);
      digitalWrite(C, HIGH); digitalWrite(D, LOW);
      digitalWrite(E, LOW);  digitalWrite(F, LOW);
      digitalWrite(G, LOW);
    break;
    default:
      digitalWrite(A, HIGH); digitalWrite(B, HIGH);
      digitalWrite(C, HIGH); digitalWrite(D, HIGH);
      digitalWrite(E, HIGH); digitalWrite(F, HIGH);
      digitalWrite(G, LOW);
    break;
  }
}
```

### **Enlace al simulador**

[Código en Tinkercad](https://www.tinkercad.com/things/jwXDFgxly2N-practica-05-p1-display-7-segmentos)

---

## **Preguntas teóricas**

1. ¿Qué diferencia hay entre `#define` y `const int` para declarar constantes? ¿Cuál ocupa menos memoria RAM?
2. ¿Por qué se apagan todos los segmentos al inicio del `loop()`? ¿Qué pasaría si no se hace?
3. ¿Cuántos dígitos diferentes puede mostrar este display? ¿Por qué el `map()` usa rango 0-7?
4. En un display de ánodo común, ¿qué nivel lógico enciende un segmento: HIGH o LOW?
5. ¿Por qué el pin 0 no se usa para los segmentos? ¿Qué función tiene en Arduino?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Agrega los casos para mostrar los dígitos 8 y 9. Investiga qué segmentos deben encenderse para cada uno.
*Pregunta:* ¿Qué segmentos se encienden para el 8? ¿Y para el 9? ¿Ambos cupieron en el `map()` original?

### **Ejercicio 2**
Cambia el tiempo entre lecturas agregando un `delay(500)` al final del `loop()`. ¿El display responde más lento al girar el potenciómetro?
*Pregunta:* ¿Es útil este retardo o perjudica la experiencia de control?

### **Ejercicio 3**
Haz que el display cuente automáticamente de 0 a 9 y vuelva a empezar, sin usar el potenciómetro. Usa un `delay(1000)` entre cada número.
*Pregunta:* ¿Cómo modificaste el código? ¿Qué estructura de control usaste?

### **Ejercicio 4**
Reemplaza todos los `digitalWrite()` del `switch` por asignaciones a un arreglo de 7 elementos. Define `int digitos[10][7]` con los patrones y usa un bucle `for` para escribir los pines.
*Pregunta:* ¿El código se vuelve más compacto? ¿Cuántas líneas ahorraste?

### **Ejercicio 5**
Agrega un botón en el pin 8 con resistencia pull-up que, al presionarlo, congele el dígito actual en el display (detenga la actualización desde el potenciómetro).
*Pregunta:* ¿Cómo implementaste la funcionalidad de congelar/mantener? ¿Usaste una bandera (`bool`) para recordar el estado?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
