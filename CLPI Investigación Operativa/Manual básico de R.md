# Manual básico de R

## 1.1 ¿Qué es R?

R es un **lenguaje de programación** y, simultáneamente, un **entorno de desarrollo** especializado en análisis estadístico, minería de datos y visualización gráfica. Es software **gratuito y de código abierto**, lo que permite su descarga, estudio, modificación y redistribución sin restricciones de licencia.

Fue creado en los años 90 por **Ross Ihaka** y **Robert Gentleman** (Universidad de Auckland, Nueva Zelanda). Actualmente el desarrollo oficial es coordinado por el **R Core Team**, mientras que una amplia comunidad contribuye con paquetes y documentación.

**R se destaca por:**

- Facilitar **análisis estadísticos complejos** con pocas líneas de código.
- Disponer de **miles de paquetes** (CRAN, Bioconductor, GitHub) que amplían su funcionalidad.
- Poseer una potente **capacidad gráfica** (gráficos de alta calidad reproducibles).
- Ser **multiplataforma**: Windows, macOS y Linux.

### Ámbitos de uso más comunes

- **Ciencia de datos**: limpieza de datos, modelado, evaluación.
- **Estadística aplicada**: pruebas, estimaciones, inferencia.
- **Aprendizaje automático (Machine Learning)**: regresión, clasificación, clustering, validación.
- **Bioinformática**: análisis de secuencias, expresión génica.
- **Economía y finanzas**: series temporales, simulaciones de riesgo.
- **Ciencias sociales**: encuestas, minería de texto, análisis de redes.

> 💡 _Ejemplo:_  
> El Banco Central de Nicaragua y universidades pueden usar R para analizar series temporales de inflación, exportaciones agrícolas (café, azúcar) y comportamiento del empleo, integrando modelos ARIMA o modelos estructurales para proyecciones macroeconómicas.

---

## 1.2 Instalación de R y RStudio

### Paso 1 — Instalar R

1. Accede a CRAN: <https://cran.r-project.org>
2. Selecciona tu sistema operativo (Windows, macOS, Linux).
3. Descarga el instalador y sigue las instrucciones del instalador (siguiente → siguiente → finalizar).

**Notas técnicas:**

- En Windows, R suele instalarse en `C:/Program Files/R/` con subcarpetas por versión (ej. `R-4.2.3`).
- En Linux, se recomienda usar el repositorio de CRAN para tu distribución o instalar el binario indicado por CRAN.

### Paso 2 — Instalar RStudio (recomendado)

- Descarga RStudio Desktop: <https://posit.co/download/rstudio-desktop>
- RStudio es un **IDE** (entorno integrado) que mejora la productividad: editor de scripts, consola, panel de entorno, visor de gráficos, historial y proyecto integrado.

**Ventajas de RStudio:**

- Resaltado de sintaxis y autocompletado.
- Integración con Git/GitHub.
- Paneles para ver variables, archivos y gráficos.
- Facilita la enseñanza y la reproducción de análisis.

---

## 1.3 Primeros pasos en la consola de R

Al abrir R o RStudio verás la **consola**: un intérprete interactivo donde puedes escribir y ejecutar comandos.

**Ejemplos básicos y explicaciones:**

```r
# Operaciones matemáticas
2 + 2       # Suma -> 4
5 * 3       # Multiplicación -> 15
10 / 4      # División -> 2.5
2^3         # Potencia -> 8

# Asignación de valores a variables
x <- 5
y <- 10

# Calcular usando variables
x + y       # Resultado -> 15

# Funciones integradas
sqrt(16)    # Raíz cuadrada -> 4
log(10)     # Logaritmo natural -> 2.302585
mean(c(2, 4, 6, 8)) # Promedio -> 5
```

**Conceptos y convenciones:**

- La asignación recomendada es `x <- valor`. Aunque `=` funciona, `<-` es la convención en la comunidad estadística.
- Los comentarios usan `#` y no se ejecutan.
- Los **vectores** son estructuras fundamentales y se crean con `c()`.
- R está orientado a operaciones vectorizadas (funciona con vectores y matrices sin necesidad de bucles explícitos en muchos casos).

> 💡 _Ejemplo:_  
> Un docente calcula promedios de calificaciones de estudiantes:

```r
notas <- c(85, 90, 78, 95, 88)
mean(notas)  # -> 87.2
```

---

## 1.4 Guardar y ejecutar scripts

Trabajar con scripts permite **organizar**, **documentar** y **reproducir** análisis.

**En RStudio:**

1. `File > New File > R Script`.
2. Escribe tu código y guarda con extensión `.R`, por ejemplo `mi_primer_script.R`.
3. Ejecuta líneas seleccionadas con **Ctrl + Enter** (Windows/Linux) o **Cmd + Enter** (Mac).
4. Para ejecutar todo el script: botón **Source** o `source("mi_primer_script.R")`.

