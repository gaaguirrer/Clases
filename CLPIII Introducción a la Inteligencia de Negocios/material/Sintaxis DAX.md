# Sintaxis DAX

---

## Requisitos de la sintaxis

Una fórmula DAX siempre comienza con un signo igual (=). Después del signo igual, se puede proporcionar cualquier expresión que se evalúe como un valor escalar o una que se pueda convertir en un valor escalar. que incluyen la siguiente información:

* Una constante escalar o expresión que usa un operador escalar (+,-,*,/,>=,...,&&, ...)
* Referencias a columnas o tablas. El lenguaje DAX siempre usa tablas y columnas como entradas a funciones, nunca una matriz o un conjunto arbitrario de valores.
* Operadores, constantes y valores proporcionados como parte de una expresión.
* El resultado de una función y sus argumentos necesarios. Algunas funciones DAX devuelven una tabla en lugar de un valor escalar y se deben ajustar en una función que evalúa la tabla y devuelve un valor escalar. A menos que la tabla sea una tabla de una sola fila, se trata como un valor escalar.
  La mayoría de las funciones DAX requieren uno o más argumentos, que pueden incluir tablas, columnas, expresiones y valores. Sin embargo, algunas funciones, como PI, no requieren ningún argumento, pero siempre requieren paréntesis para indicar el argumento NULL. Por ejemplo, siempre se debe escribir PI() en lugar de PI. También se pueden anidar funciones dentro de otras funciones.
* Expresiones. Una expresión puede contener alguno de los elementos siguientes o todos ellos: operadores, constantes o referencias a columnas.

Por ejemplo, todas las fórmulas siguientes son válidas.

| Fórmula                              | Resultado                                                                                                                                                                                                                         |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| = 3                                   | 3                                                                                                                                                                                                                                 |
| = "**Sales** "                  | **Sales**                                                                                                                                                                                                                   |
| = "Sales"[Importe]                    | Si utiliza esta fórmula dentro de la tabla Sales, obtendrá el valor de la columna Importe en la tabla Sales de la fila actual.                                                                                                  |
| = (0,03 *[Importe])``=0.03 * [Amount] | Tres por ciento del valor de la columna Importe de la tabla actual.``Aunque esta fórmula se puede usar para calcular un porcentaje, el resultado no se muestra como un porcentaje a menos que se aplique el formato en la tabla. |
| = PI()                                | Valor de la constante pi.                                                                                                                                                                                                         |

Las fórmulas pueden comportarse de forma diferente en función de cómo se utilicen. Siempre debe tener en cuenta el contexto y el modo en que los datos que se usan en la fórmula están relacionados con otros datos que podrían utilizarse en el cálculo.

## Requisitos de nomenclatura

A menudo, un modelo de datos contiene varias tablas. Las tablas y sus columnas, de forma conjunta, componen una base de datos almacenada en el motor de análisis en memoria (VertiPaq). En esa base de datos, todas las tablas deben tener nombres únicos. Los nombres de las columnas también deben ser únicos en cada tabla. Los nombres de objeto  *no distinguen mayúsculas de minúsculas* ; por ejemplo, los nombres **SALES** y **Sales** representarían la misma tabla.

Cada columna y medida que se agregan a un modelo de datos existente deben pertenecer a una tabla específica. La tabla que contiene la columna se especifica implícitamente, cuando se crea una columna calculada en una tabla, o explícitamente, cuando se crea una medida y se especifica el nombre de la tabla donde se debe almacenar la definición de la medida.

Cuando se usa una tabla o una columna como entrada para una función, generalmente se debe *calificar* el nombre de la columna. El nombre *completo* de una columna es el nombre de la tabla, seguido del nombre de la columna entre corchetes: por ejemplo, 'Ventas de EE. UU.'[Productos]. Siempre se requiere un nombre completo cuando se hace referencia a una columna en los contextos siguientes:

* Como argumento de la función, VALUES
* Como argumento de la función, ALL o EXCEPT
* En un argumento de filtro para las funciones, CALCULATE o CALCULATETABLE
* Como argumento de la función, RELATEDTABLE
* Como argumento para cualquier función de inteligencia de tiempo

Un nombre de columna *incompleto* es simplemente el nombre de la columna, entre corchetes: por ejemplo, [Importe de ventas]. Por ejemplo, si se hace referencia a un valor escalar de la misma fila de la tabla actual, se puede usar el nombre de la columna no completo.

Si el nombre de una tabla contiene espacios, palabras clave reservadas o caracteres no permitidos, deberá incluir el nombre de la tabla entre comillas simples. También deberá escribir los nombres de tabla entre comillas si el nombre contiene algún carácter fuera del rango de caracteres alfanuméricos ANSI, independientemente de si la configuración regional es compatible con el conjunto de caracteres o no. Por ejemplo, si abre un libro que contiene nombres de tablas escritos en caracteres cirílicos, como "Таблица", el nombre de la tabla debe ir entre comillas, aunque no contenga espacios.

