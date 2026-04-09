# Creación de un informe de Power BI para Power BI Report Server

Puede almacenar y administrar informes de Power BI en el portal web de Power BI Report Server, así como también en la nube del servicio Power BI ([https://powerbi.com](https://powerbi.com/)). Cree y edite informes en Power BI Desktop y publíquelos en el portal web. Luego, los lectores de informes de su organización pueden verlos en un explorador o en una aplicación móvil de Power BI de un dispositivo móvil.
![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/report-server-powerbi-report.png)

Aquí tiene cuatro pasos para ayudarle a comenzar.

[](https://learn.microsoft.com/es-es/power-bi/report-server/quickstart-create-powerbi-report?source=docs#step-1-install-power-bi-desktop-for-power-bi-report-server)## Paso 1: Instalar Power BI Desktop para Power BI Report Server

Si ya ha creado informes de Power BI en Power BI Desktop, estará casi listo para crearlos en Power BI Report Server. Se recomienda instalar la versión de Power BI Desktop para Power BI Report Server, ya que así tendrá la certeza de que el servidor y la aplicación siempre están sincronizados. Ambas versiones de Power BI Desktop pueden estar en el mismo equipo.

1. En el portal web de Report Server, seleccione la flecha  **Descargar** > **Power BI Desktop** .
   ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/install-powerbi-desktop/report-server-download-web-portal.png)

O bien, vaya a la página principal de [Power BI Report Server](https://powerbi.microsoft.com/report-server/) y seleccione  **Opciones avanzadas de descarga** .

2. En la página del Centro de descarga, seleccione  **Descargar** .
3. En función de su equipo, seleccione:

   * **PBIDesktopRS.msi** (versión de 32 bits).
   * **PBIDesktopRS_x64.msi** (versión de 64 bits).
4. Después de descargar el instalador, ejecute el Asistente para instalación de Power BI Desktop.
5. Al final del proceso de instalación, seleccione  **Iniciar Power BI Desktop ahora** .
   Se inicia automáticamente y está listo para funcionar. Sabrá que tiene la versión correcta porque en la barra de título aparece **Power BI Desktop (enero de 2021)** .
   ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/install-powerbi-desktop/power-bi-report-server-desktop.png)
6. Si no conoce Power BI Desktop, considere la posibilidad de ver los vídeos de la pantalla de inicio de sesión
   ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/report-server-powerbi-desktop-start.png)

   ---

   ## Paso 2: Seleccionar origen de datos

   Puede conectarse a una gran variedad de orígenes de datos. Más información acerca de cómo [conectarse a orígenes de datos](https://learn.microsoft.com/es-es/power-bi/report-server/connect-data-sources).


   1. En la pantalla de inicio de sesión, seleccione  **Obtener datos** .
      En la pestaña  **Inicio** , seleccione  **Obtener datos** .
   2. Seleccione el origen de datos: en este ejemplo,  **Analysis Services** .
      ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/power-bi-report-server-get-data-ssas.png)
      3. Rellene el campo **Servidor** y, opcionalmente,  **Base de datos** . Asegúrese de que **Conectar en directo** está seleccionado > **Aceptar** .
      ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/report-server-ssas-server-name.png)
      4. Elija el servidor de informes en el que guardará los informes.
      ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/report-server-select-server.png)

---

## Paso 3: Diseño del informe

Esta es la parte divertida: va a crear los objetos visuales que ilustran los datos.

Por ejemplo, puede crear un gráfico de embudo de clientes y los valores de grupo por ingresos anuales.
![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/report-server-create-funnel.png)

1. En  **Visualizaciones** , seleccione  **Gráfico de embudo** .
2. Arrastre el campo de recuento a  **Valores** . Si no es un campo numérico, Power BI Desktop lo convierte automáticamente en un *recuento* del valor.
3. Arrastre el campo al grupo de  **Grupo** .

Más información acerca del [diseño de un informe de Power BI](https://learn.microsoft.com/es-es/power-bi/create-reports/desktop-report-view).

> Nota

> Algunos objetos visuales, como el objeto visual de informe paginado, solo funcionarán en el servicio Power BI. La representación de estos objetos visuales en Power BI Report Server generará un error de "Objeto visual no admitido".

---

## Paso 4: Guardado del informe en el servidor de informes

Cuando el informe esté listo, guárdelo en la instancia de Power BI Report Server que eligió en el paso 2.

1. En el menú  **Archivo** , seleccione  **Guardar como** > **servidor de informes de Power BI** .
   ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/report-server-save-as-powerbi-report-server.png)
2. Ahora puede verlo en el portal web.
   ![Descripción de la imagen](https://learn.microsoft.com/es-es/power-bi/report-server/media/quickstart-create-powerbi-report/report-server-powerbi-report.png)

>  Nota

> Si más adelante decide editar el informe, los datos que verá en el escritorio serán siempre los que estén almacenados en caché del momento en el que se creó el informe por primera vez. Para ver los datos más recientes al editar el informe, debe actualizarlos en la aplicación Power BI Desktop.
