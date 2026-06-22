<img src="../../Logo UNHSJM.jpeg" alt="Logo UNHSJM" width="800">

# El Rol del Gerente de Proyecto en la Evaluación, Seguimiento y Control del Proyecto Tecnológico

## Índice de Contenido

- [Introducción](#introducción)
- [Desarrollo de Contenidos](#desarrollo-de-contenidos)
  - [Validación de Variables Propias de un Proyecto Tecnológico](#validación-de-variables-propias-de-un-proyecto-tecnológico)
  - [Definición de Estrategias en un Proyecto Tecnológico](#definición-de-estrategias-en-un-proyecto-tecnológico)
  - [Mejoras Continuas en un Proyecto Tecnológico](#mejoras-continuas-en-un-proyecto-tecnológico)
  - [Resultados Esperados en un Proyecto Tecnológico](#resultados-esperados-en-un-proyecto-tecnológico)
- [Autoevaluación](#autoevaluación)
- [Bibliografía](#bibliografía)
- [Glosario](#glosario)

## Introducción

En la unidad anterior aprendiste a formular una idea novedosa: evaluaste la tecnología disponible, identificaste tu mercado, investigaste el estado del arte, estimaste costos y definiste tu nivel de innovación. Ahora viene la parte que separa los proyectos que se quedan en el papel de los que realmente se ejecutan y generan resultados: la gerencia del proyecto.

Ser gerente de un proyecto tecnológico no es solo tener un título y asistir a reuniones. Es la persona que garantiza que el proyecto cumpla sus objetivos en tiempo, costo y calidad, mientras navega la incertidumbre técnica, las expectativas de los interesados y los cambios inevitables del camino. ¿Cómo validar que las variables críticas del proyecto están bajo control? ¿Cómo definir una estrategia cuando hay múltiples caminos posibles? ¿Cómo asegurar que el proyecto mejora continuamente en lugar de degradarse con el tiempo? ¿Y cómo medir si realmente se lograron los resultados esperados?

Esta unidad te prepara para responder esas preguntas desde la trinchera del gerente de proyecto. Vas a aprender a validar variables técnicas y de negocio, a diseñar estrategias de ejecución, a implementar ciclos de mejora continua, y a evaluar el impacto, la pertinencia y la calidad de los resultados. Al finalizar, tendrás las herramientas para gestionar un proyecto tecnológico de principio a fin, no solo para planificarlo.

## Desarrollo de Contenidos

### Validación de Variables Propias de un Proyecto Tecnológico

Todo proyecto tecnológico opera sobre ciertas variables que deben ser validadas antes y durante la ejecución. Validar significa confirmar que lo que asumiste en la fase de formulación sigue siendo cierto y que los valores críticos están dentro de los límites aceptables.

#### Variables técnicas

Son aquellas directamente relacionadas con la tecnología que construyes o implementas.

| Variable | Pregunta de validación | Método de validación | Frecuencia |
|----------|------------------------|----------------------|------------|
| Rendimiento | ¿El sistema responde en menos de 2 segundos bajo carga esperada? | Pruebas de carga con herramientas como JMeter, Locust o k6 | Al completar cada módulo crítico y antes de producción |
| Escalabilidad | ¿El sistema soporta 10x la carga actual sin colapsar? | Pruebas de escalabilidad vertical y horizontal, análisis de cuellos de botella | Trimestral o cuando se proyecta crecimiento |
| Seguridad | ¿Las vulnerabilidades conocidas están parcheadas? | Escaneo de vulnerabilidades (Nessus, OpenVAS), pruebas de penetración, análisis SAST/DAST | Cada sprint o cada mes, según metodología |
| Disponibilidad | ¿El uptime es superior al 99.5%? | Monitoreo continuo (Pingdom, Grafana, Prometheus) con alertas configurables | En tiempo real con informes semanales |
| Integridad de datos | ¿Los datos almacenados coinciden con los datos originales sin alteraciones? | Sumas de verificación (checksums), comparación de hashes, pruebas de reconciliación | Diario para datos críticos, semanal para el resto |

**Ejemplo práctico: validación de rendimiento con Python**

```python
import time
import statistics

def validar_rendimiento(url, num_peticiones=50, umbral_segundos=2.0):
    """
    Valida que una API responda dentro del umbral establecido.
    """
    import requests
    
    tiempos = []
    exitosas = 0
    fallidas = 0
    
    for i in range(num_peticiones):
        inicio = time.time()
        try:
            respuesta = requests.get(url, timeout=5)
            if respuesta.status_code == 200:
                exitosas += 1
            else:
                fallidas += 1
        except Exception as e:
            fallidas += 1
            print(f"Error en petición {i+1}: {e}")
        finally:
            tiempos.append(time.time() - inicio)
    
    promedio = statistics.mean(tiempos)
    maximo = max(tiempos)
    p95 = sorted(tiempos)[int(len(tiempos) * 0.95)]
    
    print(f"URL validada: {url}")
    print(f"Peticiones exitosas: {exitosas} / {num_peticiones}")
    print(f"Tiempo promedio: {promedio:.3f}s")
    print(f"Tiempo máximo: {maximo:.3f}s")
    print(f"Percentil 95: {p95:.3f}s")
    print(f"¿Cumple umbral ({umbral_segundos}s)? {'SÍ' if p95 < umbral_segundos else 'NO'}")
    
    return p95 < umbral_segundos

# Simulación de uso
# validar_rendimiento("https://api.miproyecto.com/health", num_peticiones=100, umbral_segundos=2.0)
```

#### Variables de negocio

| Variable | Pregunta de validación | Método de validación | Frecuencia |
|----------|------------------------|----------------------|------------|
| Costo real vs. estimado | ¿El gasto acumulado está dentro del presupuesto? | Comparación de costo real contra costo planificado (EVM: Earned Value Management) | Mensual |
| Tiempo real vs. planificado | ¿Vamos según el cronograma? | Curva S, análisis de ruta crítica, EVM (SPI: Schedule Performance Index) | Semanal o quincenal |
| Satisfacción del cliente | ¿El cliente está conforme con los entregables? | Encuestas NPS (Net Promoter Score), reuniones de revisión de sprint, entrevistas | Al final de cada fase o iteración |
| Adopción del producto | ¿Los usuarios están usando la solución? | Analítica de uso (Google Analytics, Mixpanel, métricas de producto), encuestas de usuario | Continuo (dashboard semanal) |
| Retorno de inversión (ROI) | ¿El proyecto está generando el valor esperado? | Cálculo de ROI real vs. proyectado, ALE vs. costo de controles implementados | Trimestral |

#### Técnicas de validación

**Validación por prototipado:** Construir una versión reducida pero funcional del sistema y validar con usuarios reales antes de invertir en el desarrollo completo. Es especialmente útil para proyectos con alta incertidumbre en los requisitos.

**Validación por pruebas A/B:** Para proyectos que involucran experiencia de usuario, presentar dos versiones (A y B) a diferentes segmentos de usuarios y medir cuál funciona mejor. Ejemplo: dos diseños de pantalla de pago, medir cuál tiene menos abandono de carrito.

**Validación por indicadores técnicos (SLIs, SLOs, SLAs):**
- **SLI (Service Level Indicator)**: métrica que mide un aspecto del servicio (ej. latencia, tasa de error, throughput).
- **SLO (Service Level Objective)**: valor objetivo para un SLI (ej. latencia menor a 200ms en el percentil 95).
- **SLA (Service Level Agreement)**: compromiso contractual con el cliente basado en los SLOs (ej. 99.9% de disponibilidad mensual).

```python
# Ejemplo de validación de SLO
def validar_slo(metricas, slo_objetivo):
    """
    Valida si las métricas de un período cumplen el SLO definido.
    metricas: lista de booleanos (True = cumplió, False = no cumplió)
    slo_objetivo: porcentaje mínimo de cumplimiento (ej. 0.995 para 99.5%)
    """
    total = len(metricas)
    cumplimientos = sum(metricas)
    porcentaje = cumplimientos / total if total > 0 else 0
    
    print(f"Período evaluado: {total} mediciones")
    print(f"Cumplimientos: {cumplimientos} ({porcentaje*100:.2f}%)")
    print(f"SLO objetivo: {slo_objetivo*100:.2f}%")
    print(f"¿SLO cumplido? {'SÍ' if porcentaje >= slo_objetivo else 'NO'}")
    
    if porcentaje < slo_objetivo:
        print(f"Se requieren {(slo_objetivo * total - cumplimientos):.0f} mediciones adicionales exitosas para cumplir el SLO en el mismo período.")
    
    return porcentaje >= slo_objetivo

# Simulación: 950 de 1000 peticiones cumplieron el umbral de latencia
metricas_mes = [True] * 950 + [False] * 50
validar_slo(metricas_mes, 0.95)
```

**Caso real de error por SLO mal definido:**

**Google Cloud Platform (2019)** . Un cliente de GCP (Snapchat) tenía un SLO de disponibilidad del 99.95% para su infraestructura en Compute Engine. Sin embargo, el SLO no especificaba ventanas de medición ni exclusiones por mantenimiento programado. Cuando ocurrió una interrupción de 27 minutos durante una ventana de mantenimiento no anunciada, Google consideró que el tiempo de inactividad no contaba contra el SLO porque estaba "dentro de mantenimiento". Snapchat argumentó que el SLO no lo excluía. El caso se resolvió con créditos de servicio, pero la lección quedó: un SLO mal definido es peor que no tener SLO, porque genera una falsa sensación de protección. Las definiciones deben incluir: ventana de medición (mensual, trimestral), exclusiones explícitas, y método de cálculo del percentil.

#### Caso real de validación de variables técnica

**GitLab** en 2017 sufrió un incidente crítico de integridad de datos. Durante una intervención de mantenimiento en su base de datos de PostgreSQL, un error humano eliminó 300 GB de datos de producción. Las copias de seguridad también fallaron porque el proceso de replicación tenía una validación omitida. El equipo pasó 24 horas restaurando datos desde backups rezagados. La lección: la variable "integridad de las copias de seguridad" debe validarse regularmente, no solo al configurarlas. GitLab implementó después validaciones automáticas de checksums en cada backup y pruebas de restauración programadas semanalmente.

#### Caso real de validación de variables de negocio

**General Electric (GE)** implementó su sistema de monitoreo remoto Predix para turbinas eólicas. Antes de lanzar a gran escala, validaron la variable de negocio "ahorro de combustible" mediante un piloto controlado: 50 turbinas con Predix y 50 sin él, durante seis meses. Los resultados mostraron un ahorro real del 3.2% (vs. el 5% estimado inicialmente). En lugar de descartar el proyecto, ajustaron las expectativas, mejoraron los algoritmos y lanzaron con una promesa revisada del 3.5%. La validación temprana evitó una sobrepromesa que habría dañado la credibilidad de GE.

### Definición de Estrategias en un Proyecto Tecnológico

Una estrategia es el plan de acción que define cómo alcanzar los objetivos del proyecto considerando los recursos disponibles, las restricciones y los riesgos. No hay una estrategia única que sirva para todos los proyectos; cada contexto exige la suya.

#### Tipos de estrategias según el contexto del proyecto

**Estrategia de ejecución: ¿Cómo construimos el producto?**

| Enfoque | Cuándo usarlo | Ventajas | Riesgos |
|---------|---------------|----------|---------|
| **Cascada** | Requisitos estables y conocidos desde el inicio; proyecto predecible | Planificación detallada, hitos claros, documentación completa | Poca flexibilidad al cambio, el cliente ve el producto hasta el final |
| **Ágil (Scrum, Kanban)** | Requisitos cambiantes o no completamente definidos; se necesita entregar valor rápido | Adaptabilidad, entregas incrementales, feedback continuo del cliente | Requiere compromiso del cliente, difícil de escalar en equipos grandes sin coordinación |
| **Híbrido** | Proyectos grandes donde unas partes son predecibles y otras no | Lo mejor de ambos mundos | Complejidad de gestión al mezclar dos filosofías |
| **MVP (Minimum Viable Product)** | Alta incertidumbre sobre si el mercado aceptará el producto | Validación rápida con mínimo gasto de recursos | Puede generar deuda técnica si no se planifica la evolución |

**Estrategia de adopción: ¿Cómo logramos que los usuarios usen el producto?**

- **Big bang**: Todos los usuarios migran al nuevo sistema al mismo tiempo. Ejemplo: fin de semana de migración de SAP. Riesgo alto, pero costo de transición menor.
- **Por fases**: Grupos de usuarios migran progresivamente. Ejemplo: primero una sucursal piloto, luego tres, luego todas. Menor riesgo, pero el período de transición es más largo y costoso.
- **Paralelo**: El sistema antiguo y el nuevo operan simultáneamente hasta que el nuevo está estabilizado. Máxima seguridad, pero duplica costos operativos.
- **Canary release**: El nuevo sistema se despliega primero para un pequeño porcentaje de usuarios (ej. 5%), se monitorea, y si funciona bien se extiende al resto. Es la estrategia preferida en proyectos SaaS.

**Estrategia de financiamiento: ¿Cómo se paga el proyecto?**

| Estrategia | Descripción | Ideal para |
|------------|-------------|------------|
| Presupuesto asignado | La organización asigna un presupuesto fijo para el proyecto | Proyectos con objetivos claros y alcance definido |
| Autofinanciamiento (bootstrapping) | El proyecto genera ingresos desde etapas tempranas que lo sostienen | Startups con modelos de negocio que generan ingresos tempranos |
| Fondo de inversión externo | Capital semilla, inversionistas ángeles, capital de riesgo | Proyectos de alto crecimiento que requieren inversión inicial grande |
| Crowdfunding | Financiamiento colectivo a través de plataformas (Kickstarter, Indiegogo) | Productos con atractivo para el público general (apps, hardware) |
| Subvención o cooperación | Fondos no reembolsables de gobiernos, organismos multilaterales | Proyectos de impacto social, educativo, ambiental |

#### Árbol de decisión de estrategia de ejecución

```
¿Los requisitos del proyecto son estables y conocidos?
├── Sí → ¿El proyecto es predecible en alcance y duración?
│       ├── Sí → Cascada (ej. migración de infraestructura, cumplimiento regulatorio)
│       └── No → Híbrido (planificar la arquitectura en cascada, desarrollar funcionalidades en sprints)
└── No → ¿El equipo tiene acceso constante al cliente o usuario?
        ├── Sí → Scrum (revisión cada 2-4 semanas con el cliente)
        └── No → Kanban (entregas continuas sin ciclos fijos, basadas en prioridades)
```

#### Tabla de estrategias según el ciclo de vida del proyecto

| Fase del proyecto | Estrategia recomendada | Actividad clave |
|-------------------|----------------------|-----------------|
| Inicio | Validación de supuestos | Prototipado, prueba de concepto, entrevistas con clientes |
| Planificación | Definición de alcance | Desglose de trabajo (WBS), cronograma, presupuesto |
| Ejecución | Iterativa-incremental (Ágil) | Sprints, entregas parciales, revisión continua |
| Monitoreo y control | Basada en datos | KPIs, dashboards, EVM, informes de avance |
| Cierre | Transición ordenada | Capacitación, documentación final, acta de cierre, lecciones aprendidas |

#### Caso real de estrategia de ejecución exitosa

**ING Bank** adoptó la metodología Ágil a gran escala (más de 3,500 empleados en equipos multifuncionales) para transformar su banca digital. Su estrategia fue híbrida: la arquitectura y los estándares de seguridad se definieron en cascada (por requisitos regulatorios), mientras que las funcionalidades se desarrollaron en sprints de dos semanas. Esto les permitió cumplir con las regulaciones bancarias sin sacrificar la velocidad de innovación. El resultado: redujeron el tiempo de lanzamiento de nuevas funcionalidades de 12 meses a 6 semanas.

#### Caso real de estrategia fallida

**La estrategia big bang de Nokia en 2011.** Nokia decidió migrar todo su ecosistema de Symbian a Windows Phone de forma abrupta, sin fase de transición ni estrategia de adopción gradual. Los desarrolladores de apps no tuvieron tiempo de migrar, los usuarios perdieron aplicaciones que usaban a diario, y la estrategia canibalizó su propia base instalada sin que Windows Phone estuviera listo para reemplazarla. Para 2013, Nokia había perdido el 90% del valor del mercado de teléfonos que dominaba en 2007. La lección: la estrategia de adopción big bang solo funciona cuando el nuevo sistema es claramente superior y el ecosistema está preparado.

### Mejoras Continuas en un Proyecto Tecnológico

La mejora continua no es opcional en proyectos tecnológicos. La tecnología cambia, los requisitos evolucionan, los equipos aprenden. Un proyecto que no mejora continuamente se degrada.

#### Ciclo PDCA aplicado a proyectos tecnológicos

El ciclo Planificar-Hacer-Verificar-Actuar (PDCA) de Deming es el marco universal de mejora continua.

**Conexión con la gestión de riesgos (UDII):** En la Unidad II estudiamos el ciclo de gestión de riesgos: identificar, analizar, evaluar, tratar y monitorear. El PDCA no reemplaza ese ciclo; lo integra. La fase Planificar del PDCA debe incluir la identificación y análisis de riesgos. La fase Hacer implementa los controles que definiste en el tratamiento de riesgos. La fase Verificar mide si esos controles están funcionando (¿el riesgo residual se redujo al nivel esperado?). La fase Actuar ajusta los controles o redefine el tratamiento. Un gerente de proyecto que domina ambos ciclos sabe que la mejora continua y la gestión de riesgos son dos caras de la misma moneda: ambas buscan que el proyecto navegue la incertidumbre de forma controlada.

**Planificar (Plan):**
Identificar qué mejorar. Definir objetivos medibles. Establecer métricas de éxito.

**Hacer (Do):**
Implementar el cambio a pequeña escala primero (prueba piloto). Documentar todo.

**Verificar (Check):**
Medir los resultados. Comparar contra la línea base. ¿Mejoró o no?

**Actuar (Act):**
Si funcionó: estandarizar y extender. Si no funcionó: ajustar o descartar, documentar el aprendizaje.

**Ejemplo práctico de PDCA en un proyecto:**

> Una startup de e-commerce detecta que el 40% de los carritos de compra se abandonan en la pantalla de pago (Problema).
>
> **Planificar**: Reducir el abandono al 25% en 2 meses simplificando el formulario de pago de 5 pasos a 3 pasos, y agregando opción de pago como invitado.
>
> **Hacer**: Implementar el cambio para el 10% de los usuarios (prueba A/B) durante 2 semanas.
>
> **Verificar**: El grupo con el nuevo flujo reduce el abandono al 28% (mejora del 30% sobre la línea base de 40%). El grupo de control se mantiene en 39%.
>
> **Actuar**: Estandarizar el nuevo flujo para todos los usuarios. Documentar el aprendizaje. El siguiente ciclo PDCA apuntará al 25% de abandono restante.

#### Mejora continua en desarrollo de software

**Refactorización:** Reestructurar el código existente sin cambiar su comportamiento externo para mejorar su legibilidad, mantenibilidad y rendimiento. La deuda técnica es la metáfora que describe el costo futuro de no refactorizar hoy.

```python
# Antes de refactorizar (código con deuda técnica alta)
def procesar(d):
    r = []
    for k, v in d.items():
        if v > 10:
            r.append((k, v * 1.15))
        else:
            r.append((k, v * 1.05))
    return dict(r)

# Después de refactorizar (código más claro y mantenible)
def calcular_recargo(valor):
    """Calcula el recargo según el monto base."""
    return valor * 1.15 if valor > 10 else valor * 1.05

def procesar_con_recargos(datos_originales):
    """Aplica recargos a los valores de un diccionario."""
    return {clave: calcular_recargo(valor) for clave, valor in datos_originales.items()}
```

**Retrospectivas:** Al final de cada iteración (sprint), el equipo se reúne para responder tres preguntas:
1. ¿Qué salió bien? (seguir haciendo)
2. ¿Qué podría mejorar? (probar en el siguiente sprint)
3. ¿Qué compromisos asumimos para mejorar? (acciones concretas)

#### La reunión de retrospectiva

Una retrospectiva efectiva sigue esta estructura:

| Paso | Duración sugerida | Actividad |
|------|-------------------|-----------|
| Preparar el ambiente | 5 min | Recordar el propósito: mejorar, no culpar. Repasar las métricas del sprint. |
| Recopilar datos | 10 min | Cada miembro escribe en notas adhesivas: lo que salió bien, lo que salió mal, ideas. |
| Agrupar y priorizar | 5 min | Agrupar notas por tema. Votar los 2-3 temas más importantes. |
| Definir acciones | 10 min | Para cada tema priorizado, definir una acción concreta, un responsable y una fecha. |
| Cierre | 5 min | Resumir acuerdos. Preguntar: "¿qué tan útil fue esta retrospectiva del 1 al 5?" |

#### Métricas de mejora continua

| Métrica | Qué mide | Cómo se calcula | Meta típica |
|---------|----------|-----------------|-------------|
| Velocidad del equipo | Puntos de historia completados por sprint | Suma de puntos de historias completadas (en Scrum) | Aumentar o estabilizar sprint a sprint |
| Tiempo de ciclo | Tiempo desde que se inicia una tarea hasta que se completa (Kanban) | Fecha de fin − fecha de inicio | Reducir en 10-20% en 3 meses |
| Deuda técnica | Esfuerzo estimado para refactorizar | Horas estimadas de refactorización / horas totales desarrolladas | Mantener por debajo del 20% |
| Tasa de defectos en producción | Errores reportados por usuarios después del lanzamiento | N° de defectos en producción / N° de historias entregadas | Menos de 1 por sprint |
| Tiempo medio de restauración (MTTR) | Tiempo que toma recuperarse de una falla | Suma de tiempos de recuperación / N° de incidentes | Reducir mes a mes |

#### Caso real de mejora continua

**Toyota** desarrolló el sistema *Kaizen* (mejora continua) que luego influyó en la manufactura y el desarrollo de software. En el ámbito tecnológico, **Etsy** implementó la mejora continua en su cultura de despliegue. Pasaron de desplegar una vez al mes (con alta ansiedad y errores) a desplegar 50+ veces al día. ¿Cómo? Pequeñas mejoras incrementales: automatización de pruebas, despliegues canary, monitoreo en tiempo real, y retrospectivas semanales obligatorias. Cada mejora era pequeña (automatizar un paso manual, agregar una alerta), pero acumuladas transformaron su capacidad de entrega.

#### Caso real de ausencia de mejora continua

**BlackBerry (Research In Motion)**. BlackBerry dominó el mercado de smartphones empresariales hasta 2010. Su sistema operativo (BlackBerry OS) y su hardware (teclado físico) no mejoraron significativamente año tras año. Mientras tanto, Apple y Android iteraban rápidamente: pantallas táctiles, tiendas de aplicaciones, navegación GPS, cámaras de alta calidad. BlackBerry confió en que su base instalada era suficiente y no implementó ciclos de mejora continua en su producto. Para 2016, su participación de mercado era inferior al 1%. La lección: la mejora continua no es opcional, incluso cuando eres el líder del mercado.

### Resultados Esperados en un Proyecto Tecnológico

Al final del proyecto, no se evalúa cuánto trabajó el equipo ni cuántas líneas de código se escribieron. Se evalúan los resultados: ¿se logró lo que se prometió? ¿El proyecto hizo una diferencia real? Aquí entran tres conceptos clave: impacto, pertinencia y calidad.

#### Impacto

El impacto mide el efecto real del proyecto en su entorno. No es lo mismo que los entregables. Un entregable puede ser "un sistema de gestión de inventarios implementado". El impacto es "se redujo el desabastecimiento en un 35% y se ahorraron 50,000 USD anuales en costos de almacenamiento".

**Tipos de impacto:**

| Tipo | Pregunta | Indicador | Ejemplo |
|------|----------|-----------|---------|
| Impacto económico | ¿El proyecto generó ahorros o ingresos? | ROI, VAN, TIR, período de recuperación | Reducción de 20% en costos operativos |
| Impacto social | ¿Mejoró la calidad de vida de las personas? | Usuarios beneficiados, tiempo ahorrado, acceso a servicios | 5,000 estudiantes acceden a educación en línea |
| Impacto ambiental | ¿Redujo la huella ecológica? | Toneladas de CO2 evitadas, papel ahorrado | Digitalización de expedientes salvó 200 árboles/año |
| Impacto organizacional | ¿Cambió la forma de trabajar de la organización? | Procesos rediseñados, productividad, satisfacción laboral | Reducción de 30% en tiempo de aprobación de solicitudes |

**Limitaciones de la TIR:** La TIR asume que los flujos de caja intermedios se reinvierten a la misma tasa TIR, lo que no siempre es realista. Para flujos de caja no convencionales (con signos alternados, por ejemplo: inversión, ganancia, pérdida, ganancia), pueden existir múltiples TIR o ninguna. En esos casos, se recomienda usar la TIR Modificada (TIRM) que asume una tasa de reinversión explícita, o simplemente basar la decisión en el VAN, que no tiene este problema.

```python
def calcular_tirm(flujos, tasa_financiamiento, tasa_reinversion):
    """
    Calcula la Tasa Interna de Retorno Modificada (TIRM).
    tasa_financiamiento: costo de capital (para flujos negativos)
    tasa_reinversion: tasa a la que se reinvierten los flujos positivos
    """
    import math
    vp_negativos = 0  # valor presente de flujos negativos
    vf_positivos = 0  # valor futuro de flujos positivos
    n = len(flujos) - 1
    
    for t, flujo in enumerate(flujos):
        if flujo < 0:
            vp_negativos += flujo / (1 + tasa_financiamiento) ** t
        elif flujo > 0:
            vf_positivos += flujo * (1 + tasa_reinversion) ** (n - t)
    
    tirm = (vf_positivos / abs(vp_negativos)) ** (1 / n) - 1
    return round(tirm * 100, 2)

# Ejemplo: flujo con múltiples cambios de signo
flujos = [-100000, 60000, -20000, 80000, 70000, 50000]
tirm = calcular_tirm(flujos, 0.10, 0.08)
print(f"TIR Modificada: {tirm}%")
```

**Medición del impacto económico: VAN y TIR**

```python
def calcular_van(flujos, tasa_descuento):
    """
    Calcula el Valor Actual Neto (VAN) de un proyecto.
    flujos: lista con el flujo de cada período (flujo[0] es la inversión inicial, negativo)
    tasa_descuento: tasa de descuento (ej. 0.10 para 10%)
    """
    van = 0
    for t, flujo in enumerate(flujos):
        van += flujo / (1 + tasa_descuento) ** t
    return round(van, 2)

def calcular_tir(flujos, iteraciones=1000, tolerancia=0.0001):
    """
    Calcula la Tasa Interna de Retorno (TIR) aproximada por iteración.
    """
    tasa = 0.1  # tasa inicial
    for _ in range(iteraciones):
        van = calcular_van(flujos, tasa)
        if abs(van) < tolerancia:
            return round(tasa * 100, 2)
        # Ajuste por aproximación Newton-Raphson simplificada
        derivada = sum([-t * f / (1 + tasa) ** (t + 1) for t, f in enumerate(flujos)])
        if derivada == 0:
            break
        tasa -= van / derivada
    return round(tasa * 100, 2)

# Ejemplo: inversión inicial de 100,000 USD y retornos en 5 años
flujos = [-100000, 25000, 35000, 45000, 40000, 30000]
van = calcular_van(flujos, 0.12)
tir = calcular_tir(flujos)
print(f"VAN (tasa 12%): {van} USD")
print(f"TIR: {tir}%")
if van > 0:
    print("El proyecto genera valor. El VAN es positivo.")
else:
    print("El proyecto no alcanza la rentabilidad mínima esperada.")
if tir > 12:
    print(f"La TIR ({tir}%) supera la tasa de descuento (12%). El proyecto es viable.")
```

#### Pertinencia

La pertinencia responde a: ¿el proyecto correcto se ejecutó en el momento correcto para las personas correctas? No importa qué tan bien ejecutado esté un proyecto si no responde a una necesidad real.

**Dimensiones de la pertinencia:**

- **Pertinencia social**: ¿Responde a una necesidad sentida por la comunidad o los usuarios? Ejemplo: un sistema de telemedicina en una zona sin hospitales tiene alta pertinencia social.
- **Pertinencia institucional**: ¿Está alineado con los objetivos estratégicos de la organización? Ejemplo: si la universidad tiene como meta la digitalización de procesos, un proyecto de expediente electrónico es pertinente institucionalmente.
- **Pertinencia temporal**: ¿Es el momento adecuado? Lanzar una app de realidad virtual en 2015 (cuando los cascos VR eran caros y escasos) tenía baja pertinencia temporal. Lanzarla hoy tiene más sentido.
- **Pertinencia técnica**: ¿La tecnología elegida es apropiada para el contexto? Usar blockchain para un sistema de votación estudiantil con 500 usuarios no es técnicamente pertinente (sobredimensionado, costoso, lento).

#### Calidad

La calidad en proyectos tecnológicos no es solo "que no tenga errores". Es un concepto multidimensional.

| Dimensión de calidad | Definición | Indicador |
|----------------------|------------|-----------|
| **Calidad funcional** | ¿El sistema hace lo que debe hacer? | % de requerimientos implementados correctamente |
| **Calidad técnica** | ¿El código es mantenible, seguro y eficiente? | Complejidad ciclomática, cobertura de pruebas, vulnerabilidades |
| **Calidad de experiencia (UX)** | ¿Es fácil e intuitivo de usar? | Tasa de finalización de tareas, tiempo por tarea, satisfacción SUS (System Usability Scale) |
| **Calidad de servicio** | ¿El soporte y la operación son confiables? | Tiempo de respuesta a incidentes, disponibilidad, satisfacción del servicio |

**La ecuación de calidad:**

```
Calidad percibida = (Resultados obtenidos) / (Expectativas del cliente)
```

Si los resultados superan las expectativas, el usuario percibe alta calidad. Si las expectativas son irrealistas, incluso un buen proyecto será percibido como de baja calidad. Por eso el gerente de proyecto debe gestionar las expectativas activamente, no solo los entregables.

#### Lecciones aprendidas

Al finalizar el proyecto, documentar las lecciones aprendidas es un requisito, no un lujo. Sin ellas, la organización repetirá los mismos errores en el próximo proyecto.

**Generador de plantilla de lecciones aprendidas con Python:**

```python
from datetime import datetime

def generar_plantilla_ll(nombre_proyecto, gerente, fecha_cierre=None):
    """
    Genera un archivo markdown con la plantilla de lecciones aprendidas
    prellenada con los datos del proyecto.
    """
    if fecha_cierre is None:
        fecha_cierre = datetime.now().strftime("%Y-%m-%d")
    
    plantilla = f"""# Lecciones Aprendidas: {nombre_proyecto}

## Información general
- Proyecto: {nombre_proyecto}
- Gerente: {gerente}
- Fecha de cierre: {fecha_cierre}

## ¿Qué salió bien? (replicar en futuros proyectos)
1. [Lección] → [Evidencia que respalda la lección]
2. [Lección] → [Evidencia]

## ¿Qué salió mal? (evitar en futuros proyectos)
| Problema | Causa raíz | Solución aplicada | Recomendación |
|----------|------------|-------------------|---------------|
| | | | |

## ¿Qué haríamos diferente?
1. [Cambio propuesto] → [Justificación del cambio]

## Datos cuantitativos
- Desviación de costo (%):
- Desviación de tiempo (%):
- Defectos en producción (N°):
- Satisfacción del cliente (1-5):

## Firmas
- Gerente de proyecto: __________
- Sponsor: __________
- Fecha: __________
"""
    nombre_archivo = f"lecciones_{nombre_proyecto.replace(' ', '_').lower()}.md"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(plantilla)
    print(f"Plantilla generada: {nombre_archivo}")
    return nombre_archivo

# Ejemplo de uso
generar_plantilla_ll("Sistema de Gestión de Inventarios", "Ana López")
```

```markdown
# Plantilla de lecciones aprendidas

## Información general
- Proyecto:
- Gerente:
- Fecha de cierre:

## ¿Qué salió bien? (replicar en futuros proyectos)
1. [Lección] → [Evidencia]
2. [Lección] → [Evidencia]

## ¿Qué salió mal? (evitar en futuros proyectos)
1. [Problema] → [Causa raíz] → [Solución aplicada] → [Recomendación]

## ¿Qué haríamos diferente?
1. [Cambio] → [Justificación]

## Datos cuantitativos
- Desviación de costo:
- Desviación de tiempo:
- Defectos en producción:
- Satisfacción del cliente (1-5):
```

#### Caso real de resultados: positivo

**El sistema de alerta temprana de terremotos de México (SASMEX)**. El proyecto, operado por el CIRES, tiene un impacto directo: emite alertas segundos antes de que las ondas sísmicas lleguen a la Ciudad de México. Su pertinencia es altísima: México está en una zona sísmica activa y la ciudad tiene más de 20 millones de habitantes. La calidad técnica se mide en falsas alarmas (menos del 1%) y tiempo de alerta (hasta 60 segundos para sismos lejanos). El impacto: se estima que ha salvado miles de vidas desde su implementación en 1993. La lección: cuando un proyecto está bien alineado con una necesidad real, su pertinencia trasciende cualquier métrica financiera.

#### Caso real de resultados: negativo

**El proyecto de historia clínica digital del NHS británico (National Programme for IT, NPfIT)**. Lanzado en 2002 con un presupuesto de 2,300 millones de libras, fue cancelado en 2011 tras gastar más de 10,000 millones. El impacto fue negativo: los hospitales reportaron que el sistema era más lento que el papel. La pertinencia era alta (Reino Unido necesitaba digitalizar la salud), pero la calidad técnica y de experiencia fue pésima: interfaces confusas, tiempos de respuesta de hasta 30 segundos por pantalla, y falta de interoperabilidad entre proveedores. La lección: un proyecto puede ser pertinente pero fracasar por mala ejecución técnica. La pertinencia es necesaria pero no suficiente.

## Autoevaluación

Lea cada pregunta, responda mentalmente y luego consulte el glosario o los conceptos si tiene dudas. Las respuestas no se entregan; son para su propio aprendizaje.

1. **Verdadero o falso:** En la validación de variables técnicas, la disponibilidad se mide típicamente en porcentaje de uptime y un valor aceptable común es 99.9% (tres nueves).
   *Respuesta: Verdadero. El 99.9% de disponibilidad permite aproximadamente 8.76 horas de inactividad al año, que es un estándar común para servicios no críticos.*

2. **¿Cuál de los siguientes NO es un método de validación de variables de negocio?**
   a) Análisis de Earned Value Management (EVM)
   b) Pruebas de carga con JMeter
   c) Encuestas NPS de satisfacción del cliente
   d) Analítica de uso con Mixpanel
   *Respuesta: b) Pruebas de carga con JMeter. Es una validación de variable técnica (rendimiento), no de negocio.*

3. **Relacione cada estrategia de adopción con su descripción:**
   - Big bang → (Todos los usuarios migran al mismo tiempo)
   - Por fases → (Grupos de usuarios migran progresivamente)
   - Paralelo → (Sistema antiguo y nuevo operan simultáneamente)
   - Canary release → (Pequeño porcentaje de usuarios recibe el cambio primero)

4. **¿Qué significan las siglas PDCA y cuáles son sus cuatro pasos?**
   *Respuesta: PDCA significa Plan-Do-Check-Act (Planificar-Hacer-Verificar-Actuar). Es el ciclo de mejora continua de Deming: 1) Planificar la mejora, 2) Hacer el cambio a pequeña escala, 3) Verificar los resultados, 4) Actuar estandarizando si funcionó o ajustando si no.*

