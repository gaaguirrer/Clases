# Guía Completa: Análisis de Factibilidades en Proyectos de Software

## Introducción

Cuando se va a desarrollar un proyecto de software, es esencial evaluar si realmente es **posible** llevarlo a cabo. El análisis de factibilidades es un estudio que determina si el proyecto puede ser ejecutado exitosamente desde múltiples perspectivas. Se deben evaluar cuatro aspectos fundamentales en este ordem:

1. **Factibilidad Técnica**
2. **Factibilidad Operativa**
3. **Factibilidad Económica**
4. **Factibilidad Legal**

Este documento te guiará a través de cada una de estas factibilidades, explicando qué son, por qué son necesarias, cómo evaluarlas en pequeños y grandes negocios, qué preguntas hacer, y cómo presentarlas formalmente.

---

## 1. FACTIBILIDAD TÉCNICA

### 1.1 ¿Qué es la Factibilidad Técnica?

La factibilidad técnica es el análisis que determina si **existe o se puede adquirir la tecnología necesaria** para desarrollar, implementar y mantener el software propuesto. Se evalúa si el equipo de desarrollo tiene las capacidades técnicas, herramientas y recursos necesarios.

**En otras palabras:** ¿Tenemos los conocimientos, herramientas y equipamientos para hacer esto posible?

### 1.2 ¿Por qué se necesita?

- **Evita fracasos por falta de capacidad técnica:** Previene que se comience un proyecto que no se puede terminar.
- **Identifica dependencias tecnológicas:** Determina qué tecnologías externas se necesitan.
- **Planifica la inversión en infraestructura:** Quantifica cuánto cuesta en equipamientos y software.
- **Reduce riesgos técnicos:** Identifica problemas potenciales desde el inicio.

### 1.3 ¿Cuándo se usa?

Se realiza **al inicio del proyecto**, durante la fase de viabilidad. Es una de las primeras evaluaciones que se hacen antes de aprobar un proyecto.

### 1.4 Componentes de la Factibilidad Técnica

#### A. Hardware (Equipos de Cómputo)

**Equipo Cliente (Para usuarios del sistema)**
- Procesador, cantidad de núcleos y frecuencia
- Memoria RAM disponible
- Almacenamiento (disco duro/SSD)
- Pantalla (resolución, tamaño)
- Conectividad (red, Wi-Fi)

**Servidor de Base de Datos**
- Requerimientos mínimos (para que funcione)
- Requerimientos óptimos (para mejor rendimiento)
- Capacidad de almacenamiento necesaria

#### B. Software

- Sistema operativo requerido
- Base de datos necesaria
- Lenguajes de programación
- Frameworks y librerías

#### C. Conectividad e Infraestructura

- Tipo de conexión a internet
- Velocidad de conexión (Mbps)
- Ancho de banda necesario

### 1.5 Evaluación en Negocios Pequeños

En negocios pequeños, el análisis es más sencillo y se enfoca en:

1. **¿Con qué equipamientos contamos actualmente?**
   - Especificar exactamente qué computadoras tienen
   - Qué sistema operativo tienen
   - Cuánta RAM y almacenamiento disponible

2. **¿Qué tendríamos que comprar?**
   - ¿Se necesita un servidor? ¿Podemos usar la nube?
   - ¿Los equipos actuales son suficientes?
   - ¿Necesitamos licencias de software?

3. **¿Tiene el equipo los conocimientos?**
   - ¿Alguien sabe programar?
   - ¿Necesitamos contratar a alguien?

4. **¿Es accesible económicamente la inversión inicial?**
   - Comparar costo vs. beneficio simple

### 1.6 Evaluación en Negocios Grandes

En empresas grandes, el análisis es más complejo:

1. **Infraestructura Empresarial Existente**
   - Inventario detallado de equipos
   - Capacidad de los servidores actuales
   - Políticas de seguridad informática

2. **Escalabilidad**
   - ¿El sistema puede crecer si la empresa crece?
   - ¿Cuántos usuarios simultáneos soporta?
   - ¿Cuántos datos puede almacenar?

3. **Integración con sistemas existentes**
   - ¿Cómo se conecta con otros sistemas de la empresa?
   - ¿Se necesitan APIs o integraciones especiales?

4. **Seguridad y Cumplimiento**
   - ¿Cumple con estándares de seguridad?
   - ¿Se puede hacer backup y recuperación de datos?
   - ¿Hay redundancia en caso de caída?

5. **Soporte y Mantenibilidad**
   - ¿Hay equipo técnico disponible para mantenerlo?
   - ¿Se puede transferir a otros proveedores si es necesario?

### 1.7 Preguntas Clave para Determinar Factibilidad Técnica

**Preguntas Generales:**
1. ¿Cuál es la capacidad de procesamiento necesaria?
2. ¿Qué volumen de datos debe manejar el sistema?
3. ¿Cuántos usuarios accederán simultáneamente?
4. ¿Qué tasa de crecimiento se espera?

**Preguntas sobre Hardware:**
5. ¿El hardware actual es suficiente o necesita actualizarse?
6. ¿Se requiere infraestructura en la nube?
7. ¿Cuál es el costo total del hardware necesario?
8. ¿Dónde se alojará el servidor (on-premise o cloud)?

**Preguntas sobre Software:**
9. ¿Qué tecnologías de desarrollo se usarán?
10. ¿Se usarán lenguajes de programación estándar o especializados?
11. ¿Se requieren licencias pagadas o se puede usar software open-source?
12. ¿Con qué versiones de sistemas operativos será compatible?

**Preguntas sobre Recursos Humanos:**
13. ¿El equipo de desarrollo tiene experiencia con estas tecnologías?
14. ¿Se necesita capacitación?
15. ¿Hay suficiente personal para desarrollar y mantener el sistema?

### 1.8 Formato de Presentación - Factibilidad Técnica

## FACTIBILIDAD TÉCNICA: [Nombre del Sistema]

### Evaluación de Equipos Actuales

#### Hardware del Cliente
| Componente | Especificación Actual | Mínimo Requerido | Óptimo Recomendado | ¿Cumple? |
|------------|----------------------|------------------|-------------------|----------|
| Procesador | [especificar] | [requerimiento] | [recomendación] | ✓/✗ |
| Núcleos | [cantidad] | [cantidad] | [cantidad] | ✓/✗ |
| Frecuencia | [GHz] | [GHz] | [GHz] | ✓/✗ |
| RAM | [GB] | [GB] | [GB] | ✓/✗ |
| Almacenamiento | [GB/TB] | [GB/TB] | [GB/TB] | ✓/✗ |
| Sistema Operativo | [SO] | [SO] | [SO] | ✓/✗ |

