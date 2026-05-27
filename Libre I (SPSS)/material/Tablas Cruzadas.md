# Manual completo: Tablas cruzadas en SPSS

## Introducción

Las tablas cruzadas (tablas de contingencia o de doble entrada) son una de las herramientas más utilizadas en el análisis de datos categóricos. Permiten visualizar la distribución conjunta de dos o más variables cualitativas, facilitando la exploración de posibles relaciones entre ellas.

## ¿Qué es una tabla cruzada?

Una tabla cruzada es una matriz que organiza la información en filas y columnas. En cada celda se muestra la frecuencia (número de casos) que cumple simultáneamente las categorías de la variable dispuesta en fila y las de la variable dispuesta en columna. Además de frecuencias absolutas, suelen incluir porcentajes que ayudan a comparar grupos de distinto tamaño.

**Ejemplo mínimo:** Si se cruzan *Género* (Hombre, Mujer) con *Práctica de deporte* (Sí, No), cada celda indica cuántos hombres practican deporte, cuántos no, y lo mismo para las mujeres.

## ¿Para qué sirve una tabla cruzada?

- **Describir la composición de una muestra:** Ver cómo se distribuyen los casos en las combinaciones de categorías.
- **Detectar patrones de asociación:** Identificar si ciertas categorías de una variable tienden a concentrarse en determinadas categorías de la otra (por ejemplo, si la proporción de personas que practican deporte es mayor en hombres que en mujeres).
- **Base para pruebas estadísticas:** Sirven de insumo para la prueba Chi-cuadrado, que evalúa si la relación observada es estadísticamente significativa.
- **Segmentar y profundizar:** Al añadir variables de control (capas) se puede examinar cómo se comporta la relación original dentro de subgrupos específicos, refinando el análisis.

---

## Pasos para realizar una tabla cruzada en SPSS

A continuación se describen los pasos operativos, tal como aparecen en el manual base, explicando su utilidad.

### Paso 1: Acceder al Menú de Tablas Cruzadas

![image](files/Users/jzhang/Desktop/Isolated.png)

La ruta para iniciar el análisis en el software es la siguiente:  
Ve al menú superior y selecciona **Analizar**.  
Elige la opción **Estadísticos descriptivos**.  
Haz clic en **Tablas cruzadas**.

*¿Qué ocurre aquí?* Se abre el cuadro de diálogo principal que permite construir la tabla, seleccionar estadísticos y personalizar la visualización.

### Paso 2: Configurar las Variables (Filas y Columnas)

Una vez abierta la ventana de configuración, deberás asignar tus variables:  
**Columnas:** Se recomienda colocar aquí la variable que tenga el menor número de categorías (por ejemplo, el *Género*, que suele tener dos: hombre y mujer).  
**Filas:** Se recomienda colocar la variable con un mayor número de categorías (por ejemplo, el *Estado Civil*, que puede incluir soltero, casado, viudo y divorciado).

*Consejo de interpretación:* Al poner la variable con menos categorías en columnas, la tabla resulta más compacta y fácil de leer, especialmente cuando se añaden porcentajes. La variable en filas suele representar el “perfil” que se quiere describir y la de columnas los “grupos de comparación”.

### Paso 3: Configurar los Porcentajes (Botón "Casillas")

Para que la tabla sea más informativa, es común añadir porcentajes:  
Haz clic en el botón **Casillas**.  
En el bloque de **Porcentajes**, puedes elegir:  

- **Fila:** El sistema calculará el porcentaje basado en el total de cada fila. Por ejemplo, de todos los solteros, qué porcentaje son mujeres y qué porcentaje son hombres.  
- **Columna:** El total del 100% se calculará verticalmente por cada columna.

*Importante:* También es posible solicitar el **porcentaje total**, que toma como base el total general de la tabla. Marcar los tres puede sobrecargar la salida; elige según tu objetivo.  
Haz clic en **Continuar** y luego en **Aceptar** para generar la tabla básica.

### Paso 4: Agregar Variables de Control (Uso de "Capas")

Si deseas analizar la relación entre más de dos variables, puedes utilizar la opción de **Capas**:  

- **Capa 1:** Puedes introducir una tercera variable (por ejemplo, si la persona cuenta con *auto propio*). Esto dividirá la tabla original en subsecciones según las categorías de esta nueva variable.  
- **Capas adicionales:** Si deseas profundizar aún más, puedes pulsar el botón **Siguiente** para añadir una “Capa 2” (por ejemplo, *tipo de vivienda*). Esto generará una tabla más compleja que cruza la información de todas las variables seleccionadas (ej. estado civil × género × auto × vivienda).

*Utilidad de las capas:* Permiten controlar el efecto de una tercera variable y observar si la relación original se mantiene, cambia o desaparece en cada subgrupo (análisis de interacción o de moderación incipiente).

### Paso 5: Interpretación de los Resultados (Lectura básica de la tabla)

Al observar la tabla resultante en el visor de resultados de SPSS:  

