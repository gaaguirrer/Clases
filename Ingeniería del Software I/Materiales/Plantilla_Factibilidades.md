# Plantilla: Análisis de Factibilidades
## [NOMBRE DE TU PROYECTO]

---

## INFORMACIÓN GENERAL DEL PROYECTO

**Nombre del Proyecto:** [Escribe el nombre]

**Instituciones/Empresa:** [Nombre de dónde se implementará]

**Objetivos del Proyecto:** 
- [Objetivo 1]
- [Objetivo 2]
- [Objetivo 3]

**Público Objetivo:** [Quiénes usarán el sistema]

**Fecha de Evaluación:** [Fecha]

**Evaluado por:** [Tu nombre y grupo]

**Duración Estimada del Proyecto:** [Meses]

---

## TABLA DE CONTENIDOS

1. Factibilidad Técnica
2. Factibilidad Operativa
3. Factibilidad Económica
4. Factibilidad Legal
5. Conclusión General

---

## 1. FACTIBILIDAD TÉCNICA

### 1.1 Hardware Actual (Equipo Cliente)

**Computadoras Disponibles:**

| Componente | Especificación | Cantidad | Observaciones |
|------------|---|---|---|
| Procesador | [ej: Intel i5] | [número] | [notas] |
| Frecuencia | [ej: 2.5 GHz] | | |
| Núcleos | [número] | | |
| RAM | [ej: 8 GB] | [cantidad equip] | |
| Almacenamiento | [ej: 256 GB SSD] | [cantidad] | |
| Sistema Operativo | [ej: Windows 10] | [cantidad] | |

#### ¿Cumple los requisitos?
- [ ] Sí, todos los equipos cumplen
- [ ] Parcialmente, algunos equipos necesitan upgrade
- [ ] No, hay que comprar equipos nuevos

**Descripción:** [Explica si es suficiente o qué necesita mejorar]

---

### 1.2 Hardware Servidor

**¿Dónde se alojará el servidor?**

- [ ] Servidor local (on-premise) en la institución
- [ ] Servidor en la nube (Azure, AWS, Google Cloud)
- [ ] Hostingcompartido

**Especificaciones Requeridas:**

| Componente | Mínimo | Óptimo | Justificación |
|------------|--------|--------|--|
| Procesador | [ej: 4 núcleos] | [ej: 8 núcleos] | [por qué] |
| RAM | [ej: 16 GB] | [ej: 32 GB] | [por qué] |
| Almacenamiento | [ej: 500 GB] | [ej: 1 TB] | [por qué] |
| Sistema Operativo | [ej: Windows Server 2022] | [otro SO?] | [por qué] |
| Base de Datos | [ej: SQL Server] | [versión] | [por qué] |

**Costo Servidor:**
- Costo Inicial: $[monto]
- Costo Mensual: $[monto]
- O Costo Anual: $[monto]

---

### 1.3 Software Requerido

**Tecnologías a Utilizar:**

| Tecnología | Versión | Licencia | Costo | Justificación |
|--|--|--|--|--|
| [Lenguaje] | [ej: 8.0] | [GPL/MIT/Comercial] | $[monto] | [por qué la elegiste] |
| [Framework] | [versión] | [tipo] | $[monto] | [justificación] |
| [BD] | [versión] | [tipo] | $[monto] | [justificación] |

**Costo Total Licencias:** $[total]

**¿Es software open-source o commercial?**
- [ ] Completamente open-source (gratuito)
- [ ] Parcialmente open-source
- [ ] Principalmente comercial
- [ ] Mixto

---

### 1.4 Conectividad e Internet

**Conexión Actual:**

| Aspecto | Valor |
|--------|-------|
| Tipo de conexión | [Ethernet/Wi-Fi/4G] |
| Proveedor | [ej: Claro] |
| Velocidad bajada | [ej: 50 Mbps] |
| Velocidad subida | [ej: 50 Mbps] |
| Costo mensual | $[monto] |

**Requerimiento Mínimo:**

| Aspecto | Valor |
|--------|-------|
| Velocidad bajada | [Mbps] |
| Velocidad subida | [Mbps] |
| Disponibilidad | [ej: 99.5%] |
| Latencia máxima | [ej: 50ms] |

**¿Necesita upgrade?**
- [ ] No, la conexión actual es suficiente
- [ ] Sí, necesita upgrade a: [especificar]
- [ ] Costo upgrade: $[monto]/mes