**Buenas prácticas:**

- Añade encabezados y comentarios explicativos (propósito del script, autor, fecha).
- Usa nombres de variables descriptivos (`promedio_estudiantes` en lugar de `p`).
- Divide el trabajo en funciones reutilizables cuando tenga sentido.
- Versiona el código con Git para control de cambios y colaboración.

---

## 1.5 Ejercicio rápido

### 1) Área de un círculo de radio 4

Fórmula:
\[
Área = \pi \times r^2
\]

```r
radio <- 4
area <- pi * radio^2
area
```

### 2) Media de los números 5, 8, 12, 20

```r
mean(c(5, 8, 12, 20))  # -> 11.25
```

### 3) Asignar e imprimir tu nombre

```r
mi_nombre <- "pepe"
print(mi_nombre)
```

**Tip práctico:** la tecla **↑** en la consola recupera comandos anteriores — muy útil para repetir o modificar instrucciones sin reescribirlas.

---

## Recomendaciones

### Paquetes esenciales para comenzar

- `ggplot2` — Visualización (Gramática de gráficos).
- `dplyr` — Manipulación de datos (verbos: `filter`, `select`, `mutate`, `summarise`, `arrange`).
- `tidyr` — Reestructuración de datos (pivotar, separar, unir columnas).
- `readr` — Lectura rápida de CSV/TSV.
- `lubridate` — Manejo de fechas y horas.
- `stringr` — Manipulación de cadenas.
- `caret` / `tidymodels` — Modelado y flujo de trabajo de machine learning.
- `shiny` — Construcción de aplicaciones web interactivas con R.

### Flujo de trabajo típico (ejemplo aplicado a producción de café por departamento — datos hipotéticos)

1. **Lectura de datos**:

```r
library(readr)
datos <- read_csv("produccion_cafe.csv")
```

2. **Limpieza y transformación**:

```r
library(dplyr)
resumen <- datos %>%
  group_by(departamento, anio) %>%
  summarise(total_toneladas = sum(toneladas, na.rm = TRUE))
```

3. **Visualización**:

```r
library(ggplot2)
ggplot(resumen, aes(x = anio, y = total_toneladas, color = departamento)) +
  geom_line() +
  labs(title = "Producción anual de café por departamento",
       x = "Año", y = "Toneladas")
```

> Este flujo es aplicable para series temporales económicas (IPC, inflación), encuestas sociales o análisis académico.

---

# Tema 2 — Fundamentos del lenguaje en R

> En este capítulo profundizaremos en las **variables**, **tipos de datos**, **operadores**, **funciones básicas** y conceptos afines. La explicación es detallada y con ejemplos reproducibles en R; además incluimos notas pedagógicas y recomendaciones prácticas para su uso en clase o investigación aplicada (con ejemplos relacionados con Nicaragua cuando procede). Mantén RStudio abierto y prueba cada fragmento: la práctica afianza la teoría.

---

## 2.1 Variables

### ¿Qué es una variable en R?

Una **variable** en R es un nombre simbólico que referencia un objeto en memoria (un número, texto, vector, data.frame, función, etc.). No es un "contenedor" físico en sentido estricto sino una etiqueta o puntero al objeto.

### Asignación

La forma recomendada por la comunidad es usar `<-`:

```r
x <- 10
y <- 3.5
```

También funciona `=` (útil en argumentos de funciones), pero `<-` es la convención:

```r
z = 20
```

### Ver y administrar variables

Para ver y manipular objetos del entorno:

```r
x         # imprime el valor de x
print(y)  # imprime y con formato

ls()                 # lista objetos en el entorno
rm(nombre_objeto)    # elimina un objeto concreto
rm(list = ls())      # vacía todo el entorno (¡cuidado!)
```

### Reasignación y mutabilidad

Puedes sobrescribir (reassign) una variable libremente:

```r
x <- 15   # antes era 10, ahora 15
```

### Buenas prácticas de nombres

- Usa nombres descriptivos y en minúsculas: `promedio_estudiantes`, `anio_ingreso`.  
- Evita empezar con números; no uses espacios (usa `_` o `.`).  
- Mantén estilo consistente (snake_case o camelCase).  
- Evita usar nombres que confundan con funciones internas o símbolos comunes (`c`, `T`, `F`).

### Scope (alcance) básico

Las variables definidas en el entorno global son accesibles desde la consola; dentro de una función, las variables locales no persisten fuera a menos que las devuelvas.

```r
f <- function() {
  local_var <- 1
  return(local_var)
}
f()        # devuelve 1
local_var  # error: objeto no encontrado
```

---

## 2.2 Tipos de datos básicos en R (detallado)

R distingue varios **tipos atómicos básicos** y **estructuras compuestas**. Conocerlos evita errores sutiles al procesar datos reales.

