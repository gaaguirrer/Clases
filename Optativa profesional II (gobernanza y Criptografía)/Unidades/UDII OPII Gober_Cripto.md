<img src="../../Logo UNHSJM.jpeg" alt="Logo UNHSJM" width="800">

# Gobierno TI, Unidad II

## Índice de Contenido

- [Introducción](#introducción)
- [Desarrollo de Contenidos](#desarrollo-de-contenidos)
  - [El Plan de Seguridad](#el-plan-de-seguridad)
  - [Procesos de Negocio](#procesos-de-negocio)
  - [Gestión de Riesgos](#gestión-de-riesgos)
  - [Isaca CISM](#isaca-cism)
- [Autoevaluación](#autoevaluación)
- [Bibliografía y Webgrafía](#bibliografía-y-webgrafía)
- [Glosario](#glosario)

## Introducción

Cuando ocurre un ciberataque, muchos preguntan: "┬┐qué tecnología falló?". Pero la pregunta clave rara vez se hace: "┬┐quién decidió qué proteger y cómo?". La respuesta está en el **gobierno de seguridad**, y de eso trata esta unidad.

En la unidad anterior aprendimos los fundamentos de la seguridad de la información: la visión estratégica, los principios CIA, el espionaje industrial y los estándares internacionales. Ahora es momento de subir un escalón. La seguridad no puede ser un conjunto de acciones aisladas; necesita un gobierno que la dirija, que establezca políticas, asigne recursos y garantice que la organización no dependa de héroes o soluciones improvisadas.

El gobierno de TI (Tecnologías de la Información) aplicado a la seguridad es el marco que alinea la protección de los datos con los objetivos del negocio, que define quién decide qué riesgos se aceptan y quién responde cuando algo falla. ┬┐Cómo saber si una inversión en seguridad es suficiente? ┬┐Cuándo conviene aceptar un riesgo en lugar de mitigarlo? En esta unidad abordaremos cuatro elementos esenciales: cómo construir un **plan de seguridad** efectivo, por qué los **procesos de negocio** son el punto de partida, cómo se **gestionan los riesgos** de forma sistemática, y cómo el marco **CISM** de ISACA estructura profesionalmente la gestión de seguridad.

Prepárate para pensar como un director de seguridad, no solo como un técnico. Al final, serás capaz de diseñar un plan de seguridad básico y construir tu propia matriz de riesgos. Te invito a leer con atención los casos reales: cada uno encierra una lección que vale más que cualquier tecnología.

## Desarrollo de Contenidos

### El Plan de Seguridad

Un plan de seguridad es el documento maestro que define qué se va a proteger, cómo se va a proteger, quién es responsable y qué recursos se destinarán. No es una lista de compras tecnológicas; es una hoja de ruta estratégica que responde a las preguntas fundamentales de la organización.

#### Componentes esenciales de un plan de seguridad

- **Alcance y objetivos**: ┬┐Qué sistemas, datos y procesos cubre el plan? ┬┐Qué metas concretas persigue (ej. reducir incidentes en un 30% en 12 meses)?
- **Políticas de seguridad**: Directrices de alto nivel aprobadas por la dirección. Por ejemplo: "toda la información confidencial debe cifrarse en tránsito y en reposo".
- **Procedimientos**: Pasos detallados para ejecutar las políticas. Por ejemplo, el procedimiento para conceder acceso a un nuevo empleado.
- **Estándares**: Especificaciones técnicas obligatorias. Ejemplo: "el cifrado debe usar AES-256".
- **Directrices**: Recomendaciones flexibles que orientan sin imponer. Ejemplo: "se recomienda usar contraseñas de al menos 12 caracteres".
- **Asignación de roles y responsabilidades**: CISO, administradores, usuarios, comité de seguridad.
- **Presupuesto**: Recursos económicos y humanos asignados.
- **Métricas e indicadores**: KPIs que permitan medir la efectividad (tiempo medio de detección, tiempo medio de respuesta, número de incidentes, % de parches aplicados a tiempo).
- **Cronograma**: Hitos y plazos de implementación.

#### Ciclo de vida del plan: enfoque PHVA (Planificar-Hacer-Verificar-Actuar)

El ciclo de mejora continua, también conocido como ciclo Deming, es la base de los sistemas de gestión como ISO 27001:

1. **Planificar**: Diagnosticar la situación actual, identificar riesgos, definir objetivos y recursos.
2. **Hacer**: Implementar los controles y procedimientos definidos en el plan.
3. **Verificar**: Medir, auditar y revisar si los controles funcionan como se esperaba.
4. **Actuar**: Corregir desviaciones, ajustar el plan y mejorar continuamente.

**Ejemplo práctico:**
Una empresa mediana detecta que ha tenido tres incidentes de phishing en seis meses. En la fase *Planificar*, decide implementar MFA para todos los accesos remotos y formación trimestral. En *Hacer*, despliega MFA y ejecuta el primer taller. En *Verificar*, revisa los logs y descubre que el MFA bloqueó dos intentos de acceso sospechosos, pero la formación tuvo solo un 60% de asistencia. En *Actuar*, ajusta el horario de los talleres para mejorar la asistencia y añade simulaciones automáticas de phishing.

#### Caso real: plan de seguridad que funcionó

**JPMorgan Chase** invierte más de 600 millones de dólares al año en ciberseguridad y cuenta con un plan que abarca desde inteligencia de amenazas hasta formación continua. En 2014, tras sufrir una brecha que afectó a 76 millones de hogares, la dirección decidió no solo reparar el daño, sino transformar su enfoque. Crearon un comité de seguridad presidido por el CEO, duplicaron el equipo de seguridad e implementaron un plan de respuesta a incidentes probado trimestralmente. Desde entonces, no han sufrido brechas significativas, demostrando que un plan bien ejecutado da resultados.

#### Caso real: fracaso por falta de plan

**British Airways** fue multada con 20 millones de libras en 2020 por una brecha en 2018 que expuso datos de 400.000 clientes. La investigación reveló que la aerolínea no tenía un plan de seguridad actualizado, sus sistemas críticos carecían de segmentación y los parches se aplicaban con retrasos de hasta seis meses. La falta de un plan de seguridad (y de un gobierno que lo exigiera) convirtió un riesgo conocido en una multa millonaria.

### Procesos de Negocio

Un error común es pensar que la seguridad es una capa que se añade "al final" de un proyecto. La realidad es que la seguridad debe integrarse en los procesos de negocio desde su diseño. Si un proceso no es seguro, el negocio está en riesgo.

#### ┬┐Qué es un proceso de negocio?

Es un conjunto de actividades interrelacionadas que transforman entradas en salidas, generando valor para el cliente. Por ejemplo: contratación de personal, facturación, atención al cliente, gestión de proveedores. Cada proceso consume, genera o modifica información, y esa información debe protegerse.

**Proceso vs. Proyecto:** Un proyecto tiene inicio y fin (ej. "implementar un firewall"). Un proceso es continuo (ej. "gestionar accesos de empleados"). La seguridad debe vivirse como proceso, no como proyecto. Muchas organizaciones fallan porque tratan la seguridad como una lista de proyectos con fecha de fin, cuando el riesgo no se toma vacaciones.

#### Integración de seguridad en procesos clave

| Proceso de negocio | Riesgo principal si falla | Controles recomendados | KPI sugerido |
|---|---|---|---|
| Onboarding de empleados | Acceso sin autorización o excesivo | Aprobación del jefe, verificación de antecedentes, mínimo privilegio, MFA | % de accesos con MFA activado en < 24h |
| Offboarding / baja | Acceso residual de exempleados | Revocación automática de cuentas, revisión periódica de usuarios activos | Tiempo medio de revocación tras la baja |
| Gestión de proveedores | Fuga de información por terceros | Evaluación de seguridad precontractual, cláusulas de confidencialidad, auditorías periódicas | N┬░ de proveedores críticos auditados por año |
| Desarrollo de software | Vulnerabilidades en producción | SAST, análisis de dependencias, pruebas de penetración previas a producción | % de proyectos con análisis de seguridad integrado en el pipeline |

Cada paso de estos procesos debe tener un **por qué**. Por ejemplo, en el onboarding: la aprobación del jefe evita que un admin cree cuentas sin control; el mínimo privilegio reduce el daño si la cuenta se compromete; la revocación automática impide que un ex-empleado acceda meses después.

#### Seguridad por diseño (Security by Design)

Este principio establece que la seguridad debe considerarse en cada etapa del ciclo de vida de un sistema o proceso, no como un añadido posterior. Implica:

- **Definir requisitos de seguridad** al mismo tiempo que los requisitos funcionales.
- **Realizar modelado de amenazas** (*threat modeling*) para identificar riesgos potenciales antes de escribir código. Un marco práctico es **STRIDE**, que clasifica amenazas en seis categorías:

  | Categoría STRIDE | ┬┐Qué busca? | Ejemplo concreto |
  |---|---|---|
  | **S**poofing (suplantación) | Alguien se hace pasar por otro | Un atacante usa credenciales robadas para acceder como administrador |
  | **T**ampering (manipulación) | Modificación no autorizada de datos | Un empleado altera el monto de una factura antes de enviarla |
  | **R**epudiation (repudio) | Negar haber realizado una acción | Un usuario afirma no haber enviado un correo que sí envió |
  | **I**nformation Disclosure (revelación) | Fuga de información confidencial | Un bucket S3 mal configurado expone datos de clientes |
  | **D**enial of Service (denegación) | Indisponibilidad del sistema | Un DDoS contra la pasarela de pagos impide vender |
  | **E**levation of Privilege (elevación) | Obtener permisos superiores a los debidos | Un atacante pasa de usuario normal a administrador del sistema |

  Aplicar STRIDE al diseñar un proceso permite anticipar ataques y definir controles antes de que ocurran.

- **Aplicar el principio de mínimo privilegio** en cada interacción.
- **Documentar decisiones de seguridad** para auditorías futuras.

#### Caso de integración exitosa: DevSecOps en Amazon

Amazon integró la seguridad directamente en su pipeline de desarrollo (DevSecOps). Cada pieza de código, antes de llegar a producción, pasa por análisis estático automatizado (SAST), escaneo de dependencias vulnerables y pruebas de seguridad dinámicas. Si algo falla, el despliegue se bloquea automáticamente. Esto no ralentiza el desarrollo; lo acelera porque los problemas se detectan en minutos, no en semanas. El resultado: miles de despliegues diarios con un nivel de seguridad que antes requería auditorías manuales.

#### Caso de integración fallida: atención al cliente y PCI DSS

Una empresa de comercio electrónico permitía a sus agentes de atención al cliente ver el número completo de tarjetas de crédito en pantalla para "agilizar la resolución de quejas". Esto violaba PCI DSS (que exige enmascarar los dígitos, mostrando solo los últimos 4). Un agente descontento copió números de tarjetas y los vendió en foros clandestinos. La empresa fue multada y perdió la capacidad de procesar pagos durante tres meses. La lección: el proceso de atención al cliente no había sido diseñado con controles de confidencialidad; primó la "agilidad" sobre la seguridad.

#### Caso emblemático: fusión Marriott-Starwood

**Marriott International** sufrió en 2018 una brecha que expuso datos de 500 millones de clientes. La causa fue que el sistema de reservas de Starwood (cadena adquirida por Marriott) no había integrado controles de seguridad en sus procesos de desarrollo. Cuando Marriott integró los sistemas de Starwood, heredó también sus vulnerabilidades. La lección: la seguridad debe evaluarse en los procesos de fusiones y adquisiciones desde el primer día, no después de firmar el contrato.

#### Gobernanza de procesos

Cada proceso de negocio debe tener un **dueño** asignado, responsable de que los controles de seguridad se apliquen y se actualicen. El dueño reporta al comité de seguridad las desviaciones, los incidentes relacionados con el proceso y las métricas de cumplimiento. Este reporte debe ser periódico (trimestral o semestral) y documentado para auditorías. Sin esta estructura de gobierno, los controles se degradan con el tiempo y el proceso vuelve a ser inseguro.

### Gestión de Riesgos

La gestión de riesgos es el corazón del gobierno de seguridad. No se trata de eliminar todos los riesgos (eso es imposible), sino de identificarlos, evaluarlos y decidir cuáles aceptar, mitigar, transferir o evitar.

#### Conceptos fundamentales

- **Activo**: Algo que tiene valor para la organización (datos, sistemas, personas, reputación).
- **Amenaza**: Cualquier cosa que pueda causar daño a un activo (hacker, incendio, error humano).
- **Vulnerabilidad**: Debilidad que puede ser explotada por una amenaza (falta de parche, contraseña débil).
- **Impacto**: Consecuencia negativa si la amenaza materializa el riesgo.
- **Probabilidad**: Posibilidad de que el riesgo ocurra.

**Fórmula conceptual:**
```
Riesgo = Amenaza × Vulnerabilidad × Impacto
```

#### Ciclo de gestión de riesgos

La gestión de riesgos sigue un ciclo continuo de cinco fases:

1. **Identificar**: Catalogar activos, amenazas y vulnerabilidades. ┬┐Qué tenemos? ┬┐Qué puede salir mal?
2. **Analizar**: Estimar la probabilidad y el impacto de cada riesgo. ┬┐Qué tan probable es? ┬┐Qué tan grave sería?
3. **Evaluar**: Comparar el nivel de riesgo contra el apetito de riesgo de la organización. ┬┐Este riesgo es aceptable o exige tratamiento?
4. **Tratar**: Aplicar la estrategia adecuada (mitigar, transferir, aceptar, evitar). ┬┐Qué hacemos con él?
5. **Monitorear**: Revisar periódicamente los riesgos, los controles y el contexto. ┬┐Sigue siendo válida nuestra evaluación?

Este ciclo se repite de forma continua. Los riesgos cambian, los controles se degradan y el negocio evoluciona.

#### Riesgo inherente vs. residual

- **Riesgo inherente**: Nivel de riesgo antes de aplicar controles. Es el riesgo "en bruto".
- **Riesgo residual**: Nivel de riesgo que permanece después de implementar controles.

**Ejemplo:** Un servidor expuesto a internet tiene un riesgo inherente Alto. Tras aplicar un firewall, MFA y parches, el riesgo residual baja a Medio. Si la organización solo acepta riesgos Bajos, deberá añadir más controles. Si su apetito de riesgo es Medio, podrá aceptar el riesgo residual.

#### Apetito y tolerancia al riesgo

- **Apetito de riesgo**: Nivel de riesgo que la organización está dispuesta a aceptar en conjunto para alcanzar sus objetivos. Una startup fintech puede tener un apetito alto; un banco tradicional, muy bajo.
- **Tolerancia al riesgo**: Límite específico de desviación aceptable para cada riesgo. Por ejemplo: "El tiempo máximo de inactividad aceptable es de 4 horas."

#### Registro de riesgos (Risk Register)

Toda gestión de riesgos debe documentarse en un **registro de riesgos**, que incluye al menos:

| ID | Riesgo | Prob. | Impacto | Nivel | Controles existentes | R. Residual | Responsable | Próxima revisión |
|---|---|---|---|---|---|---|---|---|
| R01 | Fuga de datos por empleado interno | Media | Alto | Alto | DLP, MFA, formación anual | Medio | CISO | Dic 2025 |
| R02 | DDoS en plataforma de ventas | Alta | Medio | Alto | WAF, CDN escalable, seguro cibernético | Medio | Administrador de red | Trimestral |
| R03 | Fallo eléctrico en sala de servidores | Baja | Alto | Medio | UPS, generador, redundancia en nube | Bajo | Infraestructura | Anual |

Este registro vive y se actualiza; no es un documento que se archiva y se olvida.

#### Metodologías de análisis de riesgos

**Análisis cualitativo:**
Utiliza escalas descriptivas (Alto, Medio, Bajo) para evaluar probabilidad e impacto. Es rápido y útil para priorizar. Ejemplo de matriz con semáforo:

| Probabilidad \ Impacto | Bajo | Medio | Alto |
|---|---|---|---|
| Alta | ≡ƒƒí Medio | ≡ƒö┤ Alto | ≡ƒö┤ Crítico |
| Media | ≡ƒƒó Bajo | ≡ƒƒí Medio | ≡ƒö┤ Alto |
| Baja | ≡ƒƒó Bajo | ≡ƒƒó Bajo | ≡ƒƒí Medio |

Acción sugerida por nivel:
- **Crítico**: Mitigar o transferir de inmediato.
- **Alto**: Plan de tratamiento en los próximos 30 días.
- **Medio**: Monitorear y reevaluar periódicamente.
- **Bajo**: Aceptar o proceder con controles normales.

**Análisis cuantitativo:**
Asigna valores numéricos y monetarios. Utiliza métricas como:
- **SLE (Single Loss Expectancy)**: pérdida por un incidente individual.
- **ARO (Annualized Rate of Occurrence)**: frecuencia esperada al año.
- **ALE (Annualized Loss Expectancy)**: pérdida anual esperada = SLE × ARO.

**Ejemplo cuantitativo:**
Un servidor crítico tiene un SLE de 50.000 Γé¼ (costo de recuperación + pérdida de negocio) y se estima un ARO de 0.2 (un incidente cada 5 años). Entonces ALE = 50.000 × 0.2 = 10.000 Γé¼/año. Si un firewall cuesta 3.000 Γé¼/año y reduce la probabilidad a la mitad (nuevo ARO = 0.1, nuevo ALE = 5.000 Γé¼/año), se puede calcular el **ROSI (Return on Security Investment)**:

```
ROSI = (ALE antes ΓêÆ ALE después ΓêÆ Costo del control) / Costo del control
ROSI = (10.000 ΓêÆ 5.000 ΓêÆ 3.000) / 3.000 = 0.66 ΓåÆ 66%
```

Un ROSI positivo (mayor que 0) indica que la inversión en seguridad se justifica económicamente.

#### Estrategias de tratamiento de riesgos

1. **Mitigar**: Reducir la probabilidad o el impacto mediante controles (ej. instalar antivirus, cifrar datos).
2. **Aceptar**: Asumir el riesgo de forma consciente y documentada (ej. una web informativa sin datos sensibles puede aceptar cierto riesgo de disponibilidad).
3. **Transferir**: Pasar el riesgo a un tercero (ej. contratar un seguro cibernético o externalizar la seguridad a un MSSP).
4. **Evitar**: Eliminar la actividad que genera el riesgo (ej. dejar de almacenar datos de tarjetas de crédito si no son necesarios para el negocio).

#### Marcos de referencia

Las metodologías formales de gestión de riesgos están estandarizadas:
- **ISO/IEC 27005**: Guía de gestión de riesgos de seguridad de la información, alineada con ISO 27001.
- **NIST SP 800-30**: Guía para realizar evaluaciones de riesgo, ampliamente usada en el sector público estadounidense.
- **FAIR (Factor Analysis of Information Risk)**: Modelo cuantitativo abierto que descompone el riesgo en factores medibles.

Elegir un marco depende del sector, los requisitos normativos y la madurez de la organización. Lo importante es tener un método consistente, no importa cuál se elija.

#### Caso real de gestión de riesgos deficiente

**Caso SolarWinds (2020)**: La empresa SolarWinds, proveedora de software de monitorización, fue comprometida por atacantes que insertaron código malicioso en sus actualizaciones de producto. Esto afectó a 18.000 clientes, incluyendo agencias gubernamentales de EE.UU. El riesgo de la cadena de suministro era conocido, pero fue subestimado. SolarWinds no había evaluado adecuadamente el impacto de un ataque a su proceso de compilación y distribución de software. El costo: más de 2.000 millones de dólares en pérdidas para los afectados y la quiebra virtual de la confianza en el producto. La lección: ningún riesgo debe evaluarse de forma aislada; hay que considerar el efecto dominó sobre toda la cadena.

**Un caso más reciente:** En 2023, **MGM Resorts** sufrió un ataque de ransomware que paralizó sus casinos durante 10 días, con pérdidas estimadas de 100 millones de dólares. La causa fue un único clic en un enlace de phishing que los atacantes usaron para escalar privilegios. MGM había evaluado el riesgo de phishing como "Medio" y no implementó MFA en todos los accesos de administración. La subestimación del riesgo costó caro.

#### Ejemplo de buena gestión de riesgos

**Netflix** utiliza un enfoque llamado *Chaos Engineering*. Consiste en introducir fallos intencionadamente en sus sistemas (como el famoso *Chaos Monkey* que apaga servidores aleatoriamente) para probar la resiliencia. Esta práctica permite identificar vulnerabilidades antes de que los atacantes las exploten. Netflix ha aceptado que los fallos ocurrirán, y prefiere gestionarlos de forma controlada que esperar pasivamente. Además, transfiere los riesgos restantes mediante un seguro cibernético y mantiene un fondo de contingencia para respuesta a incidentes. Es un ejemplo de cómo una organización puede integrar el ciclo de gestión de riesgos en su cultura operativa.

### Isaca CISM

ISACA (Information Systems Audit and Control Association) es una asociación profesional internacional fundada en 1969, dedicada a la gobernanza, auditoría, control y seguridad de los sistemas de información. Su certificación **CISM (Certified Information Security Manager)** es una de las más prestigiosas para profesionales que gestionan, diseñan y supervisan programas de seguridad empresarial.

#### ┬┐Qué diferencia al CISM de otras certificaciones?

Mientras que el CISSP se enfoca en la arquitectura técnica de seguridad, el **CISM está orientado a la gestión y al gobierno**. No pregunta "cómo cifrar", sino "cómo decidir qué cifrar y cuánto invertir en ello". Está diseñado para quienes ocupan o aspiran a ocupar puestos como CISO, Director de Seguridad o Gerente de Riesgos.

#### El ecosistema ISACA

Además del CISM, ISACA ofrece otras certificaciones complementarias:
- **CISA (Certified Information Systems Auditor)**: enfocada en auditoría, control y aseguramiento de sistemas de información.
- **CRISC (Certified in Risk and Information Systems Control)**: centrada en la identificación y gestión de riesgos de TI.

Un profesional de gobierno de seguridad suele combinar CISM con CISA o CRISC según su rol. Mientras CISA audita los controles y CRISC cuantifica los riesgos, CISM los gobierna y dirige.

#### Los cuatro dominios del CISM

**Dominio 1: Gobierno de Seguridad de la Información (24%)**
Establece el marco de gobierno: alinear la seguridad con los objetivos del negocio, definir roles y responsabilidades, desarrollar estrategias y asegurar el respaldo de la alta dirección.

Preguntas clave:
- ┬┐La estrategia de seguridad está alineada con la estrategia del negocio?
- ┬┐Existe un comité de seguridad con representación de la dirección?
- ┬┐Se reportan los riesgos de seguridad al consejo directivo periódicamente?

**Dominio 2: Gestión de Riesgos de Seguridad de la Información (30%)**
Cubre todo el ciclo de gestión de riesgos: identificación, análisis, evaluación y tratamiento. Incluye la clasificación de activos, la identificación de amenazas y vulnerabilidades, y la selección de controles basados en el apetito de riesgo de la organización. Este dominio se conecta directamente con la sección de Gestión de Riesgos vista anteriormente en esta unidad.

Preguntas clave:
- ┬┐Cómo se clasifican los activos de información?
- ┬┐Cada cuánto se actualiza la matriz de riesgos?
- ┬┐Quién define y aprueba el apetito de riesgo de la organización?

**Dominio 3: Programa de Seguridad de la Información (27%)**
Se centra en la creación, gestión y mejora del programa de seguridad. Incluye la definición de métricas, la gestión de recursos, la concienciación y formación, y la gestión de proyectos de seguridad. Este dominio enlaza con el Plan de Seguridad abordado al inicio de la unidad.

Preguntas clave:
- ┬┐El programa de seguridad tiene métricas definidas y medibles?
- ┬┐Se reporta periódicamente la efectividad del programa?
- ┬┐Existe un presupuesto asignado y revisado anualmente?

**Dominio 4: Gestión de Incidentes de Seguridad de la Información (19%)**
Aborda la preparación, detección, respuesta y recuperación ante incidentes. Incluye la creación de equipos de respuesta (CSIRT), la realización de ejercicios y simulacros, y la gestión de la comunicación durante una crisis.

Preguntas clave:
- ┬┐Existe un plan de respuesta a incidentes documentado y probado?
- ┬┐Se realizan simulacros al menos una vez al año?
- ┬┐Está definida la cadena de comunicación y escalamiento ante una brecha?

#### Requisitos para obtener y mantener el CISM

- **Experiencia**: 5 años de experiencia laboral en gestión de seguridad de la información (no solo técnica). Se pueden eximir hasta 3 años si se poseen otras certificaciones (CISSP, CISA, CRISC) o una titulación universitaria superior equivalente.
- **Examen**: Consta de 150 preguntas tipo test en 4 horas, administrado en centros autorizados o en línea con supervisión.
- **Recertificación**: Se renueva cada 3 años acumulando 120 CPE (Continuing Professional Education) mediante conferencias, cursos formales, publicaciones o participación en comités profesionales.

#### Cómo CISM transforma una organización

Una empresa cuyo responsable de seguridad tiene formación CISM tiende a:
- Tomar decisiones basadas en riesgos, no en tecnología.
- Comunicar la seguridad en lenguaje de negocio (ROI, riesgo residual, impacto financiero).
- Establecer métricas que demuestren el valor de la inversión en seguridad.
- Obtener respaldo de la dirección para proyectos de seguridad.

**Ejemplo de informe ejecutivo con enfoque CISM:**
Un CISO con mentalidad CISM no presenta al consejo un listado de vulnerabilidades técnicas. Presenta un informe como este:

> *"Riesgos críticos actuales: 3 (reducidos de 5 el trimestre anterior). Riesgo residual general: Medio (dentro del apetito aprobado). Inversión solicitada: 200.000 Γé¼ para renovar el programa DLP (ROSI estimado: 85%). Incidentes mayores en el trimestre: 0. Cumplimiento normativo: 100% de los controles críticos operativos."*

Este lenguaje permite que el consejo (formado mayoritariamente por no técnicos) comprenda, apruebe y respalde las decisiones de seguridad.

#### Tabla comparativa: CISM vs CISSP

| Aspecto | CISM | CISSP |
|---------|------|-------|
| Enfoque principal | Gestión y gobierno | Arquitectura técnica |
| Público objetivo | CISO, gerentes de seguridad | Arquitectos, ingenieros, consultores |
| Requisito de experiencia | 5 años en gestión de seguridad | 5 años en 2 o más dominios de seguridad |
| Dominios | 4 (gobierno, riesgos, programa, incidentes) | 8 (desde criptografía hasta seguridad física) |
| Formato del examen | 150 preguntas, 4 horas | 125-175 preguntas, 4 horas (adaptativo) |
| Periodicidad de recertificación | 3 años (120 CPE) | 3 años (120 CPE) |
| Costo aproximado (examen) | 760 USD | 749 USD |
| Idioma del examen | Inglés (principal), otros disponibles | Inglés, japonés, chino, entre otros |

#### Caso de éxito: aplicación de CISM en Banco Santander

**Banco Santander** exige que su equipo de seguridad de alto nivel cuente con certificaciones como CISM o CISSP. En sus informes anuales de gobierno corporativo, el banco reporta explícitamente al consejo de administración los riesgos cibernéticos identificados, las medidas implementadas y el nivel de riesgo residual, siguiendo las mejores prácticas del Dominio 1 de CISM. Esto ha permitido que el consejo comprenda y apruebe las inversiones en seguridad. Este enfoque conecta directamente con el ciclo de gestión de riesgos y el plan de seguridad vistos anteriormente en la unidad: CISM integra ambos en un marco de gobierno coherente.

#### Caso de fracaso: falta de gobierno al estilo CISM

En 2022, una empresa de logística sufrió un ataque de ransomware que paralizó sus operaciones durante 15 días, con pérdidas superiores a 50 millones de dólares. La investigación reveló que el CISO reportaba al director de TI (no al consejo), no existía un comité de seguridad, y los riesgos cibernéticos no se incluían en los informes de gobierno corporativo. El consejo se enteró del riesgo el día del ataque. Una estructura de gobierno alineada con CISM (Dominio 1) habría garantizado que el consejo conociera el riesgo con antelación y aprobara medidas preventivas.

El CISM no es solo una certificación; es una mentalidad que transforma la seguridad de un centro de costo en un habilitador del negocio. Con esto cerramos los contenidos de la unidad. A continuación, pon a prueba lo aprendido con la autoevaluación.

## Autoevaluación

Lea cada pregunta, responda mentalmente y luego consulte el glosario o los conceptos si tiene dudas. Las respuestas no se entregan; son para su propio aprendizaje.

1. **Verdadero o falso:** STRIDE es un marco de modelado de amenazas que clasifica los riesgos en seis categorías: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service y Elevation of Privilege.
   *Respuesta: Verdadero. STRIDE permite anticipar ataques durante la fase de diseño de sistemas y procesos.*

2. **┬┐Cuál de los siguientes NO es un componente esencial de un plan de seguridad?**
   a) Políticas de seguridad
   b) Asignación de roles y responsabilidades
   c) Lista de proveedores de software
   d) Métricas e indicadores
   *Respuesta: c) Lista de proveedores de software. Aunque los proveedores se gestionan, no es un componente estructural del plan de seguridad.*

3. **Relacione cada estrategia de tratamiento de riesgos con su definición:**
   - Mitigar ΓåÆ (Reducir probabilidad o impacto mediante controles)
   - Transferir ΓåÆ (Pasar el riesgo a un tercero, como un seguro)
   - Aceptar ΓåÆ (Asumir el riesgo de forma consciente)
   - Evitar ΓåÆ (Eliminar la actividad que genera el riesgo)

4. **┬┐Qué es el registro de riesgos (risk register) y qué información mínima debe contener?**
   *Respuesta: Es un documento vivo que cataloga todos los riesgos identificados. Debe incluir al menos: ID, descripción del riesgo, probabilidad, impacto, nivel de riesgo, controles existentes, riesgo residual, responsable y fecha de próxima revisión.*

5. **┬┐Cuál de los cuatro dominios de CISM se enfoca en la alineación de la seguridad con los objetivos del negocio?**
   *Respuesta: Dominio 1 - Gobierno de Seguridad de la Información.*

6. **Caso práctico:** Una empresa invierte 5.000 Γé¼/año en un sistema DLP. El ALE del riesgo de fuga de datos antes del control es de 30.000 Γé¼/año, y después del control se reduce a 10.000 Γé¼/año. Calcule el ROSI y determine si la inversión se justifica.
   *Respuesta: ROSI = (30.000 ΓêÆ 10.000 ΓêÆ 5.000) / 5.000 = 15.000 / 5.000 = 3 = 300%. ROSI > 0, la inversión se justifica ampliamente.*

7. **Verdadero o falso:** En seguridad informática, un "proyecto" tiene inicio y fin, mientras que un "proceso" es continuo. Tratar la seguridad como proyecto en lugar de proceso es una práctica recomendada.
   *Respuesta: Falso. La seguridad debe gestionarse como un proceso continuo, no como un proyecto con fecha de fin. El riesgo no se toma vacaciones.*

8. **Mencione las tres certificaciones principales del ecosistema ISACA y el enfoque de cada una.**
   *Respuesta: CISM (gestión y gobierno de la seguridad), CISA (auditoría de sistemas de información), CRISC (gestión de riesgos de TI).*

9. **Explique con sus palabras la diferencia entre apetito de riesgo y tolerancia al riesgo.**
   *Respuesta esperada: El apetito de riesgo es el nivel general de riesgo que la organización está dispuesta a aceptar para alcanzar sus objetivos. La tolerancia al riesgo es el límite específico de desviación aceptable para cada riesgo individual (ej. "el tiempo máximo de inactividad aceptable es de 4 horas").*

10. **Reflexión final:** Muchas organizaciones invierten en tecnología de seguridad (firewalls, antivirus, EDR) pero descuidan el gobierno (políticas, roles, métricas, planificación). ┬┐Por qué cree que ocurre esto y qué consecuencias puede traer?
    *Respuesta abierta. Se espera que el estudiante mencione: la tecnología es tangible y fácil de comprar, mientras que el gobierno requiere tiempo, disciplina y cambio cultural. Las consecuencias incluyen: inversiones sin dirección, falsa sensación de seguridad, incapacidad de medir efectividad, y falta de preparación ante incidentes.*

Si obtuvo menos de 7 respuestas correctas, revise nuevamente las secciones de Plan de Seguridad, Procesos de Negocio, Gestión de Riesgos e Isaca CISM, así como los casos reales de cada sección.

## Bibliografía

Deutsch, V. E. (2022). *Ciberseguridad para directivos: Riesgos, control y eficiencia por medio del gobierno de la seguridad*. LID Editorial.

ISACA. (2022). *Manual de Revisión del CISM* (16┬¬ ed.). ISACA.

Piattini Velthuis, M. G. & Ruiz González, F. (2022). *Gobierno de las Tecnologías y Sistemas de Información* (2┬¬ ed.). RA-MA Editorial.

Postigo Palacios, A. (2020). *Seguridad informática* (Edición 2020). Editorial Paraninfo.

## Glosario

- **ALE (Annualized Loss Expectancy)**: Pérdida monetaria esperada por año debido a un riesgo específico. Se calcula como SLE × ARO.
- **Amenaza**: Cualquier circunstancia o evento que puede causar daño a un activo de información.
- **Apetito de riesgo**: Nivel de riesgo que una organización está dispuesta a aceptar en busca de sus objetivos.
- **ARO (Annualized Rate of Occurrence)**: Frecuencia esperada con la que ocurrirá un incidente en un año.
- **CISM (Certified Information Security Manager)**: Certificación profesional de ISACA enfocada en la gestión y gobierno de la seguridad de la información.
- **CSIRT (Computer Security Incident Response Team)**: Equipo especializado en la respuesta a incidentes de seguridad informática.
- **Gobierno de TI**: Marco de responsabilidades, procesos y políticas que aseguran que el uso de la tecnología está alineado con los objetivos del negocio.
- **Impacto**: Consecuencia negativa (financiera, reputacional, legal) de la materialización de una amenaza.
- **ISACA**: Asociación profesional internacional dedicada a la gobernanza, auditoría y seguridad de los sistemas de información (fundada en 1969).
- **KPI (Key Performance Indicator)**: Indicador clave de rendimiento que permite medir la efectividad de los controles o procesos de seguridad.
- **Matriz de riesgos**: Herramienta visual que cruza la probabilidad de un evento con su impacto para priorizar riesgos.
- **Mínimo privilegio**: Principio de seguridad que otorga a cada usuario o sistema únicamente los permisos necesarios para realizar su función.
- **Mitigar**: Aplicar controles para reducir la probabilidad o el impacto de un riesgo.
- **PHVA (Planificar-Hacer-Verificar-Actuar)**: Ciclo de mejora continua (Deming) aplicado a los sistemas de gestión de seguridad.
- **Plan de seguridad**: Documento estratégico que define los objetivos, políticas, recursos y cronograma para proteger los activos de información.
- **Proceso de negocio**: Conjunto de actividades interrelacionadas que transforman entradas en salidas generando valor para el cliente.
- **Riesgo inherente**: Nivel de riesgo antes de aplicar controles de seguridad.
- **Riesgo residual**: Nivel de riesgo que permanece después de implementar controles.
- **Security by Design**: Enfoque que integra la seguridad en cada etapa del desarrollo de sistemas y procesos desde su concepción.
- **SLE (Single Loss Expectancy)**: Pérdida monetaria asociada a un único incidente de seguridad.
- **Transferir**: Traspasar el riesgo a un tercero (seguro, outsourcing).
- **Vulnerabilidad**: Debilidad o fallo en un activo que puede ser aprovechado por una amenaza.
- **Zero Trust**: Modelo de seguridad que exige verificación continua de cada acceso, sin confianza automática en la red interna.
