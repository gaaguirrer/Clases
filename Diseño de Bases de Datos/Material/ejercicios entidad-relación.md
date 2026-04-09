# GUÍA DE EJERCICIOS:

## **Modelo Entidad - Relación y conversión a Modelo Relacional**

### **Modelo Entidad - Relación**

1. **Artículos y encargos**

Una base de datos para una pequeña empresa debe contener información acerca de clientes, artículos y pedidos. Hasta el momento se registran los siguientes datos en documentos varios:

* Para cada cliente: Número de cliente (único), Direcciones de envío (varias por cliente), Saldo, Límite de crédito (depende del cliente, pero en ningún caso debe superar los 3.000.000 pts), Descuento.
* Para cada artículo: Número de artículo (único), Fábricas que lo distribuyen, Existencias de ese artículo en cada fábrica, Descripción del artículo.
* Para cada pedido: Cada pedido tiene una cabecera y el cuerpo del pedido. La cabecera está formada por el número de cliente, dirección de envío y fecha del pedido. El cuerpo del pedido son varias líneas, en cada línea se especifican el número del artículo pedido y la cantidad.

Además, se ha determinado que se debe almacenar la información de las fábricas. Sin embargo, dado el uso de distribuidores, se usará: Número de la fábrica (único) y Teléfono de contacto. Y se desean ver cuántos artículos (en total) provee la fábrica. También, por información estratégica, se podría incluir información de fábricas alternativas respecto de las que ya fabrican artículos para esta empresa.

Nota: Una dirección se entenderá como Nº, Calle, Comuna y Ciudad. Una fecha incluye hora.

Se pide hacer el diagrama ER para la base de datos que represente esta información.

2. **Sisstema de ventas**

Le contratan para hacer una BD que permita apoyar la gestión de un sistema de ventas. La empresa necesita llevar un control de proveedores, clientes, productos y ventas.

* Un proveedor tiene un RUT, nombre, dirección, teléfono y página web.
* Un cliente también tiene RUT, nombre, dirección, pero puede tener varios teléfonos de contacto. La dirección se entiende por calle, número, comuna y ciudad.
* Un producto tiene un id único, nombre, precio actual, stock y nombre del proveedor. Además se organizan en categorías, y cada producto va sólo en una categoría. Una categoría tiene id, nombre y descripción.
* Por razones de contabilidad, se debe registrar la información de cada venta con un id, fecha, cliente, descuento y monto final. Además se debe guardar el precio al momento de la venta, la cantidad vendida y el monto total por el producto.

3. **Carreteras**

Diseñar un esquema E/R que recoja la organización de una base de datos para contener la información sobre todas las carreteras del país, sabiendo que se deben cumplir las siguientes especificaciones:

* Las carreteras están divididas en varias categorías (locales, comerciales, regionales, nacionales, autovías, etc.).
* Las carreteras se dividen en tramos. Un tramo siempre pertenece a una única carretera y no puede cambiar de carretera.
* Un tramo puede pasar por varias comunas, interesando conocer el Km de la carretera y la comuna donde empieza el tramo y en donde termina.
* Para los tramos que suponen principio o final de carretera, interesa saber si es que la carretera concluye físicamente o es que confluye en otra carretera. En este caso, interesa conocer con qué carretera confluye y en qué kilómetro, tramo y comuna.

4. **Sistema de vuelos**

Obtener el diagrama E/R para un sistema de control de vuelos adaptado a las siguientes reglas de gestión (indicar las entidades, interrelaciones, etc., que se deducen de cada una de las reglas):

a) De cada aeropuerto se conoce su código, nombre, ciudad y país.
b) En cada aeropuerto pueden tomar tierra diversos modelos de aviones (el modelo de un avión determina su capacidad, es decir, el número de plazas).
c) En cada aeropuerto existe una colección de programas de vuelo. En cada programa de vuelo se indica el número de vuelo, línea aérea y días de la semana en que existe dicho vuelo.
d) Cada programa de vuelo despega de un aeropuerto y aterriza en otro.
e) Los números de vuelo son únicos para todo el mundo.
f) En cada aeropuerto hay múltiples aterrizajes y despegues. Todos los aeropuertos contemplados están en activo, es decir, tienen algún aterrizaje y algún despegue.
g) Cada vuelo realizado pertenece a un cierto programa de vuelo. Para cada vuelo se quiere conocer su fecha, plazas vacías y el modelo de avión utilizado.
h) Algunos programas de vuelo incorporan escalas técnicas intermedias entre los aeropuertos de salida y de llegada. Se entiende por escala técnica a un aterrizaje y despegue consecutivos sin altas o bajas de pasajeros.
i) De cada vuelo se quieren conocer las escalas técnicas ordenadas asignándole a cada una un número de orden.

