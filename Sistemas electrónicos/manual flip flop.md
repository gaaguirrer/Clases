# Manual de Flip Flops y Elementos Secuenciales

## Introducción

En este manual estudiaremos los **elementos secuenciales** fundamentales en el diseño de circuitos digitales. Estos componentes son la base de la memoria y el almacenamiento de datos en los sistemas electrónicos digitales.

---

## Tabla de Contenidos

1. [D Flip Flop](#d-flip-flop)
2. [D Latch](#d-latch)
3. [T Flip Flop](#t-flip-flop)
4. [SR Flip Flop](#sr-flip-flop)
5. [JK Flip Flop](#jk-flip-flop)
6. [TTY](#tty)
7. [Keyboard](#keyboard)
8. [Clock](#clock)
9. [ROM](#rom)
10. [RAM](#ram)
11. [EEPROM](#eeprom)

---

## D Flip Flop

El **D Flip Flop** (Flip Flop de Retardo) es un elemento que retrasa la entrada hasta el siguiente ciclo de reloj.

### Descripción de Pines

- **Entrada de datos (D)**: Recibe un único dato de entrada
- **Entrada de reloj (Clock)**: Sincroniza la operación del flip flop
- **Preset y Reset Asíncrono**: Modifican el comportamiento por defecto del flip flop
  - Si Reset = 1, entonces la salida del D Flip Flop = Preset
  - La salida es independiente de la entrada o del reloj
- **Enable (Habilitación)**: Activa o desactiva el funcionamiento del Flip Flop

### Tabla de Verdad

| Clock | D | Q | Q Inverso |
|-------|---|-----|-----------|
| 0 | X | Latch | Latch |
| 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |

Como se observa en la tabla, cuando el reloj está en 1, la salida Q sigue exactamente el valor de la entrada D.

### Propiedades Personalizables

- **BitWidth**: Ancho de bits del dato

---

## D Latch

El **D Latch** es un flip flop de entrada única similar al D Flip Flop, pero sin los pines de preset, reset asíncrono y habilitación.

### Descripción de Pines

- **Entrada de datos (D)**: Recibe el dato de entrada
- **Entrada de reloj (Clock)**: Controla cuándo se captura el dato

### Tabla de Verdad

| Clock | D | Q | Q Inverso |
|-------|---|-----|-----------|
| 0 | X | Latch | Latch |
| 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |

### Propiedades Personalizables

- **BitWidth**: Ancho de bits del dato

### Diferencia con D Flip Flop

La principal diferencia es que el D Latch no incluye las señales de preset, reset asíncrono y enable, lo que lo hace más simple pero con menos funcionalidad.

---

## T Flip Flop

El **T Flip Flop** (Flip Flop de Alternancia) es un elemento que alterna su salida cuando la entrada está activa.

### Descripción de Pines

- **Entrada de datos (T)**: Controla si la salida se alterna o se mantiene
- **Entrada de reloj (Clock)**: Sincroniza la operación

### Tabla de Verdad

| Entrada (T) | Estado Anterior | Siguiente Estado |
|-------------|-----------------|------------------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Cuando T = 1, la salida del siguiente estado es el complemento del estado anterior. Cuando T = 0, la salida se mantiene sin cambios.

### Aplicación

Este tipo de flip flop es útil para construir contadores y divisores de frecuencia.

---

## SR Flip Flop

El **SR Flip Flop** es uno de los circuitos secuenciales más simples. Posee dos entradas de control: S (Set) y R (Reset).

### Descripción de Pines

- **S (Set)**: Establece la salida en 1
- **R (Reset)**: Restablece la salida en 0
- **Clock**: Sincroniza la operación

### Tabla de Verdad

| S | R | Q |
|---|---|-------|
| 0 | 0 | Sin cambio |
| 1 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 1 | Inválido |

### Comportamiento

- Cuando **S = 1** y R = 0: La salida Q se establece en **1**
- Cuando **R = 1** y S = 0: La salida Q se establece en **0**
- Cuando **S = 0** y R = 0**: La salida **no cambia**
- Cuando **S = 1** y R = 1**: Estado **inválido** (no permitido)

### Nota Importante

La combinación S = 1 y R = 1 produce un estado inválido y debe evitarse en el diseño de circuitos.

---

## JK Flip Flop

El **JK Flip Flop** es una mejora del SR Flip Flop que resuelve el problema del estado inválido. Incluye dos entradas J y K.

### Descripción de Pines

- **J**: Entrada de control principal
- **K**: Entrada de control secundaria
- **Clock**: Sincroniza la operación en el flanco de reloj

### Tabla de Verdad

| J | K | Q |
|---|---|-------|
| 0 | 0 | Sin cambio |
| 1 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 1 | Alternar (Toggle) |

### Comportamiento

- Cuando **J = 0** y K = 0**: La salida **no cambia**
- Cuando **J = 1** y K = 0**: La salida se establece en **1**
- Cuando **J = 0** y K = 1**: La salida se establece en **0**
- Cuando **J = 1** y K = 1**: La salida **alterna** su valor

### Ventajas sobre SR Flip Flop

A diferencia del SR Flip Flop, cuando ambas entradas están activas (J = 1, K = 1), el JK Flip Flop no entra en estado inválido, sino que alterna la salida. Esto lo hace más versátil y seguro para implementaciones prácticas.

### Propiedades Personalizables

- **BitWidth**: Ancho de bits del dato

---

## TTY

El elemento **TTY** (Teletipo) recibe una secuencia de códigos ASCII y muestra cada carácter imprimible como salida.

### Descripción de Pines

| Nombre | Descripción |
|--------|-------------|
| **ASCII Input** (Ancho de 7 bits) | Recibe el valor ASCII del siguiente carácter a ingresar en la terminal |
| **Clock** (Ancho de 1 bit) | Cuando se activa el reloj y el pin Enable no es 0, el carácter ASCII de entrada es procesado |
| **Enable** (Ancho de 1 bit) | Cuando es 1, un flanco de reloj procesa un nuevo carácter. Cuando es 0, se ignoran las entradas de reloj y datos |
| **Reset** | Cuando es 1, se borran todos los datos de la terminal y se ignoran las demás entradas |

### Propiedades Personalizables

- **BitWidth**: Debe configurarse como **7**
- **Rows**: Número de filas
- **Columns**: Número de columnas

### Aplicación

El TTY se utiliza para visualizar datos en formato de texto dentro de circuitos simulados, funcionando como una terminal de salida.

---

## Keyboard

El elemento **Keyboard** (Teclado) permite al circuito leer pulsaciones de teclas, siempre que sean representables en código ASCII de siete bits.

### Descripción de Pines

| Nombre | Descripción |
|--------|-------------|
| **Clock** (Ancho de 1 bit) | Cuando se activa el reloj y Enable no es 0, se elimina el carácter más a la izquierda del buffer y se actualizan las salidas |
| **Enable** (Ancho de 1 bit) | Cuando es 1, un flanco de reloj procesa un nuevo carácter. Cuando es 0, se ignoran las entradas |
| **Reset** | Cuando es 1, se borran todos los datos y no se aceptan más caracteres |
| **Available (AVL)** | Se establece en 1 cuando el buffer contiene al menos un carácter. Se establece en 0 cuando está vacío |
| **ASCII Output** (Ancho de 7 bits) | Genera el código ASCII de 7 bits del carácter más a la izquierda del buffer, o 0 si está vacío |

### Propiedades Personalizables

- **Buffer Size**: Tamaño del buffer de entrada

### Aplicación

Este elemento permite la interacción del usuario con el circuito simulado, ingresando datos mediante el teclado.

---

## Clock

El elemento **Clock** (Reloj) alterna su salida a intervalos regulares de tiempo, proporcionando la señal de sincronización para todos los elementos secuenciales del circuito.

### Características Importantes

> **Nota**: Todos los relojes habilitados dentro de un circuito cambian al mismo ritmo.

### Aplicación

El Clock es fundamental en cualquier circuito secuencial, ya que determina cuándo se capturan los datos y cuándo cambian los estados de los flip flops.

---

## ROM

La **ROM** (Memoria de Solo Lectura) almacena datos de solo lectura para computadoras y dispositivos electrónicos. Se utiliza principalmente para actualizaciones de firmware.

### Descripción de Pines

- **Address (A)**: Entrada de dirección de 4 bits (la dirección inicial siempre es 0)
- **Data (D)**: Salida de 8 bits con el valor almacenado en la dirección especificada
- **Enable (En)**: Habilita la ROM

### Ejemplos de Uso

- Cartuchos de consolas de videojuegos: permiten que un sistema ejecute múltiples juegos
- **EEPROM**: Un tipo de ROM programable utilizada para la BIOS del computador

### Propiedades

- La ROM es **no volátil**: los datos persisten sin alimentación eléctrica
- Los datos se programan de fábrica y no se pueden modificar durante la operación normal

---

## RAM

La **RAM** (Memoria de Acceso Aleatorio) permite que los datos se lean y escriban durante la operación del circuito.

### Descripción de Pines

- **Address**: Dirección de memoria para lectura/escritura
- **Data In/Out**: Datos de entrada y salida
- **Read/Write**: Control de operación
- **Reset**: Restablece todos los datos a cero
- **Core Dump**: Vuelca el contenido de la RAM a la consola

### Comportamiento

- Cualquier cambio en las propiedades **Address Width** o **BitWidth** causará **pérdida de datos**
- Esto es equivalente a retirar una RAM del circuito y reemplazarla con otra de tamaño diferente

### Operaciones Especiales

- **Reset**: Establecer el pin Reset en 1 borra todos los datos
- **Core Dump**: Transicionar el pin Core Dump a 1 vuelca el contenido a la consola. Las direcciones no escritas aparecerán como undefined

### Propiedades Personalizables

- **Address Width**: Ancho de la dirección
- **BitWidth**: Ancho de bits del dato

---

## EEPROM

La **EEPROM** (Electrically Erasable Programmable Read-Only Memory) es una ROM programable utilizada para el BIOS del computador. Las EEPROM son generalmente más costosas que las RAM.

### Características

- **Espacio de direcciones máximo**: 10 bits (1024 direcciones), menor que la RAM
- Si se borra la EEPROM, **todos los valores se restablecen a cero** y los datos originales no se pueden recuperar
- Los datos **sobreviven operaciones de copiar y pegar**
- Se puede duplicar una EEPROM o crear una biblioteca de EEPROMs reutilizables

### Propiedades Personalizables

- **Address Width**: Ancho de la dirección
- **BitWidth**: Ancho de bits del dato

### Procedimiento para Poblar una EEPROM

1. Establecer **Write = 1** y hacer clic en **Reset** para bregar todo
2. Seleccionar el elemento **Keyboard** y escribir caracteres hasta que el contador de direcciones vuelva a cero
3. Establecer **Write = 0** y el texto en la EEPROM se mostrará en el elemento **TTY**
4. **Guardar el circuito**: el contenido de la EEPROM persistirá para uso futuro

---

## Resumen Comparativo

### Flip Flops

| Tipo | Entradas | Función Principal | Estado Inválido |
|------|----------|-------------------|-----------------|
| **D Flip Flop** | D, Clock | Retrasar entrada | No |
| **D Latch** | D, Clock | Almacenar dato | No |
| **T Flip Flop** | T, Clock | Alternar salida | No |
| **SR Flip Flop** | S, R, Clock | Set/Reset | Sí (S=1, R=1) |
| **JK Flip Flop** | J, K, Clock | Set/Reset/Toggle | No |

### Memorias

| Tipo | Lectura | Escritura | Volátil | Uso Principal |
|------|---------|-----------|---------|---------------|
| **ROM** | Sí | No | No | Firmware |
| **RAM** | Sí | Sí | Sí | Memoria de trabajo |
| **EEPROM** | Sí | Sí (programable) | No | BIOS, configuración |

### Elementos de Entrada/Salida

| Elemento | Función |
|----------|---------|
| **Clock** | Genera señal de sincronización |
| **Keyboard** | Lee pulsaciones de teclas (ASCII 7 bits) |
| **TTY** | Muestra caracteres ASCII como terminal |

---

## Conclusiones

Los elementos secuenciales son componentes esenciales en el diseño de sistemas digitales. Los **flip flops** constituyen la base del almacenamiento de datos, mientras que las **memorias** (ROM, RAM, EEPROM) proporcionan diferentes capacidades de almacenamiento según las necesidades del sistema. Comprender su funcionamiento y sus tablas de verdad es fundamental para diseñar circuitos digitales correctos y eficientes.