### Tipos atómicos

**numeric / double** — números reales (por defecto con decimales):

```r
a <- 3.14
class(a)   # "numeric"
typeof(a)  # "double"
```

**integer** — enteros, se especifican con `L`:

```r
b <- 5L
class(b)   # "integer"
```

**character** — cadenas de texto:

```r
nombre <- "Ana"
class(nombre)  # "character"
```

**logical** — `TRUE` / `FALSE`:

```r
c <- TRUE
d <- FALSE
class(c)  # "logical"
```

**complex** — números complejos (raro en estadística básica pero existe):

```r
z <- 1 + 2i
class(z)  # "complex"
```

### Valores especiales

- `NA` — valor faltante (missing value).  
- `NULL` — ausencia de objeto.  
- `Inf`, `-Inf` — infinito (ej.: `1/0`).  
- `NaN` — “not a number” (ej.: `0/0`).

```r
x <- NA
y <- NULL
z <- 1/0   # Inf
w <- 0/0   # NaN

is.na(x)    # TRUE
is.null(y)  # TRUE
is.nan(w)   # TRUE
```

### Estructuras compuestas y tipos derivados

**Vectores** (homogéneos: todos los elementos del mismo tipo):

```r
v_num <- c(1, 2, 3.5)        # numeric
v_char <- c("a", "b", "c")  # character
v_log <- c(TRUE, FALSE, TRUE)
```

**Matrices** (2D, homogéneas):

```r
m <- matrix(1:6, nrow = 2, ncol = 3)
```

**Arrays** (multidimensional, homogéneos).

**Listas** (heterogéneas: pueden contener distintos tipos y estructuras):

```r
lst <- list(nombre = "Ana", edad = 30, notas = c(85, 90))
```

**data.frame** (tablas; columnas pueden ser de distintos tipos):

```r
df <- data.frame(departamento = c("Matagalpa", "Jinotega"),
                 toneladas = c(15000, 14000),
                 anio = c(2020, 2020))
```

**tibble** — versión moderna de `data.frame` (mejor impresión, parte de tidyverse).

**factor** — variable categórica; internamente es un entero con etiquetas:

```r
sexo <- factor(c("M", "F", "F", "M"))
levels(sexo)
```

> **Nota importante:** factores son útiles para estadísticas y gráficas, pero al convertir entre tipos conviene usar `as.character()` y `as.numeric()` con cuidado. Por ejemplo: `as.numeric(fct)` devuelve códigos internos, no etiquetas.

### Coerción de tipos (reglas)

R realiza coerción automática a un tipo más general cuando se mezclan tipos distintos.

Orden de coerción (de más específico a más general):  
`logical` → `integer` → `numeric/double` → `complex` → `character`.

```r
c(1, "a")       # devuelve c("1", "a") — todo character
c(TRUE, 2)      # devuelve c(1, 2)     — logical se coerciona a numeric
```

Para conversión explícita: `as.numeric()`, `as.integer()`, `as.character()`, `as.factor()`.

**Cuidado:** `as.numeric(factor_variable)` devuelve los códigos internos; para números desde etiquetas: `as.numeric(as.character(factor_variable))`.

### Comprobación de tipo/propiedades

```r
class(obj); typeof(obj); mode(obj)
is.numeric(obj); is.integer(obj); is.character(obj)
is.logical(obj); is.data.frame(obj); is.factor(obj)
```

---

## 2.3 Operadores en R — explicación y matices importantes

R es **vectorizado**: operadores actúan elemento a elemento y aplican la **regla de reciclado** cuando las longitudes difieren.

### 2.3.1 Operadores aritméticos

| Operador | Ejemplo    | Resultado |
|:--------:|:-----------|:----------|
| `+`      | `2 + 3`    | `5`       |
| `-`      | `7 - 2`    | `5`       |
| `*`      | `4 * 6`    | `24`      |
| `/`      | `8 / 2`    | `4`       |
| `^`      | `2^3`      | `8`       |
| `%%`     | `9 %% 4`   | `1` (resto) |
| `%/%`    | `9 %/% 4`  | `2` (división entera) |

**Vectorización y reciclado — ejemplo:**

```r
a <- c(1,2,3)
b <- c(10,20,30)
a + b   # c(11,22,33)

# reciclado: si b tiene longitud 6 y a 3, a se recicla
b2 <- c(10,20,30,40,50,60)
a + b2  # a reciclado: (1,2,3,1,2,3) -> suma elemento a elemento
```

**Advertencia:** reciclado sin longitud múltiplo puede generar advertencia y errores lógicos.

### 2.3.2 Operadores relacionales (comparaciones)

Devuelven vectores lógicos (`TRUE` / `FALSE`):