#### Hardware del Servidor
| Componente | Especificación Mínima | Especificación Óptima |
|------------|----------------------|----------------------|
| Procesador | [especificar] | [especificar] |
| Núcleos | [cantidad] | [cantidad] |
| Frecuencia | [GHz] | [GHz] |
| RAM | [GB] | [GB] |
| Almacenamiento | [GB/TB] | [GB/TB] |

#### Software Requerido
| Componente | Versión Mínima | Versión Recomendada |
|------------|----------------|-------------------|
| Sistema Operativo Servidor | [versión] | [versión] |
| Base de Datos | [tipo/versión] | [tipo/versión] |
| Lenguaje de Programación | [lenguaje/versión] | [lenguaje/versión] |
| Frameworks | [framework/versión] | [framework/versión] |

#### Conectividad
| Aspecto | Requerimiento Mínimo | Recomendado |
|--------|---------------------|------------|
| Tipo de Conexión | [tipo] | [tipo] |
| Velocidad Bajada | [Mbps] | [Mbps] |
| Velocidad Subida | [Mbps] | [Mbps] |
| Ancho de Banda | [capacidad] | [capacidad] |

### Análisis de Brechas

1. **¿Qué tenemos?** Describir los equipos y software actual disponible.
2. **¿Qué nos falta?** Identificar deficiencias.
3. **¿Cómo lo resolvemos?** Proponer soluciones (compra, upgrade, outsourcing).

### Conclusión

Indicar si es **FACTIBLE, PARCIALMENTE FACTIBLE o NO FACTIBLE** desde el punto de vista técnico y por qué.

### 1.9 Ejemplo: Sistema de Matrícula

#### Para una Institución Educativa Pequeña

## FACTIBILIDAD TÉCNICA: Sistema de Matrícula

### Evaluación de Equipos Actuales

#### Hardware del Cliente (Administrativos)
| Componente | Actual | Mínimo Requerido | Cumple |
|------------|--------|------------------|---------|
| Procesador | i3 | i5 | ✓ |
| RAM | 8GB | 4GB | ✓ |
| SO | Windows 10 | Windows 10+ | ✓ |

#### Hardware del Servidor
Se propone usar **Azure Cloud** (alojamiento en la nube)

| Componente | Mínimo | Óptimo |
|------------|--------|--------|
| Procesador | Intel Xeon 4 núcleos | Intel Xeon 8 núcleos |
| RAM | 16GB | 32GB |
| Almacenamiento | 500GB | 1TB |

#### Software Requerido
| Componente | Versión |
|------------|---------|
| Base de Datos | SQL Server 2022 |
| Backend | .NET 8.0 |
| Frontend | React 18+ |
| SO Servidor | Windows Server 2022 |

#### Conectividad
| Aspecto | Requerimiento |
|--------|---------------|
| Conexión | Ethernet |
| Velocidad Bajada | 100 Mbps |
| Velocidad Subida | 100 Mbps |

#### Análisis de Brechas
1. **¿Qué tenemos?** La institución tiene 5 computadoras con i3-i5, Windows 10, 8GB RAM. Internet de 50 Mbps.
2. **¿Qué nos falta?** Velocidad de internet insuficiente (necesita 100 Mbps). No hay servidor local.
3. **¿Cómo lo resolvemos?** 
   - Contratar plan internet de 150 Mbps ($50 USD/mes)
   - Usar Azure Cloud para el servidor (pago mensual)
   - Las computadoras actuales son suficientes

**CONCLUSIÓN:** Factibilidad Técnica = **FACTIBLE**. La institución necesita upgradear internet y usar cloud, pero tecnológicamente es viable.

---

## 2. FACTIBILIDAD OPERATIVA

### 2.1 ¿Qué es la Factibilidad Operativa?

La factibilidad operativa evalúa si los **procesos, procedimientos y personas** de la organización pueden implementar y usar exitosamente el sistema. Se enfoca en el "cómo las personas usarán esto".

**En otras palabras:** ¿Las personas en la organización pueden aprender a usar esto y trabajar con ello día a día?

### 2.2 ¿Por qué se necesita?

- **Identifica resistencia al cambio:** Determina si la organización está lista para cambiar sus procesos.
- **Planifica la capacitación:** Cuantifica cuántas personas necesitan entrenamiento y de qué tipo.
- **Asegura la adopción:** Un buen software fracasa si la gente no lo usa.
- **Define soportes necesarios:** Qué tipo de ayuda técnica se necesitará después del lanzamiento.

### 2.3 ¿Cuándo se usa?

Se realiza **junto con la evaluación técnica** y continúa **durante toda la implementación**. Es crítica para el éxito del proyecto.

### 2.4 Componentes de la Factibilidad Operativa

#### A. Capacitación de Personal

**Identificar:**
- ¿Quién usará el sistema? (administrativos, docentes, estudiantes, directivos)
- ¿Qué nivel de conocimiento tiene actualmente?
- ¿Cuántas horas de capacitación necesita cada grupo?
- ¿En qué formato se hará la capacitación? (presencial, virtual, documentos)

#### B. Cambio de Procesos

- ¿Qué procesos actuales cambiarán?
- ¿Son cambios simples o complejos?
- ¿Hay resistencia esperada al cambio?

#### C. Soporte Técnico

- ¿Habrá un helpdesk disponible?
- ¿Cómo se reportan problemas?
- ¿Cuál es el tiempo de respuesta?

#### D. Estabilidad Operativa

- ¿El sistema es estable y confiable?
- ¿Hay redundancia en caso de fallos?
- ¿Se puede recuperar de errores?

#### E. Seguridad de la Información

- ¿Quién tiene acceso a qué información?
- ¿Cómo se protegen los datos?
- ¿Hay respaldo de información?

#### F. Interfaz de Usuario

- ¿Es intuitiva y fácil de usar?
- ¿Funciona bien en los dispositivos disponibles?
- ¿La pantalla es visible? (tamaño, resolución)

### 2.5 Evaluación en Negocios Pequeños

En pequeños negocios el análisis es directo:

1. **Capacitación Simple**
   - ¿El dueño o un responsable puede aprender rápido?
   - ¿Se necesita documentación o videos?
   - Tiempo estimado: 2-5 horas por persona

2. **Cambios de Proceso**
   - ¿Los cambios afectan significativamente cómo trabajan?
   - ¿Hay resistencia del personal?

3. **Soporte**
   - ¿Se contratan con un proveedor local o se pide ayuda por teléfono?
   - ¿Hay alguien en el negocio que sepa de tecnología?

4. **Interfaz**
   - ¿El sistema es fácil de usar para personal sin mucha experiencia técnica?

