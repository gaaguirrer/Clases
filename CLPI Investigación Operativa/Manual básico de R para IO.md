# Manual de R para Investigación de Operaciones en Ingeniería de Sistemas de Información

## Tema 1: Introducción a R y RStudio para Ingeniería de Sistemas

### 1.1 ¿Qué es R y por qué es esencial para la Ingeniería en Sistemas de Información?

**Problema:** Imagine que debe analizar el rendimiento de un servidor web bajo diferentes cargas de usuarios. ¿Cómo procesaría miles de registros de log, calcularía métricas de performance y visualizaría los resultados para tomar decisiones de capacidad?

**Solución con R:** R es un lenguaje de programación especializado en análisis estadístico y visualización que permite manipular grandes volúmenes de datos, implementar algoritmos complejos y generar reportes reproducibles - exactamente lo que necesita un ingeniero de sistemas.

> Según Chambers (2008) en _"Software for Data Analysis"_, R proporciona un entorno unificado para manipulación, cálculo y visualización de datos que es especialmente valioso para problemas de ingeniería de sistemas donde los datos son multidimensionales y requieren transformaciones complejas.

**Aplicación en sistemas de información e investigación de operaciones:**

- Análisis de rendimiento de sistemas
- Simulación de carga de usuarios
- Optimización de recursos computacionales
- Predicción de fallos y capacidad
- Análisis de redes y conectividad

---

### 1.2 Instalación de R y RStudio: Configuración del entorno profesional

**Instalación de R:**

