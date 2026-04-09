## RELATED en DAX

La función RELATED en DAX (Data Analysis Expressions) es una función que permite acceder a una tabla relacionada desde otra tabla en un modelo de datos. En otras palabras, permite recuperar valores de una tabla relacionada en función de una relación establecida entre dos tablas.

La sintaxis básica de la función RELATED es la siguiente:

```DAX
RELATED(tabla_relacionada[columna_relacionada])

```

Donde "tabla_relacionada" es el nombre de la tabla con la que se tiene una relación y "columna_relacionada" es el nombre de la columna en la que se basa la relación.

Un ejemplo sencillo de uso de la función RELATED podría ser el siguiente:

Supongamos que tenemos dos tablas en nuestro modelo de datos: "Ventas" y "Productos". La tabla "Ventas" tiene una relación con la tabla "Productos" a través de la columna "IDProducto". Si queremos agregar una nueva columna en la tabla "Ventas" que muestre el nombre del producto vendido, podemos utilizar la función RELATED de la siguiente manera:

```DAX
=RELATED(Productos[NombreProducto])

```

En este caso, la función RELATED recuperará el valor de la columna "NombreProducto" de la tabla "Productos" que esté relacionado con el valor de la columna "IDProducto" en la tabla "Ventas".

Otro ejemplo de uso de la función RELATED podría ser en la creación de medidas. Supongamos que queremos crear una medida que calcule el total de ventas por categoría de producto. Podríamos utilizar la función RELATED de la siguiente manera:

```DAX
TotalVentasPorCategoria = SUM(Ventas[Importe]) / RELATED(Productos[Categoria])

```


En este caso, la función RELATED nos permite acceder a la categoría de cada producto vendido en la tabla "Ventas" a través de la relación establecida con la tabla "Productos".

En resumen, la función RELATED es una herramienta muy útil en DAX para acceder a valores de una tabla relacionada en función de una relación establecida entre dos tablas. Se utiliza principalmente para crear nuevas columnas o medidas que dependen de valores de otras tablas relacionadas.


## SUMX en DAX


La función SUMX en DAX es una función que devuelve la suma de un valor calculado para cada fila de una tabla o expresión de tabla. En otras palabras, permite sumar los resultados de una expresión calculada para cada fila de una tabla.

La sintaxis básica de la función SUMX es la siguiente:

```DAX
SUMX(tabla, expresión)

```


Donde "tabla" es la tabla o expresión de tabla para la que se desea calcular la suma y "expresión" es la expresión que se desea calcular y sumar para cada fila de la tabla.

Un ejemplo sencillo de uso de la función SUMX podría ser el siguiente:

Supongamos que tenemos una tabla llamada "Ventas" con las columnas "Producto", "Cantidad" y "Precio". Si queremos calcular el total de ventas para cada producto, podemos utilizar la función SUMX de la siguiente manera:

```DAX
TotalVentasPorProducto = SUMX(Ventas, Ventas[Cantidad] * Ventas[Precio])

```


En este caso, la función SUMX calcula el producto de las columnas "Cantidad" y "Precio" para cada fila de la tabla "Ventas" y luego suma todos los resultados para obtener el total de ventas por producto.

Otro ejemplo de uso de la función SUMX podría ser en la creación de medidas. Supongamos que queremos crear una medida que calcule el promedio de ventas por día de la semana. Podríamos utilizar la función SUMX de la siguiente manera:


```DAX
PromedioVentasPorDia = AVERAGEX(GROUPBY(Ventas, Ventas[DiaSemana], "VentasPorDia", SUMX(CURRENTGROUP(), Ventas[Cantidad])), [VentasPorDia])

```


En este caso, la función SUMX se utiliza dentro de una expresión más compleja que agrupa las ventas por día de la semana y calcula la suma de las ventas para cada día de la semana. Luego, la función AVERAGEX calcula el promedio de ventas por día de la semana.


En resumen, la función SUMX es una herramienta muy útil en DAX para sumar los resultados de una expresión calculada para cada fila de una tabla. Se utiliza principalmente para crear medidas que dependen de cálculos complejos o agregaciones de valores en una tabla.


## Funciones de Inteligencia de Tiempo en DAX


Las funciones de inteligencia de tiempo en DAX son un conjunto de funciones que permiten trabajar con fechas y tiempos en un modelo de datos. Estas funciones se utilizan para realizar cálculos y análisis que involucran fechas, como por ejemplo, calcular el número de días entre dos fechas, encontrar el primer día del mes o del año, entre otros.

A continuación se presentan algunas de las funciones de inteligencia de tiempo más utilizadas en DAX:


| Función           | Sintaxis                                                 | Ejemplo                                                         | Casos de uso                                                                       |
| ------------------ | -------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| DATEDIFF           | DATEDIFF(fecha_inicial, fecha_final, tipo_de_diferencia) | DATEDIFF('Tabla'[FechaInicial], 'Tabla'[FechaFinal], DAY)       | Calcular la diferencia en días, meses o años entre dos fechas.                   |
| DATEADD            | DATEADD(fecha, cantidad, tipo_de_cantidad)               | DATEADD('Tabla'[FechaActual], 7, DAY)                           | Agregar o restar días, meses o años a una fecha.                                 |
| EOMONTH            | EOMONTH(fecha, cantidad_meses)                           | EOMONTH('Tabla'[Fecha], 0)                                      | Obtener el último día del mes de una fecha.                                      |
| CALENDAR           | CALENDAR(fecha_inicial, fecha_final)                     | CALENDAR(DATE(2022,1,1), DATE(2022,12,31))                      | Crear una tabla con una serie de fechas en un rango determinado.                   |
| TOTALYTD           | TOTALYTD(expresión, fecha, [calendario])                | TOTALYTD(SUM('Tabla'[Ventas]), 'Tabla'[Fecha], "1/1")           | Calcular el total acumulado desde el inicio del año fiscal hasta la fecha actual. |
| SAMEPERIODLASTYEAR | SAMEPERIODLASTYEAR(expresión, fecha, [calendario])      | SAMEPERIODLASTYEAR(SUM('Tabla'[Ventas]), 'Tabla'[Fecha], "1/1") | Calcular el valor de la expresión para el mismo período del año anterior.       |
| PREVIOUSMONTH      | PREVIOUSMONTH(fecha)                                     | PREVIOUSMONTH('Tabla'[Fecha])                                   | Obtener el mes anterior a una fecha determinada.                                   |
| NEXTDAY            | NEXTDAY(fecha)                                           | NEXTDAY('Tabla'[Fecha])                                         | Obtener el día siguiente a una fecha determinada.                                 |
| DATESYTD           | DATESYTD(fecha, [calendario])                            | DATESYTD('Tabla'[Fecha], "1/1")                                 | Obtener las fechas que corresponden al año fiscal actual hasta la fecha actual.   |



Estas son solo algunas de las funciones de inteligencia de tiempo que se pueden utilizar en DAX. Cada una tiene su propia sintaxis, ejemplo y casos de uso específicos, por lo que es importante leer la documentación de Microsoft para aprender cómo utilizarlas de manera efectiva.


En resumen, las funciones de inteligencia de tiempo en DAX son muy útiles para trabajar con fechas y tiempos en un modelo de datos. Permiten realizar cálculos y análisis complejos que involucran fechas y son ampliamente utilizadas en la creación de medidas y cálculos de tiempo en los informes y paneles de control.


## SAMEPERIODLASTYEAR en DAX


La función SAMEPERIODLASTYEAR en DAX es una función de inteligencia de tiempo que devuelve el valor de una expresión para el mismo período del año anterior. Es útil para comparar el desempeño o las tendencias de los datos en el mismo período de tiempo del año anterior.

La sintaxis de la función SAMEPERIODLASTYEAR es la siguiente:


```DAX
SAMEPERIODLASTYEAR(expresión, fecha, [calendario])

```


Donde:

* expresión: la expresión que se desea evaluar para el mismo período del año anterior.
* fecha: la columna de fecha que se utilizará para determinar el período.
* [calendario]: un parámetro opcional que especifica el calendario utilizado para determinar el año fiscal.

El parámetro [calendario] se utiliza para especificar el calendario utilizado para el cálculo. Si no se especifica ningún calendario, se utiliza el calendario predeterminado del modelo.

A continuación, se presenta un ejemplo de cómo se utiliza la función SAMEPERIODLASTYEAR:

Supongamos que tenemos una tabla de ventas con una columna de fecha y una columna de ventas. Queremos calcular las ventas del mismo período del año anterior para compararlas con las ventas actuales. La fórmula sería la siguiente:


```DAX
SAMEPERIODLASTYEAR(SUM('TablaVentas'[Ventas]), 'TablaVentas'[Fecha])
 
```


La función SAMEPERIODLASTYEAR evalúa la expresión SUM('TablaVentas'[Ventas]) para el mismo período del año anterior, utilizando la columna 'TablaVentas'[Fecha] para determinar el período.

La función SAMEPERIODLASTYEAR es útil en situaciones en las que se desea comparar el desempeño de un negocio en el mismo período del año anterior. Por ejemplo, un minorista puede utilizar esta función para comparar las ventas de un mes determinado con las ventas del mismo mes del año anterior para evaluar el crecimiento o la disminución de las ventas.


## ALL en DAX


La función ALL en DAX se utiliza para eliminar los filtros existentes en una tabla o en una columna y mostrar todos los valores. La función ALL puede ser muy útil en muchas situaciones, especialmente cuando se desea realizar cálculos con todos los datos disponibles.

La sintaxis de la función ALL es la siguiente:


```DAX
ALL(tabla o columna)

```


