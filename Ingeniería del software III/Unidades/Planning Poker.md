# Scrum y Planning Poker: Guía Completa para Principiantes

## Índice

1. [¿Qué es Scrum?](#1--qué-es-scrum)
2. [Componentes clave de Scrum](#2--componentes-clave-de-scrum)
   - [Roles](#roles)
   - [Eventos](#eventos)
   - [Artefactos](#artefactos)
3. [¿Qué es Planning Poker?](#3--qué-es-planning-poker)
4. [Cómo hacer Planning Poker: paso a paso](#4--cómo-hacer-planning-poker-paso-a-paso)
5. [Práctica](#5--práctica)
   - [5.1 Juego de roles](#51-juego-de-roles)
   - [5.2 Tabla de complejidad con ejemplos locales](#52-tabla-de-complejidad-con-ejemplos-locales)
   - [5.3 Simulación de sprint](#53-simulación-de-sprint)
6. [Evaluación del aprendizaje](#6--evaluación-del-aprendizaje)
   - [Examen teórico](#examen-teórico)
   - [Examen práctico](#examen-práctico)
   - [Autoevaluación](#autoevaluación)
7. [Errores frecuentes](#7--errores-frecuentes)
8. [Glosario rápido](#8--glosario-rápido)
9. [Conclusión y desafío final](#9--conclusión-y-desafío-final)

---

## 1. ¿Qué es Scrum?

**Definición**: Scrum es un método ágil para gestionar proyectos complejos, dividiéndolos en etapas cortas llamadas *sprints* (normalmente de 1 a 4 semanas, siendo 2 semanas lo más común), con entregas constantes de valor.

**Analogía**:

> Imagina organizar una fiesta de cumpleaños:
>
> - **Sprint**: Planear cada detalle en dos semanas.
> - **Roles**: Tú eres el Product Owner (decides la temática y los regalos). Un amigo coordinador actúa como Scrum Master: si falta la torta o el proveedor no confirma, él llama a un sustituto; no resuelve todo solo, sino que facilita que alguien lo resuelva. Los invitados que ayudan forman el Equipo de desarrollo (decoran, preparan la comida, etc.).

---

## 2. Componentes clave de Scrum

### Roles

| Rol | Responsabilidad | Ejemplo en Nicaragua |
| --- | --------------- | -------------------- |
| **Product Owner (PO)** | Define qué se construye y prioriza las funcionalidades. | Decide que una app de facturación cumpla primero con los requisitos de la DGI (Dirección General de Ingresos de Nicaragua, entidad reguladora de facturación fiscal). |
| **Scrum Master (SM)** | Facilita el proceso y elimina obstáculos. El SM no resuelve directamente, sino que ayuda al equipo a resolver o escala el problema a quien pueda hacerlo. | Si falla el internet de Claro o Tigo, el SM contacta al proveedor o busca una alternativa (por ejemplo, hotspot móvil) mientras el equipo sigue trabajando. |
| **Equipo de desarrollo** | Construye el producto (programadores, diseñadores, testers). | Desarrolla una app para caficultores de Matagalpa, asegurando que funcione sin conexión estable o durante apagones eléctricos. |

### Eventos

| Evento | Duración | Propósito |
| ------ | -------- | --------- |
| **Sprint Planning** | 2-4 horas | Planificar las tareas que se realizarán durante el sprint. |
| **Daily Standup** | 15 minutos máximos por día | Sincronizar al equipo respondiendo: ¿qué hice ayer?, ¿qué haré hoy?, ¿qué me bloquea? **Importante**: aquí solo se identifican bloqueos, no se resuelven. Si surge un problema, se agenda una reunión aparte. |
| **Sprint Review** | 1-2 horas | Mostrar los avances al cliente o a los interesados. |
| **Retrospectiva** | 1-2 horas | Identificar mejoras para aplicar en el próximo sprint. |

### Artefactos

| Artefacto | Descripción | Ejemplo |
| --------- | ----------- | ------- |
| **Product Backlog** | Lista ordenada de todas las funcionalidades deseadas para el producto. | "Generar PDF con sello de la DGI", "Exportar a Excel", "Enviar SMS con Claro o Tigo". |
| **Sprint Backlog** | Conjunto de tareas seleccionadas del Product Backlog para el sprint actual. | "Validar formato TXT para la DGI (8 puntos)". |
| **Incremento** | Versión funcional del producto al final del sprint. | App que genera facturas válidas y las almacena localmente. |
| **Definition of Done (DoD)** | Criterios que debe cumplir una tarea para considerarse terminada. Sin DoD, no hay incremento real. | Una tarea está "terminada" solo si: pasa pruebas locales, está documentada, funciona sin internet y ha sido revisada por otro miembro del equipo. |

---

## 3. ¿Qué es Planning Poker?

**Definición**: Técnica colaborativa para estimar la complejidad o el esfuerzo de las tareas usando consenso y una escala no lineal (sucesión de Fibonacci).

**Escala típica**: 0, 1, 2, 3, 5, 8, 13, 20, 40, 100, ∞, ?

- **∞ (infinito)** significa que la tarea es demasiado grande para estimarse; debe dividirse en partes más pequeñas.
- **? (interrogación)** indica que falta información para emitir una estimación; es necesario investigar más.
- **Nota sobre la escala**: Después de 13 se salta a 20, luego 40, 100. Esto es intencional: los números grandes representan tareas que casi siempre deben romperse en subtareas. Si una tarea supera 13 puntos, se recomienda dividirla.

**Metáfora**:

> Es como preguntar a varios vendedores del mercado cuánto cuesta hacer un nacatamal. Cada uno da un precio, y después de discutir los ingredientes y el tiempo, se acuerda un precio justo para todos.

---

## 4. Cómo hacer Planning Poker: paso a paso

### Materiales

- Baraja de cartas con los valores: 0, 1, 2, 3, 5, 8, 13, 20, 40, 100, ∞, ?.
- Lista de tareas del backlog (por ejemplo: "Integrar envío de SMS con la API de Claro").

### Pasos

1. **Presentación de la tarea**  
   El Product Owner explica la funcionalidad:  
   *"La app debe enviar un SMS de confirmación al emitir una factura. Las APIs de Claro y Tigo tienen poca documentación y no hay soporte técnico local."*

2. **Ronda de preguntas técnicas**  
   Cualquier miembro del equipo puede preguntar, no solo desarrolladores. Por ejemplo:  
   - Un tester puede preguntar: "¿Cómo probamos el envío sin tener acceso real a la API?"  
   - El Scrum Master puede preguntar: "¿Hay algún ejemplo de integración exitosa con esas APIs en Nicaragua?"

3. **Votación secreta y simultánea**  
   Cada persona elige una carta y la muestra boca abajo. A la cuenta de tres, todos la voltean al mismo tiempo para evitar influenciar a los demás.  

   > **Ejemplo de votación**:  
   > Cartas reveladas: 5, 8, 8, 13.

4. **Discusión abierta**  
   - Quien votó 5 explica: "Ya usé la API de Claro en otro proyecto; funciona si se sigue un tutorial específico."  
   - Quien votó 13 argumenta: "Sin soporte técnico en Nicaragua, cualquier error puede retrasarnos días."

5. **Consenso**  
   Se vuelve a votar si hay mucha dispersión. El objetivo es llegar a un acuerdo, no a una media matemática.  
   En el ejemplo, después de discutir, el equipo acepta **8 puntos** como estimación final.

---

## 5. Práctica

### 5.1 Juego de roles (role-playing)

**Ejercicio**: Simular un sprint para una app de ventas de café.

**Tarea a estimar**: "Exportar reportes de ventas en formato Excel".

**Roles sugeridos** (asignar a diferentes personas):

- **Product Owner**: Explica por qué los caficultores necesitan el Excel para llevar sus cuentas y presentar informes a cooperativas.
- **Desarrollador 1**: Pregunta sobre el formato de las fechas y los separadores decimales.
- **Desarrollador 2**: Señala que las tablets rurales tienen poca memoria y abrir archivos grandes podría ser un problema.
- **Tester**: Pregunta cómo se simulará una exportación con muchas filas sin ralentizar la app.
- **Scrum Master**: Modera la discusión, asegura que todos voten y cronometra los pasos.

**Procedimiento**:
1. El PO presenta la tarea.
2. El equipo discute dependencias (por ejemplo: ¿los datos están en una base local o en la nube?).
3. Se realiza una votación con cartas hechas a mano (pueden ser tarjetas de papel con los números de Fibonacci).
4. Se llega a un consenso.

### 5.2 Tabla de complejidad con ejemplos locales

| Puntos | Complejidad | Ejemplo en Nicaragua | Solución técnica sugerida |
| ------ | ----------- | -------------------- | ------------------------- |
| 1 | Muy fácil | Cambiar el color de un botón en la interfaz. | Editar una línea de CSS. |
| 8 | Complejo | Generar un archivo TXT con el formato que exige la DGI (Dirección General de Ingresos), sin una API oficial. | Crear un validador local con reglas basadas en la documentación pública; pruebas con casos reales. |
| 13 | Muy complejo | Implementar un sistema que pueda seguir funcionando durante apagones eléctricos de hasta cuatro horas. | Usar baterías externas, sincronización periódica a la nube cuando hay energía, y almacenamiento local con cola de reintentos. |

### 5.3 Simulación de sprint

**Proyecto**: App para gestionar ventas de artesanías en Granada.

**Velocidad del equipo**: En el primer sprint se estima a ojo; después se calcula con el promedio de puntos completados en sprints anteriores. Para este ejercicio, asumamos una velocidad de 20 puntos por sprint (dos semanas).

1. **Crear Product Backlog**  
   - "Login seguro con correo y contraseña"  
   - "Registro de ventas (producto, cantidad, precio)"  
   - "Generar facturas en PDF"  
   - "Reporte de ventas diarias"

2. **Sprint Planning**  
   El equipo selecciona tareas del backlog que sumen aproximadamente 20 puntos.  
   *Ejemplo de selección:*  
   - Login seguro (5 puntos)  
   - Registro de ventas (8 puntos)  
   - Generar facturas (8 puntos) → Total 21 puntos (se ajusta dejando una tarea para el próximo sprint o dividiéndola).

3. **Daily Standup (simulado)**  
   Cada miembro responde:  
   - "Ayer trabajé en la pantalla de login. Hoy voy a probar la validación de correos. Me bloquea que la API de verificación no tiene documentación."  
   - (El Scrum Master anota el bloqueo y agenda una conversación aparte con quien pueda ayudar.)

4. **Definition of Done (DoD) para este sprint**:  
   - El código pasa pruebas locales.  
   - La funcionalidad funciona sin conexión a internet (modo offline).  
   - Se ha probado en al menos dos dispositivos distintos.  
   - La documentación está actualizada en el repositorio.

---

## 6. Evaluación del aprendizaje

### Examen teórico

1. ¿Qué rol prioriza las tareas en el Product Backlog?  
   a) Scrum Master  
   b) Product Owner (correcta)  
   c) Equipo de desarrollo

2. ¿Por qué se recomienda usar la secuencia de Fibonacci en Planning Poker?  
   a) Porque es más fácil sumar puntos  
   b) Para reflejar la incertidumbre creciente en tareas grandes (correcta)  
   c) Por tradición histórica

3. ¿Qué evento permite al equipo mejorar su proceso?  
   a) Sprint Review  
   b) Daily Standup  
   c) Retrospectiva (correcta)

4. ¿Qué significa la carta ∞ (infinito) en Planning Poker?  
   a) La tarea es infinita, nunca termina  
   b) La tarea es demasiado grande para estimarse; debe dividirse (correcta)  
   c) El equipo no tiene límite de tiempo

5. ¿Quién puede interrumpir un sprint para agregar una tarea urgente?  
   a) Cualquier miembro del equipo  
   b) El Product Owner, solo si es una emergencia real y se cancela otra tarea de igual esfuerzo (correcta)  
   c) El Scrum Master

### Examen práctico

**Caso 1**  
Un equipo estimó 8 puntos para una tarea, pero al ejecutarla tardaron el doble del tiempo esperado. En la retrospectiva descubrieron que no habían considerado la falta de soporte técnico local para una API externa.  

**Pregunta**: ¿Qué acción debería tomar el equipo en el próximo sprint planning?  

**Criterios de corrección (respuesta aceptable si menciona al menos dos de los siguientes puntos):**  
- Dividir la tarea en partes más pequeñas.  
- Investigar primero la disponibilidad de soporte o buscar una alternativa local.  
- Agregar una actividad de "spike" (investigación técnica) al backlog.  
- Incluir un factor de riesgo en las estimaciones futuras para tareas con dependencias externas.

**Caso 2**  
Un equipo estimó 2 puntos para cambiar un texto en la interfaz. Sin embargo, la DGI publicó un nuevo requisito de formato que obligó a reescribir toda la pantalla de facturación. La tarea terminó tomando 13 puntos de esfuerzo real.  

**Pregunta**: ¿Qué falló en el proceso de estimación?  

**Criterios de corrección (respuesta aceptable si menciona al menos dos de):**  
- No consideraron factores externos (cambios normativos).  
- No incluyeron una actividad de monitoreo de requisitos legales en su backlog.  
- La estimación se basó solo en el cambio visible, no en el impacto potencial de reglas externas.  
- El Product Owner no actualizó el backlog con riesgos conocidos del entorno.

### Autoevaluación

Marca tu nivel de comprensión para cada ítem (1 = No lo entiendo, 3 = Lo entiendo parcialmente, 5 = Podría enseñarlo a otro):

| Ítem | Puntuación (1-5) |
| ---- | ---------------- |
| Puedo explicar qué es Scrum y para qué sirve. | |
| Identifico los tres roles y sus responsabilidades. | |
| Conozco los eventos de Scrum y su duración aproximada. | |
| Puedo dirigir una sesión de Planning Poker. | |
| Entiendo por qué se usa Fibonacci y qué significan ∞ y ?. | |
| Soy capaz de facilitar una retrospectiva. | |
| Puedo adaptar Scrum a un proyecto real en Nicaragua (con apagones, poca conectividad, etc.). | |

**Total (máximo 35):**  
- Menos de 15: Revisar la guía desde el inicio.  
- 15 a 25: Practicar con la simulación de sprint.  
- 26 a 35: Listo para aplicar Scrum en un proyecto real.

---

## 7. Errores frecuentes

| Error | Consecuencia | Cómo evitarlo |
| ----- | ------------ | -------------- |
| El Product Owner no está disponible porque tiene otras funciones. | El equipo no sabe qué priorizar, el backlog queda desactualizado. | Definir un horario fijo de disponibilidad; si no es posible, asignar un proxy PO. |
| Se estima en horas en lugar de puntos. | Las estimaciones se vuelven inexactas porque mezclan esfuerzo y complejidad. | Usar siempre puntos Fibonacci; no convertir a horas. |
| El equipo vota siempre 8 por miedo a discutir. | Las estimaciones no reflejan la realidad, se acumula deuda técnica. | El Scrum Master debe fomentar la discrepancia honesta; usar votos anónimos o escritos. |
| El Daily Standup se convierte en reunión de resolución de problemas. | Se alarga más de 15 minutos, el equipo pierde foco. | El SM debe detener la discusión y agendar una reunión aparte con los interesados. |
| No se define el Definition of Done. | Tareas "terminadas" que en realidad no funcionan en producción. | Escribir el DoD al inicio del proyecto y revisarlo en cada retrospectiva. |

---

## 8. Glosario rápido

| Término | Significado |
| ------- | ----------- |
| **Sprint** | Período de tiempo fijo (1-4 semanas) para completar un conjunto de tareas. |
| **Product Backlog** | Lista priorizada de todo lo que se quiere construir. |
| **Sprint Backlog** | Subconjunto del Product Backlog elegido para un sprint. |
| **Incremento** | Resultado funcional al final del sprint. |
| **Definition of Done (DoD)** | Criterios que una tarea debe cumplir para ser considerada terminada. |
| **Fibonacci** | Sucesión (1,2,3,5,8,13...) usada para estimar porque la incertidumbre crece con el tamaño. |
| **Planning Poker** | Técnica de estimación por consenso usando cartas. |
| **DGI** | Dirección General de Ingresos de Nicaragua. |
| **Velocidad del equipo** | Promedio de puntos completados por sprint. |

---

## 9. Conclusión y desafío final

Scrum y Planning Poker son herramientas prácticas para gestionar proyectos en entornos con recursos limitados o regulaciones cambiantes, una realidad común en Nicaragua y otros países de la región. Al aplicar estos métodos con ejemplos locales y actividades interactivas, los equipos pueden:

- Priorizar tareas críticas, como cumplir con los requisitos de la DGI.
- Anticipar riesgos típicos: falta de APIs documentadas, apagones eléctricos, cambios normativos inesperados.
- Entregar valor de manera constante, incluso en condiciones adversas.

**Tu desafío (en equipo)**  
Organiza un sprint para una app que promueva el turismo en León. Sigue estos pasos:

1. Define tres funcionalidades del Product Backlog (ejemplo: "Mapa de museos sin internet", "Registro de visitas", "Cupones de descuento para restaurantes").
2. Asigna los roles de Scrum (PO, SM, Equipo).
3. Realiza una sesión de Planning Poker usando la escala de Fibonacci.
4. Documenta el consenso en una tabla como esta:

| Tarea | Puntos estimados |
| ----- | ---------------- |
| [Nombre de la tarea] | [Puntos] |
| [Nombre de la tarea] | [Puntos] |
| [Nombre de la tarea] | [Puntos] |

5. Al final del sprint simulado, realiza una retrospectiva con dos preguntas: ¿Qué salió bien? ¿Qué mejoraríamos?

Este ejercicio te dará la confianza para aplicar Scrum en proyectos reales, adaptándolo a las condiciones locales.