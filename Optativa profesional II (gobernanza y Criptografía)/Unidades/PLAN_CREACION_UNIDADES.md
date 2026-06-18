# Plan de Creación y Mejora Continua de Unidades Didácticas

## Propósito

Este documento establece la metodología completa para crear, revisar y mejorar los documentos de unidad (UDI, UDII, UDIII, UDIV, etc.) de la asignatura Optativa Profesional II (Gobernanza y Criptografía). Cada unidad debe redactarse como si el profesor se dirigiera directamente a sus estudiantes, sin muletillas de asistente de IA, sin aclaraciones metacognitivas sobre el proceso de redacción, y con un tono pedagógico directo.

---

## 1. Estructura Obligatoria de Cada Unidad

Cada documento de unidad debe seguir esta estructura exacta en el orden indicado:

### 1.1 Encabezado
- Logotipo de la universidad (UNHSJM) en la parte superior con `![Logo UNHSJM](Logo UNHSJM.jpeg)`
- Título de la unidad: `# Nombre de la Unidad`
- Sin subtítulos adicionales ni metadatos del autor

### 1.2 Índice de Contenido
- Lista de enlaces ancla a cada sección principal.
- Formato:
  ```markdown
  ## Índice de Contenido
  - [Introducción](#introducción)
  - [Desarrollo de Contenidos](#desarrollo-de-contenidos)
    - [Tema 1](#tema-1)
    - [Tema 2](#tema-2)
  - [Autoevaluación](#autoevaluación)
  - [Bibliografía y Webgrafía](#bibliografía-y-webgrafía)
  - [Glosario](#glosario)
  ```

### 1.3 Introducción
- Párrafo inicial que conecta la unidad anterior con la actual.
- Explica por qué el estudiante debe interesarse en el tema.
- Plantea preguntas retóricas que despierten curiosidad.
- Sin resúmenes de lo que viene (el índice ya lo hace).
- Extensión: 1 a 3 párrafos.

### 1.4 Desarrollo de Contenidos
- Sección principal con el título `## Desarrollo de Contenidos`.
- Subsecciones temáticas con `### NombreDelTema`.
- Cada tema debe incluir:
  - **Explicación conceptual** con terminología precisa en español.
  - **Casos reales** o ejemplos documentados (con nombre de empresa, año, datos verificables).
  - **Ejemplos prácticos** con código Python cuando aplique (criptografía, automatización, análisis de datos, etc.).
  - **Tablas comparativas** o resumen cuando sea pertinente.
  - **Diagramas** en texto o ASCII cuando no se puedan incluir imágenes.

### 1.5 Autoevaluación
- Título `## Autoevaluación`.
- Instrucción inicial: *"Lea cada pregunta, responda mentalmente y luego consulte el glosario o los conceptos si tiene dudas."*
- 10 preguntas numeradas que combinen:
  - Verdadero/Falso
  - Opción múltiple
  - Relación de columnas
  - Casos prácticos (especialmente con cálculos o código)
  - Preguntas de reflexión abierta (máximo 2)
- Cada pregunta debe incluir la respuesta esperada entre bloques de cita.
- La última pregunta debe ser de reflexión abierta.
- Cierre con: *"Si obtuvo menos de 7 respuestas correctas, revise nuevamente las secciones de [lista de temas]."*

### 1.6 Bibliografía y Webgrafía
- Título `## Bibliografía y Webgrafía` (o solo `## Bibliografía`).
- Lista con formato de cita estándar (Apellido, Inicial. (Año). *Título*. Editorial).
- URLs verificables para recursos en línea.
- Mínimo 5 fuentes. Deben incluir tanto bibliografía clásica como recursos actualizados.

### 1.7 Glosario
- Título `## Glosario`.
- Lista de términos en orden alfabético con definiciones de 1 a 3 líneas cada una.
- Deben incluirse todos los términos técnicos nuevos presentados en la unidad.
- Formato: `- **Término**: Definición.`

---

## 2. Reglas de Estilo y Contenido

### 2.1 Lo que SÍ debe incluirse

