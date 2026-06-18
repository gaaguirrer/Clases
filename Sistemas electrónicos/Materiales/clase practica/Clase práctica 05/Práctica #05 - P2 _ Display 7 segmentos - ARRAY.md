# **Display 7 segmentos - ARRAY**

<img src="tkc1.png" align="left" width="350" style="margin-right: 20px;">

## **Explicación del código**

Este programa es una evolución del P1: en lugar de usar `digitalWrite()` individuales dentro de un `switch`, utiliza arreglos (arrays) para almacenar los patrones de cada dígito y un bucle `for` para escribir los pines. Esto hace el código más compacto y fácil de modificar.

### **1. Declaración de constantes y arreglos**

```cpp
#define PTM A0
int i = 0, lectura = 0, opt = 0;

int cero[7] = {HIGH, HIGH, HIGH, LOW, HIGH, HIGH, HIGH};
int uno[7] = {HIGH, LOW, LOW, LOW, LOW, LOW, HIGH};
int dos[7] = {HIGH, HIGH, LOW, HIGH, HIGH, HIGH, LOW};
int tres[7] = {HIGH, HIGH, LOW, HIGH, LOW, HIGH, HIGH};
int cuatro[7] = {HIGH, LOW, HIGH, HIGH, LOW, LOW, HIGH};
int cinco[7] = {LOW, HIGH, HIGH, HIGH, LOW, HIGH, HIGH};
int seis[7] = {LOW, LOW, HIGH, HIGH, HIGH, HIGH, HIGH};
int siete[7] = {HIGH, HIGH, LOW, LOW, LOW, LOW, HIGH};
```

- `#define PTM A0`: Macro para el pin analógico del potenciómetro.
- `cero[7]` a `siete[7]`: Arreglos de 7 elementos que almacenan el estado (HIGH/LOW) de cada segmento (A, B, C, D, E, F, G). Cada arreglo representa el patrón de un dígito.
- Cada posición del arreglo corresponde a un pin de segmento, en el orden en que se usarán en el bucle.

### **2. Configuración `setup()`**

```cpp
void setup()
{
  for (i = 0; i < 7; i++){
    pinMode(i, OUTPUT);
  }
}
```

- Configura los pines 0 a 6 como salidas. A diferencia del P1, aquí se usa el pin 0 como parte de los segmentos.

### **3. Bucle `loop()`**

```cpp
void loop()
{
  lectura = analogRead(PTM);
  opt = map(lectura, 0, 1023, 0, 7);

  switch(opt){
    case 1:
      for (i = 0; i < 7; i++){
        digitalWrite(i, uno[i]);
      }
    break;
    case 2:
      for (i = 0; i < 7; i++){
        digitalWrite(i, dos[i]);
      }
    break;
    // ... otros casos ...
    default:
      for (i = 0; i < 7; i++){
        digitalWrite(i, cero[i]);
      }
    break;
  }
}
```

- `analogRead(PTM)` y `map()`: Lee el potenciómetro y convierte al rango 0-7.
- `switch(opt)`: Según el valor seleccionado, se ejecuta un bucle `for` que recorre el arreglo correspondiente y escribe cada pin con `digitalWrite(i, arreglo[i])`.
- La ventaja frente al P1 es que la escritura de los 7 pines se hace con 3 líneas en lugar de 7, y agregar un nuevo dígito solo requiere definir un nuevo arreglo y un `case`.

### **Código completo para copiar y pegar**

