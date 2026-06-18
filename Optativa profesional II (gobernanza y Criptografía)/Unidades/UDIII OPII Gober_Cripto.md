![Logo UNHSJM](Logo UNHSJM.jpeg)

# Formulación, Organización y Desarrollo de la Idea Novedosa

## Índice de Contenido

- [Introducción](#introducción)
- [Desarrollo de Contenidos](#desarrollo-de-contenidos)
  - [Tecnología Existente para el Desarrollo del Proyecto](#tecnología-existente-para-el-desarrollo-del-proyecto)
  - [Mercado, Clientes y Beneficiarios en un Proyecto Tecnológico](#mercado-clientes-y-beneficiarios-en-un-proyecto-tecnológico)
  - [Estado del Arte de la Idea de Proyecto Tecnológico](#estado-del-arte-de-la-idea-de-proyecto-tecnológico)
  - [Costo del Proyecto Tecnológico](#costo-del-proyecto-tecnológico)
  - [Know How del Proyecto Tecnológico](#know-how-del-proyecto-tecnológico)
- [Autoevaluación](#autoevaluación)
- [Bibliografía](#bibliografía)
- [Glosario](#glosario)

## Introducción

En las unidades anteriores recorrimos un camino que va desde entender qué es la seguridad informática y por qué es estratégica para cualquier organización, hasta comprender cómo se gobierna la seguridad a través de planes, procesos y gestión de riesgos. Ahora llega el momento de poner ese conocimiento en acción. Toda política de seguridad, todo plan de gobierno, toda matriz de riesgos existe para habilitar algo: proyectos tecnológicos que generen valor.

Pero una idea, por brillante que sea, no pasa de ser una intención hasta que se formula, se organiza y se demuestra que es viable. ¿Cómo saber si la tecnología que propones existe y es madura? ¿Quién va a usar lo que quieres construir? ¿Qué se ha hecho antes, en qué fallaron otros y cómo puedes evitar esos errores? ¿Cuánto cuesta realmente llevar una idea a la realidad y cómo se financia? ¿Tu idea es realmente innovadora o solo una copia de algo que ya existe?

Esta unidad te dará las herramientas para responder esas preguntas. Vas a aprender a evaluar la tecnología disponible, a identificar tu mercado y tus beneficiarios, a investigar el estado del arte, a estimar costos con métodos probados y a definir el nivel de innovación de tu propuesta. Al final, estarás listo para presentar una idea novedosa con una base sólida que resiste el escrutinio técnico y de negocio.

## Desarrollo de Contenidos

### Tecnología Existente para el Desarrollo del Proyecto

Antes de escribir una sola línea de código o comprar un solo servidor, debes responder una pregunta fundamental: ¿la tecnología que necesitas existe, está madura y es accesible? Subestimar esta pregunta es la causa más frecuente de fracaso en proyectos tecnológicos.

#### Evaluación de madurez tecnológica

El **Technology Readiness Level (TRL)** es una escala desarrollada por la NASA que mide qué tan madura está una tecnología. Va del nivel 1 (principios básicos observados) al nivel 9 (sistema probado en entorno operativo real). Para un proyecto tecnológico, estos niveles te indican si tu idea puede construirse con tecnología existente o si necesitas investigación y desarrollo previo.

| Nivel TRL | Descripción | ¿Qué significa para tu proyecto? |
|-----------|-------------|----------------------------------|
| TRL 1 | Principios básicos observados y reportados | Solo tienes una teoría, no hay prototipo. Riesgo altísimo. |
| TRL 2 | Concepto tecnológico y/o aplicación formulada | Tienes una idea con fundamento teórico. Aún no hay nada tangible. |
| TRL 3 | Función crítica probada analítica o experimentalmente | Comienza la prueba de concepto (PoC). |
| TRL 4 | Componente validado en laboratorio | El prototipo funciona en un entorno controlado. |
| TRL 5 | Componente validado en entorno simulado | Funciona fuera del laboratorio, en condiciones parecidas a las reales. |
| TRL 6 | Sistema prototipo demostrado en entorno relevante | Ya tienes algo que puedes mostrar a posibles inversionistas. |
| TRL 7 | Sistema prototipo demostrado en entorno operativo | El sistema funciona en condiciones reales, pero aún a escala limitada. |
| TRL 8 | Sistema completo y certificado | Pasaste todas las pruebas. Estás listo para producción. |
| TRL 9 | Sistema probado con éxito en entorno operativo real | El proyecto está funcionando. Misión cumplida. |

**Ejemplo práctico:** Imagina que quieres desarrollar un sistema de autenticación biométrica por reconocimiento de venas de la palma de la mano. Si tu idea usa una cámara infrarroja comercial y algoritmos de visión artificial ya existentes (OpenCV, TensorFlow), partes de un TRL 6 o 7. Si inventas un nuevo tipo de sensor y un algoritmo completamente nuevo, partes de TRL 1 o 2, lo que implica años de I+D antes de tener un producto.

#### Criterios para seleccionar tecnología

Al evaluar qué tecnología usar en tu proyecto, considera estos cinco criterios:

1. **Madurez**: ¿Cuántos años tiene la tecnología? ¿Hay implementaciones en producción? Una tecnología con menos de dos años en producción es un riesgo alto.
2. **Comunidad y soporte**: ¿Tiene una comunidad activa? ¿Hay documentación, foros, consultores? Usar un framework sin comunidad es condenarte a resolver solo cualquier problema.
3. **Licenciamiento**: ¿Es software libre, propietario, SaaS? ¿Qué restricciones tiene? Una licencia GPL puede ser un problema si planeas un producto cerrado.
4. **Seguridad**: ¿Tiene vulnerabilidades conocidas? ¿El equipo de desarrollo responde rápido a los reportes de seguridad? Revisa el CVE (Common Vulnerabilities and Exposures) de la tecnología.
5. **Curva de aprendizaje**: ¿Tu equipo puede dominarla en el tiempo del proyecto? Elegir una tecnología que nadie conoce puede duplicar los plazos.

#### Tabla de decisión tecnológica

| Tecnología | Madurez | Comunidad | Licencia | Seguridad (CVE 2024) | Curva |
|------------|---------|-----------|----------|----------------------|-------|
| Python + Django | Alta (15+ años) | Excelente | BSD | Bajo (críticos parcheados rápido) | Baja |
| Node.js + Express | Alta (15+ años) | Excelente | MIT | Medio | Baja |
| Rust + Actix | Media (8 años) | Creciente | MIT/Apache 2.0 | Muy bajo | Alta |
| Flutter (Dart) | Media (7 años) | Buena | BSD | Bajo | Media |

**Ejemplo de decisión errónea:** Una startup latinoamericana eligió en 2022 un framework de blockchain hiperespecializado con menos de 500 estrellas en GitHub y dos contribuidores activos. Seis meses después, el framework fue abandonado por sus creadores. La startup perdió seis meses de desarrollo y tuvo que reescribir todo desde cero con tecnología más madura (Hyperledger Fabric). La lección: la novedad técnica no justifica el riesgo cuando hay alternativas probadas.

**Ejemplo de acierto:** Spotify, cuando escaló su infraestructura, adoptó tecnologías maduras como Apache Kafka para mensajería y Google Cloud Platform como proveedor de nube. No innovaron en la capa de infraestructura; innovaron en el producto. Usar tecnología madura les permitió enfocar sus recursos en lo que realmente los diferenciaba: la experiencia de usuario y los algoritmos de recomendación.

### Mercado, Clientes y Beneficiarios en un Proyecto Tecnológico

Un proyecto tecnológico no existe en el vacío. Sirve a alguien: un cliente que paga, un beneficiario que recibe el servicio, un mercado que lo demanda. Ignorar esta dimensión es la receta para construir algo que nadie usa.

#### Clasificación de proyectos según su alcance de mercado

- **Proyecto cautivo**: El cliente es la misma organización. Por ejemplo, desarrollar un sistema interno de gestión de inventarios para tu propia empresa. No necesitas "vender" a externos, pero sí demostrar el retorno de inversión internamente.
- **Proyecto comercial**: El producto se vende a terceros. Aquí el análisis de mercado es obligatorio: tamaño del mercado, competidores, precio, canales de distribución.
- **Proyecto social o de impacto**: Los beneficiarios no pagan directamente (o pagan simbólicamente). El financiamiento viene de donaciones, subvenciones o presupuesto público. Ejemplo: una aplicación para reportar baches en una ciudad.
- **Proyecto intraemprendedor**: Se desarrolla dentro de una organización existente, pero con autonomía de startup. Ejemplo: el equipo de Google que creó Gmail.

#### Segmentación de mercado y perfil de beneficiario

La segmentación divide el mercado total en grupos con características homogéneas. Los criterios típicos son:

- **Demográfico**: Edad, género, ingresos, nivel educativo, ocupación.
- **Geográfico**: País, ciudad, urbano/rural, clima.
- **Psicográfico**: Valores, estilo de vida, intereses, opiniones.
- **Conductual**: Frecuencia de uso, lealtad a marcas, beneficios buscados.
- **Tecnográfico**: Dispositivos que usan, conectividad, alfabetización digital.

**Ejemplo:** Una aplicación de telemedicina para zonas rurales de Nicaragua tendría este perfil de beneficiario:
- Demográfico: Población rural de 18 a 65 años, con acceso limitado a centros de salud.
- Geográfico: Municipios a más de 30 km de un hospital.
- Psicográfico: Valoración de la salud preventiva, confianza en la tecnología móvil (si hay cobertura).
- Conductual: Usan WhatsApp y Facebook, prefieren videollamadas cortas.
- Tecnográfico: Smartphones gama media-baja, conexión 3G/4G intermitente.

#### Estimación de la demanda

Para proyectos comerciales, necesitas estimar cuántas personas comprarán tu producto. Tres enfoques complementarios:

**Enfoque ascendente (bottom-up):**
```python
# Ejemplo: estimación de demanda para un SaaS de gestión de restaurantes en Managua
restaurantes_formales = 850  # datos de la alcaldía
porcentaje_objetivo = 0.15   # 15% del mercado en año 1
tasa_conversion = 0.25       # de los contactados, 25% compra
clientes_estimados = int(restaurantes_formales * porcentaje_objetivo * tasa_conversion)
print(f"Clientes estimados año 1: {clientes_estimados}")
```

**Enfoque descendente (top-down):**
```
Mercado total de software de gestión en Nicaragua: 5 millones USD/año
Mercado abordable (segmento restaurantes): 1.2 millones USD/año (24%)
Mercado obtenible (con nuestra propuesta de valor): 180,000 USD/año (15% del abordable)
```

**Enfoque por analogía:** Buscar startups similares en mercados comparables. Si una app de delivery similar lanzada en Costa Rica alcanzó 10,000 usuarios en su primer año, puedes usar esa cifra como referencia (ajustando por población y penetración de internet).

**Comparación de los tres enfoques:**

| Enfoque | Precisión | Esfuerzo requerido | Datos necesarios | Mejor usado cuando... |
|---------|-----------|--------------------|------------------|-----------------------|
| Bottom-up | Alta | Alto (requiere desglose detallado) | Datos internos específicos | Tienes acceso a datos concretos del mercado objetivo |
| Top-down | Media | Bajo (usa datos agregados) | Datos de mercado generales (estudios sectoriales, censos) | Necesitas una estimación rápida o no tienes datos primarios |
| Analogía | Media-Alta | Medio | Datos de proyectos/empresas similares | Hay referentes confiables en mercados parecidos al tuyo |

En la práctica, combinar los tres enfoques da la estimación más robusta. Si bottom-up, top-down y analogía convergen en cifras similares, puedes tener alta confianza en tu estimación.

#### Caso real de éxito

**M-KOPA Solar** en África Oriental. Esta empresa ofrece sistemas solares domésticos con pago por uso (pay-as-you-go) mediante dinero móvil (M-Pesa). Su mercado: hogares sin conexión eléctrica (600 millones en África subsahariana). Segmentaron por ingresos: clientes que gastan menos de 1 USD al día en combustible (keroseno, velas) y pueden pagar cuotas diarias de 0.50 USD. Su perfil de beneficiario incluía el nivel de alfabetización digital necesario para usar M-Pesa. Hoy tienen más de un millón de hogares conectados. La lección: conocían exactamente a quién servían y cómo llegaban a ellos.

#### Caso real de fracaso por ignorar el mercado

**Google Glass (versión 2013)**. Google lanzó unas gafas de realidad aumentada a 1,500 USD sin un mercado claramente definido. El producto era tecnológicamente impresionante (TRL 8), pero Google no segmentó adecuadamente: el precio era prohibitivo para consumidores, las gafas tenían poca aceptación social por la cámara incorporada, y no identificaron un caso de uso empresarial concreto hasta años después (Google Glass Enterprise, 2017). La versión original fracasó porque la pregunta no era "¿podemos construirlo?" sino "¿quién lo va a comprar?".

### Estado del Arte de la Idea de Proyecto Tecnológico

El estado del arte (state of the art) es la revisión sistemática de lo que ya existe sobre tu tema: productos, investigaciones, patentes, soluciones comerciales. Sirve para tres propósitos:

1. **Evitar reinventar la rueda**: Si ya hay una solución funcional, no tiene sentido empezar de cero.
2. **Identificar brechas**: ¿Qué problemas no resuelven las soluciones existentes? Ahí está tu oportunidad.
3. **Posicionar tu propuesta**: ¿En qué es diferente, mejor o más barata tu idea?

#### Metodología para realizar un estado del arte

**Paso 1: Definir palabras clave y ecuaciones de búsqueda**

Para un proyecto de "sistema de detección de fraudes bancarios con machine learning", las palabras clave serían:
- fraud detection machine learning banking
- detección de fraudes bancarios aprendizaje automático
- anomaly detection financial transactions
- anti-money laundering AI

**Paso 2: Buscar en fuentes relevantes**

| Fuente | Tipo de información | Utilidad |
|--------|---------------------|----------|
| Google Scholar / SciELO / Redalyc | Artículos académicos | Base teórica, metodologías, resultados de investigación |
| Patentes (Google Patents, USPTO, OMPI) | Innovaciones registradas | Saber si tu idea ya está patentada |
| Productos comerciales | Soluciones existentes en el mercado | Análisis de competidores, funcionalidades, precios |
| Repositorios (GitHub, GitLab) | Código fuente abierto | Reutilizar componentes, evaluar complejidad |
| Documentación técnica | APIs, frameworks, estándares | Conocer limitaciones técnicas |

**Paso 3: Organizar los hallazgos**

Crea una tabla comparativa como esta:

| Solución encontrada | Tipo | Fortalezas | Debilidades | ¿Inspira tu proyecto? |
|--------------------|------|------------|-------------|----------------------|
| FraudNet (artículo, 2022) | Académico | 98% precisión en dataset público | No probado en entorno real | Sí, usaré su arquitectura de red neuronal |
| SEON (comercial) | SaaS | API fácil de integrar | Costo alto (500 USD/mes) | No, pero lo usaré como referencia de UX |
| Patente US 2023/0123456 | Patente | Método novedoso de scoring | Solo aplica a tarjetas de crédito | Precaución: podría haber conflicto de propiedad intelectual |
| PayPal Fraud Protection | Producto | Probado en millones de transacciones | Caja negra, no sabemos cómo funciona | Inspiración para requerimientos funcionales |

**Paso 4: Redactar el estado del arte**

La redacción debe responder: ¿qué se ha hecho, qué falta, dónde está la oportunidad?

**Ejemplo de redacción para un proyecto:**

> *"Se han desarrollado múltiples sistemas de detección de fraudes basados en machine learning. Redes neuronales profundas como FraudNet (Gómez et al., 2022) alcanzan precisiones superiores al 95% en datasets públicos como IEEE-CIS. Sin embargo, estas soluciones presentan limitaciones: requieren grandes volúmenes de datos etiquetados que no siempre están disponibles en mercados emergentes, y suelen estar optimizadas para tarjetas de crédito, dejando fuera canales como transferencias móviles (Mendoza, 2023). En el ámbito comercial, SEON y Sift ofrecen APIs especializadas, pero sus costos (500-2000 USD/mes) las hacen inaccesibles para cooperativas y bancos pequeños. Existe, por tanto, una oportunidad para desarrollar un sistema de detección de fraudes adaptado al contexto centroamericano, que funcione con volúmenes de datos moderados y esté diseñado para canales de pago móvil."*

#### Caso real de estado del arte bien hecho

**Los creadores de Slack** (Stewart Butterfield y su equipo) investigaron a fondo el estado del arte de las herramientas de comunicación empresarial antes de lanzar su producto. Analizaron: IRC (gratuito pero poco amigable), Microsoft Teams (no existía aún), HipChat (popular pero con limitaciones de búsqueda), y el correo electrónico (universal pero ineficiente para equipos ágiles). Identificaron que ninguna herramienta combinaba: búsqueda potente, integración con otras apps, canales temáticos y una interfaz que cualquiera pudiera usar sin capacitación. Esa brecha fue la base de Slack, que hoy vale más de 27,000 millones de dólares.

#### Caso real de estado del arte mal hecho

**Quibi** (2020). La plataforma de videos cortos para móviles invirtió 1,750 millones de dólares en contenido original y tecnología. Su estado del arte fue deficiente porque ignoraron a TikTok como competidor directo, asumiendo que los usuarios pagarían por contenido premium de 10 minutos cuando TikTok ofrecía contenido gratuito de 30 segundos. Quebraron a los seis meses. Un estado del arte riguroso habría mostrado que el mercado de videos cortos ya estaba saturado y que los usuarios no estaban dispuestos a pagar por ese formato.

**Caso adicional de estado del arte mal hecho en la era de la IA generativa:**

En 2024, varias startups de chatbots para atención al cliente invirtieron millones en desarrollar modelos de lenguaje propios sin investigar adecuadamente el estado del arte. Ignoraron que OpenAI, Anthropic y Google ya ofrecían APIs de modelos fundacionales (GPT-4, Claude, Gemini) con calidad superior a la que cualquier startup podía desarrollar desde cero. El resultado: cientos de startups fracasaron al no poder competir con modelos que ya existían y eran gratuitos o de bajo costo por consulta. Una investigación de estado del arte rigurosa habría revelado que la oportunidad no estaba en construir un modelo, sino en especializar los modelos existentes para nichos concretos con fine-tuning y datos propietarios. La lección actualizada: en la era de la IA, el estado del arte cambia cada seis meses; revisarlo trimestralmente no es opcional.

### Costo del Proyecto Tecnológico

Estimar costos es la parte que nadie quiere hacer pero todos exigen. Una estimación realista separa un proyecto viable de una fantasía.

#### Estructura de costos de un proyecto tecnológico

Los costos se clasifican en tres grandes grupos:

**1. Costos de desarrollo (una sola vez o capitalizables)**

| Concepto | Ejemplo | Rango típico (%) |
|----------|---------|-------------------|
| Hardware | Servidores, estaciones de trabajo, dispositivos IoT, sensores | 5 - 15% |
| Software y licencias | Sistemas operativos, bases de datos, herramientas de desarrollo, SaaS | 5 - 10% |
| Recursos humanos | Salarios del equipo de desarrollo (programadores, diseñadores, QA) | 40 - 60% |
| Consultoría externa | Expertos en seguridad, legales, especialistas de dominio | 5 - 15% |
| Infraestructura en nube | AWS/Azure/GCP durante desarrollo y pruebas | 5 - 10% |
| Capacitación | Cursos, certificaciones para el equipo | 2 - 5% |

**2. Costos operativos (recurrentes)**

| Concepto | Ejemplo | Frecuencia |
|----------|---------|------------|
| Hospedaje y nube | Servidores, CDN, almacenamiento | Mensual |
| Mantenimiento | Corrección de errores, parches de seguridad, actualizaciones | Mensual |
| Soporte técnico | Personal o servicio externo de help desk | Mensual |
| Licencias renovables | SaaS, suscripciones anuales | Anual |
| Marketing y ventas | Publicidad, comisiones, equipo comercial | Mensual |
| Seguros | Ciberseguro, responsabilidad civil | Anual |

**3. Costos de contingencia (10-20% del total)**

Ningún proyecto sale exactamente como se planeó. La contingencia cubre imprevistos: una API que cambia y requiere adaptación, un miembro del equipo que renuncia, un requisito legal nuevo.

#### Métodos de estimación

**Estimación análoga:** Se basa en proyectos similares anteriores. Si desarrollaste un sistema de inventarios y costó 15,000 USD, un proyecto similar pero con autenticación biométrica podría costar 20,000 USD.

**Estimación paramétrica:** Usa modelos matemáticos basados en variables medibles. Por ejemplo, el modelo COCOMO (Constructive Cost Model) para software:

```python
# Ejemplo simplificado de COCOMO básico
import math

def estimar_esfuerzo_persona_mes(lineas_codigo):
    """
    COCOMO básico: esfuerzo = a * (KLOC)^b
    a=2.4, b=1.05 para proyecto orgánico (pequeño, equipo experimentado)
    """
    kloc = lineas_codigo / 1000
    a = 2.4
    b = 1.05
    esfuerzo_persona_mes = a * (kloc ** b)
    return round(esfuerzo_persona_mes, 2)

def estimar_costo(esfuerzo_persona_mes, costo_mensual_por_persona):
    return round(esfuerzo_persona_mes * costo_mensual_por_persona, 2)

lineas = 25000  # 25,000 líneas de código estimadas
esfuerzo = estimar_esfuerzo_persona_mes(lineas)
costo_persona_mes = 3500  # USD, incluyendo salario + prestaciones + overhead
costo = estimar_costo(esfuerzo, costo_persona_mes)

print(f"Esfuerzo estimado: {esfuerzo} persona-meses")
print(f"Costo estimado solo de desarrollo: {costo} USD")
```

**Estimación por juicio de expertos (Delphi):** Varios expertos estiman de forma independiente, luego discuten las diferencias y convergen en una cifra. Es útil cuando no hay datos históricos.

**Estimación bottom-up:** Descomponer todo el proyecto en tareas de 4-8 horas, estimar cada una y sumar. Es la más precisa pero la que más tiempo requiere.

#### Flujo de caja y punto de equilibrio

El flujo de caja proyecta ingresos y egresos mes a mes. El punto de equilibrio es el momento en que los ingresos acumulados igualan a los costos acumulados.

```python
meses = list(range(1, 25))
costo_mensual = 15000  # USD, operación mensual
inversion_inicial = 120000  # USD, desarrollo + lanzamiento
ingreso_mensual = [0] * 6 + [8000, 12000, 15000, 18000, 20000, 22000] * 3

flujo_acumulado = []
acumulado = -inversion_inicial
for i in range(24):
    acumulado += ingreso_mensual[i] - costo_mensual
    flujo_acumulado.append(acumulado)
    if acumulado >= 0:
        print(f"Punto de equilibrio alcanzado en el mes {i+1}")
        break
```

#### Caso real de subestimación de costos

**HealthCare.gov** (2013), el portal de seguros de salud del gobierno de EE.UU. El presupuesto inicial fue de 93.7 millones de dólares. El costo final superó los 2,100 millones. Las causas: requisitos cambiantes, múltiples contratistas trabajando sin integración, y una estimación inicial que no consideró la complejidad de integrar los sistemas de 50 estados diferentes. La lección: las estimaciones bottom-up con equipos distribuidos requieren un factor de integración que muchos olvidan.

#### Caso real de buena gestión de costos

**WhatsApp** en sus inicios. El equipo era pequeño (menos de 50 ingenieros) y mantuvieron costos operativos extremadamente bajos usando Erlang para manejar millones de conexiones simultáneas con pocos servidores. Su costo de infraestructura por usuario activo era de centavos. Cuando Facebook los adquirió en 2014 por 19,000 millones de dólares, tenían 450 millones de usuarios y solo 32 ingenieros. La arquitectura tecnológica bien pensada desde el inicio permitió una estructura de costos que hizo el proyecto viable y atractivo para inversión.

### Know How del Proyecto Tecnológico

El know how (saber hacer) es el conocimiento práctico, acumulado y a menudo tácito que permite ejecutar el proyecto con éxito. No es solo la tecnología, sino la experiencia del equipo, los procesos internos, las relaciones con proveedores y la capacidad de ejecución.

#### Nivel de innovación

La innovación no es binaria (innovador vs. no innovador). Existe un gradiente que va desde la mejora incremental hasta la disrupción radical.

| Tipo de innovación | Descripción | Ejemplo | Riesgo técnico | Impacto potencial |
|--------------------|-------------|---------|----------------|-------------------|
| **Incremental** | Mejora pequeña sobre algo existente | Agregar autenticación biométrica a una app existente | Bajo | Bajo-Medio |
| **Adjunta** | Aplicar tecnología existente a un nuevo mercado | Usar sensores IoT (existentes) para monitoreo de cultivos en una región donde no se usa | Medio | Medio |
| **Arquitectónica** | Reorganizar componentes existentes de forma novedosa | Combinar IA + realidad aumentada para capacitación industrial | Medio-Alto | Alto |
| **Radical o disruptiva** | Tecnología o modelo de negocio que cambia las reglas del juego | Netflix vs. Blockbuster, Uber vs. taxis | Alto | Muy Alto |

#### La curva de madurez del know how

El equipo que ejecuta el proyecto debe tener el know how necesario en el momento adecuado. Esta tabla te ayuda a diagnosticar si tienes las capacidades que necesitas:

| Capacidad requerida | ¿La tenemos internamente? | ¿Podemos adquirirla (contratar, capacitar)? | ¿Debemos tercerizarla? |
|--------------------|---------------------------|---------------------------------------------|------------------------|
| Desarrollo backend en Python | Sí (equipo actual) | N/A | N/A |
| Machine Learning | No | Contratar 1 ingeniero ML (3 meses) | API de AWS SageMaker (costo mensual) |
| Seguridad informática | Parcial (conceptos básicos) | Capacitar al equipo líder en OWASP (2 semanas) | Auditoría de seguridad externa (trimestral) |
| Conocimiento del sector salud | No | Asociarse con un hospital como asesor | Consultor médico (honorarios) |

#### Protección del know how

Tu conocimiento diferencial debe protegerse. Las herramientas jurídicas disponibles:

| Herramienta | Protege | Duración | Costo |
|-------------|---------|----------|-------|
| Patente | Invenciones, procesos técnicos novedosos | 20 años | Alto (miles de USD, requiere abogado) |
| Derechos de autor | Código fuente, documentación, diseños | Vida del autor + 70 años | Gratuito (se registra al crear la obra) |
| Secreto industrial | Información confidencial (fórmulas, algoritmos, listas de clientes) | Indefinido mientras se mantenga el secreto | Bajo (requiere políticas internas) |
| Marca registrada | Nombre, logotipo, eslogan | 10 años (renovable) | Medio |
| Licencias (GPL, MIT, Apache) | Define cómo otros pueden usar tu software | Perpetua | Gratuito |

**Seleccionador de licencia con Python:**

```python
def sugerir_licencia(uso_comercial, requiere_atribucion, compartir_igual, soy_empresa):
    """
    Sugiere una licencia de software según las necesidades del proyecto.
    Basado en el flujo de decisión de choosealicense.com
    """
    if not uso_comercial:
        if compartir_igual:
            return "GPL-3.0 (obliga a que derivados usen la misma licencia)"
        else:
            return "LGPL-3.0 (permite enlace desde software propietario)"
    else:
        if soy_empresa:
            return "Apache-2.0 (permite uso comercial, protege de patentes)"
        else:
            if requiere_atribucion:
                return "MIT (permite uso comercial, solo requiere atribución)"
            else:
                return "Unlicense (dedicación a dominio público)"

# Ejemplo: startup que quiere licencia permisiva para su librería Python
licencia = sugerir_licencia(
    uso_comercial=True,
    requiere_atribucion=True,
    compartir_igual=False,
    soy_empresa=True
)
print(f"Licencia sugerida: {licencia}")
```

#### Conexión con la gestión de riesgos (UDII)

La estimación de costos que viste en esta unidad se conecta directamente con la gestión de riesgos que estudiamos en la Unidad II. Recordarás el concepto de ALE (Annualized Loss Expectancy): ALE = SLE × ARO. Cuando estimas los costos de tu proyecto, estás haciendo algo similar pero en sentido inverso: estás calculando cuánto debes invertir para mitigar los riesgos de que el proyecto no se complete o no genere el valor esperado.

Cada partida de costo (desarrollo, operación, contingencia) puede entenderse como un control sobre los riesgos identificados. Si tu proyecto tiene un riesgo alto de fuga de datos (porque maneja información sensible), el presupuesto debe incluir controles de seguridad. Si tiene un riesgo alto de rechazo del mercado, el presupuesto debe incluir estudios de validación temprana. El gerente de proyecto que integra la gestión de costos con la gestión de riesgos toma decisiones más informadas que quien solo suma facturas.

#### Protección del know how que incluye: algoritmo de recomendación (Cinematrix, luego sus sucesores), sistema de entrega de contenido propio (Open Connect CDN), Chaos Engineering para resiliencia, y herramientas de producción de contenido original. Ninguna de estas capacidades se compra empaquetada. Netflix las construyó internamente a lo largo de años, y ese know how es su principal barrera de entrada contra competidores como Disney+ o HBO.

**Ejemplo real de pérdida de know how:**

**Kodak** inventó la cámara digital en 1975 (TRL 4-5 para la época), pero no desarrolló el know how comercial para explotarla. Su know how estaba en la química de películas fotográficas y papel, no en sensores digitales, software de edición y plataformas de fotografía social. Cuando el mercado migró a lo digital, Kodak perdió su ventaja y se declaró en bancarrota en 2012. La lección: el know how debe evolucionar con la tecnología. No basta con haber sido el mejor ayer.

#### Árbol de decisión de innovación

```
¿La idea resuelve un problema real?
├── Sí → ¿Existen soluciones similares?
│       ├── Sí → ¿Mi solución es significativamente mejor?
│       │       ├── Sí → Innovación incremental o adjunta (viable con recursos moderados)
│       │       └── No → Replantear: ¿qué valor agrego realmente?
│       └── No → ¿El mercado está listo para esta solución?
│               ├── Sí → Innovación radical (alto riesgo, alto retorno potencial)
│               └── No → ¿Podemos educar al mercado? (requiere presupuesto de marketing)
└── No → Detener el proyecto. No hay idea novedosa sin problema real.
```

## Autoevaluación

Lea cada pregunta, responda mentalmente y luego consulte el glosario o los conceptos si tiene dudas. Las respuestas no se entregan; son para su propio aprendizaje.

1. **Verdadero o falso:** El nivel TRL 9 significa que la tecnología ha sido probada solo en laboratorio y aún no está lista para producción.
   *Respuesta: Falso. TRL 9 significa que el sistema ha sido probado con éxito en un entorno operativo real. TRL 4 es el que corresponde a validación en laboratorio.*

2. **¿Cuál de los siguientes NO es un criterio para seleccionar tecnología en un proyecto?**
   a) Madurez de la tecnología
   b) Número de seguidores en redes sociales del creador
   c) Licenciamiento y restricciones de uso
   d) Seguridad (vulnerabilidades conocidas)
   *Respuesta: b) Número de seguidores en redes sociales del creador. Eso no es un criterio técnico ni de negocio relevante.*

3. **Relacione cada método de estimación de costos con su descripción:**
   - Estimación análoga → (Basada en proyectos similares anteriores)
   - Estimación paramétrica → (Usa modelos matemáticos como COCOMO)
   - Juicio de expertos → (Varios especialistas convergen en una cifra)
   - Bottom-up → (Descompone el proyecto en tareas individuales)

4. **¿Qué tipo de innovación implica aplicar una tecnología existente a un mercado nuevo donde no se ha usado antes?**
   *Respuesta: Innovación adjunta. Por ejemplo, usar sensores IoT (existentes en la industria) para monitoreo de cultivos en una región agrícola donde nunca se han implementado.*

5. **Según la metodología presentada, ¿cuáles son los cuatro pasos para realizar un estado del arte?**
   *Respuesta: 1) Definir palabras clave y ecuaciones de búsqueda, 2) Buscar en fuentes relevantes (académicas, patentes, comerciales, repositorios), 3) Organizar los hallazgos en tablas comparativas, 4) Redactar el estado del arte identificando brechas y oportunidades.*

6. **Caso práctico:** Tu equipo estima que un proyecto requiere 35,000 líneas de código. Usando COCOMO básico (a=2.4, b=1.05) y un costo de 4,000 USD por persona-mes, calcula el esfuerzo en persona-meses y el costo total de desarrollo.
   *Respuesta: KLOC = 35,000/1,000 = 35. Esfuerzo = 2.4 * (35^1.05) = 2.4 * 41.80 ≈ 100.32 persona-meses. Costo = 100.32 * 4,000 = 401,280 USD.*

7. **Verdadero o falso:** En la estructura de costos de un proyecto tecnológico, los recursos humanos representan típicamente entre el 40% y el 60% del total del presupuesto de desarrollo.
   *Respuesta: Verdadero. El talento humano (programadores, diseñadores, QA) suele ser la partida más grande en proyectos de tecnología.*

8. **Mencione tres herramientas jurídicas para proteger el know how de un proyecto tecnológico y qué protege cada una.**
   *Respuesta: 1) Patente: protege invenciones y procesos técnicos novedosos (20 años). 2) Derechos de autor: protege código fuente, documentación y diseños (vida del autor + 70 años). 3) Secreto industrial: protege información confidencial como fórmulas, algoritmos y listas de clientes (indefinido mientras se mantenga el secreto).*

