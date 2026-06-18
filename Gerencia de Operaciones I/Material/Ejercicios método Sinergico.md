# Ejercicios Prácticos: Método Sinérgico de Localización (Brown y Gibson)

**Instrucciones para el estudiante:** 
Como futuros administradores, su tarea es evaluar la ubicación óptima para dos plantas industriales distintas. Deben aplicar el algoritmo sinérgico para determinar la **Medida de Preferencia de Localización (MPL o IL)** de cada alternativa, considerando factores de supervivencia (críticos), eficiencia financiera (objetivos) y competitividad estratégica (subjetivos).

---

### Ejercicio 1: Planta de Envases Biodegradables "EcoPack"

**Contexto:** La empresa busca mitigar riesgos operativos y potenciar su imagen de sostenibilidad. Se han preseleccionado dos zonas principales. La gerencia ha definido un nivel de confianza **α = 0.80** (priorizando la estabilidad de costos).

#### 1. Factores Críticos (FC)
Factores indispensables. Si uno falla (0), la localización se descarta automáticamente.

| Localización | Energía Eléctrica | Agua Industrial | Uso de Suelo |
| :--- | :---: | :---: | :---: |
| **Zona A (Puerto)** | 1 | 1 | 1 |
| **Zona B (Interior)** | 1 | 1 | 1 |
| **Zona C (Residencial)** | 1 | 0 | 1 |

#### 2. Factores Objetivos (FO)
Costos anuales proyectados que impactan la rentabilidad.

| Localización | Costo del Lote | Mantenimiento | Construcción | Materia Prima |
| :--- | :---: | :---: | :---: | :---: |
| **Zona A** | $150,000 | $35,000 | $400,000 | $650,000 |
| **Zona B** | $90,000 | $40,000 | $350,000 | $720,000 |

#### 3. Factores Subjetivos (FS)
Evaluación cualitativa del entorno estratégico.

| Factor Subjetivo | Ponderación | Zona A | Zona B |
| :--- | :---: | :---: | :---: |
| **Impacto Ambiental (Imagen)** | 40% | Bueno (0.24) | Excelente (0.36) |
| **Facilidad de Transporte** | 35% | Excelente (0.32) | Regular (0.14) |
| **Servicios de Seguridad** | 25% | Regular (0.13) | Bueno (0.17) |

---

### Ejercicio 2: Ensambladora de Sensores Domóticos "SmartHome"

**Contexto:** El éxito de esta unidad productiva depende de la retención de talento humano especializado y la eficiencia logística. Para este análisis, la administración utiliza un nivel de confianza **α = 0.65**.

#### 1. Factores Críticos (FC)
Factores binarios de "todo o nada".

| Localización | Mano de Obra Técnica | Seguridad Zona | Energía Estable |
| :--- | :---: | :---: | :---: |
| **Ciudad Satélite** | 1 | 1 | 1 |
| **Parque Tecnológico** | 1 | 1 | 1 |
| **Zona Rural** | 0 | 1 | 1 |

#### 2. Factores Objetivos (FO)
Desglose mensual de costos operativos.

| Localización | Alquiler de Nave | Mantenimiento | Adecuación | Componentes |
| :--- | :---: | :---: | :---: | :---: |
| **Ciudad Satélite** | $12,000 | $4,500 | $25,000 | $110,000 |
| **Parque Tecnológico** | $18,000 | $3,500 | $30,000 | $95,000 |

#### 3. Factores Subjetivos (FS)
Criterios de percepción y beneficio cualitativo.

| Factor Subjetivo | Peso (Wj) | Ciudad Satélite | Parque Tecnológico |
| :--- | :---: | :---: | :---: |
| **Clima Social (Sindicatos)** | 0.30 | Bueno (0.21) | Excelente (0.3) |
| **Instituciones Educativas** | 0.40 | Excelente (0.4) | Excelente (0.4) |
| **Actitud de la Comunidad** | 0.30 | Regular (0.09) | Bueno (0.21) | 

---

### Tareas a realizar:
1. Calcule el **Factor Crítico (FC)** para cada alternativa.
2. Determine el valor relativo de los **Factores Objetivos (FO)** usando el método del recíproco de los costos totales.
3. Obtenga el valor relativo de los **Factores Subjetivos (FS)** mediante la suma ponderada.
4. Aplique la fórmula del algoritmo sinérgico: **IL = FC * [α(FO) + (1 - α)(FS)]**.
5. Justifique desde una perspectiva administrativa cuál es la mejor opción de localización.