Por ejemplo, el programa de vuelo 555 de Iberia con vuelos los lunes y jueves despega de Barajas-Madrid-España y aterriza en Caudell-Sydney-Australia teniendo las siguientes escalas técnicas: 1-Los Pradiños-Sao Paulo-Brasil, 2-El Emperador-Santiago-Chile y 3-Saint Kitts-Auckland-Nueva Zelanda.

¿Qué cambios se producirán en el caso anterior si en las escalas pudiesen bajar o subir pasajeros? Explicar cómo se podría representar esta nueva situación.

5. **Olimpíadas**

Las sedes olímpicas se dividen en complejos deportivos. Los complejos deportivos se subdividen en aquellos en los que se desarrolla un único deporte y en los polideportivos. Los complejos polideportivos tienen áreas designadas para cada deporte con un indicador de localización (ejemplo: centro, esquina- NE, etc.). Un complejo tiene una localización, un jefe de organización individual y un área total ocupada. Los dos tipos de complejos (deporte único y polideportivo) tendrán diferentes tipos de información. Para cada tipo de sede, se conservará el número de complejos junto con su presupuesto aproximado.

Cada complejo celebra una serie de eventos (ejemplo: la pista del estadio puede celebrar muchas carreras distintas.). Para cada evento está prevista una fecha, duración, número de participantes, número de comisarios. Una lista de todos los comisarios se conservará junto con la lista de los eventos en los que esté involucrado cada comisario, ya sea cumpliendo la tarea de juez u observador. Tanto para cada evento como para el mantenimiento se necesitará cierto equipamiento (ejemplo: arcos, pértigas, barras paralelas, etc.).

6. **Educando S.A.**

En la Empresa "Educando S.A." se lleva control de sus Bienes y Servicios. El interés primario es poder hacer que los Bienes se manejen de forma rápida y con el menor grado de error. Para esto, quien maneja la sección de "Bienes y Suministros" plantea las siguientes condiciones del negocio para la construcción de una base de datos:

• La Sección está dividida en tres (3) áreas: COMPRAS, ALMACEN, INVENTARIO.

• El área de Compras funciona de la siguiente forma:

* Recibe las solicitudes de compras de las diferentes áreas de la empresa.
* Cada solicitud tiene un responsable.
* Cada solicitud es autorizada por el jefe del área y posteriormente por el Director Financiero.
* Quien realiza una solicitud puede ser responsable de uno o varios centros de costos, con la salvedad de que él como empleado solo está adscrito a uno.
* De la solicitud se debe diligenciar la siguiente información: Número de la solicitud (consecutivo), Fecha, Responsable (nombre y cédula), Centro de Costos, Rubro presupuestal del cual se descargará la compra. En cada solicitud se pueden discriminar uno o muchos ítems con la siguiente información: ítem, nombre del bien, cantidad solicitada, unidad de medida del bien, valor unitario y valor total. Cada solicitud debe ser totalizada.
* Cada bien es identificado por un código universal que es único y es de carácter devolutivo (suministro) o un bien inmueble.
* Una vez diligenciada la solicitud, es remitida al área de compras para realizar su correspondiente cotización.
* Las cotizaciones son realizadas con uno o varios proveedores de los bienes solicitados.
* 

Una vez la cotización definitiva está lista, se crea una orden contractual que maneja la siguiente información:

* Número de la orden contractual
* NIT y nombre del proveedor al cual se le va a realizar la compra
* Fecha de la orden
* Monto total de la orden
* Fecha de entrega

Cada orden puede tener asociado uno o varios ítems de la solicitud o solicitudes que van a ser despachadas. Cada ítem tiene la siguiente información:

* Nombre del bien
* Cantidad solicitada
* Cantidad despachada
* Unidad de medida del bien
* Valor unitario
* Valor total

La orden de compra es aprobada por el Director Financiero para que sea enviada al proveedor elegido.

El área de Almacén funciona de la siguiente forma:

* Su función principal es recepcionar los bienes que llegan de los proveedores y distribuirlos a las correspondientes áreas que realizaron las solicitudes de compras.
* Cuando llega un proveedor con mercancía, este hace una entrega física de los bienes, los cuales son comparados con la factura que este entrega y con la orden de compra correspondiente. Si esta acción es correcta, se registra una entrada de almacén por cada factura relacionada, con la siguiente información:

  * Número de Entrada
  * Fecha
  * Número de factura
  * Proveedor
  * Total Bienes
  * Valor Total (los totales deben coincidir con los de la factura)

  Adjunto a esta se discriminan los ítems recibidos con la siguiente información:

  * Nombre del bien
  * Cantidad entregada
* Cuando el almacén decide despachar los bienes a las diferentes áreas solicitantes, registra cada una de las entregas en Salidas de Almacén con la siguiente información:

  * Número de Salida
  * Empleado responsable del bien a entregar
  * Fecha de salida
  * Fecha de entrega

  Por cada entrega se detalla cada uno de los ítems con la siguiente información:

  * Nombre del bien
  * Cantidad entregada