```r
5 > 3    # TRUE
5 < 3    # FALSE
5 == 5   # TRUE
5 != 3   # TRUE
5 >= 5   # TRUE
```

Comparaciones sobre vectores comparan elemento a elemento:

```r
c(1,2,3) > 2  # c(FALSE, FALSE, TRUE)
```

### 2.3.3 Operadores lógicos

- Elemento por elemento: `&` (AND), `|` (OR).  
- Evaluación solo del primer elemento: `&&`, `||` (útil en `if()`).

```r
c(TRUE, FALSE, TRUE) & c(TRUE, TRUE, FALSE)  # c(TRUE, FALSE, FALSE)
TRUE & FALSE   # FALSE
TRUE && FALSE  # FALSE (solo usa primer elemento)
```

Negación:

```r
!TRUE  # FALSE
```

### Precedencia

La precedencia es la usual (paréntesis primero). Ante la duda, use paréntesis para claridad:

```r
(1 + 2) * 3  # 9
```

---

## 2.4 Funciones básicas y creación de funciones propias

### ¿Qué es una función?

Una **función** recibe argumentos, ejecuta operaciones y devuelve (opcionalmente) un valor. R incluye muchas funciones integradas; también puede crear las suyas.

### Uso de funciones integradas

```r
sqrt(25)        # 5
abs(-8)         # 8
round(3.1416,2) # 3.14
max(1,5,9,2)    # 9
min(1,5,9,2)    # 1
mean(c(1,2,3))  # 2
```

### Ayuda y documentación

```r
help(sqrt)   # o ?sqrt
args(mean)   # muestra argumentos formales
example(lm)  # ejecuta ejemplos incluidos en documentación
```

### Crear funciones propias

Estructura básica:

```r
mi_funcion <- function(arg1, arg2 = 10) {
  resultado <- arg1 + arg2
  return(resultado)   # return() es opcional; la última expresión se devuelve
}
mi_funcion(5)  # devuelve 15 (arg2 = 10 por defecto)
```

**Ejemplo — área de un círculo con validación:**

```r
area_circulo <- function(r) {
  if (!is.numeric(r) || any(r < 0)) stop("r debe ser número no negativo")
  return(pi * r^2)
}
area_circulo(4)  # 50.26548...
```

### Funciones anónimas y `apply`/`lapply`/`sapply`

- `lapply(X, FUN)` → lista.  
- `sapply(X, FUN)` → vector o matriz cuando es posible.  
- `apply(M, MARGIN, FUN)` → matrices (`MARGIN = 1` filas, `2` columnas).

```r
lista <- list(a = 1:5, b = 6:10)
lapply(lista, mean)
sapply(lista, mean)
```

### Argumentos por nombre y por posición

Se recomienda nombrar argumentos:

```r
round(3.14159, digits = 2)
```

### Buenas prácticas al crear funciones

- Documenta con comentarios (propósito, argumentos, valor devuelto).  
- Valida entradas (`stop()` o `warning()` con mensajes claros).  
- Evita efectos secundarios innecesarios (no modificar variables globales dentro de la función).  
- Escribe funciones pequeñas y testables.

---

## 2.5 Ejercicios rápidos (con soluciones comentadas)

A continuación los ejercicios solicitados con soluciones explicadas — útiles como referencia para tus clases.

### Ejercicio 1

Crea una variable con tu edad y otra con el año actual. Calcula en qué año naciste.

**Código (solución):**

```r
edad <- 36        # sustituye por la edad real
anio_actual <- 2025
anio_nacimiento <- anio_actual - edad
anio_nacimiento
```

**Explicación:** restamos la edad al año actual. Para precisión con meses/días usar `lubridate` y fecha de nacimiento.

### Ejercicio 2

Define una variable con el valor `pi` y calcula el área de un círculo de radio 10.

**Código (solución):**

```r
r <- 10
area <- pi * r^2
area  # ≈ 314.1593
```

**Comprobación paso a paso:** `r^2 = 100`; `area = pi * 100 ≈ 314.1593`.

### Ejercicio 3

Evalúa las expresiones y determina `TRUE` o `FALSE`:

- `15 > 10 & 3 < 1`  
- `20 == 4 * 5`  
- `!(5 <= 2)`

**Cálculo y soluciones:**

```r
expr1 <- 15 > 10 & 3 < 1   # TRUE & FALSE -> FALSE
expr2 <- 20 == 4 * 5       # 4*5 = 20 -> TRUE
expr3 <- !(5 <= 2)         # 5 <= 2 -> FALSE -> !FALSE -> TRUE

expr1; expr2; expr3
```

**Comentarios:** combínalos con `if()` para tomar decisiones condicionales en scripts.

### Ejercicio 4

Redondea `7.56789` a 1 y 3 decimales.

**Código (solución):**

```r
x <- 7.56789
round(x, 1)  # 7.6
round(x, 3)  # 7.568
```

