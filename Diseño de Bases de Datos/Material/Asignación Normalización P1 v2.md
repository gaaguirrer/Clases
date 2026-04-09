## Instrucciones iniciales

* Para cada ejercicio, se le proporcionará una lista de entidades y sus campos, claves primarias y foráneas, y las relaciones que existen entre ellas.
* Determine en qué forma normal se encuentra cada tabla.
* Normalice cada tabla hasta la tercera forma normal. Asegúrese de explicar el proceso de normalización y documentar cada paso.
* Asegúrese de incluir las claves primarias y foráneas en cada tabla normalizada.
* Asegúrese de que las tablas normalizadas sigan siendo capaces de responder a las consultas que se harían en la base de datos original.

Recuerde que el proceso de normalización de bases de datos es un proceso importante que garantiza la integridad y eficiencia de una base de datos. ¡Buena suerte!

## Ejercicios

1. **Ejercicio de normalización para un Cine**:
   Entidad: Películas
   Campos: ID de película, título, director, duración, clasificación, género
   Entidad: Horarios
   Campos: ID de horario, ID de película, fecha, hora
   Entidad: Sala
   Campos: ID de sala, número de sala, capacidad, tipo de pantalla, tipo de sonido
2. **Ejercicio de normalización para una juguetería**:
   Entidad: Juguetes
   Campos: ID de juguete, nombre, marca, edad recomendada, precio, descripción
   Entidad: Categorías
   Campos: ID de categoría, nombre de categoría
   Entidad: Inventario
   Campos: ID de inventario, ID de juguete, cantidad, fecha de entrada
3. **Ejercicio de normalización para pasajes en un tren**:
   Entidad: Trenes
   Campos: ID de tren, nombre, capacidad, velocidad, ruta
   Entidad: Estaciones
   Campos: ID de estación, nombre, dirección
   Entidad: Boletos
   Campos: ID de boleto, ID de tren, ID de estación de origen, ID de estación de destino, fecha, hora, asiento
4. **Ejercicio de normalización para rutas de buses en Rivas, Nicaragua**:
   Entidad: Buses
   Campos: ID de bus, número de placa, capacidad, modelo, compañía
   Entidad: Rutas
   Campos: ID de ruta, nombre de ruta, duración, tarifa
   Entidad: Horarios
   Campos: ID de horario, ID de ruta, hora de salida, hora de llegada
5. **Ejercicio de normalización para administración de una presa hidroeléctrica**:
   Entidad: Generadores
   Campos: ID de generador, capacidad, marca, modelo, fecha de fabricación
   Entidad: Turbinas
   Campos: ID de turbina, capacidad, marca, modelo, fecha de fabricación
   Entidad: Producción
   Campos: ID de producción, ID de generador, ID de turbina, fecha, hora, cantidad de energía generada
6. **Ejercicio de normalización para un registro forestal**:
   Entidad: Árboles
   Campos: ID de árbol, especie, edad, altura, diámetro
   Entidad: Zonas
   Campos: ID de zona, nombre de zona, tamaño, tipo de suelo
   Entidad: Inspecciones
   Campos: ID de inspección, ID de árbol, ID de zona, fecha, observaciones
7. **Ejercicio de normalización para una escuela**:
   Entidad: Estudiantes
   Campos: ID de estudiante, nombre, apellido, fecha de nacimiento, género, dirección
   Entidad: Profesores
   Campos: ID de profesor, nombre, apellido, fecha de nacimiento, género, dirección
   Entidad: Cursos
   Campos: ID de curso, nombre de curso, descripción
   Entidad: Inscripciones
   Campos: ID de inscripción, ID de estudiante, ID de curso, fecha de inscripció

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