9. **Según el caso de Quibi, ¿qué error cometieron en el análisis de estado del arte?**
   *Respuesta: Ignoraron a TikTok como competidor directo. Asumieron que los usuarios pagarían por contenido premium de 10 minutos cuando el mercado ya tenía una oferta gratuita dominante (TikTok) con videos de 30 segundos. Un estado del arte riguroso habría identificado la saturación del mercado de videos cortos.*

10. **Reflexión final:** La unidad plantea que conocer el estado del arte y estimar costos son pasos indispensables antes de desarrollar cualquier proyecto tecnológico. Sin embargo, muchas startups fracasan porque prefieren "lanzar rápido y validar después" (lean startup) en lugar de investigar primero. ¿Crees que ambos enfoques son incompatibles o pueden complementarse? ¿En qué casos convendría priorizar la investigación profunda y en cuáles el lanzamiento rápido?
    *Respuesta abierta. Se espera que el estudiante reflexione sobre el equilibrio entre investigación y acción, mencionando que la investigación profunda es indispensable cuando existen altos costos de fracaso (ej. proyectos de infraestructura crítica, dispositivos médicos, sistemas financieros), mientras que el lanzamiento rápido puede funcionar en productos digitales de bajo costo donde el feedback del mercado es más valioso que el análisis teórico.*