Donde:

* tabla o columna: la tabla o la columna para la que se desean eliminar los filtros.

A continuación, se presenta un ejemplo de cómo se utiliza la función ALL:

Supongamos que tenemos una tabla de ventas con una columna de fecha, una columna de producto y una columna de ventas. Queremos calcular las ventas totales de todos los productos, sin importar la fecha. La fórmula sería la siguiente:


```DAX
CALCULATE(SUM('TablaVentas'[Ventas]), ALL('TablaVentas'[Producto]))

```


La función ALL elimina el filtro en la columna 'TablaVentas'[Producto] y muestra todas las ventas, independientemente del producto.

La función ALL también puede utilizarse en combinación con otras funciones, como FILTER y CALCULATETABLE, para realizar cálculos más complejos.

Un caso de uso común de la función ALL es en la creación de medidas que calculan la diferencia entre los valores de dos periodos de tiempo. Por ejemplo, se puede utilizar la función ALL para calcular la variación de las ventas entre dos años, eliminando el filtro de la columna de año y comparando las ventas totales de ambos años.

En resumen, la función ALL en DAX es útil cuando se desea eliminar los filtros de una tabla o una columna y realizar cálculos con todos los valores disponibles. Se puede utilizar en una variedad de situaciones para crear medidas más complejas y útiles.


## FILTER en DAX


La función FILTER en DAX se utiliza para filtrar una tabla o una columna en función de una condición especificada. La función FILTER devuelve una tabla filtrada que cumple con la condición especificada.

La sintaxis de la función FILTER es la siguiente:


```DAX
FILTER(tabla, condición)

```


Donde:

* tabla: la tabla que se va a filtrar.
* condición: la condición que se debe cumplir para que se incluya una fila en la tabla resultante.

A continuación, se presenta un ejemplo de cómo se utiliza la función FILTER:

Supongamos que tenemos una tabla de ventas con una columna de fecha, una columna de producto y una columna de ventas. Queremos filtrar la tabla para mostrar solo las ventas del producto A. La fórmula sería la siguiente:


```DAX
FILTER('TablaVentas', 'TablaVentas'[Producto] = "A")

```


La función FILTER devuelve una tabla filtrada que contiene solo las filas en las que el valor de la columna 'TablaVentas'[Producto] es "A".

La función FILTER es útil en situaciones en las que se desea filtrar una tabla o una columna en función de una condición específica. Por ejemplo, se puede utilizar la función FILTER para filtrar una tabla de ventas y mostrar solo las ventas de un determinado producto, de una región específica, o en un rango de fechas específico.

La función FILTER también puede utilizarse en combinación con otras funciones, como CALCULATE y SUMX, para realizar cálculos más complejos.

En resumen, la función FILTER en DAX es útil para filtrar una tabla o una columna en función de una condición específica, lo que permite realizar cálculos más precisos y útiles. Es una función importante en el lenguaje DAX y se utiliza en una amplia variedad de casos de uso.


## RANKX en DAX


La función RANKX en DAX se utiliza para asignar un rango a cada fila de una tabla en función de un valor específico. El rango se asigna en orden descendente o ascendente en función del valor especificado.

La sintaxis de la función RANKX es la siguiente:

```DAX
RANKX(tabla, expresión, [valor_ordenamiento], [orden])

```

Donde:

* tabla: la tabla a la que se aplicará la función RANKX.
* expresión: la expresión que se evaluará para asignar el rango.
* [valor_ordenamiento]: el valor por el cual se ordenará la tabla. Si no se especifica, se utilizará la expresión.
* [orden]: el orden en el que se ordenará la tabla. Los valores válidos son "ASC" (ascendente) o "DESC" (descendente). Si no se especifica, se utilizará "DESC".

A continuación, se presenta un ejemplo de cómo se utiliza la función RANKX:

Supongamos que tenemos una tabla de ventas con una columna de fecha, una columna de producto y una columna de ventas. Queremos asignar un rango a cada producto en función de las ventas. La fórmula sería la siguiente:


```DAX
RANKX('TablaVentas', SUM('TablaVentas'[Ventas]), , DESC)

```


La función RANKX devuelve un valor de rango para cada fila de la tabla, basado en la suma de ventas. El valor de rango se asigna en orden descendente.

La función RANKX es útil en situaciones en las que se desea asignar un rango a cada fila de una tabla en función de un valor específico. Por ejemplo, se puede utilizar la función RANKX para asignar un rango a cada producto en función de las ventas, o para asignar un rango a cada empleado en función de su rendimiento.

La función RANKX también puede utilizarse en combinación con otras funciones, como FILTER y CALCULATE, para realizar cálculos más complejos.

En resumen, la función RANKX en DAX es útil para asignar un rango a cada fila de una tabla en función de un valor específico. Se utiliza en una variedad de situaciones para crear medidas más complejas y útiles