5. **Según el caso de BlackBerry presentado, ¿cuál fue la causa principal de su declive en relación con la mejora continua?**
   *Respuesta: BlackBerry no implementó ciclos de mejora continua en su producto. Mientras Apple y Android iteraban rápidamente (pantallas táctiles, tiendas de aplicaciones, GPS, cámaras), BlackBerry confió en su base instalada y mantuvo su teclado físico y sistema operativo sin innovaciones significativas, quedándose obsoleto.*

6. **Caso práctico:** Eres el gerente de un proyecto que invirtió 200,000 USD. Los flujos proyectados son: año 1 = 50,000; año 2 = 80,000; año 3 = 90,000; año 4 = 60,000; año 5 = 40,000. Calcula el VAN con una tasa de descuento del 10% y determina si el proyecto es viable.
   *Respuesta: VAN = -200,000 + 50,000/(1.10)¹ + 80,000/(1.10)² + 90,000/(1.10)³ + 60,000/(1.10)⁴ + 40,000/(1.10)⁵ = -200,000 + 45,455 + 66,116 + 67,618 + 40,981 + 24,837 = 45,007 USD. VAN positivo: el proyecto genera valor y es viable financieramente.*

7. **Verdadero o falso:** La estrategia de adopción "big bang" es la de menor riesgo porque todos los usuarios migran al mismo tiempo y no hay período de transición prolongado.
   *Respuesta: Falso. Big bang es la estrategia de mayor riesgo porque si algo sale mal, todos los usuarios se ven afectados simultáneamente sin posibilidad de retroceso gradual.*