Si obtuvo menos de 7 respuestas correctas, revise nuevamente las secciones de Tecnología Existente, Estado del Arte, Costo del Proyecto y Know How, así como los casos de M-KOPA, Quibi, HealthCare.gov y WhatsApp.

## Bibliografía

Bernal, C. A. (2010). *Metodología de la Investigación* (3ª ed.). Pearson.

Hernández Sampieri, R., Fernández-Collado, C. y Baptista Lucio, P. (2014). *Metodología de la Investigación* (6ª ed.). McGraw-Hill.

Mankins, J. C. (1995). *Technology Readiness Levels: A White Paper*. NASA.

Porter, M. E. (2008). *Estrategia Competitiva: Técnicas para el Análisis de los Sectores Industriales y de la Competencia* (2ª ed.). Grupo Editorial Patria.

Pressman, R. S. (2010). *Ingeniería del Software: Un Enfoque Práctico* (7ª ed.). McGraw-Hill.

Schwaber, K. y Sutherland, J. (2020). *La Guía Definitiva de Scrum: Las Reglas del Juego*. Scrum.org.

**Recursos web recomendados:**

- Choose an Open Source License. Disponible en: https://choosealicense.com/
- NASA Technology Readiness Level. Disponible en: https://www.nasa.gov/directorates/heo/scan/engineering/technology/txt_accordion1.html
- Project Management Institute. Disponible en: https://www.pmi.org/
- Google Patents. Disponible en: https://patents.google.com/
- SciELO Nicaragua. Disponible en: https://www.scielo.org/es/