- **Frecuencias:** Verás el conteo directo de sujetos en cada cruce (ej. 44 mujeres solteras).  
- **Totales:** La tabla mostrará la sumatoria total por filas y columnas para facilitar el análisis de la muestra.  
- **Análisis por Capas:** Si usaste capas, la tabla se segmentará. Podrás ver, por ejemplo, cuántos solteros tienen auto y casa propia, desglosados por género.

---

## Cómo analizar e interpretar los números

La interpretación va más allá de leer casillas; se trata de comparar patrones. Sigue esta guía al mirar tu tabla cruzada:

### 1. Frecuencias absolutas
Indican el tamaño real de cada combinación. Son el punto de partida, pero no permiten comparar directamente grupos de diferente tamaño. Si en tu muestra hay 300 mujeres y 200 hombres, ver “30 mujeres practican deporte” y “20 hombres lo practican” no dice que la práctica sea igual; necesitas porcentajes.

### 2. Porcentajes: ¿Cuál elegir y cómo leerlos?

- **Porcentaje por fila (Row %):** Cada fila suma 100%. Responde a la pregunta: *“De todos los que pertenecen a esta categoría de fila, ¿cómo se distribuyen en las categorías de columna?”*  
  *Ejemplo:* De todos los solteros (fila), el 60% son mujeres y el 40% hombres. Útil cuando la variable fila es el perfil que quieres describir.

- **Porcentaje por columna (Column %):** Cada columna suma 100%. Responde a: *“Dentro de cada grupo de columna, ¿cómo se reparten las categorías de fila?”*  
  *Ejemplo:* Entre los hombres (columna), el 25% son solteros, el 50% casados, etc. Ideal cuando la variable columna es el grupo de comparación (por ejemplo, grupo control vs. experimental) y quieres ver la composición interna de cada uno.

- **Porcentaje total (% of Total):** Se calcula sobre el gran total. Responde a: *“¿Qué proporción de toda la muestra representa cada cruce?”* Sirve para ver el peso relativo de cada celda en el conjunto de datos.

*Recomendación práctica:* Si tu objetivo es comparar la distribución de la variable fila entre los grupos definidos por la variable columna, utiliza **porcentajes por columna**. Si quieres ver cómo se distribuye la variable columna dentro de cada perfil, usa **porcentajes por fila**.

### 3. Totales marginales
Los márgenes de la tabla (totales de fila y columna) son las frecuencias univariadas de cada variable por separado. Te ayudan a saber el tamaño base para los porcentajes y a detectar categorías con pocos casos, que pueden hacer los porcentajes poco fiables.

### 4. Interpretación de tablas con capas (control de terceras variables)

Cuando añades una variable de capa, SPSS produce una tabla separada para cada categoría de esa variable. El análisis consiste en comparar la relación original (sin capa) con las relaciones dentro de cada subgrupo.

- **Si la relación se mantiene similar en todas las capas:** la variable de control no modifica la asociación; la relación original es robusta.
- **Si la relación cambia de dirección o desaparece en un subgrupo:** estás frente a un efecto de interacción. Por ejemplo, la relación *“género y gusto por el café”* podría ser fuerte en menores de 30 años pero casi nula en mayores de 50. Esto te obligaría a reportar resultados segmentados.
- **Si la relación original se debilita en todas las capas:** podría ser que la variable de control explique en parte la asociación (posible variable mediadora o confusora), lo que requeriría análisis más avanzados.

---

## Análisis estadístico complementario: Prueba de Chi-cuadrado

La tabla cruzada describe la relación, pero no indica si esta es estadísticamente significativa. Para evaluarlo, desde el mismo cuadro de diálogo de **Tablas cruzadas**:

1. Haz clic en el botón **Estadísticos…**  
2. Marca la casilla **Chi-cuadrado** y pulsa **Continuar**.  
3. Al aceptar, SPSS añadirá la tabla *Pruebas de chi-cuadrado*.

En los resultados, fíjate en:

- **Chi-cuadrado de Pearson:** Valor del estadístico.  
- **Significación asintótica (bilateral) (valor p):** Si p < 0.05 (o el nivel de significación fijado), se rechaza la hipótesis de independencia; existe asociación significativa entre las variables.  
- **Atención a los supuestos:** Ninguna celda debe tener una frecuencia esperada menor que 5 en más del 20% de las casillas. Si eso ocurre, SPSS muestra una nota y deberías considerar usar la corrección de Yates (tablas 2×2) o el test exacto de Fisher.

*Interpretación:* Un valor p bajo indica que la distribución observada es poco probable si las variables fueran independientes, pero no mide la fuerza de la asociación. Para medir la fuerza puedes solicitar, en el mismo botón **Estadísticos**, el coeficiente **Phi y V de Cramer** o los coeficientes de contingencia.

---

## Conclusión

Generar una tabla cruzada en SPSS es sencillo, pero extraer conclusiones válidas requiere entender qué representan los números y elegir los porcentajes adecuados a tu pregunta de investigación. Comienza con las frecuencias, añade los porcentajes que te sirvan, interpreta comparando perfiles, y si quieres generalizar tus hallazgos más allá de la muestra, complementa con la prueba Chi-cuadrado y medidas de asociación. El uso de capas te permitirá profundizar y detectar patrones más sutiles que podrían pasar desapercibidos en un análisis bidimensional simple.