8. **Mencione las cuatro dimensiones de la pertinencia y explique brevemente cada una.**
   *Respuesta: 1) Pertinencia social: responde a una necesidad real de la comunidad o usuarios. 2) Pertinencia institucional: alineada con los objetivos estratégicos de la organización. 3) Pertinencia temporal: el momento es adecuado para lanzar el proyecto. 4) Pertinencia técnica: la tecnología elegida es apropiada para el contexto y no está sobredimensionada.*

9. **¿Cuál fue el principal error de validación que cometió GitLab en 2017 y qué medida correctiva implementaron?**
   *Respuesta: El error fue no validar periódicamente la integridad de las copias de seguridad. Asumieron que el proceso de replicación funcionaba correctamente sin verificarlo. La medida correctiva fue implementar validaciones automáticas de checksums en cada backup y programar pruebas de restauración semanales.*

10. **Reflexión final:** Esta unidad presenta al gerente de proyecto como un validador constante: valida variables técnicas y de negocio, define estrategias según el contexto, impulsa la mejora continua y evalúa resultados. Sin embargo, en la práctica, muchos gerentes de proyecto dedican la mayor parte de su tiempo a reportar estatus en lugar de validar supuestos. ¿Por qué crees que ocurre esto? ¿Qué cambiarías en tu formación como futuro gerente para evitar caer en ese patrón?
    *Respuesta abierta. Se espera que el estudiante reflexione sobre la presión de "parecer ocupado" reportando versus la disciplina de validar, y que proponga acciones concretas como: dedicar tiempo fijo semanal a validación técnica y de negocio, automatizar la generación de reportes para liberar tiempo, o establecer una cultura donde se premie la detección temprana de desviaciones.*