---

### 1.5 Análisis de Brechas Tecnológicas

**¿Qué tenemos versus qué necesitamos:**

| Aspecto | Tenemos | Necesitamos | Brecha | Solución |
|--------|---------|------------|--------|----------|
| [hardware] | [situación] | [requisito] | [diferencia] | [solución] |
| [software] | [situación] | [requisito] | [diferencia] | [solución] |
| [internet] | [situación] | [requisito] | [diferencia] | [solución] |

**Inversión Inicial Requerida:**

| Concepto | Costo |
|----------|-------|
| Upgrade de hardware | $[monto] |
| Servidor/Hosting | $[monto] |
| Licencias de software | $[monto] |
| Herramientas de desarrollo | $[monto] |
| Otros gastos | $[monto] |
| **TOTAL INICIAL** | **$[TOTAL]** |

---

### 1.6 Conclusión Técnica

**¿Es técnicamente factible?**

- [ ] **FACTIBLE** - Se tiene o se puede obtener toda la tecnología necesaria
- [ ] **PARCIALMENTE FACTIBLE** - Se necesitan algunos upgrades/compras
- [ ] **NO FACTIBLE** - No se pueden cumplir los requisitos técnicos

**Justificación:** [Explica tu veredicto en 3-5 líneas]

**Riesgos Técnicos Identificados:**

| Riesgo | Probabilidad | Solución |
|--------|------------|----------|
| [riesgo 1] | [alta/media/baja] | [cómo prevenirlo] |
| [riesgo 2] | [alta/media/baja] | [cómo prevenirlo] |

---

## 2. FACTIBILIDAD OPERATIVA

### 2.1 Usuarios del Sistema

**¿Quiénes usarán el sistema?**

| Grupo de Usuarios | Cantidad | Nivel Técnico | Uso Principal |
|-------------------|----------|---------------|---|
| [grupo 1] | [número] | [bajo/medio/alto] | [qué hace] |
| [grupo 2] | [número] | [bajo/medio/alto] | [qué hace] |
| [grupo 3] | [número] | [bajo/medio/alto] | [qué hace] |

**Total de usuarios:** [número]

**Usuarios simultáneos máximos:** [número] (¿cuántos al mismo tiempo?)

---

### 2.2 Plan de Capacitación

**¿Cuántas horas de capacitación necesita cada grupo?**

| Grupo | Horas | Formato | Responsable | Cronograma |
|-------|-------|---------|---|---|
| [grupo] | [horas] | [presencial/virtual/ambos] | [quién dicta] | [cuándo] |
| [grupo] | [horas] | [presencial/virtual/ambos] | [quién dicta] | [cuándo] |

**Materiales de Capacitación que se Crearán:**
- [ ] Manual en PDF
- [ ] Videos tutoriales
- [ ] Presentación PowerPoint
- [ ] Material imprimible
- [ ] FAQ (Preguntas Frecuentes)
- [ ] Base de conocimiento en web
- [ ] Otros: [especificar]

**Costo de Capacitación:**

| Concepto | Costo |
|----------|-------|
| Horas capacitador | $[monto] |
| Materiales | $[monto] |
| Locación/Equipo | $[monto] |
| **TOTAL** | **$[TOTAL]** |

---

### 2.3 Cambios en Procesos

**¿Qué procesos cambiarán?**

| Proceso | Cómo es ahora | Cómo será con el sistema | Impacto | Dificultad |
|---------|--------------|------------------------|--------|-----------|
| [proceso 1] | [descripción] | [descripción] | [alto/medio/bajo] | [alta/media/baja] |
| [proceso 2] | [descripción] | [descripción] | [alto/medio/bajo] | [alta/media/baja] |

**Beneficios de los cambios:**
- [Beneficio 1]
- [Beneficio 2]
- [Beneficio 3]

**Desafíos esperados:**
- [Desafío 1]
- [Desafío 2]

---

### 2.4 Resistencia al Cambio

**¿Qué grupos pueden resistirse?**

| Grupo | Nivel Resistencia | Razones | Estrategia Mitigación |
|-------|-------------------|---------|-----|
| [grupo] | [alta/media/baja] | [por qué se resisten] | [qué hacer] |
| [grupo] | [alta/media/baja] | [por qué se resisten] | [qué hacer] |

---

### 2.5 Soporte Técnico

**¿Quién dará soporte después de lanzar?**