> Nota
>
> Para facilitar la entrada de los nombres completos de las columnas, use la característica AutoComplete en el editor de fórmulas.

#### Tablas

* Los nombres de tabla son necesarios siempre que la columna sea de una tabla distinta de la actual. Los nombres de tabla deben ser únicos en la base de datos.
* Los nombres de tabla deben ir entre comillas simples si contienen espacios, otros caracteres especiales o cualquier carácter alfanumérico que no sea el inglés.

#### Medidas

* Los nombres de medida siempre deben ir entre corchetes.
* Los nombres de medida pueden contener espacios.
* Cada nombre de medida debe ser único en el modelo. Por lo tanto, el nombre de la tabla es opcional delante de un nombre de medida cuando se hace referencia a una medida existente. Sin embargo, cuando se crea una medida, siempre se debe especificar una tabla en la que se almacenará la definición de la medida.

#### Columnas

Los nombres de columna deben ser únicos en el contexto de una tabla. Sin embargo, varias tablas pueden tener columnas con los mismos nombres (la desambiguación viene con el nombre de la tabla).

En general, se puede hacer referencia a las columnas sin hacer referencia a la tabla base a la que pertenecen, excepto cuando pueda haber un conflicto de nombres para resolver o con ciertas funciones que requieren que los nombres de columna estén completos.

#### Palabras clave reservadas

Si el nombre que se utiliza para una tabla es el mismo que el de una palabra clave reservada de Analysis Services, se genera un error y se debe cambiar el nombre de la tabla. Sin embargo, puede utilizar palabras clave en nombres de objetos si el nombre del objeto está entre corchetes (en las columnas) o con comillas (en las tablas).

> Nota
>
> Las comillas se pueden representar con varios caracteres diferentes, en función de la aplicación. Si se pegan fórmulas de un documento o una página web externos, asegúrese de comprobar el código ASCII del carácter que se usa para las comillas de apertura y cierre, con el fin de garantizar que son iguales. De lo contrario, puede que DAX no reconozca los símbolos como comillas, lo que haría que la referencia no fuera válida.

#### Caracteres especiales

Los caracteres y tipos de caracteres siguientes no son válidos en los nombres de tablas, columnas o medidas:

* Espacios iniciales o finales; a menos que los espacios se incluyan entre delimitadores de nombre, corchetes o apóstrofes únicos.
* Caracteres de control
* Los caracteres siguientes no son válidos en los nombres de objetos:
  .,;':/\*|?&%$!+=()[]{}<>

#### Ejemplos de nombres de objeto

En la tabla siguiente se muestran ejemplos de algunos nombres de objeto:

| Tipos de objeto                           | Ejemplos                           | Comentario                                                                                                                                                                                                                                                                                    |
| ----------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre de tabla                           | **Sales**                    | Si el nombre de la tabla no contiene espacios ni otros caracteres especiales, no es necesario que el nombre se incluya entre comillas.                                                                                                                                                        |
| Nombre de tabla                           | **"Canada Sales"**           | Si el nombre contiene espacios, tabulaciones u otros caracteres especiales, incluya el nombre entre comillas simples.                                                                                                                                                                         |
| Nombre completo de la columna             | **Ventas[Importe]**          | El nombre de la tabla precede al nombre de la columna y el nombre de la columna se incluye entre corchetes.                                                                                                                                                                                   |
| Nombre completo de la medida              | **Ventas[Beneficio]**        | El nombre de la tabla precede al nombre de la medida y el nombre de la columna se incluye entre corchetes. En determinados contextos, siempre es necesario un nombre completo.                                                                                                                |
| Nombre de columna no completo             | **[Importe]**                | El nombre no completo es simplemente el nombre de la columna, entre corchetes. Entre los contextos en los que se puede usar el nombre no completo se incluyen las fórmulas de una columna calculada en la misma tabla o en una función de agregación que está buscando en la misma tabla. |
| Columna completa de la tabla con espacios | **"Canada Sales"[Cantidad]** | El nombre de la tabla contiene espacios, por lo que debe ir entre comillas simples.                                                                                                                                                                                                           |

### Otras restricciones

La sintaxis necesaria para cada función y el tipo de operación que puede realizar varían en gran medida dependiendo de la función. Pero, por lo general, las reglas siguientes se aplican a todas las fórmulas y expresiones:

* Las fórmulas y expresiones DAX no pueden modificar o insertar valores individuales en las tablas.
* No se pueden crear filas calculadas con DAX. Solo se pueden crear medidas y columnas calculadas.
* Al definir columnas calculadas, se pueden anidar funciones en cualquier nivel.
* DAX tiene varias funciones que devuelven una tabla. Normalmente, se usan los valores que devuelven estas funciones como entrada a otras funciones, que requieren una tabla como entrada.

