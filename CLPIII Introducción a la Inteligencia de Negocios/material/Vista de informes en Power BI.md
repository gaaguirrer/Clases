# Trabajo con la Vista de informes en Power BI Desktop

---

Si ya ha trabajado con Power BI, sabrá lo fácil que es crear informes que ofrezcan perspectivas dinámicas e información sobre los datos. Power BI también tiene características más avanzadas en Power BI Desktop. Con Power BI Desktop, cree consultas avanzadas, mezcle datos de varios orígenes, cree relaciones entre tablas y mucho más.

Power BI Desktop incluye una  *vista de informes* , donde puede crear varias páginas del informe con visualizaciones. La vista de informes de Power BI Desktop proporciona una experiencia de diseño similar a la vista de edición del informe en el  *servicio Power BI* . Puede mover visualizaciones, copiar y pegar, combinar, etc.

Con Power BI Desktop, también puede trabajar con las consultas y modelar los datos para asegurarse de que ofrecen la mejor información en los informes. A continuación, puede guardar el archivo de Power BI Desktop donde quiera, ya sea en la unidad local o en la nube.

[](https://learn.microsoft.com/es-es/power-bi/create-reports/desktop-report-view#lets-take-a-look)## Veámoslo

Al cargar los datos por primera vez en Power BI Desktop, verá la vista de informes con un lienzo en blanco, con vínculos que le ayudarán a agregar datos al informe.


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/report-view-blank-canvas.png)


Puede cambiar entre las vistas  **Informe** , **Datos** y **Modelo** si selecciona los iconos de la barra de navegación de la izquierda:


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/pbi_reportviewinpbidesigner_changeview.png)


Una vez haya agregado algunos datos, puede agregar campos a una nueva visualización en el lienzo.


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/add-visual.png)


Para cambiar el tipo de visualización, puede seleccionarlo en el lienzo y, a continuación, seleccionar un nuevo tipo en  **Visualizaciones** .


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/change-visual.png)


> Sugerencia

> No deje de experimentar con diferentes tipos de visualización. Es importante que la visualización transmita la información de los datos de manera clara.



Un informe tiene al menos una página en blanco al inicio. Las páginas aparecen en el área de navegación en la parte inferior de la vista  **Informe** . Puede agregar todo tipo de visualizaciones a una página, pero es importante no abusar. Demasiadas visualizaciones en una página le dan un aspecto ocupado y dificultarán la búsqueda de información adecuada. Puede agregar nuevas páginas a un informe. Solo tiene que seleccionar **Nueva página** en la pestaña **Insertar** de la cinta de opciones y, después, seleccionar **Página en blanco**


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/pbidesignerreportviewnewpage.png)


También puede seleccionar el icono **+** situado junto a las páginas del área de navegación debajo del lienzo para crear una página.


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/new-page-icon.png)


Para eliminar una página, haga clic en la **x** en la pestaña de la página en la parte inferior de la vista Informe.


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/pbi_reportviewinpbidesigner_deletepage.png)


> Nota

> Los informes y las visualizaciones no se pueden anclar a un panel desde Power BI Desktop. Para ello, necesitará publicar en el sitio Power BI. Para más información, consulte [Publicar conjuntos de datos e informes desde Power BI Desktop](https://learn.microsoft.com/es-es/power-bi/create-reports/desktop-upload-desktop-files).

---



## Copiar y pegar entre informes

Puede tomar fácilmente un objeto visual de un informe de Power BI Desktop y pegarlo en otro informe. Use el método abreviado de teclado Ctrl+C para copiar el objeto visual del informe. En el otro informe de Power BI Desktop, use Ctrl+V para pegar el objeto visual en el otro informe. Puede copiar un objeto visual cada vez o todos los objetos visuales de una página y pegarlos en el informe de Power BI Desktop de destino.

La capacidad de copiar y pegar objetos visuales es útil para personas que con frecuencia compilan y actualizan varios informes. Si la copia es entre archivos, la configuración y el formato que se han establecido explícitamente en el panel de formato se mantienen, mientras que los elementos visuales que dependen de un tema o la configuración predeterminada se actualizan automáticamente para coincidir con el tema del informe de destino. Cuando le haya dado a un objeto visual el formato y la apariencia que desee, puede copiarlo y pegarlo en nuevos informes y conservar el trabajo.

Si los campos del modelo son diferentes, verá un error en el objeto visual y una advertencia sobre qué campos no existen. El error es similar a la experiencia que ve cuando se elimina un campo en el modelo que usa un objeto visual.


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/report-view_07.png)


Para corregir el error, reemplace los campos incorrectos por los campos que desea usar del modelo en el informe donde pegó el objeto visual. Si usa un objeto visual personalizado, también debe importar ese objeto visual personalizado en el informe de destino.


---



## Ocultación de páginas de informes

Al crear un informe, también puede ocultar algunas de sus páginas. Este enfoque puede ser útil si necesita crear datos u objetos visuales subyacentes en un informe, pero no quiere que esas páginas estén visibles para otros usuarios. Ocultar páginas puede ser útil cuando se crean tablas u objetos visuales auxiliares que se usan en otras páginas del informe. Hay muchas otras razones creativas que pueden llevarle a crear una página de informe y, después, ocultarla en un informe que desea publicar.

La ocultación de una página del informe es fácil. Haga clic con el botón derecho en la pestaña de la página del informe y seleccione **Ocultar** en el menú que aparece.


![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/report-view_05.png)


Hay algunas consideraciones que debe tener en cuenta al ocultar una página del informe:

  ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/create-reports/media/desktop-report-view/report-view_06.png)


* *No puede* ver una página de informe oculta cuando ve el informe en el servicio Power BI en la  **vista de lectura** , pero *puede* verlo en la vista  **Editar** .
* Si está viendo la página oculta cuando guarda el informe y, después, lo publica en el servicio Power BI, esa página será la primera que verán los lectores del informe.
* Ocultar una página del informe *no* es una medida de seguridad. Los usuarios aún pueden acceder a la página y el contenido se puede ver usando, por ejemplo, métodos de obtención de detalles.
* No aparecen flechas de navegación en el modo de vista cuando una página está oculta en este modo.