```cpp
// Display 7 segmentos - ARRAY

#define PTM A0

int i = 0, lectura = 0, opt = 0;

int cero[7] = {HIGH, HIGH, HIGH, LOW, HIGH, HIGH, HIGH};
int uno[7] = {HIGH, LOW, LOW, LOW, LOW, LOW, HIGH};
int dos[7] = {HIGH, HIGH, LOW, HIGH, HIGH, HIGH, LOW};
int tres[7] = {HIGH, HIGH, LOW, HIGH, LOW, HIGH, HIGH};
int cuatro[7] = {HIGH, LOW, HIGH, HIGH, LOW, LOW, HIGH};
int cinco[7] = {LOW, HIGH, HIGH, HIGH, LOW, HIGH, HIGH};
int seis[7] = {LOW, LOW, HIGH, HIGH, HIGH, HIGH, HIGH};
int siete[7] = {HIGH, HIGH, LOW, LOW, LOW, LOW, HIGH};

void setup()
{
  for (i = 0; i < 7; i++){
    pinMode(i, OUTPUT);
  }
}

void loop()
{
  lectura = analogRead(PTM);
  opt = map(lectura, 0, 1023, 0, 7);

  switch(opt){
    case 1:
      for (i = 0; i < 7; i++){ digitalWrite(i, uno[i]); }
    break;
    case 2:
      for (i = 0; i < 7; i++){ digitalWrite(i, dos[i]); }
    break;
    case 3:
      for (i = 0; i < 7; i++){ digitalWrite(i, tres[i]); }
    break;
    case 4:
      for (i = 0; i < 7; i++){ digitalWrite(i, cuatro[i]); }
    break;
    case 5:
      for (i = 0; i < 7; i++){ digitalWrite(i, cinco[i]); }
    break;
    case 6:
      for (i = 0; i < 7; i++){ digitalWrite(i, seis[i]); }
    break;
    case 7:
      for (i = 0; i < 7; i++){ digitalWrite(i, siete[i]); }
    break;
    default:
      for (i = 0; i < 7; i++){ digitalWrite(i, cero[i]); }
    break;
  }
}
```

### **Enlace al simulador**

[Código en Tinkercad](https://www.tinkercad.com/things/6yAmXqS3itj-practica-05-p2-display-7-segmentos-array)

---

## **Preguntas teóricas**

1. ¿Qué ventaja tiene usar arreglos (arrays) frente a variables individuales para almacenar los patrones de segmentos?
2. ¿Por qué en este código se usa el pin 0 mientras que en el P1 no? ¿Qué implicaciones tiene?
3. ¿Qué es más eficiente en memoria: 8 arreglos separados o una matriz bidimensional? Explica.
4. ¿Cómo se accede al elemento `i` de un arreglo en C++? ¿Por qué la indexación empieza en 0?
5. Si se quisiera agregar el dígito 8, ¿cuántas líneas de código habría que añadir?

---

## **Ejercicios prácticos (modificar el código y anotar cambios)**

**Instrucciones:** Copia el código original, realiza la modificación indicada, carga el programa en el simulador (o en Arduino real) y describe cómo cambia el comportamiento del circuito.

### **Ejercicio 1**
Agrega los arreglos para los dígitos 8 y 9. Ajusta el `map()` para que el rango sea 0-9.
*Pregunta:* ¿Cuántos nuevos arreglos definiste? ¿El código sigue siendo manejable?

### **Ejercicio 2**
Haz que el display muestre una secuencia automática: 0, 1, 2, ..., 9 y vuelva a 0, usando un `delay(500)`.
*Pregunta:* ¿Cómo eliminaste la dependencia del potenciómetro? ¿Qué estructura de control usaste?

### **Ejercicio 3**
Reemplaza los 8 arreglos individuales por una sola matriz bidimensional `int digitos[8][7]`.
*Pregunta:* ¿Cómo se accede a los elementos de una matriz? ¿El código se simplifica aún más?

### **Ejercicio 4**
Agrega un efecto de "barrido" donde todos los segmentos parpadeen 3 veces antes de mostrar el dígito seleccionado.
*Pregunta:* ¿Cómo implementaste el parpadeo? ¿Usaste un bucle `for` anidado?

### **Ejercicio 5**
Modifica el código para que los segmentos A y G parpadeen (alternen entre HIGH y LOW a 500 ms) mientras el dígito se muestra estáticamente.
*Pregunta:* ¿Cómo separas la actualización del dígito del parpadeo? ¿Usaste `millis()` o `delay()`?

---

*Entregar las respuestas a las preguntas teóricas y la descripción de los cambios observados en cada ejercicio.*
