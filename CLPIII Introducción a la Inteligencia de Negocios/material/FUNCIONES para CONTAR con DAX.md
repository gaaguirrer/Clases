# ¿Qué es DAX para Power BI?

DAX (Data Analysis Expressions) es un lenguaje de fórmulas utilizado en Power BI (y en otras herramientas de Microsoft como Excel y SQL Server Analysis Services) para realizar cálculos y análisis de datos. DAX se utiliza para crear medidas, columnas calculadas y tablas calculadas en Power BI.

DAX es un lenguaje funcional y formulaico que permite al usuario crear cálculos complejos y realizar análisis de datos avanzados en Power BI. Algunas de las funciones que se pueden realizar con DAX incluyen:

* Realizar cálculos matemáticos y estadísticos
* Filtrar datos según ciertos criterios
* Realizar búsquedas y comparaciones de texto
* Realizar cálculos de fechas y horas
* Realizar cálculos de tiempo de ejecución

DAX es especialmente útil para realizar análisis de negocios, ya que permite al usuario crear medidas y columnas calculadas que se pueden utilizar en los informes de Power BI para realizar análisis y tomar decisiones informadas basadas en los datos.

En resumen, DAX es un lenguaje de fórmulas utilizado en Power BI para realizar cálculos y análisis de datos avanzados.

En Power BI, las columnas y las medidas son dos tipos diferentes de elementos que se pueden crear en el modelo de datos.

* **Columnas:** Una columna es una entidad en el modelo de datos que contiene un conjunto de valores que se repiten en cada fila de la tabla. Las columnas se crean a partir de los datos fuente y se pueden agregar a tablas existentes o crear nuevas tablas en el modelo. Las columnas pueden ser de diferentes tipos de datos como texto, numérico, fecha, booleano, etc. Las columnas se utilizan en las visualizaciones como categorías o valores.
* **Medidas:** Una medida es una expresión que realiza un cálculo sobre una columna o un conjunto de columnas. Las medidas se crean utilizando funciones DAX y se pueden utilizar en visualizaciones para realizar cálculos en tiempo real. Las medidas pueden calcular totales, promedios, porcentajes, ratios, etc. Las medidas no contienen datos reales en sí mismas, sino que calculan el resultado en función de los datos de las columnas.

La principal diferencia entre las columnas y las medidas es que las columnas son datos reales almacenados en el modelo de datos, mientras que las medidas son cálculos que se realizan en tiempo real basados en los datos de las columnas. Las medidas se utilizan para agregar, analizar y comparar datos, mientras que las columnas se utilizan para categorizar, filtrar y agrupar datos.

En resumen, las columnas contienen datos reales y las medidas realizan cálculos sobre esos datos para obtener información más detallada y útil.

## OPERADORES en DAX

| Operador | Descripción                                               | Ejemplo                                        |
| -------- | ---------------------------------------------------------- | ---------------------------------------------- |
| +        | Suma                                                       | `2 + 3`devuelve `5`                        |
| -        | Resta                                                      | `5 - 2`devuelve `3`                        |
| *        | Multiplicación                                            | `2 * 3`devuelve `6`                        |
| /        | División                                                  | `6 / 2`devuelve `3`                        |
| ^ o **   | Exponenciación                                            | `2 ^ 3`devuelve `8`                        |
| &        | Concatenación de texto                                    | `"Hola" & " mundo"`devuelve `"Hola mundo"` |
| &&       | AND lógico                                                | `TRUE() && FALSE()`devuelve `FALSE()`      |
|          |                                                            | o                                              |
| =        | Igualdad                                                   | `2 = 2`devuelve `TRUE()`                   |
| <> o !=  | Desigualdad                                                | `2 <> 3`devuelve `TRUE()`                  |
| <        | Menor que                                                  | `2 < 3`devuelve `TRUE()`                   |
| <=       | Menor o igual que                                          | `2 <= 2`devuelve `TRUE()`                  |
| >        | Mayor que                                                  | `3 > 2`devuelve `TRUE()`                   |
| >=       | Mayor o igual que                                          | `3 >= 3`devuelve `TRUE()`                  |
| IN       | Comprueba si un valor se encuentra en una lista de valores | `2 IN {1, 2, 3}`devuelve `TRUE()`          |
| NOT      | Negación lógica                                          | `NOT(TRUE())`devuelve `FALSE()`            |

