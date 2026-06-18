# Ejercicios Resueltos: Método Sinérgico de Localización

Como administradores, deben recordar que el Índice de Localización (IL) permite equilibrar los costos tangibles con las percepciones estratégicas, asegurando que la ubicación elegida no solo sea barata, sino viable y competitiva a largo plazo [1, 5, 6].

---

### Ejercicio 1: Planta de Ensamblaje de Scooters Eléctricos "MoveGreen"

**Caso:** La gerencia busca instalar su primera planta de ensamblaje. Se evalúan tres ubicaciones: **Ciudad Central**, **Zona Industrial** y **Periferia Norte**. El nivel de confiabilidad definido es **α = 0.70**.

#### 1. Factores Críticos (FC) [1, 7]
Indispensables: Energía Estable, Mano de Obra Técnica y Seguridad de la Zona.

| Ubicación | Energía | Mano de Obra | Seguridad | **FC Total** |
| :--- | :---: | :---: | :---: | :---: |
| **Ciudad Central** | 1 | 1 | 1 | **1** |
| **Zona Industrial** | 1 | 1 | 1 | **1** |
| **Periferia Norte** | 1 | 1 | 0 | **0** |

*Análisis: La Periferia Norte se descarta por falta de seguridad (FC = 0).*

#### 2. Factores Objetivos (FO) [7, 8]
Costos anuales operativos (USD):

| Concepto | Ciudad Central | Zona Industrial |
| :--- | :---: | :---: |
| Alquiler de Nave | $150,000 | $100,000 |
| Mantenimiento | $30,000 | $40,000 |
| Construcción/Adecuación| $200,000 | $260,000 |
| Costo de Componentes | $620,000 | $600,000 |
| **Costo Total (Ci)** | **$1,000,000** | **$1,000,000** |

**Cálculo del FO:**
*   Suma de Recíprocos: $(1/1,000,000) + (1/1,000,000) = 0.000002$
*   FO (Ciudad Central) = $(1/1,000,000) / 0.000002 = \mathbf{0.50}$
*   FO (Zona Industrial) = $(1/1,000,000) / 0.000002 = \mathbf{0.50}$

#### 3. Factores Subjetivos (FS) [2, 4]
Calificaciones dadas por el comité (Escala 0-1):

| Factor Subjetivo | Peso | Ciudad Central | Zona Industrial |
| :--- | :---: | :---: | :---: |
| Impacto Ambiental | 0.30 | 0.60 | 0.80 |
| Facilidad de Transporte | 0.40 | 0.90 | 0.50 |
| Calidad de Vida Empleados| 0.30 | 0.80 | 0.40 |
| **FS Total** | **1.0** | **0.78** | **0.56** |

*Cálculo FS Central: (0.3*0.6)+(0.4*0.9)+(0.3*0.8) = 0.78*

#### 4. Índice de Localización (IL) [4, 9]
Fórmula: $IL = FC \times [0.70(FO) + 0.30(FS)]$

*   **IL (Ciudad Central):** $1 \times [0.70(0.50) + 0.30(0.78)] = 0.35 + 0.234 = \mathbf{0.584}$
*   **IL (Zona Industrial):** $1 \times [0.70(0.50) + 0.30(0.56)] = 0.35 + 0.168 = \mathbf{0.518}$

**Resultado:** Se selecciona **Ciudad Central** por tener el mayor IL.

---

### Ejercicio 2: Fábrica de Textiles de Algodón Orgánico "PureFiber"

**Caso:** La administración evalúa dos regiones: **Valle Sur** y **Costa Este**. Se utiliza un **α = 0.50** para dar igual peso a los costos y a la estrategia cualitativa.

#### 1. Factores Críticos (FC) [1]
Indispensables: Suministro de Agua (proceso de teñido), Materia Prima Cercana y Permisos Ambientales.

| Región | Agua | Materia Prima | Permisos | **FC Total** |
| :--- | :---: | :---: | :---: | :---: |
| **Valle Sur** | 1 | 1 | 1 | **1** |
| **Costa Este** | 1 | 1 | 1 | **1** |

#### 2. Factores Objetivos (FO) [7, 8]
Costos mensuales operativos (USD):

| Concepto | Valle Sur | Costa Este |
| :--- | :---: | :---: |
| Arrendamiento Terreno | $12,000 | $20,000 |
| Seguros y Tasas | $5,000 | $8,000 |
| Mano de Obra Directa | $45,000 | $35,000 |
| Suministros Orgánicos | $88,000 | $107,000 |
| **Costo Total (Ci)** | **$150,000** | **$170,000** |

**Cálculo del FO:**
1.  Recíprocos: $1/150,000 = 0.00000667$; $1/170,000 = 0.00000588$
2.  Suma recíprocos: $0.00001255$
3.  **FO (Valle Sur):** $0.00000667 / 0.01255 = \mathbf{0.531}$
4.  **FO (Costa Este):** $0.00000588 / 0.01255 = \mathbf{0.469}$

#### 3. Factores Subjetivos (FS) [2]
Calificación (Excelente=1, Bueno=0.7, Regular=0.4):

| Factor Subjetivo | Peso | Valle Sur | Costa Este |
| :--- | :---: | :---: | :---: |
| Proximidad a Puerto | 0.50 | Regular (0.4) | Excelente (1.0) |
| Clima Social | 0.20 | Bueno (0.7) | Bueno (0.7) |
| Infraestructura Vial | 0.30 | Bueno (0.7) | Excelente (1.0) |
| **FS Total** | **1.0** | **0.55** | **0.94** |

*Cálculo FS Costa: (0.5*1.0)+(0.2*0.7)+(0.3*1.0) = 0.94*

#### 4. Índice de Localización (IL) [4]
Fórmula: $IL = FC \times [0.50(FO) + 0.50(FS)]$

*   **IL (Valle Sur):** $1 \times [0.50(0.531) + 0.50(0.55)] = 0.2655 + 0.275 = \mathbf{0.5405}$
*   **IL (Costa Este):** $1 \times [0.50(0.469) + 0.50(0.94)] = 0.2345 + 0.47 = \mathbf{0.7045}$

**Resultado:** Se selecciona **Costa Este**. A pesar de tener costos más altos (menor FO), su ventaja estratégica en logística y puertos (FS) la hace la mejor opción administrativa.