## Glosario

- **Bottom-up (estimación)**: Método de estimación que descompone el proyecto en tareas pequeñas, estima cada una por separado y suma los resultados.
- **COCOMO**: Constructive Cost Model, modelo matemático para estimar esfuerzo y costo de desarrollo de software, creado por Barry Boehm en 1981.
- **Estado del arte**: Revisión sistemática de lo que existe (investigaciones, productos, patentes) sobre un tema determinado, utilizada para identificar brechas y oportunidades.
- **Flujo de caja**: Proyección de ingresos y egresos de efectivo a lo largo del tiempo, utilizada para evaluar la viabilidad financiera de un proyecto.
- **Innovación adjunta**: Aplicación de una tecnología existente a un mercado o contexto nuevo donde no se había utilizado antes.
- **Innovación incremental**: Mejora pequeña y progresiva sobre un producto, servicio o proceso existente.
- **Innovación radical**: Cambio disruptivo que transforma un mercado o crea uno nuevo, generalmente basado en una tecnología novedosa.
- **Know how**: Conocimiento práctico, experiencia acumulada y capacidades técnicas que permiten ejecutar un proyecto con éxito.
- **Mercado abordable**: Porción del mercado total que una empresa puede alcanzar dado su modelo de negocio, recursos y capacidades.
- **Mercado obtenible**: Fracción del mercado abordable que una empresa puede capturar realistamente en un período determinado.
- **Punto de equilibrio**: Momento en el que los ingresos acumulados igualan a los costos acumulados; a partir de ese punto el proyecto comienza a generar ganancias.
- **Segmentación de mercado**: División del mercado total en grupos homogéneos con características demográficas, geográficas, psicográficas, conductuales o tecnográficas compartidas.
- **TRL (Technology Readiness Level)**: Escala de 9 niveles que mide la madurez de una tecnología, desde principios básicos (TRL 1) hasta sistema probado en entorno operativo real (TRL 9).