| Aspecto | Descripción |
|--------|------------|
| Personal disponible | [Nombre/Cantidad] |
| Horario | [ej: Lunes-Viernes 8am-5pm] |
| Contacto | [Teléfono/Email] |
| Tiempo de respuesta | [ej: 30 minutos] |
| Nivel 1 (Crítico) | [tiempo] |
| Nivel 2 (Mayor) | [tiempo] |
| Nivel 3 (Menor) | [tiempo] |

**¿Habrá soporte 24/7?**
- [ ] Sí, completo
- [ ] Sí, solo emergencias
- [ ] No, solo horario de oficina

**Costo Soporte Anual:** $[monto]

---

### 2.6 Seguridad de Información

**¿Cómo se protegen los datos?**

| Medida | Descripción | Responsable |
|--------|------------|---|
| Autenticación | [ej: Usuario + contraseña] | [quién] |
| Autorización | [ej: 4 niveles de acceso] | [quién] |
| Encriptación | [ej: HTTPS + datos cifrados] | [quién] |
| Respaldo | [ej: Diario a las 11pm] | [quién] |
| Auditoría | [ej: Log de accesos] | [quién] |

**¿Quién puede ver qué información?**

| Rol | Datos que Puede Ver | Puede Editar |
|-----|-------------------|---|
| [rol 1] | [datos] | Sí/No |
| [rol 2] | [datos] | Sí/No |
| [rol 3] | [datos] | Sí/No |

---

### 2.7 Interfaz de Usuario

**¿Es fácil de usar?**

| Aspecto | Calificación | Observaciones |
|--------|---|---|
| Está intuitiva | [5/5] | [notas] |
| Se ve bien | [5/5] | [notas] |
| Es rápida | [5/5] | [notas] |
| Funciona en móvil | [5/5] | [notas] |
| Accesible para discapacitados | [5/5] | [notas] |

---

### 2.8 Conclusión Operativa

**¿Es operativamente factible?**

- [ ] **FACTIBLE** - El personal puede aprender y usar el sistema
- [ ] **PARCIALMENTE FACTIBLE** - Con capacitación extra y apoyo
- [ ] **NO FACTIBLE** - Demasiada resistencia o complejidad

**Justificación:** [Explica tu decisión]

**Costo Operativo Anual (después de implementación):** $[monto]

---

## 3. FACTIBILIDAD ECONÓMICA

### 3.1 Costos de Desarrollo

**Salarios de Personal:**

| Rol | Cantidad | Salario/Mes | Meses | Subtotal |
|-----|----------|-------------|-------|----------|
| [rol 1] | [número] | $[monto] | [meses] | $[total] |
| [rol 2] | [número] | $[monto] | [meses] | $[total] |
| **TOTAL PERSONAL** | | | | **$[TOTAL]** |

**Hardware y Software:**

| Concepto | Cantidad | Costo/Unidad | Subtotal |
|----------|----------|---|---|
| [concepto] | [cantidad] | $[monto] | $[total] |
| [concepto] | [cantidad] | $[monto] | $[total] |
| **TOTAL HARDWARE/SW** | | | **$[TOTAL]** |

**Otros Gastos:**

| Concepto | Monto |
|----------|-------|
| [gasto 1] | $[monto] |
| [gasto 2] | $[monto] |
| **TOTAL OTROS** | **$[TOTAL]** |

**COSTO TOTAL DESARROLLO (AÑO 0): $[TOTAL]**

---

### 3.2 Costos de Mantenimiento (Anuales)

| Concepto | Costo/Mes | Costo/Año |
|----------|-----------|-----------|
| Servidor/Hosting | $[monto] | $[monto] |
| Licencias de software | $[monto] | $[monto] |
| Soporte técnico | $[monto] | $[monto] |
| Actualizaciones | $[monto] | $[monto] |
| **TOTAL MANTENIMIENTO** | **$[TOTAL]** | **$[TOTAL]** |

---

### 3.3 Beneficios Cuantitativos

**¿Qué dinero se ahorra o se gana?**

| Beneficio | Valor Mensual | Valor Anual | Justificación |
|-----------|--|--|--|
| [beneficio 1] | $[monto] | $[monto] | [por qué] |
| [beneficio 2] | $[monto] | $[monto] | [por qué] |
| **TOTAL BENEFICIOS** | **$[TOTAL]** | **$[TOTAL]** | |