- **Voz directa del profesor**: Usar "te invito a", "exploraremos", "observa el siguiente caso", "reflexiona sobre esto". Nunca "en este documento", "como se mencionó anteriormente", "como vimos".
- **Ejemplos reales documentados**: Cada tema debe tener al menos un caso real con: nombre de organización, año, qué ocurrió, por qué es relevante, qué lección deja.
- **Código Python funcional**: Cuando el tema lo permita (criptografía, procesamiento de datos, automatización), incluir bloques de código con ` ```python ` que el estudiante pueda copiar y ejecutar.
- **Tablas**: Para comparar conceptos, resumir información o presentar datos estructurados.
- **Preguntas que desafíen**: En la autoevaluación, incluir al menos 2 preguntas que requieran aplicar lo aprendido a un escenario nuevo (no solo memorización).
- **Transiciones entre secciones**: Una frase puente al final de cada tema que lleve al siguiente.

### 2.2 Lo que NO debe incluirse

- **Aclaraciones de IA**: Frases como "como asistente de IA", "como modelo de lenguaje", "según mi conocimiento", "no tengo acceso a internet actualizado", "puedo ayudarte a", "estaré encantado de".
- **Autoreferencias del proceso de escritura**: "He creado este documento", "en este documento se presentan", "a continuación se detalla", "el presente documento".
- **Notas metacognitivas sobre la redacción**: "He decidido incluir", "consideré importante agregar", "nótese que esta sección", "vale la pena destacar que".
- **Explicaciones redundantes del índice**: El índice ya muestra la estructura; no hay que explicarla otra vez en texto.
- **Lenguaje burocrático vacío**: "En virtud de lo anteriormente expuesto", "en base a lo antes mencionado", "cabe señalar que".
- **Adverbios y calificativos innecesarios**: "muy importante", "extremadamente relevante", "fundamentalmente", "esencialmente".

### 2.3 Reglas de Formato

- Títulos con `#` (uno para el principal, `##` para secciones mayores, `###` para subsecciones).
- Negritas para términos clave en su primera aparición.
- Cursivas para títulos de obras y énfasis suave.
- Bloques de código con lenguaje especificado.
- Citas textuales con `>`.
- Tablas con formato GitHub Markdown.
- Listas con `-` o `1.` según corresponda.
- Sin HTML incrustado (excepto la imagen del logo).

### 2.4 Extensión Mínima por Unidad

- Introducción: 100-300 palabras.
- Desarrollo de contenidos: mínimo 2000 palabras.
- Autoevaluación: 10 preguntas completas.
- Glosario: mínimo 15 términos.
- Bibliografía: mínimo 5 fuentes.

---

## 3. Esquema de Revisiones y Mejora Continua

Cada unidad debe pasar por un ciclo completo de revisión y mejora antes de darse por terminada. El ciclo consta de **dos fases**:

### 3.1 Fase I — Revisión de Correcciones

#### 3.1.1 Acción: Revisar
Se lee el documento completo de principio a fin buscando:

**Categorías de correcciones obligatorias:**

| Categoría | Qué buscar | Ejemplo de error |
|-----------|------------|------------------|
| **Ortografía** | Tildes faltantes, errores de ortografía, puntuación incorrecta | "esta" por "está", "tubo" por "tuvo" |
| **Gramática** | Concordancias, tiempos verbales, preposiciones incorrectas | "habian" por "habían", "se los explico" por "se lo explico" |
| **Precisión técnica** | Conceptos incorrectos, definiciones ambiguas, fechas equivocadas, nombres mal escritos | Decir "cifrado simétrico usa RSA" (FALSO) |
| **Claridad pedagógica** | Párrafos confusos, explicaciones que requieren más contexto, ejemplos que no ilustran el punto | Una explicación de hashing sin mencionar la irreversibilidad |
| **Formato y estructura** | Encabezados incorrectos, índices rotos, tablas mal formateadas, imágenes sin alt text | Un `##` donde debería ir `###` |
| **Consistencia** | Términos que cambian de nombre a mitad del documento, estilos mixtos | Usar "cifrado" y "encriptado" indistintamente |
| **Completitud** | Secciones del plan que faltan, temas del sílabo no cubiertos, glosario incompleto | Falta la sección de autoevaluación |

#### 3.1.2 Acción: Listar Correcciones
Se elabora una lista numerada de todas las correcciones encontradas, con la siguiente estructura por cada una:

```
C-001 | [Categoría] | [Ubicación exacta] | [Descripción del problema] | [Corrección propuesta]
```

Ejemplo:
```
C-001 | Ortografía | Sección 3.2, párrafo 2 | "desarollo" está mal escrito | Cambiar a "desarrollo"
C-002 | Precisión técnica | Tema 1, ejemplo RSA | Se dice "RSA usa 56 bits" | Corregir a "RSA usa típicamente 2048 bits o más"
```

#### 3.1.3 Acción: Aplicar Correcciones
Se modifica el documento aplicando cada corrección de la lista. Después de aplicar todas, se tacha la lista como verificada.

### 3.2 Fase II — Revisión de Oportunidades de Mejora

#### 3.2.1 Acción: Revisar (segunda pasada)
Se relee el documento ya corregido buscando oportunidades de mejora (no errores, sino mejoras).

**Categorías de mejoras obligatorias:**

