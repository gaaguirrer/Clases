# Filtros y resaltado en informes de Power BI

---

En este artículo se presentan el filtrado y el resaltado en el servicio Power BI. aunque la experiencia es casi exactamente la misma que en Power BI Desktop. Los *filtros* eliminan todos los datos excepto aquellos en los que desea centrarse. En términos generales, *resaltar* no es lo mismo que filtrar. En la mayoría de los objetos visuales, el resaltado no elimina los datos no relacionados. En su lugar, se resaltan los datos relacionados. El resto de los datos permanecen visibles pero atenuados. Consulte [Filtro y resaltado cruzado](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-reports-filters-and-highlighting#cross-filter-and-cross-highlight-visuals) más adelante en este artículo para obtener más información.

![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/power-bi-reports-filters-and-highlighting/power-bi-filter-reading.png)

Hay muchas formas de filtrar y resaltar en los informes de Power BI. Colocar toda la información en un artículo podría ser demasiado, por lo que se han realizado las siguientes divisiones:

* Introducción a los filtros y el resaltado, el artículo que está leyendo ahora.
* Cómo [funcionan los filtros y el resaltado en la Vista de lectura](https://learn.microsoft.com/es-es/power-bi/consumer/end-user-interactions) del servicio Power BI. Sus posibilidades son más limitadas que la Vista de edición, pero dispone de un amplio abanico de opciones de filtrado y resaltado.
* Cómo [crear filtros en el panel Filtros](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-report-add-filter) de Power BI Desktop y del servicio Power BI. Si dispone de permisos de edición en un informe, puede crear, modificar y eliminar filtros en él.
* Una vez agregados los filtros, puede [darles formato](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-report-filter) para que se comporten según lo previsto y para que presenten un aspecto similar al del resto del informe.
* Ha aprendido cómo funcionan los filtros y el resaltado de forma predeterminada. Ahora aprenderá a [cambiar el modo en que las visualizaciones de una página se filtran y resaltan entre sí](https://learn.microsoft.com/es-es/power-bi/create-reports/service-reports-visual-interactions).
* Obtenga información sobre otros [tipos de filtros en los informes de Power BI](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-report-filter-types).

---

## Introducción al panel Filtros

Puede aplicar filtros en el panel **Filtros** o [realizar selecciones en las segmentaciones](https://learn.microsoft.com/es-es/power-bi/visuals/power-bi-visualization-slicers) directamente en la propia página del informe. El panel Filtros muestra los campos de objetos visuales individuales y cualquier otro filtro que el diseñador de informes agregue.

![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/power-bi-reports-filters-and-highlighting/power-bi-add-filter-reading-view.png)

Hay cuatro tipos de filtros estándar que se crean en el panel Filtros.

* El **filtro de objeto visual** se aplica a un solo objeto visual de una página del informe. Verá los filtros de nivel de objeto visual cuando seleccione un objeto visual en el lienzo del informe. Incluso si no puede editar un informe, puede seleccionar un objeto visual y filtrarlo.
* El **filtro de página** se aplica a todos los objetos visuales de la página del informe.
* El **filtro de informe** se aplica a todas las páginas del informe.
* **Filtro de obtención de detalles** : con la obtención de detalles en el servicio Power BI y Power BI Desktop, puede crear una página en el informe de *destino* que se centra en una entidad específica, como un proveedor. Desde las otras páginas del informe, los usuarios pueden hacer clic con el botón derecho en un punto de datos de esa entidad y obtener detalles en la página específica.

Para crear los primeros filtros de objeto visual, de página y de informe, consulte [Incorporación de un filtro a un informe en Power BI](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-report-add-filter).

Para crear filtros de obtención de detalles, vea [Configuración de la obtención de detalles en informes de Power BI](https://learn.microsoft.com/es-es/power-bi/create-reports/desktop-drillthrough).

---

### Filtros básicos y avanzados

De forma predeterminada, los lectores de informes pueden cambiar del filtrado **Básico** al  **Avanzado** .

Los **filtros básicos** muestran una lista de todos los valores del campo. Puede realizar búsquedas en los filtros de página, objeto visual e informe en la vista de lectura o edición, para identificar y seleccionar el valor que quiera.

![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/power-bi-reports-filters-and-highlighting/power-bi-search-filter.png)

Si aparece la palabra **Todo** junto al filtro, significa que no está filtrado, y se muestran todos los valores del campo. Por ejemplo, **Cadena es (Todo)** indica que la página del informe incluye datos sobre todas las cadenas del almacén. En cambio, el filtro de nivel de informe **AñoFiscal es 2013 o 2014** indica que el informe solo muestra los datos de los años fiscales 2013 y 2014.

Los **filtros avanzados** permiten usar filtros más complicados. Por ejemplo, puede buscar valores que contengan o no contengan, empiecen por o no empiecen por, un valor específico.

![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/power-bi-reports-filters-and-highlighting/power-bi-advanced-filter.png)

---

## Filtros en las vistas de lectura y edición

Existen dos modos de interactuar con los informes en el servicio Power BI: la vista de lectura y la vista de edición. Las funcionalidades de filtrado disponibles dependen del modo en el que se encuentre.

* En la [Vista de lectura](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-reports-filters-and-highlighting#filters-in-reading-view), puede interactuar con los filtros que ya existen en el informe y guardar las selecciones que haya hecho. pero no podrá agregar nuevos filtros.
* En la [Vista de edición](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-reports-filters-and-highlighting#filters-in-editing-view), puede agregar todos los tipos de filtros. Al guardar el informe, los filtros se guardan con él, aunque los lectores del informe lo abran en una aplicación móvil. Las personas que consulten el informe en la Vista de lectura interactúan con los filtros que haya agregado, pero no pueden agregar nuevos filtros.

---

### Filtros en la vista de lectura

En el servicio Power BI, si selecciona un objeto visual en la Vista de lectura, el panel Filtros tiene un aspecto similar al ejemplo siguiente:

![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/power-bi-reports-filters-and-highlighting/power-bi-filter-reading-view.png)

Los objetos visuales tienen filtros para todos sus campos. Al crear un informe, puede agregar más. En este panel Filtros, el objeto visual tiene tres filtros.

En la Vista de lectura, puede modificar los filtros existentes para explorar los datos. Solo está filtrando la vista del informe. Al cerrar el informe, los cambios que realice se guardan con la vista del informe, aunque se abra en una aplicación móvil. Para deshacer el filtrado y volver a los valores predeterminados establecidos por el autor del informe, seleccione **Restablecer valores predeterminados** en la barra de menús superior.

![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/media/power-bi-reset-icon.png)

Para obtener más información sobre la Vista de lectura, vea [Ver el panel Filtros del informe](https://learn.microsoft.com/es-es/power-bi/consumer/end-user-report-filter).

---

### Filtros en la vista de edición

Al abrir un informe en Power BI Desktop, verá que **Filtros** es solo uno de los distintos paneles de edición disponibles. Verá los mismos paneles si abre un informe en la Vista de edición en el servicio Power BI.

![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/power-bi-reports-filters-and-highlighting/power-bi-add-filter-editing-view.png)

Esta página del informe tiene cuatro filtros de nivel de página. Al seleccionar el gráfico de columnas, vemos que también tiene tres filtros de nivel de objeto visual.

---

#### Trabajo con filtros en la Vista de edición

* Obtenga información sobre cómo [Agregar filtros a un informe](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-report-add-filter) en Power BI Desktop y en la Vista de edición en el servicio Power BI.
* Una vez agregados los filtros, tiene muchas opciones para darles formato. Por ejemplo, puede ocultar, bloquear o reordenar los filtros o darles formato para que coincidan con el resto del informe. Obtenga información sobre cómo [dar formato a los filtros en un informe](https://learn.microsoft.com/es-es/power-bi/create-reports/power-bi-report-filter).
* También puede cambiar la forma en que interactúan los objetos visuales. Para ajustar el filtro y resaltado cruzado, vea [Cambiar cómo interactúan los objetos visuales en un informe de Power BI](https://learn.microsoft.com/es-es/power-bi/create-reports/service-reports-visual-interactions).

---

## Objetos visuales de resaltado cruzado y filtro cruzado

Puede explorar las relaciones entre los objetos visuales del informe sin usar filtros ni segmentaciones. Seleccione un valor o una etiqueta de eje en un objeto visual para aplicar un *filtro cruzado* o *resaltado cruzado* en los valores relacionados en otros objetos visuales de la página. No todos se comportan de la misma manera.

* **Resaltado cruzado** : la selección de un valor en un objeto visual resalta los datos relacionados en objetos visuales como gráficos de barras y de columnas. El resaltado cruzado no elimina los datos no relacionados de esos objetos visuales. Los datos no relacionados continúan mostrándose, pero aparecen atenuados.
* **Filtrado cruzado** : la selección de un valor en un objeto visual actúa como filtro en otros objetos visuales, como gráficos de líneas, gráficos de dispersión y mapas. En esos objetos visuales, solo se muestran los datos relacionados. Los datos no relacionados no son visibles, como si se tratara de un filtro.

Para quitar el resaltado, vuelva a seleccionar el valor, o bien seleccione cualquier espacio vacío en el mismo objeto visual. Para obtener más ejemplos, consulte la sección [Resaltado cruzado y filtrado cruzado](https://learn.microsoft.com/es-es/power-bi/consumer/end-user-interactions#cross-filtering-and-cross-highlighting) de "Aplicación de un filtro cruzado entre objetos visuales en un informe de Power BI".


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/power-bi-reports-filters-and-highlighting/power-bi-adhoc-filter.gif)