* Una entrada de almacén puede generar muchas salidas de almacén, por ejemplo: Pueden ingresar 500 pacas de papel higiénico, pero como se debe repartir entre varias áreas, cada una requiere de una salida de almacén.

El área de inventarios funciona de la siguiente forma:

* Es la encargada de administrar y controlar la ubicación de los bienes dentro de la empresa, por esto antes de que el bien salga del almacén debe ser codificado a través de un código único que lo haga identificable dentro de la empresa.
* La ubicación del bien se identifica por la siguiente información:
  * Responsable del bien
  * Fecha de entrega
  * Dirección del bien (ubicación)

Diseñar modelo ER para la base de datos.


7.  **Torneo de Tenis Grand Slam**

El sistema debe memorizar todos los encuentros que se han desarrollado desde que existe el torneo, así como las siguientes características de estos.

Descripción:

El Grand Slam se compone de cuatro torneos anuales que se celebran en Gran Bretaña, Estados Unidos, Francia y Australia. En cada país se pueden desarrollar en distintos lugares (p. ej., en EE. UU. puede desarrollarse en Forest Hill o en Flashing Meadows).

Cada partido tiene asociado un premio de consolación para el perdedor que dependerá de la fase en que se encuentre el torneo (p. ej., el perdedor de octavos de final puede ganar 5.000 dólares). El ganador de la final recibirá el premio correspondiente al torneo.

Cada torneo tiene cinco modalidades: Individual masculino, individual femenino, dobles masculino, dobles femenino y dobles mixtos.

También hay que tener en cuenta la nacionalidad de un jugador, de forma que este puede ser apátrida o tener varias nacionalidades.

Resultados a considerar:

El sistema debe dar respuesta a las siguientes preguntas:

1. Dado un año y un torneo, composición y resultado de los partidos.
2. Lista de árbitros que participaron en el torneo.
3. Ganancias percibidas en premios por un jugador a lo largo del torneo.
4. Lista de entrenadores que han entrenado a un jugador a lo largo del torneo y fechas en las que lo hizo.

Ejemplos de acceso a la base de datos:

1. Connors ganó a Gerulaitis en Roland Garros en 1979 en cuartos de final en individuales masculinos por 6-3 4-6/7-5 6-0.
2. El señor Wilkinson arbitró ese partido.
3. Alemania ha ganado dos veces las individuales masculinas de Wimbledon. Borg ha ganado 2.000.000 de dólares a lo largo de su participación en el Grand Slam.
4. El ganador de Roland Garros de 1987 ganó 20.000 dólares.
5. Noah ha jugado cuatro veces en dobles mixtos con Mandlikova.



8. **Sitio web de información de películas en cartelera**

Se desea crear un sitio web con información referente a las películas en cartelera en las salas de un dudoso cine cercano a la plaza de armas.

De cada película, se almacena una ficha con su título de distribución, su título original, su género, el idioma original, si tiene subtítulos en español o no, los países de origen, el año de la producción, la URL del sitio web de la película, la duración (en horas y minutos), la calificación (Apta todo público, +9 años, +15 años, +18 años), fecha de estreno en Santiago, un resumen y un identificador de la película.

De cada película, interesa conocer la lista de directores y el reparto, es decir, para cada actor que trabaja, el nombre de todos los personajes que interpreta.

Además, interesa disponer de información sobre los directores y actores que trabajan en cada película. De ambos, se conoce su nombre (que lo identifica) y su nacionalidad. Además, se desea conocer la cantidad de películas en las que dirigieron o actuaron. Tenga en cuenta que hay personas que cumplen los dos roles.

Los cines pueden tener más de una sala y cada semana cada uno de los cines envía la cartelera para dicha semana, indicando el detalle de las funciones. Para cada función se conoce el día de la semana y la hora de comienzo, y obviamente la sala y la película que exhibe. De cada sala se sabe el nombre, un número que la identifica dentro del cine y la cantidad de butacas que posee. De cada cine se conoce el nombre que lo identifica, su dirección y teléfono para consultas.

Algunos cines cuentan con promociones. Estas promociones dependen de la función. Por ejemplo, de lunes a jueves antes de las 18:00 se aplica un 50% de descuento en la sala X del cine Y para la película Z, o la función del lunes a las 14:00 para la película A en la sala B, no se cobra a los escolares con túnica. De cada promoción se conoce una descripción y el descuento que aplica.

Además del resumen de la película que se incluye en la ficha, interesa mostrar la opinión de las personas que vieron la película. De cada opinión se conoce el nombre de la persona que la realiza, su edad, la fecha en que registró su opinión, la calificación que le dio a la película (Obra Maestra, Muy Buena, Buena, Regular, Mala) y el comentario propiamente dicho. A cada opinión se le asigna un número que la identifica respecto de la película sobre la cual opina.