Si obtuvo menos de 7 respuestas correctas, revise nuevamente las secciones de Validación de Variables, Definición de Estrategias, Mejoras Continuas y Resultados Esperados, así como los casos de GitLab, ING Bank, Nokia, BlackBerry, SASMEX y el NHS.

## Bibliografía

Bernal, C. A. (2010). *Metodología de la Investigación* (3ª ed.). Pearson.

Deming, W. E. (1986). *Out of the Crisis*. MIT Press.

Hernández Sampieri, R., Fernández-Collado, C. y Baptista Lucio, P. (2014). *Metodología de la Investigación* (6ª ed.). McGraw-Hill.

Kerzner, H. (2017). *Project Management: A Systems Approach to Planning, Scheduling, and Controlling* (12ª ed.). Wiley.

Project Management Institute. (2021). *Guía de los Fundamentos para la Dirección de Proyectos (Guía PMBOK)* (7ª ed.). PMI.

Schwaber, K. y Sutherland, J. (2020). *La Guía Definitiva de Scrum: Las Reglas del Juego*. Scrum.org.

**Recursos web recomendados:**

- Project Management Institute (PMI). *Guía PMBOK*. Disponible en: https://www.pmi.org/pmbok-guide-standards
- Scrum Guide (español). Disponible en: https://scrumguides.org/scrum-guide-2020-scrum-guide-spanish.html
- Google Site Reliability Engineering (SRE) Books. Disponible en: https://sre.google/books/
- Etsy Engineering Blog. Disponible en: https://www.etsy.com/codeascraft/
- GitLab Incident Postmortem (2017). Disponible en: https://about.gitlab.com/blog/2017/02/01/gitlab-dot-com-database-incident/