**Comentario:** el redondeo a 3 decimales sube porque el cuarto decimal es >= 5.

---

## 2.6 Errores comunes y recomendaciones pedagógicas

- **Confundir `NA` y `NULL`:** `NA` es dato faltante dentro de una estructura; `NULL` indica ausencia del objeto. `length(NA) == 1`, `length(NULL) == 0`.  
- **Factores vs caracteres:** comprobar `str(df)` después de leer datos. `as.numeric(factor)` no devuelve etiquetas.  
- **Coerción implícita indeseada:** mezclar tipos en vectores convierte todo a `character`.  
- **Reciclado involuntario:** operar vectores de longitudes distintas sin control puede producir errores silenciosos.  
- **Comparaciones con punto flotante:** evitar `==` para números reales; use `all.equal()` para tolerancia.

---

## 2.7 Código de ejemplo completo

```r
# --- Crear variables ---
edad <- 30
anio_actual <- 2025
anio_nacimiento <- anio_actual - edad

# --- Área circulo ---
r <- 10
area <- pi * r^2

# --- Expresiones lógicas ---
expr1 <- 15 > 10 & 3 < 1
expr2 <- 20 == 4 * 5
expr3 <- !(5 <= 2)

# --- Redondeo ---
x <- 7.56789
r1 <- round(x, 1)
r3 <- round(x, 3)

# Mostrar resultados
list(anio_nacimiento = anio_nacimiento,
     area = area,
     expr1 = expr1, expr2 = expr2, expr3 = expr3,
     round_1 = r1, round_3 = r3)
```

# Tema 3 – Estructuras de datos en R

En R, los datos no se guardan solo como valores individuales, sino en estructuras organizadas.  
Las más usadas son: **vectores, listas, matrices, data frames y factores**.

---

## 3.1 Vectores

Un **vector** es la estructura más simple en R: una secuencia de elementos del mismo tipo (numéricos, lógicos o de texto).

### Crear vectores

```r
    # Crear un vector numérico
    v1 <- c(1, 2, 3, 4, 5)

    # Vector de caracteres
    v2 <- c("A", "B", "C")

    # Vector lógico
    v3 <- c(TRUE, FALSE, TRUE)

    # Secuencias automáticas
    1:10          # Números del 1 al 10
    seq(0, 20, 2) # De 0 a 20 de 2 en 2
    rep(5, 4)     # Repite el número 5 cuatro veces
```

**Nota pedagógica:** `1:10` es una forma rápida para secuencias cortas; `seq()` es más flexible para pasos y longitudes. `rep()` repite valores.

### Operaciones vectorizadas

Una de las ventajas de R es que permite **operaciones vectorizadas**, es decir, que se aplican a todos los elementos al mismo tiempo.

```r
    x <- c(2, 4, 6)
    y <- c(1, 3, 5)

    x + y    # -> c(3, 7, 11)
    x * y    # -> c(2, 12, 30)
```

**Explicación:** las operaciones aritméticas se aplican elemento a elemento. Si las longitudes difieren, R aplica la **regla de reciclado** (recycle rule): el vector más corto se repite para emparejar la longitud del más largo (y R emite advertencia si la longitud no es múltiplo).

### Acceso y modificación de elementos

```r
    v <- c(10, 20, 30, 40, 50)

    v[1]      # primer elemento -> 10
    v[3]      # tercer elemento -> 30
    v[2:4]    # subvector desde 2 hasta 4 -> c(20,30,40)
    v[-1]     # todos menos el primero
    v[v > 25] # elementos mayores a 25 -> c(30,40,50)

    # Asignación por índice
    v[1] <- 15   # v ahora: 15,20,30,40,50

    # Nombres de componentes
    names(v) <- c("a","b","c","d","e")
    v["c"]      # acceso por nombre
```

**Nota:** el indexado en R es **1-based** (comienza en 1), a diferencia de otros lenguajes como Python.

---

## 3.2 Listas

### Definición formal (Factores)

Una **lista** (`list`) es una estructura que puede contener elementos de diferentes tipos y estructuras: vectores, matrices, data.frames, otras listas, funciones, etc. Es la forma más flexible de agregar información empacada.

### Crear y usar listas — ejemplos

```r
    mi_lista <- list(
      nombre = "Ana",
      edad = 25,
      notas = c(8, 9, 10),
      aprobado = TRUE
    )

    # Acceso por nombre
    mi_lista$nombre   # "Ana"
    mi_lista$notas    # c(8,9,10)

    # Acceso por posición (doble corchete devuelve el elemento en su tipo original)
    mi_lista[[2]]     # 25

    # Acceso por índice simple (devuelve lista de longitud 1)
    mi_lista[2]       # lista con el segundo elemento
```

### Ejemplo de uso real

Guardar resultados de un análisis por estudiante:

```r
    estudiante <- list(
      id = 123,
      nombre = "María",
      calificaciones = c(parcial1 = 85, parcial2 = 90, final = 92),
      estadisticas = list(promedio = mean(c(85,90,92)), desviacion = sd(c(85,90,92)))
    )
```

**Nota:** `[[ ]]` devuelve el valor contenido (por ejemplo, un vector), mientras que `[ ]` devuelve una sub-lista.

---

## 3.3 Matrices

### Definición formal de factores

Una **matriz** es un arreglo bidimensional (filas × columnas) con todos sus elementos del **mismo tipo** (homogéneo). Se usa en álgebra lineal, operaciones matriciales y cuando se necesita una estructura rectangular homogénea.

### Crear matrices — ejemplos

```r
    # Matriz 3x3 columna por columna (predeterminado)
    m <- matrix(1:9, nrow = 3, ncol = 3)

    # Matriz llenada por filas
    m2 <- matrix(1:9, nrow = 3, byrow = TRUE)

    # Acceso
    m[1,2]   # fila 1, columna 2
    m[,2]    # columna 2 completa
    m[3,]    # fila 3 completa
```

### Operaciones matriciales

```r
    A <- matrix(1:4, nrow = 2)  # 2x2
    B <- matrix(c(5,6,7,8), nrow = 2)
    A %*% B   # multiplicación matricial
    t(A)      # traspuesta
    solve(A)  # matriz inversa (si es invertible)
```

**Advertencia:** `*` es multiplicación elemento a elemento; la multiplicación matricial es `%*%`.

Las matrices son muy usadas en operaciones algebraicas, por ejemplo, en modelos estadísticos y machine learning.

---

## 3.4 Data Frames (y tibbles)

Un **data.frame** es una estructura tabular donde cada columna puede ser de distinto tipo (numérico, carácter, lógico, factor). Es la estructura estándar para conjuntos de datos “rectangulares” y la más utilizada para análisis.

`tibble` (del paquete `tibble`/`tidyverse`) es una versión mejorada: impresión más legible y manejo más estricto de subsetting.

### Crear y manipular data.frames — ejemplos

```r
    # Crear un data frame simple
    df <- data.frame(
      nombre = c("Ana", "Luis", "Marta"),
      edad = c(23, 30, 28),
      aprobado = c(TRUE, FALSE, TRUE),
      stringsAsFactors = FALSE
    )

    # Mostrar y explorar
    df
    str(df)        # estructura
    summary(df)    # resumen

    # Acceso a columnas
    df$edad
    df[["nombre"]]

    # Acceso a filas y celdas
    df[1, ]          # fila 1 completa
    df[2, "nombre"]  # celda fila 2, columna 'nombre'


```

### Ejemplo aplicado (producción de café por departamento — datos hipotéticos)

Supongamos que tenemos un CSV con producción de café por departamento y año:

```r
    df_cafe <- data.frame(
      departamento = c("Matagalpa","Matagalpa","Jinotega","Jinotega"),
      anio = c(2020, 2021, 2020, 2021),
      toneladas = c(15000, 15500, 14000, 14200)
    )

    # Sumar producción por departamento (ejemplo con dplyr)
    library(dplyr)
    resumen <- df_cafe %>%
      group_by(departamento) %>%
      summarise(total_toneladas = sum(toneladas, na.rm = TRUE))
```

**Nota:** usar `stringsAsFactors = FALSE` es buena idea si no quieres que `read.csv()` convierta cadenas a `factor` (en versiones antiguas esto era comportamiento por defecto).

---

## 3.5 Factores

Un **factor** es un vector que representa variables categóricas. Internamente almacena un vector de enteros (códigos) y un atributo `levels` (las etiquetas). Los factores son fundamentales para modelado estadístico (regresiones, tablas de contingencia) y para controlar el orden en gráficos.

### Crear y usar factores — ejemplos

```r
    sexo <- factor(c("Mujer", "Hombre", "Mujer", "Mujer", "Hombre"))
    levels(sexo)   # muestra las categorías únicas
    nlevels(sexo)  # número de niveles

    # Factores ordenados (importante para categorías ordinales)
    nivel <- factor(c("Bajo", "Medio", "Alto", "Medio"), levels = c("Bajo","Medio","Alto"), ordered = TRUE)
```

### Precaución con conversión

Convertir factores a numérico directamente puede llevar a errores sutiles:

```r
    f <- factor(c("10","20","30"))
    as.numeric(f)               # devuelve 1,2,3 (códigos internos)
    as.numeric(as.character(f)) # devuelve 10,20,30 (valores numéricos reales)
```

---

## 3.6 Ejercicios rápidos (con soluciones comentadas)

```r
    v <- 1:20
    v[v %% 3 == 0]  # -> 3,6,9,12,15,18
```