## Operadores y constantes DAX

En la tabla siguiente se enumeran los operadores que son compatibles con DAX. Para obtener más información sobre la sintaxis de los operadores individuales, vea [Operadores DAX](https://learn.microsoft.com/es-es/dax/dax-operator-reference).

| Tipo de operador                    | Símbolo y uso                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Operador de paréntesis             | () orden de prioridad y agrupación de argumentos                                                             |
| Operadores aritméticos             | + (suma)``- (resta/``signo)``* (multiplicación)``/ (división)``^ (exponenciación)                          |
| Operadores de comparación          | = (igual a)``> (mayor que)``< (menor que)``>= (mayor o igual que)``<= (menor o igual que)``<> (no es igual a) |
| Operador de concatenación de texto | & (concatenación)                                                                                            |
| Operadores de lógica               | && (y)``                                                                                                      |

## Tipos de datos

No es necesario convertir o especificar de cualquier otro modo el tipo de datos de una columna o valor que se usa en una fórmula DAX. Cuando se usan datos en una fórmula DAX, este identifica automáticamente los tipos de datos de las columnas a las que se hace referencia y de los valores que se escriben, y realiza las conversiones implícitas, cuando sea necesario, para completar la operación especificada.

Por ejemplo, si se intenta agregar un número a un valor de fecha, el motor interpretará la operación en el contexto de la función y convertirá los números a un tipo de datos común y, después, presentará el resultado en el formato previsto, una fecha.

Sin embargo, existen algunas limitaciones en los valores que se pueden convertir correctamente. Si un valor o una columna tienen un tipo de datos que es incompatible con la operación actual, DAX devuelve un error. Además, DAX no proporciona funciones que permitan cambiar o convertir explícitamente el tipo de datos de los datos existentes que se han importado en un modelo de datos.

> Importante
>
> DAX no admite el uso del tipo de datos variable. Por lo tanto, cuando se cargan o importan datos en un modelo de datos, se espera que los datos de cada columna sean normalmente de un tipo de datos coherente.

Algunas funciones devuelven valores escalares, incluidas cadenas, mientras que otras funcionan con números, enteros y reales, o con fechas y horas. El tipo de datos necesario para cada función se describe en la sección [Funciones DAX](https://learn.microsoft.com/es-es/dax/dax-function-reference).

Se pueden usar tablas que contengan varias columnas y varias filas de datos como argumento para una función. Algunas funciones también devuelven tablas, que se almacenan en memoria y se pueden usar como argumentos para otras funciones.

## Fecha y hora

DAX almacena los valores de fecha y hora con el tipo de datos datetime utilizado por Microsoft SQL Server. El formato datetime usa un número de punto flotante donde los valores de fecha corresponden a la parte entera que representa el número de días desde el 30 de diciembre de 1899. Los valores de hora corresponden a la parte decimal de un valor de fecha donde las horas, los minutos y los segundos se representan mediante fracciones decimales de un día. Las funciones de fecha y hora de DAX convierten implícitamente los argumentos al tipo de datos datetime.

> Nota
>
> El valor DateTime máximo exacto admitido por DAX es el 31 de diciembre de 9999 00:00:00.

### Literal de fecha y hora

A partir de la versión de agosto de 2021 de Power BI Desktop, los valores date y datetime de DAX se pueden especificar como literales con el formato `dt"YYYY-MM-DD"`, `dt"YYYY-MM-DDThh:mm:ss"` o `dt"YYYY-MM-DD hh:mm:ss"`. Cuando se especifican como literal, no es necesario usar las funciones [DATE](https://learn.microsoft.com/es-es/dax/date-function-dax), [TIME](https://learn.microsoft.com/es-es/dax/time-function-dax), [DATEVALUE](https://learn.microsoft.com/es-es/dax/datevalue-function-dax) y [TIMEVALUE](https://learn.microsoft.com/es-es/dax/timevalue-function-dax) en la expresión.

Por ejemplo, la expresión siguiente usa las funciones DATE y TIME para filtrar por OrderDate:

```DAX
EVALUATE
FILTER (
        FactInternetSales,
        [OrderDate] > (DATE(2015,1,9) + TIME(2,30,0)) &&[OrderDate] < (DATE(2015,12,31) + TIME(11,59,59))
)
```

La misma expresión de filtro se puede especificar como literal:

```DAX
EVALUATE
FILTER (
        FactInternetSales,
        [OrderDate] > dt"2015-1-9T02:30:00" && [OrderDate] < dt"2015-12-31T11:59:59"
)
```

>  Nota
>
> El formato literal con tipo date y datetime de DAX no se admite en todas las versiones de Power BI Desktop, Analysis Services y Power Pivot en Excel. Normalmente, las funcionalidades de DAX nuevas y actualizadas se presentan primero en Power BI Desktop y, después, se incluyen en Analysis Services y Power Pivot en Excel.