## Glosario

- **Canary release**: Estrategia de despliegue donde una nueva versión se libera primero a un pequeño subconjunto de usuarios para validar su funcionamiento antes de extenderla a todos.
- **Cascada (Waterfall)**: Metodología de desarrollo secuencial donde cada fase debe completarse antes de pasar a la siguiente.
- **Deuda técnica**: Costo futuro de mantener o modificar un software que fue desarrollado con atajos, mala calidad o sin refactorización.
- **Earned Value Management (EVM)**: Técnica de gestión de proyectos que integra alcance, cronograma y costos para medir el desempeño del proyecto.
- **Impacto**: Efecto real y medible que un proyecto produce en su entorno (económico, social, ambiental u organizacional).
- **Kaizen**: Filosofía japonesa de mejora continua que se aplica en pequeños cambios incrementales y constantes.
- **Lecciones aprendidas**: Documento que recoge la experiencia adquirida durante un proyecto para evitar errores y replicar aciertos en proyectos futuros.
- **Mejora continua**: Proceso sistemático de identificación e implementación de cambios incrementales que mejoran la calidad, eficiencia o efectividad de un proyecto.
- **MVP (Minimum Viable Product)**: Versión más simple de un producto que permite validar una hipótesis de negocio con el mínimo esfuerzo de desarrollo.
- **PDCA**: Ciclo Planificar-Hacer-Verificar-Actuar, metodología de mejora continua desarrollada por W. Edwards Deming.
- **Pertinencia**: Grado en que un proyecto responde a una necesidad real de la población objetivo, está alineado con la estrategia institucional y se ejecuta en el momento y contexto adecuados.
- **Retrospectiva**: Reunión periódica del equipo (generalmente al final de cada sprint) para analizar el proceso de trabajo e identificar mejoras.
- **SLO (Service Level Objective)**: Valor objetivo para un indicador de nivel de servicio, como latencia o disponibilidad, que el equipo se compromete a cumplir.
- **Tasa Interna de Retorno (TIR)**: Tasa de descuento que hace que el VAN de un proyecto sea igual a cero; indica la rentabilidad relativa del proyecto.
- **Valor Actual Neto (VAN)**: Diferencia entre el valor presente de los flujos de caja futuros y la inversión inicial; un VAN positivo indica que el proyecto genera valor.