### 2.6 Evaluación en Negocios Grandes

En empresas grandes es más estructurada:

1. **Programa de Capacitación Formal**
   - Capacitadores profesionales designados
   - Programas estructurados por roles
   - Certificación de usuarios
   - Material de capacitación (manuales, videos, e-learning)

2. **Gestión del Cambio**
   - Plan de comunicación a toda la organización
   - Identificación de "power users" que canalicen el cambio
   - Estrategia para minimizar resistencia

3. **Centro de Soporte Dedicado**
   - Equipo helpdesk disponible
   - Sistema de tickets para reporte de problemas
   - SLA (Service Level Agreement) definidos
   - Base de datos de problemas y soluciones

4. **Seguridad Empresarial**
   - Políticas de acceso basadas en roles
   - Auditoría de acceso a datos sensibles
   - Encriptación de datos
   - Cumplimiento normativo

### 2.7 Preguntas Clave para Determinar Factibilidad Operativa

**Preguntas sobre Capacitación:**
1. ¿Cuántas personas usarán el sistema?
2. ¿Cuál es el nivel de experiencia técnica del personal?
3. ¿Cuántas horas de capacitación se necesitan por persona?
4. ¿Qué formato de capacitación es más efectivo para esta organización?
5. ¿Se necesitan manuales de usuario? ¿En qué idioma?

**Preguntas sobre Procesos:**
6. ¿Cuánto cambiarán los procesos actuales?
7. ¿Hay procesos que se pueden automatizar?
8. ¿Cuál es el nivel de resistencia esperado?
9. ¿Los líderes de la organización apoyan el cambio?

**Preguntas sobre Soporte:**
10. ¿Cuántas personas de soporte técnico se necesitan?
11. ¿Qué disponibilidad tendrá el soporte? (24/7, horario de oficina)
12. ¿Hay SLA (acuerdos de nivel de servicio) definidos?
13. ¿Se incluye capacitación de soporte técnico en el proyecto?

**Preguntas sobre Confiabilidad:**
14. ¿Qué es el tiempo de actividad esperado del sistema? (uptime)
15. ¿Hay un plan de recuperación ante desastres?
16. ¿Se hacen respaldos automáticos de datos?

**Preguntas sobre Seguridad:**
17. ¿Cuántos niveles de acceso diferentes existen?
18. ¿Quién puede ver qué información?
19. ¿Se registran las acciones de los usuarios? (auditoría)
20. ¿Cómo se protegen los datos sensibles?

### 2.8 Formato de Presentación - Factibilidad Operativa

## FACTIBILIDAD OPERATIVA: [Nombre del Sistema]

### 1. Capacitación de Personal

#### Usuarios del Sistema
| Grupo de Usuarios | Cantidad | Nivel Técnico Actual | Horas Capacitación | Formato | Responsable |
|-------------------|----------|----------------------|--------------------|---------|----|
| [especificar] | [número] | [bajo/medio/alto] | [horas] | [presencial/virtual] | [persona] |
| [especificar] | [número] | [bajo/medio/alto] | [horas] | [presencial/virtual] | [persona] |

#### Materiales de Capacitación
- [ ] Manuales de usuario en PDF
- [ ] Videos tutoriales
- [ ] Presentaciones
- [ ] Documentación técnica para administradores
- [ ] FAQs (Preguntas frecuentes)

### 2. Cambios de Procesos

#### Procesos Afectados
| Proceso Actual | Cambio Propuesto | Impacto (Alto/Medio/Bajo) | Riesgos |
|----------------|------------------|---------------------------|---------|
| [proceso] | [cambio] | [nivel] | [riesgos] |

#### Análisis de Resistencia al Cambio
- Nivel de Resistencia Esperado: [bajo/medio/alto]
- Razones principales: [listar]
- Estrategia de mitigación: [describir]

### 3. Soporte Técnico

#### Estructura de Soporte
| Aspecto | Descripción |
|--------|------------|
| Personas disponibles | [cantidad] |
| Horario disponible | [horario] |
| Canales de contacto | [teléfono/mail/ticket] |
| Tiempo de respuesta Nivel 1 | [tiempo] |
| Tiempo de respuesta Nivel 2 | [tiempo] |

### 4. Estabilidad y Confiabilidad

| Métrica | Valor Comprometido |
|--------|------------------|
| Tiempo de actividad (Uptime) | [%] |
| Tiempo de recuperación ante fallos (RTO) | [tiempo] |
| Pérdida de datos máxima permitida (RPO) | [datos] |
| Frecuencia de respaldos | [diaria/semanal] |

### 5. Seguridad de Información

#### Control de Acceso
| Rol | Datos Accesibles | Permiso Lectura | Permiso Escritura |
|-----|------------------|-----------------|-----------------|
| [rol] | [datos] | ✓/✗ | ✓/✗ |

#### Medidas de Seguridad
- Autenticación: [descripción]
- Encriptación: [descripción]
- Auditoría: [descripción]
- Respaldo: [descripción]

### 6. Interfaz de Usuario

| Aspecto | Evaluación | Notas |
|--------|-----------|-------|
| Facilidad de uso | [fácil/media/difícil] | [observaciones] |
| Intuitiva | [sí/no] | [observaciones] |
| Adaptada para equipo actual | [sí/no] | [observaciones] |
| Soporte para dispositivos móviles | [sí/no] | [observaciones] |

### Conclusión

Indicar si es **FACTIBLE, PARCIALMENTE FACTIBLE o NO FACTIBLE** desde el punto de vista operativo.

### 2.9 Ejemplo: Sistema de Matrícula

#### Para una Institución Educativa

## FACTIBILIDAD OPERATIVA: Sistema de Matrícula

### 1. Capacitación de Personal

#### Usuarios del Sistema
| Grupo | Cantidad | Nivel Técnico | Horas | Formato |
|-------|----------|----------------|-------|---------|
| Administrativos | 3 | Medio | 8 | Presencial |
| Docentes | 12 | Bajo | 4 | Virtual |
| Estudiantes | 350 | Bajo | 2 | Video + FAQ |
| Directivos | 2 | Medio | 6 | Presencial |

#### Materiales
- [x] Manual administrativos (PDF)
- [x] Videos de 5 min por función principal
- [x] FAQ en web del colegio
- [x] Documentación técnica

### 2. Cambios de Procesos

#### Procesos Afectados
| Proceso | Cambio | Impacto |
|---------|--------|---------|
| Matriculación | De presencial a online | Alto |
| Cambio de asignaturas | De formulario a sistema | Medio |
| Consulta de calificaciones | De físico a online | Medio |