| Categoría | Qué buscar | Ejemplo de mejora |
|-----------|------------|-------------------|
| **Ampliación de ejemplos** | Temas que se beneficiarían de un caso real adicional o un ejemplo práctico más detallado | Un tema sobre hashing sin ejemplo de colisión real (SHA-1) |
| **Profundización conceptual** | Conceptos que podrían explicarse con más capas o matices | Explicar TLS solo a nivel de protocolo sin mencionar la negociación de cifrados |
| **Conexiones interunitarias** | Lazos que faltan entre esta unidad y otras del curso | No mencionar que el cifrado visto en UDIII se usa en los protocolos de gobierno de UDIV |
| **Ejercicios prácticos** | Oportunidad de agregar un mini-ejercicio con código o análisis | Un tema que menciona AES pero no incluye un ejemplo Python con pycryptodome |
| **Actualización de referencias** | Casos o tecnologías desactualizadas que podrían reemplazarse con ejemplos más recientes | Citar un ataque de 2010 cuando hay uno similar de 2024 más relevante |
| **Material complementario** | Enlaces, lecturas adicionales, videos recomendados que enriquezcan | Agregar referencia a un paper seminal o un video técnico |
| **Refuerzo pedagógico** | Puntos donde una tabla resumen, un diagrama o una analogía mejorarían la comprensión | Explicar Diffie-Hellman sin la analogía de los colores (mezcla de pintura) |
| **Inclusión de código** | Donde hay teoría sin código Python que podría tener un ejemplo ejecutable | Explicar RSA matemáticamente sin mostrar la implementación en Python |

#### 3.2.2 Acción: Listar Oportunidades de Mejora
Se elabora una lista numerada con estructura:

```
M-001 | [Categoría] | [Ubicación exacta] | [Descripción de la mejora] | [Cambio propuesto]
```

**Regla fundamental:** Ninguna mejora puede implicar reducir, eliminar o simplificar texto existente. Solo se permite agregar contenido nuevo (párrafos, ejemplos, tablas, código, referencias). Si una mejora sugiere reemplazar algo, debe preservarse el texto original y añadirse el nuevo como complemento.

#### 3.2.3 Acción: Aplicar Mejoras
Se modifica el documento añadiendo cada mejora propuesta. Al finalizar, se marca la lista como verificada.

---

## 4. Flujo de Trabajo por Unidad

```
INICIO
  │
  ├── [1] Escribir versión inicial del documento siguiendo la estructura (sección 1)
  │       y las reglas de estilo (sección 2).
  │
  ├── [2] FASE I — REVISIÓN DE CORRECCIONES
  │     ├── 2.1 Revisar el documento completo (sección 3.1.1)
  │     ├── 2.2 Listar todas las correcciones encontradas (formato C-001)
  │     └── 2.3 Aplicar todas las correcciones en el documento
  │
  ├── [3] FASE II — REVISIÓN DE OPORTUNIDADES DE MEJORA
  │     ├── 3.1 Revisar el documento corregido (sección 3.2.1)
  │     ├── 3.2 Listar todas las mejoras propuestas (formato M-001)
  │     └── 3.3 Aplicar todas las mejoras (solo agregar, nunca reducir)
  │
  └── [4] Documento finalizado
```

---

## 5. Distribución Temática de las Unidades

Basado en el nombre de la asignatura «Optativa Profesional II (Gobernanza y Criptografía)» y las unidades ya existentes:

| Unidad | Título | Temas principales |
|--------|--------|-------------------|
| UDI (existente) | Introducción a la Seguridad Informática | Visión estratégica, CIA, espionaje industrial, estándares, GnuPG |
| UDII (existente) | Gobierno TI | Plan de seguridad, procesos de negocio, gestión de riesgos, ISACA CISM |
| UDIII (por crear) | Criptografía | Cifrado simétrico (AES), cifrado asimétrico (RSA, ECC), funciones hash, firmas digitales, PKI, TLS, criptografía en Python |
| UDIV (por crear) | Gobernanza Aplicada y Cumplimiento | Auditoría de seguridad, cumplimiento normativo (GDPR, PCI DSS, ISO 27001), blockchain y criptografía aplicada, continuidad del negocio, gobierno de datos |

---

## 6. Formato del Encabezado de Listas de Corrección/Mejora

Al final de cada plan, antes de considerar terminado el documento de unidad, se debe incluir un bloque con las listas de correcciones y mejoras aplicadas, con el siguiente formato:

```markdown
---

## Control de Revisiones

### Fase I — Correcciones Aplicadas

| ID | Categoría | Ubicación | Problema | Corrección |
|----|-----------|-----------|----------|------------|
| C-001 | ... | ... | ... | ... |

### Fase II — Mejoras Aplicadas

| ID | Categoría | Ubicación | Mejora | Cambio realizado |
|----|-----------|-----------|--------|-------------------|
| M-001 | ... | ... | ... | ... |

```

---

## 7. Notas Finales

- Este plan es un documento vivo: puede actualizarse si se identifican mejoras en el proceso mismo.
- Las listas de corrección y mejora de cada unidad deben conservarse dentro del mismo archivo de la unidad (al final) como evidencia del proceso de calidad.
- Ninguna mejora de la Fase II puede eliminar texto escrito en la versión corregida. Si se considera que algo sobra, debe añadirse una nota aclaratoria adicional, no borrarse.