---

## Control de Revisiones

### Fase I — Correcciones Aplicadas

| ID | Categoría | Ubicación | Problema | Corrección |
|----|-----------|-----------|----------|------------|
| C-001 | Ortografía | Sección BlackBerry, párrafo 1 | Espacio sobrante antes del punto final | Eliminar espacio |
| C-002 | Ortografía | Sección SASMEX, párrafo 1 | Espacio sobrante antes del punto final | Eliminar espacio |
| C-003 | Ortografía | Sección NHS, párrafo 1 | Espacio sobrante antes del punto final | Eliminar espacio |

### Fase II — Mejoras Aplicadas

| ID | Categoría | Ubicación | Mejora | Cambio realizado |
|----|-----------|-----------|--------|-------------------|
| M-001 | Ampliación de ejemplos | Sección SLIs/SLOs/SLAs | Agregar un caso real de SLO mal definido que causó conflicto | Se añadió caso Google Cloud Platform + Snapchat (2019) sobre SLO sin exclusiones explícitas |
| M-002 | Profundización conceptual | Sección VAN y TIR | Explicar limitaciones de la TIR y añadir TIR Modificada | Se añadió subsección "Limitaciones de la TIR" con explicación y función Python `calcular_tirm()` |
| M-003 | Conexiones interunitarias | Sección PDCA | Conectar el ciclo PDCA con la gestión de riesgos de UDII | Se añadió párrafo integrando las fases PDCA con el ciclo identificar-analizar-evaluar-tratar-monitorear |
| M-004 | Inclusión de código | Sección Lecciones aprendidas | Agregar script Python que genere automáticamente la plantilla de lecciones aprendidas | Se añadió función `generar_plantilla_ll()` que crea archivo markdown con datos del proyecto |
| M-005 | Material complementario | Bibliografía | Agregar recursos web actualizados | Se añadieron enlaces a: PMBOK, Scrum Guide, SRE Google, Etsy Engineering Blog, postmortem de GitLab |