#### Resistencia al Cambio
- Docentes mayores resistencia a usar sistema digital
- Estrategia: Capacitación extra + soporte técnico dedicado
- Cost: 2 horas extra de capacitación

### 3. Soporte Técnico

| Aspecto | Descripción |
|--------|------------|
| Personas | 1 administrativo + soporte externo |
| Horario | 7am - 3pm (horario escolar) |
| Contacto | Ext. 105 + email soporte |
| Respuesta Nivel 1 | 30 minutos |
| Respuesta Nivel 2 | 4 horas |

### 4. Estabilidad y Confiabilidad

| Métrica | Compromiso |
|--------|-----------|
| Uptime | 99.5% |
| RTO | 2 horas máximo |
| RPO | 1 hora de datos |
| Respaldos | Diarios a las 11pm |

### 5. Seguridad

#### Control de Acceso
| Rol | Datos | Lectura | Escritura |
|-----|-------|---------|----------|
| Estudiante | Sus calificaciones | ✓ | ✗ |
| Profesor | Sus estudiantes | ✓ | ✓ |
| Admin | Todo | ✓ | ✓ |

### Conclusión

**Factibilidad Operativa: FACTIBLE**

El personal puede ser capacitado. Los materi requieren cambios significativos pero manejables. Se requiere soporte dedicado.

---

## 3. FACTIBILIDAD ECONÓMICA

### 3.1 ¿Qué es la Factibilidad Económica?

La factibilidad económica analiza si el proyecto es **lucrativamente viable**. Se determina si los beneficios que genera el sistema superan los costos de desarrollo, implementación y mantenimiento.

**En otras palabras:** ¿Se gasta dinero en esto y luego se recupera ese dinero con beneficios?

### 3.2 ¿Por qué se necesita?

- **Justifica la inversión:** Demuestra por qué gastar dinero en el proyecto.
- **Planifica presupuesto:** Identifica cuánto invertir y en qué.
- **Mide rentabilidad:** Ayuda a decidir si continuar o cancelar el proyecto.
- **Attrae inversión:** Importante para conseguir financiamiento.

### 3.3 ¿Cuándo se usa?

Se realiza **al inicio del proyecto** y se **revisa periódicamente** durante el desarrollo. Es uno de los análisis más importantes para la aprobación del proyecto.

### 3.4 Componentes de la Factibilidad Económica

#### A. Costos de Desarrollo (Año 0)

Incluyen todo lo gastado en crear el sistema:
- Salarios de desarrolladores
- Salarios de diseñadores
- Herramientas de desarrollo
- Hardware de pruebas
- Capacitación del equipo
- Otros gastos

#### B. Costos de Implementación

- Instalación en el sitio del cliente
- Configuración de servidor
- Migración de datos
- Training de usuarios

#### C. Costos de Mantenimiento (Recurrentes)

Gastos mensuales o anuales:
- Hosting/servidor en la nube
- Licencias de software
- Soporte técnico
- Actualizaciones y parches

#### D. Beneficios y Ganancias

**Beneficios Cuantitativos (se puede medir en dinero):**
- Reducción de costos operativos
- Reducción de tiempo de procesos
- Aumento de ingresos
- Pago de cliente por usar el sistema

**Beneficios Cualitativos (difíciles de medir):**
- Mejor satisfacción de clientes
- Mejor imagen de marca
- Reducción de errores
- Mejor decisiones por mejor información

#### E. Indicadores Financieros

**Valor Actual Neto (VAN):**
- Suma de todos los ingresos futuros menos los costos, ajustados al valor presente
- Si VAN > 0: El proyecto es rentable
- Si VAN < 0: El proyecto pierde dinero

**Tasa Interna de Retorno (TIR):**
- Es el porcentaje de ganancia anual
- Debe ser mayor que la tasa de descuento (tasa del banco)
- Típicamente se busca TIR > 15-20%

**Payback Period:**
- ¿En cuántos años se recupera la inversión inicial?
- Generalmente debe ser < 3 años

### 3.5 Evaluación en Negocios Pequeños

En pequeños negocios es más simple:

1. **Costos Iniciales**
   - ¿Cuánto tengo que invertir ahora?
   - ¿Puedo pagarlo? ¿Necesito financiamiento?

2. **Beneficios Esperados**
   - ¿Cuánto dinero me ahorra cada mes?
   - ¿Cuánto dinero adicional genera?
   - ¿En cuánto tiempo recupero mi dinero?

3. **Análisis Simple**
   - Dividir inversión inicial entre beneficio mensual
   - Resultado = meses hasta recuperar inversión

**Ejemplo:** Si invierto $5,000 y gano $500 mensuales, en 10 meses recupero mi dinero.

### 3.6 Evaluación en Negocios Grandes

En empresas grandes es más detallado:

1. **Análisis Costo-Beneficio Detallado**
   - Proyectar los 3-5 próximos años
   - Incluir inflación e incrementos salariales
   - Considerar cambios en demanda

2. **Indicadores Financieros Complejos**
   - Calcular VAN con tasa de descuento real
   - Calcular TIR y comparar con costo de capital
   - Calcular ROI (Retorno sobre Inversión)
   - Análisis de sensibilidad (qué pasa si...)

3. **Escenarios Alternativos**
   - Escenario pesimista (si las cosas van mal)
   - Escenario probable (estimación realista)
   - Escenario optimista (si todo va perfecto)

4. **Período de Recuperación**
   - Payback period simple
   - Payback period descontado

### 3.7 Preguntas Clave para Determinar Factibilidad Económica

**Preguntas sobre Costos:**
1. ¿Cuál es el presupuesto total de desarrollo?
2. ¿Cuánto cuesta cada rol (desarrollador, diseñador, PM)?
3. ¿Cuál es el tiempo estimado de desarrollo?
4. ¿Qué costos recurrentes habrá (hosting, licencias)?
5. ¿Se necesita hardware nuevo?

**Preguntas sobre Beneficios:**
6. ¿Cuáles son los beneficios concretos del sistema?
7. ¿En dinero, cuánto vale cada beneficio?
8. ¿Cuándo comenzarán a generarse los beneficios?
9. ¿Los beneficios serán constantes o variables?
10. ¿Se pueden financiar parcialmente con venta del sistema?

**Preguntas sobre Viabilidad:**
11. ¿El VAN es positivo?
12. ¿La TIR supera el costo de capital?
13. ¿En cuántos años se recupera la inversión?
14. ¿Hay capacidad financiera para hacer la inversión?
15. ¿Qué nivel de riesgo hay en las proyecciones?

### 3.8 Formato de Presentación - Factibilidad Económica


## FACTIBILIDAD ECONÓMICA: [Nombre del Sistema]