**Beneficios Cualitativos (difíciles de medir):**
- [Beneficio]
- [Beneficio]
- [Beneficio]

---

### 3.4 Proyección Financiera (5 años)

| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
|----------|-------|-------|-------|-------|-------|-------|
| **INGRESOS** | | | | | | |
| [concepto] | $0 | $[monto] | $[monto] | $[monto] | $[monto] | $[monto] |
| [concepto] | $0 | $[monto] | $[monto] | $[monto] | $[monto] | $[monto] |
| **TOTAL INGRESOS** | **$0** | **$[T]** | **$[T]** | **$[T]** | **$[T]** | **$[T]** |
| **COSTOS** | | | | | | |
| Desarrollo | -$[TOTAL] | $0 | $0 | $0 | $0 | $0 |
| Mantenimiento | $0 | -$[TOTAL] | -$[TOTAL] | -$[TOTAL] | -$[TOTAL] | -$[TOTAL] |
| **TOTAL COSTOS** | **-$[T]** | **-$[T]** | **-$[T]** | **-$[T]** | **-$[T]** | **-$[T]** |
| **FLUJO DE CAJA** | **-$[T]** | **$[T]** | **$[T]** | **$[T]** | **$[T]** | **$[T]** |

---

### 3.5 Indicadores Financieros

**Calcula estos indicadores:**

| Indicador | Fórmula/Cálculo | Resultado | Interpretación |
|-----------|--|--|--|
| **VAN** (Valor Actual Neto) | [Cálculo] | $[resultado] | ¿Positivo o negativo? |
| **TIR** (Tasa Interna Retorno) | [Cálculo] | [%] | ¿Mayor que costo de capital? |
| **Payback Period** | años = inversión / beneficio anual | [años] | ¿Menos de 3 años? |
| **ROI** (Retorno Inversión) | (beneficio-costo)/costo | [%] | ¿Mayor que 20%? |

**¿Es rentable?**
- VAN > $0 = Sí es rentable
- TIR > 15% = Buena rentabilidad
- Payback < 3 años = Recuperación rápida

---

### 3.6 Análisis de Sensibilidad

**¿Qué pasa si las cosas no salen como se planea?**

| Escenario | VAN | TIR | Payback | Conclusión |
|-----------|-----|-----|---------|-----------|
| **Pesimista** (30% menos) | $[monto] | [%] | [años] | [viable/no viable] |
| **Probable** (estimación real) | $[monto] | [%] | [años] | [viable/no viable] |
| **Optimista** (30% más) | $[monto] | [%] | [años] | [viable/no viable] |

---

### 3.7 Conclusión Económica

**¿Es económicamente viable?**

- [ ] **VIABLE** - El proyecto genera beneficios mayores que costos
- [ ] **CONDICIONALMENTE VIABLE** - Solo si se cumplen ciertas condiciones
- [ ] **NO VIABLE** - Los costos superan los beneficios

**Justificación:** [Explica por qué]

**Recomendación Financiera:** [Qué harías: ejecutar, modificar, rechazar]

---

## 4. FACTIBILIDAD LEGAL

### 4.1 Leyes Aplicables

**¿Qué leyes afectan este proyecto?**

| Ley | ¿Aplica? | Impacto | Medida de Cumplimiento |
|-----|----------|--------|----------------------|
| [Ley de datos] | Sí/No | [impacto] | [cómo cumplir] |
| [Ley laboral] | Sí/No | [impacto] | [cómo cumplir] |
| [Ley tributaria] | Sí/No | [impacto] | [cómo cumplir] |

---

### 4.2 Protección de Datos Personales

**¿El sistema recopila datos personales?**

- [ ] Sí, muchos datos
- [ ] Sí, algunos datos
- [ ] No, datos anónimos

**¿Qué datos se recopilarán?**
- [Tipo de dato 1]: [Justificación]
- [Tipo de dato 2]: [Justificación]
- [Tipo de dato 3]: [Justificación]

**¿Se obtiene consentimiento de usuarios?**
- [ ] Sí, explícito
- [ ] Sí, implícito
- [ ] No se requiere
- [ ] Necesita mejorarse

**Medidas de Protección:**
- [Medida 1]
- [Medida 2]
- [Medida 3]

---

### 4.3 Propiedad Intelectual

**¿Quién es dueño del código?**

- [ ] Cliente (institución que compra)
- [ ] Desarrollador (quien lo hace)
- [ ] Compartido

**¿Es código original o reutiliza código existente?**