### Listas — información personal

```r
    mi_lista <- list(
      nombre = "Amo",
      edad = 35,
      notas = c(85, 90, 95)
    )
```

### Matrices — segunda fila

```r
    m <- matrix(1:16, nrow = 4, byrow = TRUE)
    m[2, ]  # segunda fila completa
```

### Data.frame — seleccionar columna

```r
    df <- data.frame(
      nombre = c("Ana", "Luis", "Marta", "José"),
      edad = c(23, 30, 28, 40),
      ciudad = c("Managua", "León", "Granada", "Estelí"),
      stringsAsFactors = FALSE
    )
    df$ciudad  # devuelve vector de ciudades
```

### Factores — niveles

```r
    nivel <- factor(c("Alto", "Medio", "Bajo", "Alto", "Bajo"))
    levels(nivel)  # -> "Alto" "Bajo" "Medio"  (orden lexicográfico por defecto)

    # Si se desea un orden específico:
    nivel2 <- factor(c("Alto","Medio","Bajo","Alto","Bajo"), levels=c("Bajo","Medio","Alto"), ordered=TRUE)
    levels(nivel2)
```

---

Las estructuras de datos en R son robustas y potentes; dominarlas permite pasar rápidamente de cálculos elementales a análisis reproducibles y gráficos informativos. Para tus clases en Nicaragua, enfatiza ejemplos reales (producción de café por departamento, encuestas municipales, datos del Banco Central) y promueve la práctica sistemática: **crear, inspeccionar, transformar y validar** datos en cada paso.

Tema 4 — Manipulación de datos en R (versión extendida y explicativa)  
Objetivo: ofrecer una guía exhaustiva y práctica —con fundamentos conceptuales y ejemplos aplicados a Nicaragua— sobre las operaciones más habituales para limpiar, transformar y preparar datos en R, con explicaciones detalladas de por qué se hace cada paso y qué interpretar de los resultados.

Nota metodológica: en docencia e investigación es esencial que cada decisión de limpieza vaya acompañada de su justificación (científica y práctica) y de un registro —comentarios en el script— que explique la elección. Esto favorece reproducibilidad y permite a otros (estudiantes, colegas, revisores) evaluar la validez de los resultados.

---

# Tema 4 — Manipulación de datos en R (versión extendida y explicativa)  

La manipulación de datos no es sólo una serie de operaciones técnicas: es el proceso que convierte registros brutos en información fiable. Sus objetivos concretos son:

- Corregir errores de captura (nombres mal escritos, filas duplicadas, tipos equivocados)  
- Tratar valores faltantes de forma que las imputaciones o eliminaciones no introduzcan sesgos  
- Transformar variables para que los modelos y gráficos reflejen relaciones reales (p. ej., tasas en lugar de totales)  
- Estructurar los datos de modo que cumplan con el principio de *tidy data* (cada variable en columna, observación en fila)  

Desde un punto de vista científico, las buenas prácticas se apoyan en: **transparencia** (documentar), **trazabilidad** (scripts en lugar de hojas), y **validación** (comparar con fuentes oficiales y emplear pruebas simples — sanity checks).

---

### 2. Flujo de trabajo típico (explicado paso a paso)

- **Carga e inspección inicial** — detectar problemas inmediatos (separador erróneo, encabezados duplicados, columnas con mezcla de tipos).  
  - Qué comprobar: `str()` para tipos, `head()` para contenido, `summary()` para rangos y outliers.  

- **Normalizar nombres y tipos** — nombres consistentes facilitan reproducibilidad.  
  - Qué comprobar: `names()` y `sapply(df, class)`.  

- **Detectar NA y patrones** — decidir estrategia adecuada (eliminar, imputar, modelar los missing).  
  - Qué comprobar: %NA por variable y por grupo.  

- **Transformaciones y creación de variables** — indicadores comparables (ej. rendimiento t/ha).  
  - Qué comprobar: plausibilidad.  

- **Agrupaciones y agregaciones** — indicadores territoriales.  
  - Qué comprobar: sumas vs fuentes oficiales.  

- **Uniones** — enriquecer datos con contexto (población, precios).  
  - Qué comprobar: filas perdidas por join (`anti_join()`).  

- **Reshape** — formatos wide/long.  
  - Qué comprobar: filas/columnas antes y después.  

- **Exportación** — compartir y archivar datos limpios.  
  - Siempre acompañar con diccionario y README.  

---

### 3. Ejemplo (producción de café en Nicaragua)

#### 3.1 Preparación — librerías

```r
library(dplyr)      
library(tidyr)      
library(lubridate)  
library(janitor)    
```

Explicación: dplyr y tidyr forman el núcleo del tidyverse. lubridate evita errores comunes con fechas. janitor limpia nombres.

#### 3.2 Crear dataset simulado