### 1. Costos de Desarrollo (Año 0)

#### Personal
| Rol | Cantidad | Costo/Mes | Meses | Subtotal |
|-----|----------|-----------|-------|----------|
| [rol] | [número] | $[monto] | [meses] | $[total] |
| [rol] | [número] | $[monto] | [meses] | $[total] |
| **TOTAL PERSONAL** | | | | **$[TOTAL]** |

#### Hardware y Software
| Concepto | Cantidad | Costo Unitario | Subtotal |
|----------|----------|---|---|
| [concepto] | [número] | $[monto] | $[total] |
| **TOTAL HARDWARE/SOFTWARE** | | | **$[TOTAL]** |

#### Otros Gastos
| Concepto | Monto |
|----------|-------|
| [concepto] | $[monto] |
| [concepto] | $[monto] |
| **TOTAL OTROS** | **$[TOTAL]** |

**TOTAL COSTOS DE DESARROLLO: $[GRAN TOTAL]**

### 2. Costos Anuales de Mantenimiento (Año 1 en adelante)

| Concepto | Costo Mensual | Costo Anual |
|----------|---------------|------------|
| Servidor/Hosting | $[monto] | $[monto] |
| Licencias | $[monto] | $[monto] |
| Soporte técnico | $[monto] | $[monto] |
| Actualizaciones | $[monto] | $[monto] |
| **TOTAL MANTENIMIENTO** | **$[TOTAL]** | **$[TOTAL]** |

### 3. Beneficios Esperados

#### Beneficios Cuantitativos
| Beneficio | Valor Mensual | Valor Anual | Justificación |
|-----------|---------------|------------|---------------|
| [beneficio] | $[monto] | $[monto] | [explicación] |
| [beneficio] | $[monto] | $[monto] | [explicación] |
| **TOTAL BENEFICIOS** | **$[TOTAL]** | **$[TOTAL]** | |

#### Beneficios Cualitativos
- [beneficio cualitativo]
- [beneficio cualitativo]
- [beneficio cualitativo]

### 4. Proyección Financiera (5 años)

| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
|----------|-------|-------|-------|-------|-------|-------|
| **INGRESOS** | | | | | | |
| [concepto] | $0 | $[monto] | $[monto] | $[monto] | $[monto] | $[monto] |
| [concepto] | | $[monto] | $[monto] | $[monto] | $[monto] | $[monto] |
| **TOTAL INGRESOS** | **$0** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** |
| **COSTOS** | | | | | | |
| Desarrollo | $[TOTAL] | $0 | $0 | $0 | $0 | $0 |
| Mantenimiento | $0 | $[TOTAL] | $[TOTAL] | $[TOTAL] | $[TOTAL] | $[TOTAL] |
| **TOTAL COSTOS** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** |
| **FLUJO DE CAJA** | **-$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** | **$[TOTAL]** |

### 5. Indicadores Financieros

| Indicador | Cálculo | Resultado | Interpretación |
|-----------|---------|-----------|----------------|
| VAN | [fórmula] | $[resultado] | [interpretación] |
| TIR | [fórmula] | [%] | [interpretación] |
| Payback Period | [fórmula] | [años] | [interpretación] |
| ROI Año 5 | [fórmula] | [%] | [interpretación] |

### 6. Análisis de Sensibilidad

#### Escenario Pesimista (30% menos beneficios)
| Indicador | Valor |
|-----------|-------|
| VAN | $[resultado] |
| TIR | [%] |
| Payback | [años] |

#### Escenario Probable
| Indicador | Valor |
|-----------|-------|
| VAN | $[resultado] |
| TIR | [%] |
| Payback | [años] |

#### Escenario Optimista (30% más beneficios)
| Indicador | Valor |
|-----------|-------|
| VAN | $[resultado] |
| TIR | [%] |
| Payback | [años] |

### Conclusión

Indicar si es **VIABLE, CONDICIONALMENTE VIABLE o NO VIABLE** desde el punto de vista económico.

### 3.9 Ejemplo: Sistema de Matrícula

#### Para una Institución Educativa (Caso: Vender el Sistema)

## FACTIBILIDAD ECONÓMICA: Sistema de Matrícula

### 1. Costos de Desarrollo (Año 0)

#### Personal
| Rol | Cantidad | Costo/Mes | Meses | Subtotal |
|-----|----------|-----------|-------|----------|
| Desarrollador Backend | 2 | $400 | 18 | $14,400 |
| Diseñador UI/UX | 1 | $300 | 12 | $3,600 |
| Project Manager | 1 | $450 | 18 | $8,100 |
| QA/Testing | 1 | $250 | 6 | $1,500 |
| **TOTAL PERSONAL** | | | | **$27,600** |

#### Hardware y Software
| Concepto | Cantidad | Costo |
|----------|----------|-------|
| Licencias de desarrollo | 1 | $2,000 |
| Servidor de pruebas | 1 | $1,500 |
| **TOTAL** | | **$3,500** |

**TOTAL AÑO 0: $31,100**

### 2. Costos Anuales (Año 1+)

| Concepto | Costo Anual |
|----------|------------|
| Servidor cloud (Azure) | $1,800 |
| Soporte nivel 1 | $4,800 |
| Actualizaciones | $2,400 |
| **TOTAL** | **$9,000** |

### 3. Beneficios Esperados

#### Opción A: Para institución que usa el sistema internamente
| Beneficio | Valor Anual | Justificación |
|-----------|------------|---------------|
| Reducción pago terceros para matrícula | $8,000 | No pagar servicios externos |
| Reducción tiempo administrativo | $12,000 | 1 administrativo dedica 4 hrs/sem menos |
| Reducción errores/retrasos | $3,000 | Menos problemas = menos costos |
| **TOTAL** | **$23,000** | |

#### Opción B: Para empresa que vende el sistema
| Beneficio | Valor Anual | Justificación |
|-----------|------------|---------------|
| Venta del sistema (5 clientes) | $50,000 | $10,000 por cliente |
| Soporte técnico (5 clientes) | $12,000 | $2,400 por cliente anual |
| Mantenimiento/actualizaciones | $6,000 | Módulos adicionales |
| **TOTAL** | **$68,000** | |

### 4. Proyección (5 años) - Opción B (Venta)

| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
|----------|-------|-------|-------|-------|-------|-------|
| Ingresos por ventas | $0 | $50,000 | $80,000 | $100,000 | $100,000 | $120,000 |
| Ingresos por soporte | $0 | $12,000 | $24,000 | $36,000 | $48,000 | $60,000 |
| **TOTAL INGRESOS** | **$0** | **$62,000** | **$104,000** | **$136,000** | **$148,000** | **$180,000** |
| Desarrollo inicial | -$31,100 | $0 | $0 | $0 | $0 | $0 |
| Mantenimiento | $0 | -$9,000 | -$9,000 | -$9,000 | -$9,000 | -$9,000 |
| Personal soporte | $0 | -$15,000 | -$20,000 | -$25,000 | -$30,000 | -$35,000 |
| **TOTAL COSTOS** | **-$31,100** | **-$24,000** | **-$29,000** | **-$34,000** | **-$39,000** | **-$44,000** |
| **FLUJO DE CAJA** | **-$31,100** | **$38,000** | **$75,000** | **$102,000** | **$109,000** | **$136,000** |

### 5. Indicadores Financieros

| Indicador | Resultado | Interpretación |
|-----------|-----------|----------------|
| VAN (tasa 10%) | $258,547 | **Muy rentable** |
| TIR | 82% | **Excelente retorno** |
| Payback | 0.8 años | **Menos de 1 año** |
| ROI Año 5 | 338% | **Muy positivo** |

### Conclusión

**Factibilidad Económica: MUY VIABLE**

El proyecto es altamente rentable con VAN positivo de $258,547, TIR de 82% y payback en menos de 1 año.

---

## 4. FACTIBILIDAD LEGAL

### 4.1 ¿Qué es la Factibilidad Legal?

La factibilidad legal evalúa si el proyecto **cumple con todas las leyes, regulaciones y normativas** aplicables. Se asegura que el sistema puede operarse legalmente sin violar derechos de terceros.

**En otras palabras:** ¿Podemos hacer esto legalmente o violaremos alguna ley?

### 4.2 ¿Por qué se necesita?

- **Evita problemas legales:** Previne demandas por violación de leyes.
- **Protege propiedad intelectual:** Asegura que el código y diseño sean protegidos.
- **Cumple regulaciones:** Respeta leyes de protección de datos, privacidad, etc.
- **Establece acuerdos:** Define claramente responsabilidades y derechos de todas las partes.

### 4.3 ¿Cuándo se usa?

Se realiza **al inicio del proyecto** y **se revisa antes de lanzar**. Algunos aspectos legales continúan durante todo el ciclo de vida del sistema.

### 4.4 Componentes de la Factibilidad Legal

#### A. Leyes de Protección de Datos

**Privacidad de Información:**
- ¿El sistema recopilará datos personales?
- ¿Cumple con leyes de protección (GDPR, Local Privacy Laws)?
- ¿Se obtiene consentimiento de los usuarios?

**Confidencialidad:**
- ¿Cómo se protegen los datos?
- ¿Quién puede acceder?
- ¿Se cifran los datos?

#### B. Derechos de Propiedad Intelectual

**Derecho de Autor (Copyright):**
- ¿El código es original o usa código de terceros?
- ¿Se protege el código bajo copyright?
- ¿Se respetan los derechos de terceros?

**Patentes de Software:**
- ¿El sistema incluye tecnología patentada?
- ¿Se necesita licencia de patentes?
- ¿Se puede patentar el sistema?

#### C. Licencias de Software

**Open Source:**
- ¿Se usa código open-source?
- ¿Qué licencia tiene (MIT, GPL, Apache)?
- ¿Se cumple con los términos de la licencia?

**Propietario:**
- ¿El software será propietario?
- ¿Cuánto cuesta la licencia?
- ¿Se restringe el uso?

#### D. Contratos y Acuerdos

**Contrato de Desarrollo:**
- ¿Hay acuerdo claro entre cliente y desarrollador?
- ¿Define resultados esperados, costos, fechas?
- ¿Define quién es dueño del código?

**Acuerdos de Servicio (SLA):**
- ¿Se define nivel de servicio esperado?
- ¿Hay penalizaciones por incumplimiento?

**Términos de Servicio:**
- ¿Los usuarios aceptan las condiciones?
- ¿Se define responsabilidad de cada parte?

#### E. Cumplimiento Normativo Sectorial

Dependiendo del sector:
- **Educación:** Protección de datos de estudiantes
- **Salud:** HIPAA u regulaciones de privacidad médica
- **Finanzas:** PCI DSS para datos de tarjetas
- **Gobierno:** Estándares de seguridad de gobierno

### 4.5 Evaluación en Negocios Pequeños

En pequeños negocios:

1. **Consulta Legal Simple**
   - ¿Se violarán leyes locales?
   - ¿Se pueden recopilar datos de clientes?
   - ¿Se necesita pedir permiso a alguien?

2. **Protección Básica**
   - ¿El código es registrado bajo copyright?
   - ¿Se firma contrato con cliente?
   - ¿Se tiene póliza de responsabilidad civil?

3. **Términos y Políticas**
   - ¿Hay Términos de Servicio?
   - ¿Hay Política de Privacidad?

### 4.6 Evaluación en Negocios Grandes

En empresas grandes:

1. **Departamento Legal Dedicado**
   - Abogados especializados en tecnología
   - Revisión exhaustiva de contratos
   - Análisis de riesgos legales

2. **Cumplimiento Normativo Complejo**
   - Auditorías de cumplimiento
   - Certificaciones (ISO, SOC2, etc.)
   - Inscripción ante reguladores

3. **Protección de Propiedad Intelectual**
   - Patentes de software
   - Copyright registrado
   - Secretos comerciales protegidos

4. **Acuerdos Multi-Parte**
   - Contratos con proveedores
   - Acuerdos de confidencialidad (NDA)
   - Contratos con empleados (propiedad intelectual)

### 4.7 Preguntas Clave para Determinar Factibilidad Legal

**Preguntas sobre Protección de Datos:**
1. ¿Qué datos personales recopilará el sistema?
2. ¿Cuál es la ley de protección de datos aplicable?
3. ¿Se obtiene consentimiento explícito de usuarios?
4. ¿Hay mecanismos de borrado de datos?
5. ¿Se realizan auditorías de seguridad?

**Preguntas sobre Propiedad Intelectual:**
6. ¿El código es completamente original?
7. ¿Se usa código open-source? ¿Qué licencia?
8. ¿Se registrará el código bajo copyright?
9. ¿Se solicitará patente de software?
10. ¿Quién es propietario del código? (cliente/desarrollador)

**Preguntas sobre Licencias:**
11. ¿Se usarán bibliotecas de terceros?
12. ¿Se respetan los términos de licencia?
13. ¿Se necesita licencia de software pagada?
14. ¿El sistema será open-source o propietario?

**Preguntas sobre Contratos:**
15. ¿Hay contrato claro de desarrollo?
16. ¿Define expectativas, costos y fechas?
17. ¿Define responsabilidades de cada parte?
18. ¿Define quién es dueño del resultado?
19. ¿Hay acuerdos de confidencialidad (NDA)?