---

## Control de Revisiones

### Fase I — Correcciones Aplicadas

| ID | Categoría | Ubicación | Problema | Corrección |
|----|-----------|-----------|----------|------------|
| C-001 | Ortografía | Sección Google Glass, párrafo 1 | Espacio sobrante antes del punto final: `**Google Glass (versión 2013)** .` | Eliminar espacio: `**Google Glass (versión 2013)**.` |
| C-002 | Precisión técnica | Autoevaluación, pregunta 6 | El cálculo de COCOMO usaba 35^1.05 ≈ 42.17 cuando el valor correcto es ≈ 41.80 | Actualizar respuesta: esfuerzo = 100.32 persona-meses, costo = 401,280 USD |

### Fase II — Mejoras Aplicadas

| ID | Categoría | Ubicación | Mejora | Cambio realizado |
|----|-----------|-----------|--------|-------------------|
| M-001 | Ampliación de ejemplos | Sección Estimación de la demanda | Agregar tabla comparativa de los tres enfoques de estimación (bottom-up, top-down, analogía) | Se añadió tabla con criterios de precisión, esfuerzo, datos necesarios y cuándo usar cada enfoque |
| M-002 | Actualización de referencias | Sección Estado del Arte | Agregar caso actual de startups de IA generativa que fracasaron por ignorar el estado del arte | Se añadió caso de startups de chatbots (2024) que compitieron contra OpenAI/Anthropic/Google sin investigar el mercado |
| M-003 | Conexiones interunitarias | Sección Know How | Conectar la estimación de costos con la gestión de riesgos de UDII | Se añadió subsección "Conexión con la gestión de riesgos (UDII)" explicando la relación entre costos y ALE |
| M-004 | Inclusión de código | Sección Protección del know how | Agregar herramienta en Python para seleccionar licencias de software | Se añadió función `sugerir_licencia()` con flujo de decisión basado en choosealicense.com |
| M-005 | Material complementario | Bibliografía | Agregar recursos web actualizados | Se añadieron enlaces a: choosealicense.com, NASA TRL, PMI, Google Patents, SciELO |