Para usuarios de Windows:  
Visitar [R para windows](https://cran.r-project.org/bin/windows/base/)
Descargar y ejecutar el instalador

Para Ubuntu/Debian:  
sudo apt-get install r-base r-base-dev

Para macOS:  
Visitar [R para mac](https://cran.r-project.org/bin/macosx/)

**Instalación de RStudio:**

- Descargar desde [R Studio](https://posit.co/download/rstudio-desktop/)
- Instalar la versión Desktop Open Source License

**Verificación de la instalación:**

Ejecutar en la consola de R:

```r
version$version.string
```

Debería mostrar: _"R version 4.3.1 (2023-06-16)"_

> Según Wickham & Grolemund (2017) en _"R for Data Science"_, es fundamental mantener un entorno consistente mediante el uso de proyectos específicos y control de versiones.

---

### 1.3 Interface de RStudio: Herramientas para el ingeniero de sistemas

**Páneles principales y su utilidad en ingeniería de sistemas:**

- **Consola (Console):** Ejecución inmediata de código y pruebas rápidas

Ejemplo: Calcular capacidad teórica de servidor

```r
capacidad_teorica <- function(usuarios_concurrentes, tiempo_respuesta) {
 return(usuarios_concurrentes / tiempo_respuesta)
}
capacidad_teorica(1000, 2) # 500 transacciones/segundo
```

- **Editor de scripts (Source):** Donde se desarrollan programas completos

Ejemplo: Script para análisis de rendimiento

```r
analizar_rendimiento <- function(datos_servidor) {
 uso_cpu <- mean(datos_servidor$cpu_usage)
  latency_p95 <- quantile(datos_servidor$response_time, 0.95)
 return(list(cpu = uso_cpu, latency = latency_p95))
}
```

- **Entorno (Environment):** Monitorización de variables y objetos en memoria  
  Fundamental para debuggear problemas de rendimiento y memoria

- **Panel de gráficos (Plots):** Visualización de métricas de performance

Ejemplo rápido de visualización:

```r
load_data <- c(65, 78, 82, 90, 95, 98, 100, 99, 97)
plot(load_data, type = "b", main = "Carga del servidor bajo estrés")
```

---

### 1.4 Primeros pasos: Operaciones básicas aplicadas

**Problema:** Calcular métricas de performance básicas para un servidor web.

**Operaciones fundamentales:**

1. Asignación de variables (asignando métricas de performance)

```r
   response_times <- c(2.1, 1.8, 2.5, 3.2, 2.9, 1.5, 2.8)
   concurrent_users <- c(100, 150, 200, 250, 300, 350, 400)
```

2. Cálculo de estadísticas descriptivas (según Jain, 1991 en _"The Art of Computer Systems Performance Analysis"_)

```r
   mean_response <- mean(response_times)
   median_response <- median(response_times)
   std_dev_response <- sd(response_times)
```

4. Análisis de correlación entre usuarios y tiempo de respuesta

```r
   correlation <- cor(concurrent_users, response_times)
```

5. Resultados

```r
   cat("Estadísticas de rendimiento:\n")
   cat("Tiempo promedio de respuesta:", mean_response, "segundos\n")
   cat("Desviación estándar:", std_dev_response, "\n")
   cat("Correlación usuarios-tiempo:", correlation, "\n")
```

**Sistema de ayuda integrado:**

```r
?mean
?sd
?cor

Buscar por tema:
??"standard deviation"
??"correlation"
```

---

### 1.5 Problema integrador: Análisis inicial de capacidad de servidor

**Escenario:** Usted es ingeniero de sistemas en una empresa que experimenta problemas de rendimiento. Debe analizar datos preliminares para determinar si existe una relación entre la cantidad de usuarios concurrentes y el tiempo de respuesta.

**Solución paso a paso:**

Datos simulados (en la práctica vendrían de logs reales):

```r
usuarios <- c(50, 100, 150, 200, 250, 300, 350, 400)
tiempos_respuesta <- c(1.2, 1.5, 1.8, 2.1, 2.7, 3.5, 4.8, 6.3)
```

1. Análisis exploratorio básico

```r
   summary(tiempos_respuesta)
   cat("Máximo tiempo de respuesta:", max(tiempos_respuesta), "segundos\n")
```

2. Modelado preliminar (regresión lineal simple)

```r
   modelo <- lm(tiempos_respuesta ~ usuarios)
   coeficientes <- coef(modelo)
```

3. Predicción para 500 usuarios

```r
   prediccion_500 <- coeficientes[1] + coeficientes[2] \* 500
   cat("Tiempo de respuesta estimado para 500 usuarios:", round(prediccion_500, 2), "segundos\n")
```

4. Evaluación de capacidad según SLA (Service Level Agreement)

```r
   sla_maximo <- 5.0 # 5 segundos máximo de respuesta
   capacidad_maxima <- (sla_maximo - coeficientes[1]) / coeficientes[2]
   cat("Capacidad máxima dentro del SLA:", round(capacidad_maxima), "usuarios concurrentes\n")
```

---

### 1.6 Ejercicios de autoevaluación

**Ejercicio 1:** Calcule el percentil 95 de los tiempos de respuesta y determine si cumple con un SLA de 4 segundos para el 95% de las requests.

Datos:

```r
response_times <- c(1.2, 1.5, 1.8, 2.1, 2.7, 3.5, 4.8, 6.3, 2.9, 3.1)
```

Solución:

```r
p95 <- quantile(response_times, 0.95)
cumple_sla <- p95 <= 4
cat("Percentil 95:", p95, "\n")
cat("¿Cumple SLA?", cumple_sla, "\n")
```

**Ejercicio 2:** Simule la carga de usuarios para una hora pico y calcule los recursos necesarios.

Parámetros del sistema:

```r
usuarios_pico <- 1000
transacciones_por_usuario <- 5
tiempo_promedio_transaccion <- 2.5 # segundos
```

Cálculo de capacidad requerida:

```r
total_transacciones <- usuarios_pico \* transacciones_por_usuario
capacidad_requerida <- total_transacciones / tiempo_promedio_transaccion
cat("Capacidad requerida:", capacidad_requerida, "transacciones/segundo\n")
```

---

### 1.7 Recursos adicionales y referencias

**Libro recomendado:** _"The Art of Computer Systems Performance Analysis"_ by Raj Jain

**Paquetes R útiles para ingeniería de sistemas:**

- bench para benchmarking de código
- profvis para profiling de performance
- future para procesamiento paralelo

**Comunidades:** RStudio Community, Stack Overflow para preguntas específicas

> _"Without data, you're just another person with an opinion"_ - W. Edwards Deming, estadístico y pionero en control de calidad, cuya filosofía es fundamental para la ingeniería de sistemas basada en datos.

## Tema 2: Fundamentos de Programación en R para Análisis de Sistemas

### 2.1 Introducción a la Programación en R

Para un ingeniero de sistemas, la programación es fundamental para:

- **Automatización de tareas:** Permite automatizar procesos repetitivos como monitoreo de sistemas.
- **Análisis de datos:** Facilita el análisis de grandes volúmenes de datos de sistemas.
- **Simulación:** Permite modelar y simular el comportamiento de sistemas antes de implementarlos.
- **Resolución de problemas:** Ayuda a resolver problemas complejos mediante algoritmos.

R es especialmente útil porque está diseñado específicamente para análisis de datos, tiene una amplia comunidad de usuarios, es gratuito y cuenta con herramientas poderosas para visualización.

---

### 2.2 Variables y Tipos de Datos Básicos

**¿Qué es una variable?**

Una variable es como un contenedor con una etiqueta donde puedes almacenar información. La etiqueta es el nombre de la variable y el contenido es el valor.

Ejemplos:

- Variable numérica (almacena números):

```r
cantidad_servidores <- 5
temperatura_cpu <- 65.5
```

- Variable de texto (entre comillas):

```r
nombre_servidor <- "servidor_principal"
ubicacion <- "Sala A"
```

- Variable lógica (TRUE o FALSE):

```r
esta_activo <- TRUE
necesita_mantenimiento <- FALSE
```

**Tipos de datos comunes en R:**

| Tipo      | Ejemplo | Descripción           | Uso en sistemas          |
| --------- | ------- | --------------------- | ------------------------ |
| numeric   | 15.7    | Números con decimales | Métricas de rendimiento  |
| integer   | 10L     | Números enteros       | Cantidad de dispositivos |
| character | "Hola"  | Texto                 | Nombres de servidores    |
| logical   | TRUE    | Verdadero o falso     | Estados de conexión      |

---

### 2.3 Operadores Básicos

**Operadores aritméticos:**

- Suma: `usuarios_concurrentes <- 100 + 50`
- Resta: `espacio_libre <- 1000 - 350`
- Multiplicación: `almacenamiento_total <- 500 * 4`
- División: `promedio_uso <- 450 / 5`
- Potencia: `bytes_en_gb <- 1024^3`

**Operadores de comparación:**

- Igualdad: `5 == 5 → TRUE`
- Desigualdad: `5 != 3 → TRUE`
- Mayor que: `10 > 5 → TRUE`
- Menor que: `3 < 2 → FALSE`
- Mayor o igual: `5 >= 5 → TRUE`

---

### 2.4 Estructuras de Datos Básicas

**Vectores:** listas de valores del mismo tipo.  
Ejemplo:

```r
tiempos_respuesta <- c(2.1, 1.8, 2.5, 3.2, 2.9)
```

**Data frames:** tablas con filas y columnas.  
Ejemplo:

```r
recursos_sistema <- data.frame(
  servidor = c("srv01", "srv02", "srv03"),
  ram_gb = c(16, 32, 64),
  cpu_cores = c(4, 8, 16),
  activo = c(TRUE, TRUE, FALSE)
)
```

---

### 2.5 Funciones Básicas

Una función es como una herramienta que realiza una tarea específica.

Ejemplos en R:

- `mean()` → promedio
- `max()` → valor máximo
- `min()` → valor mínimo
- `length()` → número de elementos
- `summary()` → resumen estadístico

---

### 2.6 Estructuras de Control

**Condicionales:**  
Permiten tomar decisiones.  
Ejemplo:  
`if (uso_cpu > 90) { … } else { … }`

**Bucles:**  
Repiten acciones automáticamente.  
Ejemplo: `for (hora in 1:8) { … }`

---

### 2.7 Creando Funciones Propias

Ejemplo:

```r
calcular_capacidad <- function(usuarios, recursos_por_usuario, recursos_totales) {
  usuarios_soportados <- recursos_totales / recursos_por_usuario
  if (usuarios <= usuarios_soportados) {
    mensaje <- paste("Sistema puede soportar", usuarios, "usuarios. Capacidad adecuada.")
  } else {
    mensaje <- paste("ALERTA: Solo soporta", floor(usuarios_soportados), "usuarios.")
  }
  return(mensaje)
}
```

---

### 2.8 Trabajando con Archivos CSV

- Guardar datos: write.csv(datos, "archivo.csv", row.names = FALSE)
- Leer datos: read.csv("archivo.csv")

Ejemplo de aplicación: guardar métricas de servidores y luego analizarlas.

---

### 2.9 Ejercicios Prácticos

**Ejercicio 1: Monitoreo Simple de Sistema**  
Analizar uso promedio de memoria y disco y generar un informe CSV con resultados.

**Ejercicio 2: Análisis de Rendimiento de Servidor Web**  
Calcular estadísticas básicas de tiempos de respuesta, verificar cumplimiento de estándar y generar gráfico comparativo.

---

### 2.10 Consejos para Principiantes

- Empieza simple y aumenta la complejidad poco a poco.
- Prueba el código frecuentemente.
- Usa comentarios para documentar.
- No memorices: usa la ayuda de R.
- Practica regularmente.
- Aprende de los errores.

---

## Tema 3: Manipulación de Datos con dplyr y tidyr para Análisis de Sistemas

### 3.1 Introducción a la Manipulación de Datos

**¿Qué es la manipulación de datos y por qué es crucial para ingenieros de sistemas?**  
La manipulación de datos es el proceso de limpiar, transformar y reorganizar datos brutos para hacerlos adecuados para el análisis. Como ingeniero de sistemas, te encontrarás constantemente con datos de diversas fuentes: logs de servidores, métricas de rendimiento, registros de red, y más. Estos datos rara vez vienen en el formato perfecto para análisis inmediato.

**dplyr** y **tidyr** son paquetes de R diseñados específicamente para estas tareas. Forman parte del "tidyverse", una colección de paquetes de R para ciencia de datos que comparten una filosofía común de organización de datos y gramática para la manipulación de datos.

#### Filosofía de los paquetes tidyverse

La filosofía detrás de dplyr y tidyr se basa en tres principios fundamentales:

- Cada variable forma una columna
- Cada observación forma una fila
- Cada tipo de unidad observacional forma una tabla

Estos principios crean datos "tidy" (ordenados), que son mucho más fáciles de manipular, visualizar y modelar.

#### Instalación y carga de paquetes

```r
# Instalar los paquetes necesarios
# Esto solo necesitas hacerlo una vez en tu computadora
install.packages("dplyr")   # Para manipulación de datos
install.packages("tidyr")   # Para reorganización de datos
install.packages("readr")   # Para lectura eficiente de archivos

# Cargar los paquetes en tu sesión de R
# Esto debes hacerlo cada vez que inicies R y quieras usar estos paquetes
library(dplyr)  # Carga las funciones de dplyr
library(tidyr)  # Carga las funciones de tidyr
library(readr)  # Carga las funciones de readr

# Verificar que los paquetes se cargaron correctamente
# No debería aparecer ningún mensaje de error
```

---

### 3.2 Importación de Datos desde Archivos CSV

#### La importancia de una buena importación de datos

En ingeniería de sistemas, frecuentemente trabajarás con datos exportados desde sistemas de monitoreo, logs de servidores, o herramientas de análisis de rendimiento. Estos datos comúnmente se exportan en formato CSV (Comma-Separated Values).

La función read_csv() del paquete readr es más eficiente que la función base read.csv() porque:

- Es más rápida con archivos grandes
- No convierte strings a factores por defecto
- Muestra una barra de progreso para archivos grandes
- Proporciona mejores mensajes de error

#### Creación y lectura de un archivo CSV de ejemplo

```r

# Primero, creemos un conjunto de datos de ejemplo que simule métricas de servidores

# Este data frame representa mediciones tomadas cada 5 minutos de diferentes servidores

datos_ejemplo <- data.frame(
servidor = c("web01", "web02", "db01", "db02", "cache01", "web03"), # Nombres de servidores
cpu_uso = c(45, 62, 38, 71, 56, 48), # % de uso de CPU
mem_uso = c(60, 75, 45, 82, 67, 58), # % de uso de memoria
temp = c(65, 68, 62, 72, 66, 64), # Temperatura en °C
estado = c("activo", "activo", "activo", "sobrecarga", "activo", "activo"), # Estado del servidor
timestamp = as.POSIXct(c("2023-10-01 08:00:00", "2023-10-01 08:05:00",
"2023-10-01 08:10:00", "2023-10-01 08:15:00",
"2023-10-01 08:20:00", "2023-10-01 08:25:00")) # Marca de tiempo
)

# Guardar el data frame en un archivo CSV

# write_csv() es la función de readr para escribir archivos CSV

write_csv(datos_ejemplo, "datos_servidores.csv")

# Ahora leemos el archivo CSV que acabamos de crear

# read_csv() detecta automáticamente los tipos de datos

datos_servidores <- read_csv("datos_servidores.csv")

# Examinar la estructura de los datos importados

# glimpse() proporciona una vista transposed de los datos (filas → columnas, columnas → filas)

print("Estructura de los datos importados:")
glimpse(datos_servidores)

# También podemos usar head() para ver las primeras filas

print("Primeras filas de los datos:")
head(datos_servidores)
```

---

### 3.3 Verbos Básicos de dplyr

dplyr proporciona una gramática coherente para la manipulación de datos, con verbos que corresponden a las operaciones más comunes. El operador %>% (pipe) nos permite encadenar estas operaciones de manera legible.

#### 3.3.1 filter() - Filtrar filas basado en condiciones

El verbo filter() permite seleccionar un subconjunto de filas basado en condiciones lógicas. Es especialmente útil para focalizar el análisis en datos relevantes.

```r
# Filtrar servidores con uso de CPU mayor a 50%

# %>% pasa el resultado de la izquierda a la función de la derecha

servidores_alta_carga <- datos_servidores %>%
filter(cpu_uso > 50) # Mantiene solo filas donde cpu_uso > 50

print("Servidores con alta carga de CPU (mayor al 50%):")
print(servidores_alta_carga)

# Filtrar servidores activos con temperatura menor a 70°C

# Podemos combinar múltiples condiciones con , o &

servidores_estables <- datos_servidores %>%
filter(estado == "activo", # Estado debe ser "activo"
temp < 70) # Temperatura menor a 70°C

print("Servidores estables (activos y temperatura < 70°C):")
print(servidores_estables)

# Filtrar usando operador OR (|)

servidores_problematicos <- datos_servidores %>%
filter(cpu_uso > 70 | # Uso de CPU > 70%
mem_uso > 75 | # Uso de memoria > 75%
temp > 70) # Temperatura > 70°C

print("Servidores con al menos un indicador problemático:")
print(servidores_problematicos)
```

#### 3.3.2 select() - Seleccionar columnas específicas

El verbo select() permite elegir un subconjunto de columnas, útil cuando trabajas con datasets con muchas columnas y solo necesitas algunas.

```r

# Seleccionar solo las columnas de interés para análisis de rendimiento

# Listamos los nombres de las columnas que queremos mantener

metricas_esenciales <- datos_servidores %>%
select(servidor, # Columna con nombre del servidor
cpu_uso, # Columna con uso de CPU
mem_uso, # Columna con uso de memoria
 temp) # Columna con temperatura

print("Métricas esenciales de rendimiento:")
print(metricas_esenciales)

# Seleccionar columnas que contengan "uso" en su nombre

# contains() es una función helper que busca patrones en nombres de columnas

metricas_uso <- datos_servidores %>%
select(servidor, # Mantener columna servidor
contains("uso")) # Mantener columnas que contengan "uso"

print("Métricas de uso (CPU y memoria):")
print(metricas_uso)

# También podemos excluir columnas usando el signo -

metricas_sin_tiempo <- datos_servidores %>%
select(-timestamp) # Excluir columna timestamp

print("Datos sin la columna de timestamp:")
print(metricas_sin_tiempo)
```

#### 3.3.3 mutate() - Crear nuevas columnas

El verbo mutate() permite crear nuevas columnas basadas en transformaciones de columnas existentes. Es extremadamente útil para calcular métricas derivadas.

```r

# Crear nuevas columnas calculadas basadas en las existentes

datos_analisis <- datos_servidores %>%
mutate( # Calcular si el servidor está bajo estrés (condición lógica) # Un servidor está bajo estrés si uso de CPU > 70% O uso de memoria > 75%
bajo_estres = cpu_uso > 70 | mem_uso > 75,

    # Categorizar nivel de temperatura usando case_when()
    # case_when() permite crear condiciones complejas similares a if-else
    nivel_temp = case_when(
      temp < 65 ~ "Óptima",             # Si temp < 65 → "Óptima"
      temp >= 65 & temp < 70 ~ "Aceptable",  # Si 65 ≤ temp < 70 → "Aceptable"
      temp >= 70 ~ "Crítica"             # Si temp ≥ 70 → "Crítica"
    ),

    # Calcular un índice de salud del servidor (fórmula compuesta)
    # Pondera diferentes métricas para crear un índice único
    indice_salud = 100 - (cpu_uso * 0.4 +   # CPU contribuye 40%
                         mem_uso * 0.3 +    # Memoria contribuye 30%
                         temp / 2)          # Temperatura contribuye (temp/2)%

)

print("Datos con nuevas métricas calculadas:")
print(datos_analisis)

# Podemos usar mutate() para modificar columnas existentes también

datos_normalizados <- datos_servidores %>%
mutate( # Normalizar métricas a escala 0-1
cpu_normalizado = cpu_uso / 100, # Convertir % a proporción
mem_normalizado = mem_uso / 100 # Convertir % a proporción
)

print("Datos con métricas normalizadas:")
print(datos_normalizados)
```

#### 3.3.4 arrange() - Ordenar filas

El verbo arrange() ordena las filas de un data frame basado en los valores de una o más columnas. Por defecto ordena en orden ascendente.

```r

# Ordenar por uso de CPU descendente

# desc() ordena en orden descendente

servidores_ordenados_cpu <- datos_servidores %>%
arrange(desc(cpu_uso)) # Ordenar de mayor a menor uso de CPU

print("Servidores ordenados por uso de CPU (descendente):")
print(servidores_ordenados_cpu)

# Ordenar por múltiples criterios

# Primero por estado, luego por uso de memoria descendente

servidores_ordenados_multiple <- datos_servidores %>%
arrange(estado, # Ordenar por estado (A-Z)
desc(mem_uso)) # Luego por memoria descendente

print("Servidores ordenados por estado y uso de memoria:")
print(servidores_ordenados_multiple)

# Ordenar personalizado con factor levels

# Podemos definir un orden específico para una columna

orden_estados <- c("sobrecarga", "activo") # Definir orden deseado

datos_ordenados_personalizado <- datos_servidores %>%
mutate(estado = factor(estado, levels = orden_estados)) %>% # Convertir a factor con orden específico
arrange(estado) # Ordenar según el orden del factor

print("Servidores ordenados por estado personalizado:")
print(datos_ordenados_personalizado)
```

#### 3.3.5 summarize() - Resumir datos

El verbo summarize() (o summarise()) colapsa múltiples valores en un solo valor resumen. Es especialmente útil con group_by() para crear resúmenes por grupo.

```r

# Calcular estadísticas resumidas para todo el dataset

resumen_estadisticas <- datos_servidores %>%
summarize(
n_servidores = n(), # Contar número de filas
cpu_promedio = mean(cpu_uso), # Calcular promedio de CPU
cpu_maximo = max(cpu_uso), # Encontrar valor máximo de CPU
mem_promedio = mean(mem_uso), # Calcular promedio de memoria
temp_promedio = mean(temp), # Calcular promedio de temperatura
servidores_sobrecarga = sum(estado == "sobrecarga") # Contar servidores en sobrecarga
)

print("Resumen estadístico del sistema:")
print(resumen_estadisticas)

# Podemos calcular múltiples estadísticas para una misma columna

resumen_detallado <- datos_servidores %>%
summarize( # Para uso de CPU
cpu_media = mean(cpu_uso),
cpu_mediana = median(cpu_uso),
cpu_desviacion = sd(cpu_uso),
cpu_min = min(cpu_uso),
cpu_max = max(cpu_uso),

    # Para uso de memoria
    mem_media = mean(mem_uso),
    mem_mediana = median(mem_uso),

    # Para temperatura
    temp_media = mean(temp)

)

print("Resumen detallado de métricas:")
print(resumen_detallado)
```

---

### 3.4 Operaciones con group_by()

#### El poder del agrupamiento en el análisis de datos

El verbo group_by() permite agrupar datos por una o más variables, para luego realizar operaciones dentro de cada grupo. Esto es extremadamente útil para análisis comparativos.

```r

# Agrupar por estado y calcular métricas para cada grupo

metricas_por_estado <- datos_servidores %>%
group_by(estado) %>% # Agrupar por la columna estado
summarize(
n = n(), # Número de servidores en cada estado
cpu_promedio = mean(cpu_uso), # Promedio de CPU por estado
mem_promedio = mean(mem_uso), # Promedio de memoria por estado
temp_promedio = mean(temp) # Promedio de temperatura por estado
) %>%
arrange(desc(cpu_promedio)) # Ordenar por CPU promedio descendente

print("Métricas agrupadas por estado del servidor:")
print(metricas_por_estado)

# Agrupar por tipo de servidor (inferido del nombre)

metricas_por_tipo <- datos_servidores %>%
mutate( # Extraer tipo de servidor del nombre (primera parte antes de números)
tipo_servidor = case_when(
grepl("^web", servidor) ~ "Web Server", # Si empieza con "web"
grepl("^db", servidor) ~ "Database Server", # Si empieza con "db"
 grepl("^cache", servidor) ~ "Cache Server", # Si empieza con "cache"
TRUE ~ "Otro" # Para cualquier otro caso
)
) %>%
group_by(tipo_servidor) %>% # Agrupar por el tipo de servidor
summarize(
n = n(), # Número de servidores por tipo
cpu_promedio = round(mean(cpu_uso), 1), # CPU promedio redondeado
mem_promedio = round(mean(mem_uso), 1), # Memoria promedio redondeado
temp_maxima = max(temp) # Temperatura máxima por tipo
)

print("Métricas por tipo de servidor:")
print(metricas_por_tipo)

# Agrupamiento múltiple y operaciones más complejas

# Podemos agrupar por múltiples variables y calcular varias métricas

if ("timestamp" %in% colnames(datos_servidores)) {
metricas_por_hora_estado <- datos_servidores %>%
mutate(hora = format(timestamp, "%H:%M")) %>% # Extraer hora del timestamp
group_by(hora, estado) %>% # Agrupar por hora y estado
summarize(
n = n(),
cpu_promedio = mean(cpu_uso),
.groups = "drop" # Eliminar agrupamiento después del summarize
)

print("Métricas por hora y estado:")
print(metricas_por_hora_estado)
}
```

---

### 3.5 Manipulación de Datos con tidyr

`tidyr` complementa a `dplyr` proporcionando funciones para reorganizar datos, especialmente para cambiar entre formatos wide (ancho) y long (largo).

#### 3.5.1 pivot_longer() - Convertir datos wide a long

Los datos en formato "wide" tienen una columna para cada variable, mientras que los datos en formato "long" tienen una columna para los nombres de variables y otra para los valores. pivot_longer() convierte de wide a long.

```r

# Crear un subset de datos en formato wide

datos_wide <- datos_servidores %>%
select(servidor, cpu_uso, mem_uso, temp) # Seleccionar columnas de métricas

print("Datos en formato wide (una columna por métrica):")
print(datos_wide)

# Convertir a formato long (más adecuado para visualización y algunos análisis)

datos_long <- datos_wide %>%
pivot_longer(
cols = c(cpu_uso, mem_uso, temp), # Columnas a convertir
names_to = "metrica", # Nombre de la nueva columna para los nombres de métricas
values_to = "valor" # Nombre de la nueva columna para los valores
)

print("Datos en formato long (una fila por combinación servidor-métrica):")
print(datos_long)

# Podemos hacer análisis más fácilmente con datos en formato long

analisis_long <- datos_long %>%
group_by(metrica) %>%
summarize(
promedio = mean(valor),
maximo = max(valor),
minimo = min(valor)
)

print("Resumen de métricas en formato long:")
print(analisis_long)
```

#### 3.5.2 `pivot_wider()` - Convertir datos long a wide

`pivot_wider()` es la operación inversa a `pivot_longer()`, convirtiendo datos de formato long a wide.

```r

# Convertir de vuelta a formato wide desde formato long

datos_wide_nuevo <- datos_long %>%
pivot_wider(
names_from = metrica, # Columna que contiene los nombres para las nuevas columnas
values_from = valor # Columna que contiene los valores para las nuevas columnas
)

print("Datos convertidos de nuevo a formato wide:")
print(datos_wide_nuevo)

# pivot_wider() es útil para crear tablas resumen

tabla_resumen <- datos_servidores %>%
group_by(estado) %>%
summarize(
cpu_promedio = mean(cpu_uso),
mem_promedio = mean(mem_uso)
) %>%
pivot_wider(
names_from = estado,
values_from = c(cpu_promedio, mem_promedio)
)

print("Tabla resumen con métricas por estado:")
print(tabla_resumen)
```

#### 3.5.3 `separate()` - Dividir columnas

El verbo `separate()` divide una columna en múltiples columnas basado en un separador. Útil cuando tienes información combinada en una sola columna.

```r

# Crear datos con información combinada (simulando datos de un sistema legacy)

datos_combinados <- data.frame(
servidor_info = c("web01-salaA-activo", "db01-salaB-activo", "cache01-salaA-mantenimiento"),
cpu_uso = c(45, 38, 56)
)

print("Datos con información combinada en una columna:")
print(datos_combinados)

# Separar la columna combinada en columnas individuales

datos_separados <- datos_combinados %>%
separate(
servidor_info, # Columna a separar
into = c("servidor", "sala", "estado"), # Nombres de las nuevas columnas
sep = "-" # Separador (guión)
)

print("Datos después de separar la columna combinada:")
print(datos_separados)

# Podemos controlar cuántas divisiones hacer

datos_separados_limitados <- datos_combinados %>%
separate(
servidor_info,
into = c("servidor", "info_restante"), # Solo dos nuevas columnas
sep = "-", # Separador
extra = "merge" # Mantener el resto unido en la última columna
)

print("Datos con separación limitada:")
print(datos_separados_limitados)
```

---

### 3.6 Unión de Datos

#### Combinando información de múltiples fuentes

En situaciones reales, frecuentemente necesitarás combinar datos de múltiples fuentes. dplyr proporciona varias funciones para unir datos:

- `left_join()`: Mantiene todas las filas del dataset izquierdo
- `right_join()`: Mantiene todas las filas del dataset derecho
- `inner_join()`: Mantiene solo filas con coincidencias en ambos datasets
- `full_join()`: Mantiene todas las filas de ambos datasets

```r

# Crear un dataset con información adicional de servidores

info_servidores <- data.frame(
servidor = c("web01", "web02", "db01", "db02", "cache01", "web03"),
capacidad_ram = c(16, 32, 64, 64, 32, 16), # RAM en GB
capacidad_cpu = c(4, 8, 16, 16, 8, 4), # Núcleos de CPU
sistema_operativo = c("Linux", "Linux", "Linux", "Windows", "Linux", "Linux"),
ubicacion = c("Sala A", "Sala B", "Sala C", "Sala C", "Sala A", "Sala B")
)

print("Información adicional de servidores:")
print(info_servidores)

# Unir los datos de rendimiento con la información de capacidad

# left_join() mantiene todos los servidores del dataset izquierdo (datos_servidores)

datos_completos <- datos_servidores %>%
left_join(info_servidores, by = "servidor") %>% # Unir por columna servidor
mutate( # Calcular porcentaje de uso respecto a la capacidad
ram_porcentaje = (mem_uso / capacidad_ram) _ 100, # % de RAM utilizada
cpu_porcentaje = (cpu_uso / capacidad_cpu) _ 100 # % de CPU utilizada
)

print("Datos completos unidos con información de capacidad:")
print(datos_completos)

# Identificar servidores que no tienen información de capacidad

servidores_sin_info <- datos_servidores %>%
anti_join(info_servidores, by = "servidor") # Encuentra filas sin coincidencia

print("Servidores sin información de capacidad:")
print(servidores_sin_info)

# Unión con múltiples columnas clave (si fuera necesario)

# Supongamos que necesitamos unir por servidor y timestamp

if (all(c("servidor", "timestamp") %in% colnames(datos_servidores)) {

# Crear datos adicionales con timestamp

info_detallada <- data.frame(
servidor = c("web01", "web02"),
timestamp = as.POSIXct(c("2023-10-01 08:00:00", "2023-10-01 08:05:00")),
proceso_principal = c("nginx", "apache")
)

# Unir por múltiples columnas

datos_detallados <- datos_servidores %>%
inner_join(info_detallada, by = c("servidor", "timestamp"))

print("Datos con información detallada por servidor y timestamp:")
print(datos_detallados)
}
```

---

### 3.7 Ejercicio Práctico: Análisis de Rendimiento Completo

Vamos a aplicar todo lo aprendido en un análisis completo de rendimiento de sistemas.

```r

# Cargar datos de ejemplo (si no están disponibles)

if (!file.exists("datos_servidores.csv")) {

# Crear datos de ejemplo

datos_ejemplo <- data.frame(
servidor = c("web01", "web02", "db01", "db02", "cache01", "web03"),
cpu_uso = c(45, 62, 38, 71, 56, 48),
mem_uso = c(60, 75, 45, 82, 67, 58),
temp = c(65, 68, 62, 72, 66, 64),
estado = c("activo", "activo", "activo", "sobrecarga", "activo", "activo"),
timestamp = as.POSIXct(c("2023-10-01 08:00:00", "2023-10-01 08:05:00",
"2023-10-01 08:10:00", "2023-10-01 08:15:00",
"2023-10-01 08:20:00", "2023-10-01 08:25:00"))
)
write_csv(datos_ejemplo, "datos_servidores.csv")
print("Archivo de datos creado: datos_servidores.csv")
}

# Leer los datos

datos <- read_csv("datos_servidores.csv")

# Análisis completo del sistema

analisis_completo <- datos %>%

# Filtrar servidores activos (excluir mantenimiento, etc.)

filter(estado == "activo") %>%

# Calcular métricas adicionales

mutate( # Calcular una métrica compuesta de carga
carga_total = cpu_uso _ 0.6 + mem_uso _ 0.4, # CPU pesa 60%, memoria 40%

    # Categorizar nivel de rendimiento basado en carga total
    nivel_rendimiento = case_when(
      carga_total < 50 ~ "Óptimo",          # Carga baja → óptimo
      carga_total >= 50 & carga_total < 70 ~ "Aceptable",  # Carga media → aceptable
      carga_total >= 70 ~ "Crítico"         # Carga alta → crítico
    ),

    # Calcular si está cerca del límite (uso > 80% en cualquier métrica)
    cerca_limite = cpu_uso > 80 | mem_uso > 80 | temp > 70

) %>%

# Agrupar por nivel de rendimiento

group_by(nivel_rendimiento) %>%

# Calcular estadísticas para cada grupo

summarize(
n_servidores = n(), # Número de servidores en cada categoría
cpu_promedio = mean(cpu_uso), # Promedio de CPU
mem_promedio = mean(mem_uso), # Promedio de memoria
temp_promedio = mean(temp), # Promedio de temperatura
servidores_cerca_limite = sum(cerca_limite), # Número cerca del límite
porcentaje_cerca_limite = mean(cerca_limite) \* 100, # Porcentaje cerca del límite
.groups = "drop" # Eliminar agrupamiento después del summarize
) %>%

# Ordenar por nivel de rendimiento

arrange(factor(nivel_rendimiento, levels = c("Óptimo", "Aceptable", "Crítico")))

print("Análisis completo del rendimiento del sistema:")
print(analisis_completo)

# Guardar el análisis en un archivo CSV

write_csv(analisis_completo, "analisis_rendimiento_completo.csv")
print("Análisis guardado en 'analisis_rendimiento_completo.csv'")

# Crear un resumen ejecutivo

resumen_ejecutivo <- analisis_completo %>%
summarise(
total_servidores = sum(n_servidores),
porcentaje_optimo = sum(n_servidores[nivel_rendimiento == "Óptimo"]) / total_servidores _ 100,
porcentaje_aceptable = sum(n_servidores[nivel_rendimiento == "Aceptable"]) / total_servidores _ 100,
porcentaje_critico = sum(n_servidores[nivel_rendimiento == "Crítico"]) / total_servidores _ 100,
porcentaje_total_cerca_limite = sum(servidores_cerca_limite) / total_servidores _ 100
)

print("Resumen ejecutivo del estado del sistema:")
print(resumen_ejecutivo)
```

---

### 3.8 Ejercicio Avanzado: Simulación de Datos y Análisis

Para practicar con datos más realistas, vamos a simular un conjunto de datos más completo.

```r

# Función para simular datos de servidores más realistas

simular_datos_servidores <- function(n_servidores = 10, n_mediciones = 24) {
datos_simulados <- data.frame()

for (i in 1:n_servidores) { # Determinar tipo de servidor
tipo <- sample(c("web", "db", "cache", "app"), 1)
servidor_id <- paste0(tipo, sprintf("%02d", i))

    # Generar características base según tipo
    if (tipo == "web") {
      cpu_base <- sample(40:60, 1)
      mem_base <- sample(50:70, 1)
    } else if (tipo == "db") {
      cpu_base <- sample(30:50, 1)
      mem_base <- sample(60:80, 1)
    } else if (tipo == "cache") {
      cpu_base <- sample(50:70, 1)
      mem_base <- sample(40:60, 1)
    } else {  # app
      cpu_base <- sample(45:65, 1)
      mem_base <- sample(55:75, 1)
    }

    for (j in 1:n_mediciones) {
      # Simular variación a lo largo del tiempo
      hora <- j
      variacion <- sin(j / 6) * 15  # Variación sinusoidal simulando patrón diario

      cpu <- max(5, min(95, cpu_base + variacion + rnorm(1, 0, 5)))
      mem <- max(10, min(90, mem_base + variacion * 0.8 + rnorm(1, 0, 4)))
      temp <- 60 + cpu / 2 + rnorm(1, 0, 2)

      # Determinar estado basado en métricas
      if (cpu > 85 | mem > 85 | temp > 75) {
        estado <- "alerta"
      } else if (cpu > 70 | mem > 75 | temp > 70) {
        estado <- "advertencia"
      } else {
        estado <- "normal"
      }

      # Crear fila de datos
      fila <- data.frame(
        servidor = servidor_id,
        tipo = tipo,
        hora = hora,
        cpu_uso = round(cpu),
        mem_uso = round(mem),
        temp = round(temp, 1),
        estado = estado
      )

      datos_simulados <- bind_rows(datos_simulados, fila)
    }

}

return(datos_simulados)
}

# Generar datos simulados

set.seed(123) # Para resultados reproducibles
datos_simulados <- simular_datos_servidores(8, 12) # 8 servidores, 12 mediciones

print("Datos simulados de servidores:")
glimpse(datos_simulados)
head(datos_simulados)

# Análisis de tendencias por tipo de servidor

analisis_tendencias <- datos_simulados %>%
group_by(tipo, hora) %>%
summarize(
n_servidores = n(),
cpu_promedio = mean(cpu_uso),
mem_promedio = mean(mem_uso),
temp_promedio = mean(temp),
alertas = sum(estado == "alerta"),
advertencias = sum(estado == "advertencia"),
.groups = "drop"
) %>%
mutate(
porcentaje_alertas = (alertas / n_servidores) _ 100,
porcentaje_problemas = ((alertas + advertencias) / n_servidores) _ 100
)

print("Tendencias de rendimiento por tipo de servidor:")
print(analisis_tendencias)

# Identificar horas críticas

horas_criticas <- analisis_tendencias %>%
filter(porcentaje_problemas > 30) %>%
arrange(desc(porcentaje_problemas))

print("Horas con más del 30% de servidores con problemas:")
print(horas_criticas)

# Guardar datos simulados y análisis

write_csv(datos_simulados, "datos_servidores_simulados.csv")
write_csv(analisis_tendencias, "analisis_tendencias.csv")
write_csv(horas_criticas, "horas_criticas.csv")

print("Datos simulados guardados en 'datos_servidores_simulados.csv'")
print("Análisis de tendencias guardado en 'analisis_tendencias.csv'")
print("Horas críticas guardadas en 'horas_criticas.csv'")
```

---

### 3.9 Buenas Prácticas y Consejos

1. **Manejo de datos faltantes (NA)**

```r

# Identificar valores faltantes

valores_faltantes <- datos_servidores %>%
summarise(across(everything(), ~sum(is.na(.))))

print("Valores faltantes por columna:")
print(valores_faltantes)

# Estrategias para manejar NA

datos_sin_na <- datos_servidores %>%
drop_na() # Eliminar filas con NA

# O reemplazar NA con valores específicos

datos_reemplazados <- datos_servidores %>%
mutate(
cpu_uso = ifelse(is.na(cpu_uso), mean(cpu_uso, na.rm = TRUE), cpu_uso),
mem_uso = ifelse(is.na(mem_uso), median(mem_uso, na.rm = TRUE), mem_uso)
)
```

2. **Validación de datos**

```r

# Verificar que los datos están dentro de rangos esperados

validacion <- datos_servidores %>%
summarise(
cpu_fuera_rango = sum(cpu_uso < 0 | cpu_uso > 100, na.rm = TRUE),
mem_fuera_rango = sum(mem_uso < 0 | mem_uso > 100, na.rm = TRUE),
temp_fuera_rango = sum(temp < 0 | temp > 100, na.rm = TRUE)
)

print("Validación de rangos de datos:")
print(validacion)
```

3. **Optimización para grandes volúmenes de datos**

```r

# Para datasets muy grandes, considera:

# 1. Usar data.table en lugar de dplyr

# 2. Usar las funciones \_if o \_at de dplyr para operaciones selectivas

# 3. Processar datos en chunks

# Ejemplo con mutate_if

datos_numericos_normalizados <- datos_servidores %>%
mutate_if(is.numeric, scale) # Normalizar todas las columnas numéricas

print("Datos numéricos normalizados:")
print(datos_numericos_normalizados)
```

---

### 3.10 Recursos Adicionales

- Documentación oficial de dplyr: [Guía completa con ejemplos](https://dplyr.tidyverse.org/)
- Documentación oficial de tidyr: [Referencia de todas las funciones](https://tidyr.tidyverse.org/)
- Cheatsheet de data manipulation: [Hoja de referencia rápida](https://www.rstudio.com/resources/cheatsheets/)
- Libro "R for Data Science": [Capítulos 5, 9, 12 y 13 cubren estos temas en profundidad](https://r4ds.had.co.nz/)
- Video tutoriales: [Tutorial interactivo](https://www.datacamp.com/courses/dplyr-data-manipulation-r-tutorial)

---

## Tema 4: Visualización de Datos con `ggplot2` para Análisis de Sistemas

### 4.1 Introducción a la Visualización de Datos

**¿Por qué la visualización de datos es crucial para ingenieros de sistemas?**  
La visualización de datos transforma números y métricas en imágenes comprensibles que permiten identificar patrones, tendencias y anomalías de manera instantánea. Para un ingeniero de sistemas, esto significa:

- Monitoreo en tiempo real del estado de servidores y redes
- Identificación rápida de problemas mediante patrones visuales
- Comunicación efectiva del estado del sistema a no técnicos
- Toma de decisiones basada en datos con evidencia visual

`ggplot2` es el paquete de visualización más poderoso de R, basado en la "Gramática de Gráficos" que permite construir visualizaciones capa por capa.

**Instalación y carga de paquetes**  

```r
# Instalar los paquetes necesarios (solo una vez)
install.packages("ggplot2")  # Para visualización
install.packages("gridExtra") # Para organizar múltiples gráficos
install.packages("scales")    # Para formato de escalas

# Cargar los paquetes
library(ggplot2)
library(gridExtra)
library(scales)

# Verificar la versión de ggplot2
packageVersion("ggplot2")
```

---

### 4.2 Fundamentos de ggplot2: La Gramática de Gráficos

`ggplot2` sigue una filosofía de capas donde cada componente del gráfico se añade por separado:

- **Datos:** El dataframe que contiene la información
- **Aesthetics (aes):** Mapeo de variables a elementos visuales
- **Geometries (geom):** Tipo de gráfico (barras, líneas, puntos)
- **Scales:** Control de ejes y leyendas
- **Facets:** División en subgráficos
- **Themes:** Estilo visual general

**Creando tu primer gráfico**  

```r
# Crear datos de ejemplo para practicar
datos_rendimiento <- data.frame(
  servidor = c("Web01", "Web02", "DB01", "DB02", "Cache01"),
  cpu_uso = c(45, 62, 38, 71, 56),
  mem_uso = c(60, 75, 45, 82, 67),
  temp = c(65, 68, 62, 72, 66)
)

# Gráfico básico de barras - Uso de CPU por servidor
grafico_barras <- ggplot(datos_rendimiento, aes(x = servidor, y = cpu_uso)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Uso de CPU por Servidor",
       x = "Servidor",
       y = "Uso de CPU (%)") +
  theme_minimal()

print(grafico_barras)

# Guardar el gráfico
ggsave("uso_cpu_servidores.png", grafico_barras, width = 8, height = 6, dpi = 300)
```

---

### 4.3 Tipos de Gráficos para Análisis de Sistemas

#### 4.3.1 Gráficos de Líneas para Series Temporales

```r
# Crear datos de series temporales (simulación de métricas por hora)
set.seed(123)
horas <- 24
series_temporales <- data.frame(
  hora = 1:horas,
  cpu_uso = 50 + 20 * sin(1:horas / 3) + rnorm(horas, 0, 5),
  mem_uso = 60 + 15 * sin(1:horas / 4) + rnorm(horas, 0, 4),
  temp = 65 + 5 * sin(1:horas / 2) + rnorm(horas, 0, 2)
)

# Gráfico de línea para uso de CPU a lo largo del tiempo
grafico_linea <- ggplot(series_temporales, aes(x = hora, y = cpu_uso)) +
  geom_line(color = "blue", size = 1) +
  geom_point(color = "darkblue", size = 2) +
  labs(title = "Uso de CPU a lo Largo del Tiempo",
       x = "Hora",
       y = "Uso de CPU (%)") +
  theme_minimal() +
  scale_x_continuous(breaks = seq(1, 24, by = 3))

print(grafico_linea)
ggsave("serie_temporal_cpu.png", grafico_linea, width = 10, height = 6, dpi = 300)
```

#### 4.3.2 Gráficos de Dispersión para Correlaciones

```r
# Gráfico de dispersión para ver relación entre CPU y memoria
grafico_dispersion <- ggplot(datos_rendimiento, aes(x = cpu_uso, y = mem_uso)) +
  geom_point(aes(color = servidor, size = temp), alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Relación entre Uso de CPU y Memoria",
       x = "Uso de CPU (%)",
       y = "Uso de Memoria (%)",
       color = "Servidor",
       size = "Temperatura (°C)") +
  theme_minimal() +
  scale_color_brewer(palette = "Set1")

print(grafico_dispersion)
ggsave("correlacion_cpu_mem.png", grafico_dispersion, width = 9, height = 7, dpi = 300)
```

#### 4.3.3 Boxplots para Distribución de Métricas

```r
# Crear datos más extensos para boxplots
set.seed(456)
datos_boxplot <- data.frame(
  servidor = rep(c("Web01", "Web02", "DB01", "DB02", "Cache01"), each = 20),
  cpu_uso = c(
    rnorm(20, 45, 8), rnorm(20, 62, 10), rnorm(20, 38, 6),
    rnorm(20, 71, 12), rnorm(20, 56, 9)
  )
)

# Boxplot de distribución de uso de CPU por servidor
grafico_boxplot <- ggplot(datos_boxplot, aes(x = servidor, y = cpu_uso, fill = servidor)) +
  geom_boxplot(alpha = 0.7) +
  geom_jitter(width = 0.2, alpha = 0.5) +
  labs(title = "Distribución de Uso de CPU por Servidor",
       x = "Servidor",
       y = "Uso de CPU (%)") +
  theme_minimal() +
  theme(legend.position = "none") +
  scale_fill_brewer(palette = "Pastel1")

print(grafico_boxplot)
ggsave("distribucion_cpu.png", grafico_boxplot, width = 10, height = 6, dpi = 300)
```

#### 4.3.4 Heatmaps para Patrones de Uso

```r
# Crear datos para heatmap (uso por hora y día)
set.seed(789)
dias <- 7
heatmap_data <- expand.grid(hora = 1:24, dia = 1:dias)
heatmap_data$uso <- 40 + 30 * sin(heatmap_data$hora/4) + 
                    10 * cos(heatmap_data$dia) + 
                    rnorm(nrow(heatmap_data), 0, 5)

# Heatmap de uso del sistema
grafico_heatmap <- ggplot(heatmap_data, aes(x = hora, y = dia, fill = uso)) +
  geom_tile() +
  scale_fill_gradient2(low = "green", mid = "yellow", high = "red", 
                       midpoint = 50, name = "Uso (%)") +
  labs(title = "Patrón de Uso del Sistema por Hora y Día",
       x = "Hora del Día",
       y = "Día de la Semana") +
  theme_minimal() +
  scale_x_continuous(breaks = seq(1, 24, by = 3)) +
  scale_y_continuous(breaks = 1:7)

print(grafico_heatmap)
ggsave("heatmap_uso_sistema.png", grafico_heatmap, width = 10, height = 6, dpi = 300)
```

---

### 4.4 Personalización Avanzada de Gráficos

#### 4.4.1 Temas y Estilos

```r
# Personalización completa de un gráfico
grafico_personalizado <- ggplot(datos_rendimiento, aes(x = servidor, y = cpu_uso, fill = servidor)) +
  geom_bar(stat = "identity", alpha = 0.8) +
  geom_text(aes(label = paste0(cpu_uso, "%")), vjust = -0.5, size = 4) +
  labs(title = "Análisis de Rendimiento de Servidores",
       subtitle = "Uso de CPU por servidor",
       x = "Servidores",
       y = "Uso de CPU (%)",
       caption = "Fuente: Sistema de monitoreo - Octubre 2023") +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
    plot.subtitle = element_text(size = 12, hjust = 0.5),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 10),
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none",
    panel.background = element_rect(fill = "white"),
    panel.grid.major = element_line(color = "gray90"),
    panel.grid.minor = element_blank(),
    plot.caption = element_text(face = "italic", color = "gray50")
  ) +
  scale_fill_manual(values = c("#E41A1C", "#377EB8", "#4DAF4A", "#984EA3", "#FF7F00")) +
  ylim(0, 80)

print(grafico_personalizado)
ggsave("grafico_personalizado.png", grafico_personalizado, width = 10, height = 7, dpi = 300)
```

#### 4.4.2 Múltiples Gráficos con Facets

```r
# Preparar datos para facets
datos_facets <- datos_rendimiento %>%
  pivot_longer(cols = c(cpu_uso, mem_uso, temp), 
               names_to = "metrica", 
               values_to = "valor")

# Gráfico con facets para diferentes métricas
grafico_facets <- ggplot(datos_facets, aes(x = servidor, y = valor, fill = servidor)) +
  geom_bar(stat = "identity") +
  facet_wrap(~metrica, scales = "free_y", 
             labeller = labeller(metrica = c("cpu_uso" = "CPU (%)",
                                            "mem_uso" = "Memoria (%)",
                                            "temp" = "Temperatura (°C)"))) +
  labs(title = "Métricas de Rendimiento por Servidor",
       x = "Servidor",
       y = "Valor") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        legend.position = "none")

print(grafico_facets)
ggsave("metricas_facets.png", grafico_facets, width = 12, height = 8, dpi = 300)
```

---

### 4.5 Dashboard de Monitoreo de Sistemas

```r
# Crear un dashboard con múltiples gráficos
# Gráfico 1: Uso de CPU
g1 <- ggplot(datos_rendimiento, aes(x = servidor, y = cpu_uso, fill = servidor)) +
  geom_bar(stat = "identity") +
  labs(title = "Uso de CPU", x = "", y = "CPU (%)") +
  theme_minimal() +
  theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust = 1))

# Gráfico 2: Uso de Memoria
g2 <- ggplot(datos_rendimiento, aes(x = servidor, y = mem_uso, fill = servidor)) +
  geom_bar(stat = "identity") +
  labs(title = "Uso de Memoria", x = "", y = "Memoria (%)") +
  theme_minimal() +
  theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust = 1))

# Gráfico 3: Temperatura
g3 <- ggplot(datos_rendimiento, aes(x = servidor, y = temp, fill = servidor)) +
  geom_bar(stat = "identity") +
  labs(title = "Temperatura", x = "Servidor", y = "Temperatura (°C)") +
  theme_minimal() +
  theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust = 1))

# Gráfico 4: Correlación
g4 <- ggplot(datos_rendimiento, aes(x = cpu_uso, y = mem_uso, color = servidor, size = temp)) +
  geom_point(alpha = 0.7) +
  labs(title = "Correlación CPU-Memoria", x = "CPU (%)", y = "Memoria (%)") +
  theme_minimal()

# Combinar gráficos en un dashboard
dashboard <- grid.arrange(g1, g2, g3, g4, ncol = 2, 
                          top = "Dashboard de Monitoreo de Sistemas")

# Guardar el dashboard
ggsave("dashboard_monitoreo.png", dashboard, width = 14, height = 10, dpi = 300)
```

---

### 4.6 Ejercicio Práctico: Análisis Visual de Datos de Rendimiento

```r
# Cargar datos de rendimiento (simulados)
set.seed(1234)
datos_completos <- data.frame(
  timestamp = seq.POSIXt(from = as.POSIXct("2023-10-01 00:00:00"), 
                         to = as.POSIXct("2023-10-01 23:59:00"), by = "5 min"),
  cpu_uso = 50 + 25 * sin(seq(0, 2*pi, length.out = 288)) + rnorm(288, 0, 5),
  mem_uso = 60 + 20 * cos(seq(0, 2*pi, length.out = 288)) + rnorm(288, 0, 4),
  network_in = abs(rnorm(288, 100, 30)),
  network_out = abs(rnorm(288, 80, 25))
)

# Análisis 1: Tendencia de uso de CPU
analisis_cpu <- ggplot(datos_completos, aes(x = timestamp, y = cpu_uso)) +
  geom_line(color = "blue", alpha = 0.7) +
  geom_smooth(method = "loess", span = 0.1, color = "red", se = FALSE) +
  labs(title = "Tendencia de Uso de CPU",
       x = "Hora del Día",
       y = "Uso de CPU (%)") +
  theme_minimal() +
  scale_x_datetime(date_labels = "%H:%M", date_breaks = "2 hours")

# Análisis 2: Comparación CPU vs Memoria
analisis_comparativo <- ggplot(datos_completos, aes(x = timestamp)) +
  geom_line(aes(y = cpu_uso, color = "CPU"), alpha = 0.7) +
  geom_line(aes(y = mem_uso, color = "Memoria"), alpha = 0.7) +
  labs(title = "Comparación: Uso de CPU vs Memoria",
       x = "Hora del Día",
       y = "Uso (%)",
       color = "Métrica") +
  theme_minimal() +
  scale_x_datetime(date_labels = "%H:%M", date_breaks = "2 hours") +
  scale_color_manual(values = c("CPU" = "blue", "Memoria" = "red"))

# Análisis 3: Tráfico de red
analisis_red <- ggplot(datos_completos, aes(x = timestamp)) +
  geom_area(aes(y = network_in, fill = "Entrada"), alpha = 0.5) +
  geom_area(aes(y = network_out, fill = "Salida"), alpha = 0.5) +
  labs(title = "Tráfico de Red",
       x = "Hora del Día",
       y = "Ancho de Banda (Mbps)",
       fill = "Dirección") +
  theme_minimal() +
  scale_x_datetime(date_labels = "%H:%M", date_breaks = "2 hours") +
  scale_fill_manual(values = c("Entrada" = "green", "Salida" = "orange"))

# Guardar análisis
ggsave("tendencia_cpu.png", analisis_cpu, width = 12, height = 6, dpi = 300)
ggsave("comparacion_cpu_mem.png", analisis_comparativo, width = 12, height = 6, dpi = 300)
ggsave("trafico_red.png", analisis_red, width = 12, height = 6, dpi = 300)

# Crear reporte visual completo
reporte_completo <- grid.arrange(analisis_cpu, analisis_comparativo, analisis_red, ncol = 1)
ggsave("reporte_rendimiento_completo.png", reporte_completo, width = 14, height = 12, dpi = 300)
```

---

### 4.7 Buenas Prácticas para Visualización en Ingeniería de Sistemas

**Principios de diseño efectivo:**  

- Claridad sobre estética: La legibilidad es más importante que el diseño elegante  
- Escalas apropiadas: Usar escalas logarítmicas para datos con amplio rango  
- Colores significativos: Usar colores intuitivos (rojo para alertas, verde para normal)  
- Contexto importante: Incluir líneas de referencia para valores objetivos  
- Consistencia: Mantener el mismo estilo en todos los gráficos de un reporte

**Ejemplo de gráfico con mejores prácticas:**  

```r
# Gráfico con líneas de referencia y anotaciones
umbral_critico <- 70
umbral_advertencia <- 60

grafico_umbrales <- ggplot(datos_completos, aes(x = timestamp, y = cpu_uso)) +
  geom_line(color = "blue", alpha = 0.7) +
  geom_hline(yintercept = umbral_critico, color = "red", linetype = "dashed", size = 1) +
  geom_hline(yintercept = umbral_advertencia, color = "orange", linetype = "dashed", size = 1) +
  annotate("text", x = min(datos_completos$timestamp), y = umbral_critico + 2, 
           label = "Umbral Crítico", color = "red", hjust = 0) +
  annotate("text", x = min(datos_completos$timestamp), y = umbral_advertencia + 2, 
           label = "Umbral Advertencia", color = "orange", hjust = 0) +
  labs(title = "Uso de CPU con Umbrales de Alerta",
       x = "Hora del Día",
       y = "Uso de CPU (%)") +
  theme_minimal() +
  scale_x_datetime(date_labels = "%H:%M", date_breaks = "2 hours")

print(grafico_umbrales)
ggsave("cpu_con_umbrales.png", grafico_umbrales, width = 12, height = 6, dpi = 300)
```

---

### 4.8 Recursos Adicionales y Referencias

- Documentación oficial de [ggplot2](https://ggplot2.tidyverse.org/)
- Galería de [gráficos](https://www.r-graph-gallery.com/)
- Cheatsheet de [ggplot2](https://www.rstudio.com/resources/cheatsheets/)
- Libro recomendado: "ggplot2: Elegant Graphics for Data Analysis" de Hadley Wickham  
- Paletas de [colores](https://colorbrewer2.org/)

---

## Tema 5: Análisis de Series Temporales en Sistemas

### 5.1 Introducción al Análisis de Series Temporales

**¿Qué es una serie temporal y por qué es importante para ingenieros de sistemas?**  
Una serie temporal es una secuencia de puntos de datos recolectados o registrados en intervalos de tiempo regulares. En ingeniería de sistemas, esto es fundamental porque:

- **Monitoreo de rendimiento:** Permite seguir métricas como uso de CPU, memoria, disco y red a lo largo del tiempo.  
- **Detección de anomalías:** Identifica comportamientos inusuales que pueden indicar problemas.  
- **Pronóstico de capacidad:** Predice necesidades futuras de recursos basándose en patrones históricos.  
- **Planificación de capacidad:** Ayuda a tomar decisiones informadas sobre escalamiento de sistemas.  

Las series temporales en sistemas suelen mostrar patrones estacionales (diarios, semanales) y tendencias a largo plazo que son cruciales para la gestión proactiva de infraestructura.

```r  
# Cargar librerías necesarias para análisis de series temporales  
library(ggplot2)    # Para visualización  
library(dplyr)      # Para manipulación de datos  
library(lubridate)  # Para manejo de fechas y horas  
library(forecast)   # Para análisis de series temporales y pronóstico  
library(anomalize)  # Para detección de anomalías  
library(tseries)    # Para pruebas estadísticas de series temporales  
library(zoo)        # Para operaciones con ventanas temporales  

# Configurar tema para gráficos (mejora la presentación visual)  
theme_set(theme_minimal(base_size = 12))  
```

---

### 5.2 Creación y Visualización de Series Temporales

**Generación de datos de ejemplo para análisis**  
Vamos a crear datos simulados que representen métricas típicas de un sistema. Esto nos permitirá practicar sin necesidad de acceso a sistemas reales.

```r  
# Establecer semilla para reproducibilidad (los mismos resultados cada vez)  
set.seed(123)  

# Crear secuencia de marcas de tiempo cada 5 minutos durante 7 días  
fechas <- seq(as.POSIXct("2023-10-01 00:00:00"),  
              as.POSIXct("2023-10-07 23:59:00"), by = "5 min")  

# Generar datos de uso de CPU con patrones realistas:  
# - Patrón diario (mayor uso durante el día, menor por la noche)  
# - Patrón semanal (diferencias entre días laborables y fin de semana)  
# - Ruido aleatorio (variaciones naturales)  
datos_series <- data.frame(  
  timestamp = fechas,  
  cpu_uso = 50 + 25 * sin(2 * pi * (hour(fechas) + minute(fechas)/60)/24) +  
            10 * sin(2 * pi * yday(fechas)/7) + rnorm(length(fechas), 0, 5),  
  mem_uso = 60 + 20 * cos(2 * pi * (hour(fechas) + minute(fechas)/60)/24) +  
            8 * cos(2 * pi * yday(fechas)/7) + rnorm(length(fechas), 0, 4)  
)  

# Añadir algunas anomalías simuladas (picos de uso)  
set.seed(456)  
indices_anomalias <- sample(1:nrow(datos_series), 20)  
datos_series$cpu_uso[indices_anomalias] <- datos_series$cpu_uso[indices_anomalias] +   
  runif(20, 30, 50)  

# Convertir a objeto de serie temporal (ts)  
# frequency = 24*12 porque tenemos 12 mediciones por hora (cada 5 min) × 24 horas  
serie_cpu <- ts(datos_series$cpu_uso,   
                frequency = 24*12,  
                start = c(2023, 10, 1))  

# Examinar la estructura de la serie temporal  
print("Resumen de la serie temporal de CPU:")  
print(summary(serie_cpu))  
print(paste("Longitud de la serie:", length(serie_cpu)))  
print(paste("Frecuencia (mediciones por día):", frequency(serie_cpu)))  
```

**Análisis del resultado:** Hemos creado una serie temporal con 2016 puntos (7 días × 24 horas × 12 mediciones por hora). El uso de CPU muestra un rango típico entre 20% y 90%, con una media alrededor del 50%, lo que es realista para muchos sistemas.

**Visualización de la serie temporal**

```r  
# Gráfico de la serie temporal completa  
grafico_serie <- autoplot(serie_cpu) +  
  labs(title = "Serie Temporal del Uso de CPU",  
       subtitle = "7 días de datos con intervalos de 5 minutos",  
       x = "Tiempo",  
       y = "Uso de CPU (%)") +  
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),  
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))  

print(grafico_serie)  
ggsave("serie_temporal_cpu.png", grafico_serie, width = 12, height = 6, dpi = 300)  

# Preparar datos para análisis de patrones  
datos_series <- datos_series %>%  
  mutate(  
    hora = hour(timestamp),  
    dia_semana = wday(timestamp, label = TRUE, week_start = 1),  
    es_fin_semana = ifelse(dia_semana %in% c("sáb", "dom"), "Fin de semana", "Día laboral")  
  )  

# Calcular promedio por hora para ver patrones diarios  
promedio_hora <- datos_series %>%  
  group_by(hora) %>%  
  summarise(cpu_promedio = mean(cpu_uso),  
            cpu_sd = sd(cpu_uso))  

# Visualizar patrón diario con intervalo de confianza  
grafico_hora <- ggplot(promedio_hora, aes(x = hora, y = cpu_promedio)) +  
  geom_ribbon(aes(ymin = cpu_promedio - cpu_sd, ymax = cpu_promedio + cpu_sd),   
              fill = "lightblue", alpha = 0.5) +  
  geom_line(color = "blue", size = 1) +  
  geom_point(color = "darkblue", size = 2) +  
  labs(title = "Patrón Diario del Uso de CPU",  
       subtitle = "Con banda de desviación estándar (variabilidad típica)",  
       x = "Hora del Día",  
       y = "Uso Promedio de CPU (%)") +  
  scale_x_continuous(breaks = seq(0, 23, by = 3)) +  
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),  
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))  

print(grafico_hora)  
ggsave("patron_diario_cpu.png", grafico_hora, width = 10, height = 6, dpi = 300)  
```

**Análisis del resultado:** El gráfico de patrón diario muestra claramente cómo el uso de CPU sigue un ciclo circadiano, con mayor utilización durante las horas del día y menor durante la noche. La banda de desviación estándar muestra la variabilidad esperada en cada hora.

---

### 5.3 Descomposición de Series Temporales

**Análisis de componentes: tendencia, estacionalidad y residuales**  
La descomposición de series temporales separa una serie en tres componentes:

- **Tendencia:** Movimiento a largo plazo.  
- **Estacionalidad:** Patrones que se repiten en intervalos regulares.  
- **Residuales:** Lo que queda después de eliminar tendencia y estacionalidad (ruido + anomalías).  

```r  
# Descomposición STL (Seasonal-Trend decomposition using Loess)  
# s.window = "periodic" asume que la estacionalidad es constante  
descomposicion <- stl(serie_cpu, s.window = "periodic")  

# Examinar los componentes  
print("Resumen de la descomposición STL:")  
print(summary(descomposicion))  

# Visualizar todos los componentes juntos  
grafico_descomposicion <- autoplot(descomposicion) +  
  labs(title = "Descomposición STL de la Serie Temporal de CPU",  
       subtitle = "Componentes: Observado, Estacional, Tendencia y Residual") +  
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),  
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))  

print(grafico_descomposicion)  
ggsave("descomposicion_stl.png", grafico_descomposicion, width = 12, height = 8, dpi = 300)  

# Extraer componentes individuales para análisis detallado  
tendencia <- descomposicion$time.series[, "trend"]  
estacionalidad <- descomposicion$time.series[, "seasonal"]  
residuales <- descomposicion$time.series[, "remainder"]  

# Crear dataframe con todos los componentes  
componentes <- data.frame(  
  timestamp = datos_series$timestamp,  
  original = datos_series$cpu_uso,  
  tendencia = as.numeric(tendencia),  
  estacionalidad = as.numeric(estacionalidad),  
  residuales = as.numeric(residuales)  
)  

# Calcular fuerza de componentes (varianza explicada)  
varianza_original <- var(componentes$original, na.rm = TRUE)  
varianza_residual <- var(componentes$residuales, na.rm = TRUE)  
fuerza_estacional <- max(0, 1 - (varianza_residual/varianza_original))  
fuerza_tendencia <- max(0, 1 - (varianza_residual/var(componentes$original - componentes$estacionalidad, na.rm = TRUE)))  

print(paste("Fuerza de estacionalidad:", round(fuerza_estacional, 3)))  
print(paste("Fuerza de tendencia:", round(fuerza_tendencia, 3)))  

# Visualizar componentes por separado  
componentes_largo <- componentes %>%  
  pivot_longer(cols = -timestamp, names_to = "componente", values_to = "valor")  

grafico_componentes <- ggplot(componentes_largo, aes(x = timestamp, y = valor)) +  
  geom_line(color = "steelblue", alpha = 0.8) +  
  facet_wrap(~componente, ncol = 1, scales = "free_y") +  
  labs(title = "Componentes de la Serie Temporal de CPU",  
       subtitle = "Descomposición en observado, tendencia, estacionalidad y residuales",  
       x = "Tiempo",  
       y = "Valor") +  
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),  
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))  

print(grafico_componentes)  
ggsave("componentes_series.png", grafico_componentes, width = 12, height = 10, dpi = 300)  
```

**Análisis del resultado:** La descomposición STL revela que:  

- La **tendencia** muestra cambios suaves a lo largo de los 7 días.  
- La **estacionalidad** muestra un patrón claro de 24 horas (patrón diario).  
- Los **residuales** contienen principalmente ruido pero también algunas anomalías.  

Los valores de fuerza (cercanos a 1) indican que tanto la estacionalidad como la tendencia son componentes fuertes en esta serie temporal, lo que es típico en métricas de sistemas.

---

### 5.4 Detección de Anomalías en Series Temporales

**Identificación de valores atípicos y comportamientos anómalos**  
Las anomalías en sistemas pueden indicar problemas como picos de tráfico inesperados, fallos de hardware, o ataques de seguridad.

```r  
# Detección de anomalías usando el método GESD (Generalized Extreme Studentized Deviate)  
anomalias <- datos_series %>%  
  time_decompose(cpu_uso, method = "stl", frequency = "auto", trend = "auto") %>%  
  anomalize(remainder, method = "gesd", alpha = 0.05, max_anoms = 0.2) %>%  
  time_recompose()  

# Examinar resultados de la detección de anomalías  
print("Resumen de anomalías detectadas:")  
print(table(anomalias$anomaly))  

# Filtrar solo las anomalías  
anomalias_info <- anomalias %>%  
  filter(anomaly == "Yes") %>%  
  select(timestamp, cpu_uso, remainder, anomaly)  

print("Estadísticas de las anomalías detectadas:")  
print(summary(anomalias_info$cpu_uso))  

# Visualizar anomalías en el contexto de la serie temporal  
grafico_anomalias <- anomalias %>%  
  plot_anomalies(time_recomposed = TRUE) +  
  labs(title = "Detección de Anomalías en el Uso de CPU",  
       subtitle = "Puntos rojos indican valores anómalos (alpha = 0.05)",  
       x = "Tiempo",  
       y = "Uso de CPU (%)") +  
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),  
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))  

print(grafico_anomalias)  
ggsave("anomalias_cpu.png", grafico_anomalias, width = 12, height = 6, dpi = 300)  

# Analizar cuándo ocurren las anomalías  
anomalias_hora <- anomalias %>%  
  filter(anomaly == "Yes") %>%  
  mutate(hora = hour(timestamp)) %>%  
  group_by(hora) %>%  
  summarise(n_anomalias = n(),  
            cpu_promedio = mean(cpu_uso),  
            cpu_maximo = max(cpu_uso))  

print("Distribución de anomalías por hora del día:")  
print(anomalias_hora)  

# Visualizar distribución temporal de anomalías  
grafico_anomalias_hora <- ggplot(anomalias_hora, aes(x = hora, y = n_anomalias)) +  
  geom_bar(stat = "identity", fill = "coral", alpha = 0.8) +  
  labs(title = "Distribución de Anomalías por Hora del Día",  
       subtitle = "Número de anomalías detectadas en cada hora",  
       x = "Hora del Día",  
       y = "Número de Anomalías") +  
  scale_x_continuous(breaks = 0:23) +  
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),  
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))  

print(grafico_anomalias_hora)  
ggsave("anomalias_por_hora.png", grafico_anomalias_hora, width = 10, height = 6, dpi = 300)  
```

**Análisis del resultado:** La detección de anomalías ha identificado correctamente los picos de uso que insertamos artificialmente en los datos. La distribución por horas muestra que las anomalías tienden a ocurrir con mayor frecuencia durante las horas pico de actividad, lo que es consistente con problemas reales en sistemas (mayor probabilidad de issues durante alta carga).

---
### 5.5 Pronóstico de Series Temporales
**Modelado y predicción de métricas de sistema**

El pronóstico de series temporales permite anticipar necesidades futuras de recursos y planificar *capacity planning*.

```r
# Dividir datos en conjunto de entrenamiento (80%) y prueba (20%)
# Esto nos permite evaluar la precisión de nuestros modelos
train_size <- floor(0.8 * length(serie_cpu))
train <- window(serie_cpu, end = train_size / frequency(serie_cpu))
test <- window(serie_cpu, start = (train_size + 1) / frequency(serie_cpu))

print(paste("Tamaño conjunto entrenamiento:", length(train)))
print(paste("Tamaño conjunto prueba:", length(test)))

# Modelo ARIMA automático (selecciona mejores parámetros automáticamente)
# ARIMA = AutoRegressive Integrated Moving Average
modelo_arima <- auto.arima(train, 
                          seasonal = TRUE, 
                          stepwise = TRUE, 
                          approximation = FALSE,
                          trace = TRUE)  # Muestra proceso de selección

# Examinar el modelo seleccionado
print("Resumen del modelo ARIMA:")
print(summary(modelo_arima))

# Realizar pronóstico
pronostico <- forecast(modelo_arima, h = length(test))

# Evaluar precisión del modelo
precision <- accuracy(pronostico, test)
print("Precisión del modelo ARIMA:")
print(precision)

# Visualizar pronóstico vs valores reales
grafico_pronostico <- autoplot(pronostico) +
  autolayer(test, series = "Datos reales") +
  labs(title = "Pronóstico del Uso de CPU con Modelo ARIMA",
       subtitle = paste("ARIMA", paste(modelo_arima$arma, collapse = ","), 
                       "- MAPE:", round(precision[2, "MAPE"], 2), "%"),
       x = "Tiempo",
       y = "Uso de CPU (%)") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))

print(grafico_pronostico)
ggsave("pronostico_arima.png", grafico_pronostico, width = 12, height = 6, dpi = 300)

# Comparar con modelo de suavizado exponencial (ETS)
modelo_ets <- ets(train)
pronostico_ets <- forecast(modelo_ets, h = length(test))
precision_ets <- accuracy(pronostico_ets, test)

# Crear comparativa de modelos
comparacion <- data.frame(
  Modelo = c("ARIMA", "ETS"),
  MAPE = c(precision[2, "MAPE"], precision_ets[2, "MAPE"]),
  RMSE = c(precision[2, "RMSE"], precision_ets[2, "RMSE"]),
  AIC = c(modelo_arima$aic, modelo_ets$aic)
)

print("Comparación de modelos de pronóstico:")
print(comparacion)

# Gráfico comparativo de ambos modelos
grafico_comparativo <- autoplot(train, series = "Entrenamiento") +
  autolayer(test, series = "Prueba (real)") +
  autolayer(pronostico$mean, series = "ARIMA") +
  autolayer(pronostico_ets$mean, series = "ETS") +
  labs(title = "Comparación de Modelos de Pronóstico",
       subtitle = "ARIMA vs Suavizado Exponencial (ETS)",
       x = "Tiempo",
       y = "Uso de CPU (%)") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))

print(grafico_comparativo)
ggsave("comparacion_modelos.png", grafico_comparativo, width = 12, height = 6, dpi = 300)
```

**Análisis del resultado:**  
El modelo ARIMA ha demostrado ser efectivo para pronosticar el uso de CPU, con un MAPE (Error Porcentual Absoluto Medio) del X.X%, lo que indica una buena precisión. La comparación con el modelo ETS muestra que [el modelo X performa mejor/peor] basado en las métricas MAPE y RMSE.

---

### 5.6 Análisis de Estacionalidad y Tendencia

**Identificación de patrones recurrentes y tendencias a largo plazo**

```r
# Análisis de autocorrelación (ACF) - mide correlación con valores pasados
acf_plot <- ggAcf(serie_cpu, lag.max = 24*12*2) +  # 2 días de lags
  labs(title = "Función de Autocorrelación (ACF) del Uso de CPU",
       subtitle = "Correlación con valores pasados (lags)") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))

print(acf_plot)
ggsave("acf_cpu.png", acf_plot, width = 10, height = 6, dpi = 300)

# Análisis de autocorrelación parcial (PACF)
pacf_plot <- ggPacf(serie_cpu, lag.max = 24*12*2) +
  labs(title = "Función de Autocorrelación Parcial (PACF) del Uso de CPU",
       subtitle = "Correlación directa con valores pasados, eliminando intermediarios") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))

print(pacf_plot)
ggsave("pacf_cpu.png", pacf_plot, width = 10, height = 6, dpi = 300)

# Prueba de estacionariedad (Augmented Dickey-Fuller)
prueba_adf <- adf.test(serie_cpu)
print("Prueba de Dickey-Fuller Aumentada:")
print(prueba_adf)

if (prueba_adf$p.value < 0.05) {
  print("La serie es ESTACIONARIA (rechazamos H0)")
} else {
  print("La serie NO ES ESTACIONARIA (no podemos rechazar H0)")
}

if (prueba_adf$p.value >= 0.05) {
  serie_diff <- diff(serie_cpu)
  prueba_adf_diff <- adf.test(na.omit(serie_diff))
  print("Prueba ADF después de diferenciación:")
  print(prueba_adf_diff)
}

# Análisis espectral
periodograma <- spectrum(serie_cpu, plot = FALSE)
picos_estacionales <- data.frame(
  frecuencia = periodograma$freq,
  espectro = periodograma$spec
) %>% arrange(desc(espectro)) %>% head(10)

print("Principales frecuencias estacionales identificadas:")
print(picos_estacionales)

# Convertir frecuencias a períodos (horas)
picos_estacionales$periodo_horas <- 1 / (picos_estacionales$frecuencia / frequency(serie_cpu))
print("Periodos correspondientes a las frecuencias principales:")
print(picos_estacionales[, c("frecuencia", "periodo_horas", "espectro")])
```

**Análisis del resultado:**  
El análisis ACF muestra picos en los lags 288, 576, etc. (24 horas × 12 mediciones/hora = 288), confirmando la estacionalidad diaria. La prueba ADF indica que la serie [es/no es] estacionaria, lo que [justifica/no justifica] la aplicación de diferenciación. El análisis espectral identifica las frecuencias más importantes, siendo la de 24 horas la más dominante.

---

### 5.7 Ejercicio Práctico: Análisis Completo de Series Temporales

**Caso de estudio: Análisis de rendimiento de un servidor web**

```r
# Crear datos más complejos simulando un servidor web real
set.seed(789)
datos_web <- data.frame(
  timestamp = seq(as.POSIXct("2023-09-01 00:00:00"), 
                  as.POSIXct("2023-10-31 23:59:00"), by = "15 min"),
  respuesta_promedio = 100 + 50 * sin(2 * pi * (hour(timestamp) + minute(timestamp)/60)/24) +
                       30 * sin(2 * pi * yday(timestamp)/30) + rnorm(length(timestamp), 0, 10),
  solicitudes_por_segundo = 50 + 40 * cos(2 * pi * (hour(timestamp) + minute(timestamp)/60)/24) +
                            25 * cos(2 * pi * yday(timestamp)/30) + rnorm(length(timestamp), 0, 8)
)

# Añadir anomalías y eventos especiales
set.seed(101112)
indices_picos <- sample(1:nrow(datos_web), 30)
datos_web$respuesta_promedio[indices_picos] <- datos_web$respuesta_promedio[indices_picos] + runif(30, 100, 300)

datos_web$solicitudes_por_segundo[datos_web$timestamp >= as.POSIXct("2023-10-15 00:00:00") & 
                                  datos_web$timestamp <= as.POSIXct("2023-10-15 23:59:59")] <- 
  datos_web$solicitudes_por_segundo[datos_web$timestamp >= as.POSIXct("2023-10-15 00:00:00") & 
                                   datos_web$timestamp <= as.POSIXct("2023-10-15 23:59:59")] * 3

datos_web$solicitudes_por_segundo[datos_web$timestamp >= as.POSIXct("2023-10-20 00:00:00") & 
                                  datos_web$timestamp <= as.POSIXct("2023-10-20 23:59:59")] <- 
  datos_web$solicitudes_por_segundo[datos_web$timestamp >= as.POSIXct("2023-10-20 00:00:00") & 
                                   datos_web$timestamp <= as.POSIXct("2023-10-20 23:59:59")] * 2.5

# Convertir a series temporales
serie_respuesta <- ts(datos_web$respuesta_promedio, 
                      frequency = 24*4,
                      start = c(2023, 9, 1))

# Función para análisis completo
analisis_completo <- function(serie, nombre_metrica) {
  descomposicion <- stl(serie, s.window = "periodic")
  
  anomalias <- time_decompose(
    data.frame(timestamp = datos_web$timestamp, valor = as.numeric(serie)),
    valor, method = "stl", frequency = "auto", trend = "auto"
  ) %>% anomalize(remainder, method = "gesd") %>% time_recompose()
  
  train_size <- floor(0.75 * length(serie))
  train <- window(serie, end = train_size / frequency(serie))
  test <- window(serie, start = (train_size + 1) / frequency(serie))
  
  modelo <- auto.arima(train, seasonal = TRUE)
  pronostico <- forecast(modelo, h = length(test))
  precision <- accuracy(pronostico, test)
  
  return(list(
    descomposicion = descomposicion,
    anomalias = anomalias,
    modelo = modelo,
    pronostico = pronostico,
    precision = precision
  ))
}

analisis_respuesta <- analisis_completo(serie_respuesta, "Tiempo de Respuesta")

grafico_resultados <- autoplot(analisis_respuesta$pronostico) +
  autolayer(window(serie_respuesta, 
                   start = (floor(0.75 * length(serie_respuesta)) + 1) / frequency(serie_respuesta)), 
            series = "Valores Reales") +
  labs(title = "Pronóstico del Tiempo de Respuesta del Servidor Web",
       subtitle = paste("MAPE:", round(analisis_respuesta$precision[2, "MAPE"], 2), "%"),
       x = "Tiempo",
       y = "Tiempo de Respuesta (ms)") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, color = "gray50"))

print(grafico_resultados)
ggsave("pronostico_respuesta.png", grafico_resultados, width = 12, height = 6, dpi = 300)

reporte <- data.frame(
  Metrica = "Tiempo de Respuesta",
  MAPE = round(analisis_respuesta$precision[2, "MAPE"], 2),
  RMSE = round(analisis_respuesta$precision[2, "RMSE"], 2),
  Anomalias_Detectadas = sum(analisis_respuesta$anomalias$anomaly == "Yes"),
  Eventos_Especiales = sum(datos_web$timestamp >= as.POSIXct("2023-10-15 00:00:00") & 
                           datos_web$timestamp <= as.POSIXct("2023-10-15 23:59:59"))
)

print("Reporte de Análisis de Rendimiento del Servidor Web:")
print(reporte)
```

**Análisis del resultado:**  
El análisis completo del servidor web revela un MAPE de X.X% en el pronóstico del tiempo de respuesta, lo que indica una precisión [excelente/aceptable/insuficiente]. Se detectaron X anomalías y se identificaron claramente los eventos especiales programados.

---

### 5.8 Alertas y Monitoreo Automatizado

**Sistema de detección de problemas en tiempo real**

```r
# Función para generar alertas basadas en umbrales estadísticos
generar_alertas <- function(serie, ventana = 24*12, umbral_sigma = 3, umbral_minimo = 0) {  
  media_movil <- rollmean(serie, ventana, fill = NA, align = "right")
  sd_movil <- rollapply(serie, ventana, sd, fill = NA, align = "right")
  
  outliers_alto <- which(serie > (media_movil + umbral_sigma * sd_movil))
  outliers_bajo <- which(serie < umbral_minimo)
  outliers <- c(outliers_alto, outliers_bajo)
  
  if (length(outliers) > 0) {
    alertas <- data.frame(
      timestamp = datos_web$timestamp[outliers],
      valor = serie[outliers],
      umbral_superior = media_movil[outliers] + umbral_sigma * sd_movil[outliers],
      umbral_inferior = umbral_minimo,
      tipo = ifelse(serie[outliers] > (media_movil[outliers] + umbral_sigma * sd_movil[outliers]), "Alto", "Bajo")
    )
  } else {
    alertas <- data.frame()
  }
  
  return(alertas)
}

alertas_respuesta <- generar_alertas(serie_respuesta, umbral_sigma = 2.5)

print("Resumen de alertas generadas:")
if (nrow(alertas_respuesta) > 0) {
  print(table(alertas_respuesta$tipo))
  print(head(alertas_respuesta))
} else {
  print("No se generaron alertas")
}

if (nrow(alertas_respuesta) > 0) {
  grafico_alertas <- ggplot(datos_web, aes(x = timestamp, y = respuesta_promedio)) +
    geom_line(color = "gray", alpha = 0.7) +
    geom_ribbon(aes(ymin = 0, ymax = 100), fill = "green", alpha = 0.1) +
    geom_ribbon(aes(ymin = 100, ymax = 200), fill = "yellow", alpha = 0.1) +
    geom_ribbon(aes(ymin = 200, ymax = Inf), fill = "red", alpha = 0.1) +
    geom_point(data = alertas_respuesta, aes(color = tipo), size = 2) +
    labs(title = "Sistema de Alertas para Tiempo de Respuesta",
         subtitle = "Alertas basadas en umbrales estadísticos (2.5σ)",
         x = "Tiempo",
         y = "Tiempo de Respuesta (ms)",
         color = "Tipo de Alerta") +
    theme(plot.title = element_text(hjust = 0.5, face = "bold"),
          plot.subtitle = element_text(hjust = 0.5, color = "gray50")) +
    scale_color_manual(values = c("Alto" = "red", "Bajo" = "blue"))
  
  print(grafico_alertas)
  ggsave("alertas_respuesta.png", grafico_alertas, width = 12, height = 6, dpi = 300)
}

if (nrow(alertas_respuesta) > 0) {
  write.csv(alertas_respuesta, "alertas_tiempo_respuesta.csv", row.names = FALSE)
  print("Alertas guardadas en 'alertas_tiempo_respuesta.csv'")
}
```

**Análisis del resultado:**  
El sistema de alertas ha generado X alertas por valores anormalmente altos y Y alertas por valores anormalmente bajos. Estas alertas podrían integrarse con sistemas de monitoreo como Nagios, Zabbix o Prometheus.

---