**Preguntas sobre Cumplimiento Normativo:**
20. ¿Se aplica alguna regulación especial a este sector?
21. ¿El sistema necesita certificaciones?
22. ¿Se requiere notificación a autoridades?

### 4.8 Formato de Presentación - Factibilidad Legal

## FACTIBILIDAD LEGAL: [Nombre del Sistema]

### 1. Análisis de Leyes Aplicables

#### Leyes de Protección de Datos

| Ley | Aplicable | Impacto | Medida de Cumplimiento |
|-----|-----------|--------|----------------------|
| [ley local de datos] | Sí/No | [impacto] | [medida] |
| [GDPR si aplica] | Sí/No | [impacto] | [medida] |
| [otra ley] | Sí/No | [impacto] | [medida] |

#### Datos Personales a Recopilar
- [tipo de dato]: [justificación]
- [tipo de dato]: [justificación]

#### Medidas de Protección
- Encriptación: [descripción]
- Acceso restringido: [descripción]
- Auditoría: [descripción]
- Retención: [descripción]

### 2. Propiedad Intelectual

#### Código Fuente
- [x] Completamente original
- [ ] Usa código open-source: [especificar licencia]
- [ ] Usa bibliotecas comerciales

#### Protección
- Copyright: [sí/no] - Registro: [número]
- Patente: [sí/no] - Solicitud: [número]
- Secreto comercial: [sí/no] - Medidas: [descripción]

#### Derechos de Propiedad
| Elemento | Dueño | Justificación |
|----------|-------|---------------|
| Código | [cliente/desarrollador] | [razón] |
| Diseño | [cliente/desarrollador] | [razón] |
| Documentación | [cliente/desarrollador] | [razón] |

### 3. Licencias de Software

#### Software Open-Source Utilizado
| Nombre | Licencia | Cumplimiento |
|--------|----------|------------|
| [nombre] | [licencia] | ✓/✗ |
| [nombre] | [licencia] | ✓/✗ |

#### Software Comercial Utilizado
| Nombre | Licencia | Costo Anual | Comercializab |
|--------|----------|----------|------------|
| [nombre] | [tipo] | $[costo] | Sí/No |

#### Modelo de Licencia del Sistema
- [ ] Open-source (especificar licencia: ___)
- [ ] Propietario (restringir uso)
- [ ] SaaS (acceso por suscripción)
- [ ] Freemium

### 4. Contratos y Acuerdos

#### Contrato de Desarrollo
- [x] Existe contrato escrito
- [ ] Define alcance del proyecto
- [ ] Define costos y cronograma
- [ ] Define derechos de propiedad
- [ ] Define responsabilidades
- [ ] Define penalizaciones por incumplimiento

#### Contrato de Mantenimiento/Soporte
- [x] Existe contrato
- [ ] Define SLA (nivel de servicio)
- [ ] Define disponibilidad
- [ ] Define tiempo de respuesta

#### Términos de Servicio
- [ ] Existe documento
- [ ] Define responsabilidades del proveedor
- [ ] Define responsabilidades del usuario
- [ ] Define limitación de responsabilidad
- [ ] Define ley aplicable y jurisdicción

#### Política de Privacidad
- [ ] Existe documento
- [ ] Describe datos recopilados
- [ ] Describe uso de datos
- [ ] Describe medidas de seguridad
- [ ] Describe derechos del usuario (acceso, borrado)

#### Acuerdo de Confidencialidad (NDA)
- [ ] Firmado por todas las partes
- [ ] Define información confidencial
- [ ] Define período de confidencialidad
- [ ] Define penalizaciones por violación

### 5. Cumplimiento Normativo Sectorial

#### Regulaciones Específicas del Sector
| Regulación | Requisito | Cumplimiento |
|-----------|----------|------------|
| [nombre] | [requisito] | ✓/✗ |
| [nombre] | [requisito] | ✓/✗ |

#### Certificaciones Necesarias
- [ ] ISO 27001 (Seguridad de Información)
- [ ] SOC 2 (Controles de servicio)
- [ ] HIPAA (Si aplica a salud)
- [ ] PCI DSS (Si maneja tarjetas)
- [ ] Otra: [especificar]

### 6. Riesgos Legales Identificados

| Riesgo | Probabilidad | Impacto | Medida Preventiva |
|--------|------------|--------|-----------------|
| [riesgo] | [alta/media/baja] | [impacto] | [medida] |
| [riesgo] | [alta/media/baja] | [impacto] | [medida] |

### 7. Documentos Legales Requeridos

- [x] Contrato de desarrollo: [archivo]
- [x] Términos de servicio: [archivo]
- [x] Política de privacidad: [archivo]
- [ ] Otras: [especificar]

### Conclusión

Indicar si es **FACTIBLE, PARCIALMENTE FACTIBLE o NO FACTIBLE** desde el punto de vista legal.


### 4.9 Ejemplo: Sistema de Matrícula

#### Para una Institución Educativa


## FACTIBILIDAD LEGAL: Sistema de Matrícula

### 1. Leyes Aplicables

#### Leyes de Protección de Datos

| Ley | Aplicable | Medida |
|-----|-----------|--------|
| Ley de Protección de Datos Personales de Nicaragua | Sí | Encriptación + Política Privacy |
| GDPR (si estudiantes EU) | No | N/A |
| Confidencialidad de educación | Sí | Acceso solo personal autorizado |

#### Datos Personales a Recopilar
- Número de cédula: Identificación única
- Nombres y apellidos: Identificación
- Correo electrónico: Comunicación
- Calificaciones: Evaluación académica
- Horarios: Organización

#### Protección de Datos
- Encriptación: Todas las contraseñas encriptadas con bcrypt
- Acceso: Solo administrativos y estudiantes propios datos
- Auditoría: Log de accesos cada 24 horas
- Retención: Datos padres actuales 5 años, históricos 10 años

### 2. Propiedad Intelectual

#### Código
- Completamente original
- Desarrollado por equipo interno UNP
- Copyright registrado en DNDA

#### Derechos de Propiedad
| Elemento | Dueño |
|----------|-------|
| Código fuente | UNP |
| Diseño | UNP |
| Documentación | UNP |

### 3. Licencias de Software

#### Software Open-Source
| Software | Licencia | Impacto |
|----------|----------|---------|
| .NET Framework | MIT | Permitido |
| React | BSD | Permitido |

#### Modelo del Sistema
- Propietario (UNP es único dueño)
- Para uso interno institucional

### 4. Contratos

