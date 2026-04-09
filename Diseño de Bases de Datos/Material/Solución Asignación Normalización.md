## Instrucciones iniciales

* Para cada ejercicio, se le proporcionará una lista de entidades y sus campos, claves primarias y foráneas, y las relaciones que existen entre ellas.
* Determine en qué forma normal se encuentra cada tabla.
* Normalice cada tabla hasta la tercera forma normal. Asegúrese de explicar el proceso de normalización y documentar cada paso.
* Asegúrese de incluir las claves primarias y foráneas en cada tabla normalizada.
* Asegúrese de que las tablas normalizadas sigan siendo capaces de responder a las consultas que se harían en la base de datos original.

Recuerde que el proceso de normalización de bases de datos es un proceso importante que garantiza la integridad y eficiencia de una base de datos. ¡Buena suerte!

## Ejercicios

1. **Sistema de gestión de tienda de ropa**
   Entidades: Clientes (*id_cliente, nombre, dirección*), Productos *(id_producto, nombre, precio*), Ventas (*id_venta, fecha, id_cliente), Detalles de Venta (id_venta, id_producto, cantidad*)
   Relaciones: Un cliente puede realizar varias ventas; una venta puede incluir varios productos.
   Forma Normal Actual: 2FN
   Solución: Crear una nueva tabla para manejar la relación muchos a muchos entre Ventas y Productos. Luego, dividir la tabla Detalles de Venta en dos tablas separadas: una para almacenar información de detalles de venta y otra para almacenar información de productos.
2. **Sistema de gestión de una empresa**
   Entidades: Empleados (*id_empleado, nombre, dirección, salario*), Departamentos (*id_departamento, nombre*), Asignaciones (*id_asignacion, id_empleado, id_departamento, fecha_inicio, fecha_fin*)
   Relaciones: Un empleado puede ser asignado a varios departamentos; un departamento puede tener varios empleados asignados.
   Forma Normal Actual: 1FN
   Solución: Dividir la tabla Asignaciones en dos tablas separadas: una para almacenar información de asignaciones y otra para almacenar información de empleados.
3. **Sistema de gestión de cine**
   Entidades: Películas (*id_pelicula, título, género, duración*), Salas (*id_sala, número, capacidad*), Funciones (*id_funcion, fecha, hora, id_pelicula, id_sala*)
   Relaciones: Una película puede ser proyectada en varias salas; una función es para una película y una sala específicas.
   Forma Normal Actual: 1FN
   Solución: Dividir la tabla Funciones en dos tablas separadas: una para almacenar información de funciones y otra para almacenar información de películas.
4. **Sistema de gestión de gimnasio**
   Entidades: Socios (*id_socio, nombre, dirección*), Rutinas (*id_rutina, nombre, descripción*), Asignaciones (*id_asignacion, id_socio, id_rutina, fecha_inicio, fecha_fin*)
   Relaciones: Un socio puede tener varias asignaciones de rutina; una rutina puede ser asignada a varios socios.
   Forma Normal Actual: 1FN
   Solución: Dividir la tabla Asignaciones en dos tablas separadas: una para almacenar información de asignaciones y otra para almacenar información de socios.
5. **Sistema de gestión de biblioteca universitaria**
   Entidades: Estudiantes (*id_estudiante, nombre, dirección*), Libros (*id_libro, título, autor, editorial*), Préstamos (*id_prestamo, fecha_prestamo, fecha_devolucion, id_libro, id_estudiante*)
   Relaciones: Un estudiante puede tomar varios préstamos; un libro puede ser prestado varias veces.
   Forma Normal Actual: 1FN
   Solución: Dividir la tabla Préstamos en dos tablas separadas: una para almacenar información de préstamos y otra para almacenar información de libros.
6. **Sistema de gestión de reservas de vuelos**
   Entidades: Pasajeros (*id_pasajero, nombre, dirección*), Vuelos (*id_vuelo, fecha, hora, origen, destino*), Reservas (*id_reserva, fecha, id_pasajero, id_vuelo*)
   Relaciones: Un pasajero puede hacer varias reservas; un vuelo puede tener varias reservas.
   Forma Normal Actual: 1FN
   Solución: Dividir la tabla Reservas en dos tablas separadas: una para almacenar información de reservas y otra para almacenar información de pasajeros. Luego, crear una nueva tabla para manejar la relación muchos a muchos entre Vuelos y Pasajeros.
7. **Sistema de gestión de tareas**
   Entidades: Tareas (*id_tarea, descripción, fecha_limite, estado),* Categorías *(id_categoria, nombre*)
   Relaciones: Una tarea puede tener una categoría; una categoría puede tener varias tareas.
   Forma Normal Actual: 1FN
   Solución: La tabla Tareas ya se encuentra en 2FN y 3FN. No se necesita ninguna normalización adicional. Sin embargo, se puede crear una nueva tabla para manejar la relación uno a muchos entre Categorías y Tareas.

## Criterios de evaluación

**Rúbrica de Evaluación - Ejercicio de Normalización de Base de Datos**

*Criterio 1*: Identificación de la forma normal de cada tabla (30%)

* El estudiante identificó correctamente la forma normal de cada tabla.
* El estudiante proporcionó explicaciones claras y coherentes sobre su identificación.

*Criterio 2*: Normalización de las tablas hasta la tercera forma normal (60%)

* El estudiante normalizó correctamente las tablas hasta la tercera forma normal.
* El estudiante proporcionó explicaciones claras y coherentes sobre el proceso de normalización y documentó cada paso.
* El estudiante incluyó claves primarias y foráneas en cada tabla normalizada.

*Criterio 3*: Organización y presentación (10%)

* El estudiante presentó el trabajo de manera organizada y fácil de seguir.
* El trabajo fue entregado en el formato solicitado y dentro del plazo establecido.

Puntuación total: 100%
