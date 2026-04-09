### Diagrama de secuencia UML

El **diagrama de secuencia** es un tipo de diagrama de interacción del Lenguaje de Modelado Unificado (**UML**). Su propósito principal es representar de manera gráfica y cronológica **cómo interactúan los distintos objetos, actores o componentes** de un sistema para llevar a cabo un proceso específico o un caso de uso.  

**¿Para qué sirve?**  
- Describe de forma detallada el **orden de los mensajes** que se envían entre actores y objetos.  
- Ayuda a **visualizar la lógica de ejecución**, facilitando el análisis y diseño del software.  
- Identifica **responsabilidades** de cada objeto o clase involucrada en el proceso.

**Importancia en ingeniería de software**  
- Permite detectar **inconsistencias o ambigüedades** en los requisitos.  
- Facilita la comunicación entre desarrolladores, analistas, usuarios y clientes.  
- Sirve como **documentación técnica** que guía la implementación y las pruebas.  
- Es útil para analizar la viabilidad de procesos complejos.

---

## Elementos del diagrama de secuencia UML

### 1. **Actor**
Representa una **entidad externa** (persona, sistema o dispositivo) que interactúa con el sistema enviando o recibiendo mensajes.  
*Ejemplo:* Docente que registra asistencia de sus estudiantes en un sistema universitario.

---

### 2. **Objeto**
Una **instancia concreta de una clase** que participa en la interacción.  
*Ejemplo:* Objeto `ControlAsistencia` que almacena y procesa las faltas de los estudiantes.

---

### 3. **Línea de vida (*Lifeline*)**
Línea vertical que parte de un actor u objeto, indicando su **existencia durante la interacción**.  
*Ejemplo:* Línea de vida del objeto `Estudiante` mientras se consulta su historial de asistencias.

---

### 4. **Activación (*Execution specification*)**
Rectángulo angosto sobre la línea de vida que indica que el actor u objeto **está ejecutando una acción** tras recibir un mensaje.  
*Ejemplo:* Periodo en el que el objeto `ControlAsistencia` valida los datos de la asistencia.

---

### 5. **Mensaje síncrono**
Flecha continua con punta llena que indica una **llamada a método que requiere respuesta** antes de continuar.  
*Ejemplo:* `registrarFalta()` enviado desde la interfaz al objeto `ControlAsistencia`.

---

### 6. **Mensaje asíncrono**
Flecha continua con punta abierta que representa un mensaje que **no requiere respuesta inmediata**.  
*Ejemplo:* `enviarNotificaciónEmail()` a un servicio externo de notificaciones.

---

### 7. **Mensaje de retorno**
Flecha discontinua que indica el **retorno de un valor o confirmación** tras ejecutar un mensaje síncrono.  
*Ejemplo:* Retorno de `confirmación` después de registrar la falta.

---

### 8. **Fragmento combinado (*Combined fragment*)**
Rectángulo que agrupa partes de la secuencia que representan **alternativas, repeticiones o condiciones** (por ejemplo, *alt*, *loop*, *opt*).  
*Ejemplo:* Fragmento `alt` que representa dos escenarios: notificar al coordinador si el estudiante supera el número máximo de faltas o solo registrar la falta si no lo supera.


---

### 9. **Notas (*Comments*)**
Rectángulo doblado en una esquina, unido mediante línea discontinua, usado para explicar detalles adicionales o aclarar decisiones de diseño.  
*Ejemplo:* Nota que explica por qué el sistema envía una alerta automática a la coordinación académica cuando un estudiante acumula más de tres faltas.

---

El diagrama de secuencia permite representar **cómo fluye la lógica de interacción** entre los diferentes elementos de un sistema, integrando los requisitos funcionales con el diseño técnico. Esto refuerza la comprensión entre todas las partes involucradas, previene errores de interpretación y contribuye a crear sistemas robustos, como podría ser el caso de un sistema de control académico implementado para universidades en Nicaragua.

Si deseas, puedo preparar un ejemplo completo (dibujado con PlantUML o Mermaid) para un caso real basado en un sistema universitario nicaragüense.