- [ ] 100% original
- [ ] Usa librerías open-source: [especificar]
- [ ] Compra código de terceros
- [ ] Mixto

**¿Se registrará el código?**

- [ ] Bajo copyright
- [ ] Como patente
- [ ] No se registra

---

### 4.4 Licencias de Software

**¿Se utilizan softwares con licencia?**

| Software | Licencia | Costo | Cumplimiento |
|----------|----------|-------|---|
| [software] | [tipo] | $[costo] | ✓/✗ |
| [software] | [tipo] | $[costo] | ✓/✗ |

**¿Se respetan los términos de las licencias?**
- [ ] Sí, completamente
- [ ] Parcialmente
- [ ] Necesita revisar

---

### 4.5 Contratos Necesarios

**¿Qué documentos legales se necesitan?**

- [ ] Contrato de Desarrollo (Cliente + Desarrollador)
- [ ] Contrato de Servicios (Soporte)
- [ ] Acuerdo de Confidencialidad (NDA)
- [ ] Términos de Servicio del sistema
- [ ] Política de Privacidad
- [ ] Otros: [especificar]

**¿Quién los preparará?**

| Documento | Responsable | Plazo |
|-----------|------------|-------|
| [documento] | [persona/abogado] | [cuándo] |

---

### 4.6 Riesgos Legales

**¿Qué riesgos legales existen?**

| Riesgo | Probabilidad | Impacto | Prevención |
|--------|------------|--------|-----------|
| [riesgo 1] | [alta/media/baja] | [grave/moderado/leve] | [cómo evitarlo] |
| [riesgo 2] | [alta/media/baja] | [grave/moderado/leve] | [cómo evitarlo] |

---

### 4.7 Conclusión Legal

**¿Es legalmente factible?**

- [ ] **FACTIBLE** - Se puede hacer respetando todas las leyes
- [ ] **PARCIALMENTE FACTIBLE** - Con algunas limitaciones legales
- [ ] **NO FACTIBLE** - Hay obstáculos legales importantes

**Justificación:** [Explica tu decisión]

**Acción Recomendada:** [Qué debes hacer]

---

## 5. CONCLUSIÓN GENERAL

### Matriz de Factibilidades

| Factibilidad | Estado | Condiciones/Comentarios |
|-------------|--------|---|
| **TÉCNICA** | Factible/Parcial/No | [notas] |
| **OPERATIVA** | Factible/Parcial/No | [notas] |
| **ECONÓMICA** | Viable/Condicional/No | [notas] |
| **LEGAL** | Factible/Parcial/No | [notas] |

### Veredicto Final

**¿SE DEBE EJECUTAR EL PROYECTO?**

- [ ] **SÍ** - Proceder a desarrollar
- [ ] **CONDICIONALMENTE** - Ejecutar si se cumplen ciertas condiciones
- [ ] **NO** - Rechazar el proyecto

**Justificación General:**
[Escribe 5-8 líneas resumiendo por qué es o no es factible en general]

### Condiciones o Restricciones

Si respondiste "Condicionalmente", especifica:
1. [Condición 1]
2. [Condición 2]
3. [Condición 3]

### Recomendaciones

1. [Recomendación 1]
2. [Recomendación 2]
3. [Recomendación 3]
4. [Recomendación 4]
5. [Recomendación 5]

### Próximos Pasos

- [ ] Aprobación de proyecto
- [ ] Realizar cambios sugeridos (especificar cuáles)
- [ ] Revisión de factibilidades en [fecha]
- [ ] Rechazo del proyecto
- [ ] Otra acción: [especificar]

---

## REFERENCIAS Y FUENTES

Documentos consultados o referencias usadas:
- [Referencia 1]
- [Referencia 2]
- [Referencia 3]

---

## ANEXOS

### Anexo A: Especificaciones Técnicas Detalladas

[Incluir información técnica adicional si es necesario]

### Anexo B: Detalles de Costos

[Incluir desglose detallado de costos]

### Anexo C: Documentos Legales

[Listar documentos legales adjuntos]

### Anexo D: Cartas de Apoyo

[Si existen cartas de instituciones o expertos]

---

**Fecha de Presentación:** __________________

**Firma del Evaluador:** __________________

**Nombre (Legible):** __________________

---

*Nota: Esta plantilla debe completarse con información específica de tu proyecto. Cada sección debe tener datos reales y números específicos, no genéricos.*