#### Contrato de Desarrollo
- [x] Firmado entre UNP y Desarrolladores
- [x] Define alcance, costos, cronograma
- [x] Especifica que UNP es propietario
- [x] Define SLA post-implementación

#### Términos de Servicio
- Existe documento
- Define responsabilidades de UNP
- Define responsabilidades de estudiantes
- Define límites de responsabilidad

#### Política de Privacidad
- Publicada en web de UNP
- Explica qué datos se recopilan
- Explica cómo se usan
- Explica medidas de seguridad
- Explica derechos de estudiantes (acceso, corrección)

#### Acuerdo de Confidencialidad
- Firmado por personal accede a datos
- Prohíbe compartir información
- Define sanciones por violación

### 5. Regulaciones Especiales

#### Ley de Contraloría General (Nicaragua)
- [x] Cumple regulaciones de privacidad
- [x] Protege datos públicos
- [x] Permite auditoría externa

#### Certificaciones
- [ ] ISO 27001 (no aplica para institución pequeña)
- [x] Política de seguridad interna documentada

### 6. Riesgos Legales

| Riesgo | Probabilidad | Medida |
|--------|-----------|--------|
| Fuga de datos personales | Media | Encriptación + firewall |
| Acceso no autorizado | Baja | Autenticación + auditoría |
| Violación copyright | Baja | Código original, licencias respetadas |

### Conclusión

**Factibilidad Legal: FACTIBLE**

Sistema cumple con leyes de protección de datos, tiene derechos de propiedad claros, y contratos definidos.

---

## 5. RESUMEN: FORMATO DE PRESENTACIÓN COMPLETO

Cuando presentes tu evaluación de factibilidades, incluye en este orden:

### Estructura General del Documento

# EVALUACIÓN DE FACTIBILIDADES
## [NOMBRE DEL PROYECTO/SISTEMA]

**Fecha:** [fecha]
**Presentado por:** [nombre]
**Institución:** [institución]

---

## TABLA DE CONTENIDOS

1. Factibilidad Técnica
2. Factibilidad Operativa
3. Factibilidad Económica
4. Factibilidad Legal
5. Conclusión General

---

## 1. FACTIBILIDAD TÉCNICA

[Usar formato de la sección anterior]

### Conclusión Parcial: [FACTIBLE / PARCIALMENTE FACTIBLE / NO FACTIBLE]

---

## 2. FACTIBILIDAD OPERATIVA

[Usar formato de la sección anterior]

### Conclusión Parcial: [FACTIBLE / PARCIALMENTE FACTIBLE / NO FACTIBLE]

---

## 3. FACTIBILIDAD ECONÓMICA

[Usar formato de la sección anterior]

### Conclusión Parcial: [VIABLE / CONDICIONALMENTE VIABLE / NO VIABLE]

---

## 4. FACTIBILIDAD LEGAL

[Usar formato de la sección anterior]

### Conclusión Parcial: [FACTIBLE / PARCIALMENTE FACTIBLE / NO FACTIBLE]

---

## 5. CONCLUSIÓN GENERAL

### Matriz de Factibilidades

| Factibilidad | Estado | Observaciones |
|-------------|--------|---------------|
| Técnica | [sí/no] | [observación breve] |
| Operativa | [sí/no] | [observación breve] |
| Económica | [sí/no] | [observación breve] |
| Legal | [sí/no] | [observación breve] |

### Veredicto Final

**¿Es viable el proyecto?** [SÍ / NO / CON CONDICIONES]

**Justificación:** [Explicación clara en 3-5 líneas]

**Recomendaciones:**
1. [Primera recomendación]
2. [Segunda recomendación]
3. [Tercera recomendación]

**Próximos Pasos:**
- [ ] Aprobar proyecto
- [ ] Realizar cambios propuestos
- [ ] Rechazo del proyecto
- [ ] Evaluación en [fecha futura]

---

## 6. ASPECTOS IMPORTANTES A RECORDAR

### Al Evaluar Factibilidades Recuerda:

1. **Orden es importante:** Técnica → Operativa → Económica → Legal

2. **Sé específico:** No digas "computadora moderna", especifica RAM, procesador, etc.

3. **Adapta al contexto:** Pequeño negocio = análisis simple; Empresa grande = análisis complejo

4. **Incluye números:** Dinero, horas, personas, capacidades

5. **Identifica riesgos:** ¿Qué podría salir mal? ¿Cómo prevenirlo?

6. **Documenta todo:** Cada decisión debe estar argumentada

7. **Presenta alternativas:** ¿Se puede hacer de otra forma? ¿Cuál es mejor?

8. **Obtén datos reales:** No inventes especificaciones; investiga:
   - Costo real de desarrolladores en tu región
   - ¿Qué utilidad real proporciona?
   - ¿Qué leyes exactas aplican?

9. **Involucra expertos:** Consulta con:
   - Responsables técnicos (TI)
   - Responsables operativos (procesos)
   - Contadores/Finanzas
   - Abogados/Legal

10. **Revisa periódicamente:** Las factibilidades pueden cambiar con el tiempo

---

## 7. CHECKLIST PARA TU PRESENTACIÓN

Antes de presentar tu análisis de factibilidades, verifica que incluyas:

### Técnica
- [ ] Hardware actual especificado (procesador, RAM, SO)
- [ ] Hardware servidor con mínimos y óptimos
- [ ] Software requerido listado
- [ ] Conectividad/internet evaluado
- [ ] Brecha tecnológica identificada
- [ ] Soluciones propuestas

### Operativa
- [ ] Usuarios identificados and cantidad
- [ ] Horas de capacitación estimadas
- [ ] Materiales de capacitación planeados
- [ ] Procesos que cambiarán identificados
- [ ] Resistencia al cambio evaluada
- [ ] Soportetécnico planeado
- [ ] Seguridad de datos considerada

### Económica
- [ ] Costos de desarrollo especificados (salarios x meses)
- [ ] Costos de infraestructura identificados
- [ ] Costos de mantenimiento anuales
- [ ] Beneficios cuantitativos calculados
- [ ] Proyección 3-5 años presentada
- [ ] VAN, TIR, Payback calculados
- [ ] Análisis de sensibilidad realizado

### Legal
- [ ] Leyes de protección de datos evaluadas
- [ ] Datos personales a recopilar identificados
- [ ] Medidas de seguridad listadas
- [ ] Propiedad intelectual definida
- [ ] Software open-source evaluado
- [ ] Contratos considerados
- [ ] Riesgos legales identificados

---

**¡ÉXITO EN TU EVALUACIÓN DE FACTIBILIDADES!**

Recuerda: Una buena evaluación de factibilidades es la diferencia entre un proyecto exitoso y uno que fracasa.