Estos operadores se pueden utilizar en combinación con funciones y referencias de columnas y medidas en DAX para realizar cálculos y análisis de datos.

## FUNCIONES de fecha en DAX

| Función | Descripción                                                                                                     | Sintaxis                                                     | Ejemplo                                                                                                                                                     |
| -------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DATE     | Devuelve una fecha creada a partir de los argumentos de año, mes y día.                                        | DATE(año, mes, día)                                        | DATE(2022, 3, 24) devuelve 24 de marzo de 2022.                                                                                                             |
| NOW      | Devuelve la fecha y hora actuales.                                                                               | NOW()                                                        | NOW() devuelve la fecha y hora actuales.                                                                                                                    |
| TODAY    | Devuelve la fecha actual.                                                                                        | TODAY()                                                      | TODAY() devuelve la fecha actual.                                                                                                                           |
| YEAR     | Devuelve el año de una fecha.                                                                                   | YEAR(fecha)                                                  | YEAR('2022-03-24') devuelve 2022.                                                                                                                           |
| MONTH    | Devuelve el mes de una fecha.                                                                                    | MONTH(fecha)                                                 | MONTH('2022-03-24') devuelve 3.                                                                                                                             |
| DAY      | Devuelve el día de una fecha.                                                                                   | DAY(fecha)                                                   | DAY('2022-03-24') devuelve 24.                                                                                                                              |
| HOUR     | Devuelve la hora de una fecha y hora.                                                                            | HOUR(fecha_hora)                                             | HOUR('2022-03-24 15:30:45') devuelve 15.                                                                                                                    |
| MINUTE   | Devuelve el minuto de una fecha y hora.                                                                          | MINUTE(fecha_hora)                                           | MINUTE('2022-03-24 15:30:45') devuelve 30.                                                                                                                  |
| SECOND   | Devuelve el segundo de una fecha y hora.                                                                         | SECOND(fecha_hora)                                           | SECOND('2022-03-24 15:30:45') devuelve 45.                                                                                                                  |
| WEEKDAY  | Devuelve el número de día de la semana para una fecha.                                                         | WEEKDAY(fecha, tipo_inicio_semana)                           | WEEKDAY('2022-03-24', 2) devuelve 5, ya que el 24 de marzo de 2022 es un jueves (siendo el tipo de inicio de semana = 2, es decir, lunes = 1).              |
| WEEKNUM  | Devuelve el número de semana para una fecha.                                                                    | WEEKNUM(fecha, tipo_inicio_semana)                           | WEEKNUM('2022-03-24', 2) devuelve 12, ya que el 24 de marzo de 2022 es la semana 12 del año (siendo el tipo de inicio de semana = 2, es decir, lunes = 1). |
| FORMAT   | Devuelve una cadena de texto formateada de acuerdo con el formato especificado.                                  | FORMAT(valor, formato)                                       | FORMAT(123456.789, "#,##0.00") devuelve "123,456.79".                                                                                                       |
| EOMONTH  | Devuelve la fecha del último día del mes que se encuentra a un número de meses antes o después de una fecha. | EOMONTH(fecha, meses)                                        | EOMONTH('2022-03-24', 1) devuelve '2022-04-30'.                                                                                                             |
| DATEDIFF | Devuelve la diferencia entre dos fechas en la unidad de tiempo especificada.                                     | DATEDIFF(fecha_inicio, fecha_fin, unidad_tiempo)             | DATEDIFF('2022-03-24', '2022-                                                                                                                               |
| TIME     | Crea una hora a partir de sus componentes.                                                                       | TIME(`<hora>`, `<minuto>`, `<segundo>`)                | TIME(14, 30, 0) devuelve '14:30:00'                                                                                                                         |
| NOWUTC   | Devuelve la fecha y hora UTC actual.                                                                             | NOWUTC()                                                     | NOWUTC() devuelve '2023-03-24 19:22:45'                                                                                                                     |
| EOMONTH  | Devuelve el último día del mes para la fecha proporcionada.                                                    | EOMONTH(`<fecha>`, `<meses>`)                            | EOMONTH('2022-01-15', 2) devuelve '2022-03-31'                                                                                                              |
| DATEDIFF | Devuelve la diferencia entre dos fechas.                                                                         | DATEDIFF(`<unidad de tiempo>`, `<fecha1>`, `<fecha2>`) | DATEDIFF(DAY, '2022-01-15', '2022-01-20') devuelve 5                                                                                                        |
| DATEADD  | Agrega una cantidad específica de tiempo a una fecha.                                                           | DATEADD(`<fecha>`, <número>, `<unidad de tiempo>`)      | DATEADD('2022-01-15', 2, YEAR) devuelve '2024-01-15'                                                                                                        |
| CALENDAR | Crea una tabla con un rango de fechas.                                                                           | CALENDAR(`<fecha inicial>`, `<fecha final>`)             | CALENDAR('2022-01-01', '2022-12-31') devuelve una tabla con todas las fechas del año 2022.                                                                 |

## FUNCIÓN IF()  con DAX

La función IF() en DAX es una función condicional que devuelve un valor si se cumple una condición y otro valor si no se cumple. Aquí están algunos detalles y ejemplos:

| Función | Descripción                                                                | Sintaxis                                           | Ejemplo                           |
| -------- | --------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------- |
| IF()     | Devuelve un valor si se cumple una condición y otro valor si no se cumple. | IF(condición, valor_si_verdadero, valor_si_falso) | IF([Ventas]>1000, "Alto", "Bajo") |

La sintaxis de la función IF() consta de tres argumentos: la condición, el valor a devolver si la condición es verdadera y el valor a devolver si la condición es falsa. Si la condición se cumple, la función devuelve el valor_si_verdadero, de lo contrario, devuelve el valor_si_falso.

En el ejemplo anterior, la función IF() evalúa la columna "Ventas" y devuelve "Alto" si la venta es superior a 1000, de lo contrario, devuelve "Bajo".

La función IF() también se puede utilizar con otras funciones DAX, como SUM(), AVERAGE(), MAX(), MIN(), entre otras. Por ejemplo:

| Función       | Descripción                                                                             | Sintaxis                                   | Ejemplo                                           |
| -------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------- |
| IF() con SUM() | Devuelve la suma de una columna si se cumple una condición y otra suma si no se cumple. | IF(condición, SUM(columna), SUM(columna)) | IF([Ventas]>1000, SUM([Ventas]), SUM([Ventas])/2) |

En el ejemplo anterior, la función IF() evalúa la columna "Ventas" y devuelve la suma de "Ventas" si es superior a 1000, de lo contrario, devuelve la mitad de la suma de "Ventas".

En resumen, la función IF() es una función condicional en DAX que se utiliza para evaluar una condición y devolver un valor en función del resultado de esa condición. La función IF() también se puede combinar con otras funciones DAX para realizar cálculos más complejos en Power BI

## FUNCIONES para CONTAR con DAX

| Función      | Descripción                                                                                                      | Ejemplo                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| COUNT         | Cuenta el número de filas que contienen valores numéricos en una columna determinada                            | COUNT(Table1[Column1])                            |
| COUNTA        | Cuenta el número de filas que contienen cualquier valor (texto, número, fecha, etc.) en una columna determinada | COUNTA(Table1[Column1])                           |
| COUNTBLANK    | Cuenta el número de filas en una columna determinada que están en blanco                                        | COUNTBLANK(Table1[Column1])                       |
| COUNTROWS     | Cuenta el número total de filas en una tabla o en una tabla resultante de una expresión                         | COUNTROWS(Table1)                                 |
| DISTINCTCOUNT | Cuenta el número de valores distintos en una columna determinada                                                 | DISTINCTCOUNT(Table1[Column1])                    |
| COUNTX        | Cuenta el número de filas en una tabla filtrada que cumplen una condición determinada                           | COUNTX(FILTER(Table1, [Column1] > 10), [Column2]) |

## FUNCIONES de TEXTO  con DAX

A continuación se enumeran algunas funciones de texto comunes en DAX, con una breve descripción, comparación, explicación de la sintaxis y ejemplos:

| Función    | Descripción                                                                                                  | Comparación                                | Sintaxis                                                             | Ejemplo                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------- |
| CONCATENATE | Une dos o más cadenas de texto.                                                                              | Equivalente a "&" operador.                 | CONCATENATE (cadena1, cadena2, ..., cadenaN)                         | CONCATENATE ("Hola", " ", "mundo") devuelve "Hola mundo"            |
| LEFT        | Devuelve los caracteres de la izquierda de una cadena de texto.                                               | Equivalente a la función Excel LEFT.       | LEFT (cadena, [num_caracteres])                                      | LEFT ("Hola mundo", 4) devuelve "Hola"                              |
| RIGHT       | Devuelve los caracteres de la derecha de una cadena de texto.                                                 | Equivalente a la función Excel RIGHT.      | RIGHT (cadena, [num_caracteres])                                     | RIGHT ("Hola mundo", 5) devuelve "mundo"                            |
| MID         | Devuelve una cantidad especificada de caracteres de una cadena de texto, comenzando en un punto especificado. | Equivalente a la función Excel MID.        | MID (cadena, start_num, [num_caracteres])                            | MID ("Hola mundo", 5, 5) devuelve "mundo"                           |
| SUBSTITUTE  | Reemplaza todas las apariciones de una cadena de texto con otra cadena de texto.                              | Equivalente a la función Excel SUBSTITUTE. | SUBSTITUTE (cadena, cadena_antigua, cadena_nueva, [núm_ocurrencia]) | SUBSTITUTE ("Hola mundo", "mundo", "amigos") devuelve "Hola amigos" |
| UPPER       | Convierte todos los caracteres de una cadena de texto en mayúsculas.                                         | Equivalente a la función Excel UPPER.      | UPPER (cadena)                                                       | UPPER ("Hola mundo") devuelve "HOLA MUNDO"                          |
| LOWER       | Convierte todos los caracteres de una cadena de texto en minúsculas.                                         | Equivalente a la función Excel LOWER.      | LOWER (cadena)                                                       | LOWER ("Hola MUNDO") devuelve "hola mundo"                          |

Estas funciones se pueden utilizar en combinación con otras funciones DAX para realizar operaciones más complejas en cadenas de texto. Por ejemplo, para contar el número de caracteres en una cadena de texto, se puede utilizar la función LEN:

| Función | Descripción                                 | Sintaxis     | Ejemplo                        |
| -------- | -------------------------------------------- | ------------ | ------------------------------ |
| LEN      | Devuelve la longitud de una cadena de texto. | LEN (cadena) | LEN ("Hola mundo") devuelve 11 |

Para utilizar estas funciones en una tabla de DAX, se pueden crear medidas que apliquen estas funciones a una columna específica en la tabla. Por ejemplo, para contar el número de caracteres en la columna "Nombre" de la tabla "Clientes", se puede utilizar la siguiente medida:

```DAX
LongitudNombre = LEN(Clientes[Nombre])
```

## FUNCIÓN CALCULATE()  con DAX

La función CALCULATE es una de las funciones más poderosas y útiles en DAX. Permite cambiar el contexto de evaluación de una expresión, lo que significa que puede aplicar filtros y condiciones específicas para calcular los resultados que necesita.

La sintaxis básica de la función CALCULATE es la siguiente:

```DAX
CALCULATE(<expresión>, <filtro1>, <filtro2>, ...)
```

La expresión es la medida o columna que se quiere calcular, mientras que los filtros son las condiciones que se quieren aplicar para modificar el contexto de evaluación.

A continuación, se presentan algunas funciones que se pueden usar en combinación con CALCULATE para lograr diferentes resultados:

| Función    | Descripción                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------- |
| SUMX()      | Devuelve la suma de una expresión evaluada para cada fila de una tabla o conjunto de valores.     |
| AVERAGE()   | Devuelve el promedio de una expresión evaluada para cada fila de una tabla o conjunto de valores. |
| COUNTROWS() | Devuelve el número de filas en una tabla.                                                         |
| FILTER()    | Devuelve una tabla filtrada según una o varias condiciones.                                       |
| ALL()       | Elimina uno o varios filtros del contexto de evaluación.                                          |

A continuación, se presenta un ejemplo de cómo se puede usar la función CALCULATE para calcular la cantidad total de ventas en una tienda en un mes determinado, pero solo para las ventas que superan un valor mínimo:

```DAX
Total Ventas con Filtro :=
CALCULATE(
    SUM(Sales[Amount]),
    Sales[Store] = "Tienda A",
    Sales[Month] = "Enero",
    Sales[Amount] > 100
)

```

En este ejemplo, la expresión es la suma de las ventas, mientras que los filtros se aplican a la tienda, el mes y el valor mínimo. La función CALCULATE evalúa la expresión solo para las ventas que cumplen con los filtros especificados, lo que resulta en el total de ventas con el filtro aplicado.

En resumen, la función CALCULATE es esencial para realizar cálculos avanzados en DAX, ya que permite aplicar filtros y condiciones específicas para calcular resultados precisos.


# FUNCIÓN RELATED Extrae CAMPOS RELACIONADOS

La función RELATED es una función de DAX que se utiliza para extraer valores de una tabla relacionada. Esta función toma como argumento el nombre de la tabla relacionada y el nombre del campo que se desea recuperar.

La función RELATED es útil cuando se trabaja con múltiples tablas en Power BI, ya que permite extraer datos de una tabla relacionada sin tener que fusionar las tablas.

A continuación se presenta una tabla que agrupa algunas de las funciones más utilizadas en conjunto con la función RELATED:


| Función     | Descripción                                     | Sintaxis                                                      | Ejemplo                                   |
| ------------ | ------------------------------------------------ | ------------------------------------------------------------- | ----------------------------------------- |
| RELATED      | Extrae valores de una tabla relacionada          | RELATED(tabla_relacionada[campo_relacionado])                 | RELATED(orders[customer_id])              |
| RELATEDTABLE | Retorna una tabla relacionada                    | RELATEDTABLE(tabla_relacionada)                               | RELATEDTABLE(orders)                      |
| CROSSFILTER  | Establece la dirección de una relación cruzada | CROSSFILTER(tabla_relacionada[campo_relacionado], dirección) | CROSSFILTER(customers[customer_id], BOTH) |
| FILTER       | Filtra los resultados de una tabla               | FILTER(tabla, condición)                                     | FILTER(products, products[price] > 100)   |


Un ejemplo de uso de la función RELATED podría ser el siguiente: si tenemos dos tablas, "orders" y "customers", relacionadas por el campo "customer_id", podríamos utilizar la función RELATED para extraer el nombre del cliente asociado a cada pedido en la tabla "orders". La fórmula sería la siguiente:

```DAX
=RELATED(customers[name])

```


Esta fórmula extraerá el nombre del cliente asociado al pedido actual en la tabla "orders".


j