```r
set.seed(42)
produccion_cafe <- data.frame(
  id = 1:20,
  departamento = rep(c("Matagalpa","Jinotega","Nueva Segovia","Estelí"), each = 5),
  municipio = rep(c("San Ramón","La Dalia","Jalapa","Estelí","Dipilto"), 4),
  ano = sample(2015:2020, 20, replace = TRUE),
  hectareas = round(runif(20, 2, 50),1),
  toneladas = round(rnorm(20, mean = 20, sd = 8),1),
  valor_export_usd = round(runif(20, 3000, 50000), 0)
)
```

**Introducir NA intencionales**
produccion_cafe$toneladas[c(3,12)] <- NA
produccion_cafe$valor_export_usd[7] <- NA

#### 3.3 Inspección inicial

```r
head(produccion_cafe)
glimpse(produccion_cafe)
summary(produccion_cafe)

produccion_cafe %>% filter(if_any(everything(), is.na))
```

#### 3.4 Normalizar nombres

```r
produccion_cafe <- produccion_cafe %>% 
  janitor::clean_names()
```

#### 3.5 Estrategias para NA

```r
produccion_cafe %>% group_by(departamento) %>%
  summarise(n_missing_ton = sum(is.na(toneladas)), total = n())

produccion_cafe <- produccion_cafe %>%
  group_by(departamento) %>%
  mutate(toneladas = if_else(is.na(toneladas),
                             round(mean(toneladas, na.rm = TRUE), 1),
                             toneladas)) %>%
  ungroup()

produccion_cafe <- produccion_cafe %>%
  mutate(valor_export_usd = if_else(is.na(valor_export_usd),
                                    round(median(valor_export_usd, na.rm = TRUE), 0),
                                    valor_export_usd))
```

#### 3.6 Crear variables derivadas

```r
produccion_cafe <- produccion_cafe %>%
  mutate(rendimiento_t_ha = round(toneladas / hectareas, 2))
```

#### 3.7 Filtrado y ordenamiento

```r
produccion_cafe %>%
  filter(departamento == "Matagalpa", rendimiento_t_ha > 0.5) %>%
  arrange(desc(rendimiento_t_ha))
```

#### 3.8 Agrupación y resumen

```r
resumen_depto_ano <- produccion_cafe %>%
  group_by(departamento, ano) %>%
  summarise(
    hectareas_tot = sum(hectareas, na.rm = TRUE),
    toneladas_tot = sum(toneladas, na.rm = TRUE),
    rendimiento_prom = round(mean(rendimiento_t_ha, na.rm = TRUE), 2),
    obs = n(),
    .groups = "drop"
  ) %>%
  arrange(departamento, ano)

resumen_depto_ano
```

#### 3.9 Uniones

```r
poblacion_municipal <- data.frame(
  municipio = c("San Ramón","La Dalia","Jalapa","Estelí","Dipilto"),
  poblacion_2019 = c(22000, 18000, 15000, 51000, 9000)
)

produccion_muni <- produccion_cafe %>%
  left_join(poblacion_municipal, by = "municipio") %>%
  mutate(toneladas_perc = round(toneladas / poblacion_2019, 5))
```

#### 3.10 Reshape (wide ↔ long)

```r
# df_wide %>% pivot_longer(cols = starts_with("mes_"), names_to = "mes", values_to = "valor")

#### 3.11 Exportar

# write.csv(produccion_cafe, "produccion_cafe_limpia.csv", row.names = FALSE)
# writexl::write_xlsx(produccion_cafe, "produccion_cafe_limpia.xlsx")
# saveRDS(produccion_cafe, "produccion_cafe_limpia.rds")
```

### 4. Técnicas avanzadas

- Manejo de fechas (lubridate::ymd, dmy)
- Duplicados: distinct(), investigar antes de eliminar
- Outliers: gráficos + reglas lógicas
- Imputación avanzada: mice, missForest
- Datos grandes: data.table, duckdb, dbplyr
- Reproducibilidad: renv, packrat

### 5. Buenas prácticas

- Scripts claros y comentados
- Usar set.seed()
- Diccionario de datos
- Control de versiones (git)
- Tests con stopifnot()

### 6. Actividades y ejercicios sugeridos

- Diagnóstico de NA
- Comparación de estrategias de imputación
- Unión y conciliación de tablas
- Reporte reproducible en RMarkdown

### 7. Errores típicos

- No revisar str() → tipos incorrectos
- as.numeric() sobre factores → errores
- Join sin normalizar texto
- Eliminar NA sin analizar patrón
- Comparar floats con ==

### 8. Recursos y lecturas

- R for Data Science — Wickham & Grolemund
- Advanced R — Wickham
- Documentación oficial de dplyr, tidyr, mice, etc.
- Paquetes útiles: janitor, naniar, visdat, missForest, dbplyr


