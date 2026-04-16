# Ejemplos Prácticos: Evaluación de Factibilidades
## Sistema de Matrícula - Institución Educativa

---

## DESCRIPCIÓN DEL SISTEMA DE MATRÍCULA

### ¿Qué es?

El Sistema de Matrícula es an software que permite a estudiantes y administrativos gestionar el proceso de registro de asignaturas de forma electrónica. Incluye:

**Casos de Uso Principales:**
1. **Autenticarse en el sistema** - Estudiantes, docentes y administrativos acceden con usuario/contraseña
2. **Consultar oferta académica** - Ver qué asignaturas están disponibles
3. **Matricular asignaturas** - Elegir y registrar asignaturas para el semestre
4. **Modificar matrícula** - Cambiar asignaturas en período permitido
5. **Gestión de períodos** - Administrativos definen fechas de matrícula
6. **Asignación de cupos** - Limitarquién matricula según capacidad
7. **Generación de reportes** - Ver quién está matriculado en cada asignatura

### Actores del Sistema
- **Estudiante:** Consulta, matriz, modifica su matrícula
- **Docente:** Consulta estudiantes matriculados
- **Administrativo:** Gestiona períodos, cupos, reportes
- **Jefe de Carrera:** Supervisa la matrícula de su carrera

### Clases Principales
```
Usuario (abstracta)
├── Estudiante
├── Administrativo
├── Docente
└── JefeCarrera

Asignatura
├── código
├── nombre
├── horario
├── docente
└── cupos

Matrícula
├── estudiante
├── asignaturas[]
├── periodo
└── estado

Periodo
├── fechaInicio
├── fechaFin
└── permitaModificación

OfertaAcademica
├── asignaturas[]
├── carrera
└── periodo
```

---

## 1. EJEMPLO COMPLETO: FACTIBILIDAD TÉCNICA - SISTEMA DE MATRÍCULA

### Contexto
**Institución:** Universidad Nacional Centro
**Estudiantes:** 450
**Administrativos:** 5
**Docentes:** 25
**Hardware Actual:** 5 computadoras i3, 8GB RAM, Windows 10

### 1.1 Evaluación de Equipos Actuales

#### Hardware Cliente

```
┌─────────────────────────────────────────────────────────┐
│              HARDWARE ADMINISTRATIVOS                    │
├────────────────────────────────────────────────────────┤
│                                                          │
│  Equipo Actual Available:                              │
│  • Procesador: Intel® Core™ i3-8100                    │
│  • Núcleos: 4                                           │
│  • Frecuencia: 3.60 GHz                                │
│  • RAM: 8 GB DDR4                                       │
│  • Almacenamiento: 256 GB SSD                          │
│  • Sistema Operativo: Windows 10 Pro                   │
│                                                          │
│  Requerimiento Mínimo para Sistema Matrícula:          │
│  • Procesador: Intel® Core™ i5 (4 núcleos)            │
│  • Frecuencia: 2.5 GHz                                 │
│  • RAM: 4 GB DDR4                                       │
│  • Almacenamiento: 100 GB                              │
│  • Sistema Operativo: Windows 10/11                    │
│                                                          │
│  Requerimiento Óptimo:                                 │
│  • Procesador: Intel® Core™ i7 (4 núcleos)            │
│  • Frecuencia: 3.0 GHz                                 │
│  • RAM: 8 GB DDR4                                       │
│  • Almacenamiento: 256 GB SSD                          │
│  • Sistema Operativo: Windows 11                       │
│                                                          │
│  ┌─ CUMPLIMIENTO ─────────────────────────────────┐    │
│  │ ✓ Procesador: Excede mínimo (i3 > i5 requerido)│   │
│  │   (Nota: Just meets minimum, upgrade to i7      │   │
│  │    would be better)                             │   │
│  │ ✓ RAM: Cumple mínimo (8GB = 4GB req.)          │   │
│  │ ✓ Almacenamiento: Cumple (256GB > 100GB)       │   │
│  │ ✓ SO: Cumple (Windows 10)                      │   │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Análisis:** El hardware actual es BORDERLINE. Cumple los mínimos pero está cerca del límite. No es ideal para múltiples usuarios simultáneos.

---

#### Hardware Servidor

```
┌──────────────────────────────────────────────────────┐
│          OPCIONES DE SERVIDOR                        │
├──────────────────────────────────────────────────────┤
│                                                       │
│ OPCIÓN 1: Servidor Local On-Premise                 │
│                                                       │
│ REQUERIMIENTOS MÍNIMOS (450 estudiantes):            │
│ • Procesador: Intel Xeon E3-1240 v6                 │
│   - Núcleos: 4 / Hilos: 8                           │
│   - Frecuencia: 3.50 GHz                            │
│ • RAM: 16 GB DDR4 UDIMM                             │
│ • Almacenamiento: 500 GB HDD (7.2k RPM)             │
│ • Sistema Operativo: Windows Server 2022            │
│ • Redundancia: UPS (Uninterruptible Power Supply)   │
│                                                       │
│ REQUERIMIENTOS ÓPTIMOS:                             │
│ • Procesador: Intel Xeon E5-1620 v3 (Dual)          │
│   - Núcleos: 8 / Hilos: 16                          │
│   - Frecuencia: 3.70 GHz                            │
│ • RAM: 32 GB DDR4 RDIMM                             │
│ • Almacenamiento: 1 TB SSD + 1 TB HDD Backup        │
│ • Sistema Operativo: Windows Server 2022            │
│ • Redundancia: Cluster de 2 servidores              │
│ • Respaldo: Sistema de UPS + Generador              │
│                                                       │
│ COSTO:                                               │
│ • Servidor + instal: $3,500 - $5,000 inicial        │
│ • Mantenimiento: $500 - $1,000/año                  │
│                                                       │
├──────────────────────────────────────────────────────┤
│                                                       │
│ OPCIÓN 2: Servidor en Nube (Azure/AWS)              │
│                                                       │
│ CONFIGURACIÓN RECOMENDADA:                          │
│ • Máquina Virtual: Standard D2s v3                  │
│   - 2 vCPUs (equivalente a i7)                      │
│   - 8 GB RAM                                         │
│   - 30 GB SSD (OS) + 100 GB SSD (datos)             │
│ • Base de Datos: SQL Server en Azure                │
│ • Almacenamiento: 200 GB                            │
│ • Respaldo automático: Diario                       │
│                                                       │
│ VENTAJAS:                                            │
│ ✓ Escalable (si crecen estudiantes)                 │
│ ✓ Respaldos automáticos                             │
│ ✓ Disponible 24/7 con SLA 99.95%                    │
│ ✓ No requiere mantenimiento técnico                 │
│ ✓ Fácil agregar recursos                            │
│                                                       │
│ COSTO:                                               │
│ • Máquina virtual + BD: $150-200/mes                │
│ • Total anual: $1,800-2,400                         │
│                                                       │
├──────────────────────────────────────────────────────┤
│                                                       │
│ RECOMENDACIÓN: Usar NUBE (Azure)                    │
│                                                       │
│ Razones:                                             │
│ 1. Costo inicial bajo ($0 en tecnología)            │
│ 2. Costo operativo predecible                       │
│ 3. Automático backup y recuperación                 │
│ 4. Escalabilidad si crece matrícula                 │
│ 5. Soporte 24/7 de Microsoft                        │
│ 6. Sin preocupación de hardware fallando             │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

#### Software Requerido

```
┌─────────────────────────────────────────────────┐
│         STACK DE TECNOLOGÍA                     │
├─────────────────────────────────────────────────┤
│                                                  │
│ SERVIDOR (Backend)                             │
│ ┌────────────────────────────────────────────┐ │
│ │ • Lenguaje: C# con .NET 8                  │ │
│ │ • Framework: ASP.NET Core                  │ │
│ │ • Versión: 8.0 (última estable)            │ │
│ │ • Base de Datos: SQL Server 2022           │ │
│ │   - Express (gratuito) para 450 usuarios   │ │
│ │   - O Standard si requiere más capacidad   │ │
│ └────────────────────────────────────────────┘ │
│                                                  │
│ CLIENTE WEB (Frontend)                         │
│ ┌────────────────────────────────────────────┐ │
│ │ • Framework: React 18+                     │ │
│ │ • Build: Vite o webpack                    │ │
│ │ • Componentes: Material-UI o Bootstrap     │ │
│ │ • Navegador: Chrome, Firefox, Safari,      │ │
│ │   Edge (versiones actuales)                │ │
│ └────────────────────────────────────────────┘ │
│                                                  │
│ CLIENTE MÓVIL (Opcional)                       │
│ ┌────────────────────────────────────────────┐ │
│ │ • Framework: React Native o Flutter        │ │
│ │ • Plataforma: Android 10+ / iOS 12+        │ │
│ └────────────────────────────────────────────┘ │
│                                                  │
│ SISTEMA OPERATIVO                              │
│ ┌────────────────────────────────────────────┐ │
│ │ Servidor:                                  │ │
│ │ • Windows Server 2022 (recomendado para    │ │
│ │   .NET)                                    │ │
│ │ • O Linux Ubuntu 22.04 LTS (gratuito,     │ │
│ │   alternativa económica)                   │ │
│ │                                             │ │
│ │ Cliente:                                   │ │
│ │ • Windows 10/11                            │ │
│ │ • macOS 12+                                │ │
│ │ • Linux (cualquier distribución)           │ │
│ └────────────────────────────────────────────┘ │
│                                                  │
│ LICENCIAS                                       │
│ ┌────────────────────────────────────────────┐ │
│ │ • SQL Server Express: GRATUITO             │ │
│ │ • .NET Framework: GRATUITO (Open Source)   │ │
│ │ • React: GRATUITO (MIT License)            │ │
│ │ • Windows Server: ~$500 licencia           │ │
│ │   (o Linux gratuito)                       │ │
│ │ • Total licencias: $0-500 (según SO)       │ │
│ └────────────────────────────────────────────┘ │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

#### Conectividad e Internet

```
┌───────────────────────────────────────────────────┐
│           REQUERIMIENTOS DE INTERNET              │
├───────────────────────────────────────────────────┤
│                                                    │
│ ESTADO ACTUAL:                                    │
│ • Conexión: Ethernet                             │
│ • Tipo de Línea: Fibra óptica                    │
│ • Velocidad Bajada: 50 Mbps                      │
│ • Velocidad Subida: 50 Mbps                      │
│ • Proveedor: Claro                               │
│ • Costo Mensual: $30                             │
│                                                    │
│ REQUERIMIENTO MÍNIMO (Fase 1):                   │
│ • Bajada: 50 Mbps ✓ (Actual cumple)              │
│ • Subida: 50 Mbps ✓ (Actual cumple)              │
│ • Latencia: < 100ms                              │
│ • Disponibilidad: 98% mensual                    │
│                                                    │
│ REQUERIMIENTO ÓPTIMO (Fase 2+):                  │
│ • Bajada: 100 Mbps ✓ Upgrade a $45/mes           │
│ • Subida: 100 Mbps                               │
│ • Latencia: < 50ms                               │
│ • Disponibilidad: 99.9% mensual                  │
│ • Redundancia: Doble conexión (fibra + mobile)   │
│                                                    │
│ CÁLCULO DE ANCHO DE BANDA:                       │
│ • Usuarios simultáneosmax: 50 estudiantes        │
│ • Por usuario: 1 Mbps promedio                   │
│ • Total requerido: 50 Mbps                       │
│ • Con seguridad (2x): 100 Mbps                   │
│                                                    │
│ PLAN RECOMENDADO:                                │
│ • Mantener 50 Mbps actual (fase 1)               │
│ • Upgrade a 100 Mbps si crece               │
│ • Ancho de banda garantizado: 75 Mbps min.       │
│                                                    │
├───────────────────────────────────────────────────┤
│ ANÁLISIS DE SEGURIDAD DE RED                     │
│                                                    │
│ • Firewall: Requiere (hardware)                  │
│ • VPN: Para administrativos remotos               │
│ • Certificado SSL: Para HTTPS                    │
│ • WAF: Web Application Firewall (opcional)       │
│                                                    │
└───────────────────────────────────────────────────┘
```

---

### 1.2 Brecha Tecnológica (Gap Analysis)

```
╔═══════════════════════════════════════════════════╗
║              ANÁLISIS DE BRECHAS                  ║
╚═══════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────┐
│ HARDWARE                                           │
├────────────────────────────────────────────────────┤
│                                                     │
│ Administrativos:                                  │
│ ┌─ Brecha Identificada  ─────────────────────┐   │
│ │ • Procesadores i3 son borderline            │   │
│ │ • Para mejor experiencia: Upgrade a i7      │   │
│ │ • Costo upgrade: $500-700 por equipo        │   │
│ │ • Costo total (5 equipos): $2,500-3,500     │   │
│ │ • Plazo: Antes o durante implementación     │   │
│ └────────────────────────────────────────────┘   │
│                                                     │
│ • RAM: 8GB ES SUFICIENTE ✓                        │
│ • Almacenamiento: 256GB ES SUFICIENTE ✓           │
│ • SO: Windows 10 ES COMPATIBLE ✓                  │
│                                                     │
│ Servidor:                                         │
│ ┌─ Solución  ─────────────────────────────────┐  │
│ │ NO COMPRAR SERVIDOR FÍSICO                  │  │
│ │ Usar Azure Cloud en su lugar                │  │
│ │ • Ahorra $3,500-5,000 inicial               │  │
│ │ • Costo operativo: $150-200/mes             │  │
│ │ • Mantenimiento: Lo hace Microsoft           │  │
│ └─────────────────────────────────────────────┘  │
│                                                     │
└────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────┐
│ SOFTWARE                                           │
├────────────────────────────────────────────────────┤
│                                                     │
│ Licencias:                                        │
│ • .NET (Backend): GRATUITO (Open Source)          │
│ • SQL Server Express: GRATUITO                    │
│ • React (Frontend): GRATUITO                      │
│ • Visual Studio Community: GRATUITO               │
│                                                     │
│ Total Costo Licencias: $0-500                     │
│ (Depende si usan Windows Server o Linux)          │
│                                                    │
└────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────┐
│ PERSONAL TÉCNICO (Soporte)                        │
├────────────────────────────────────────────────────┤
│                                                     │
│ Necesidad Identificada:                           │
│ • 1 Técnico de TI para soporte diario             │
│ • 1 DBA (Database Admin) part-time (4 hrs/sem)    │
│                                                     │
│ Opción 1: Contratar interno                       │
│ • Costo: $400-500/mes                             │
│ • Disponibilidad: 24h en campus                   │
│                                                     │
│ Opción 2: Outsourcing                             │
│ • Costo: $300-400/mes                             │
│ • Disponibilidad: Remoto 9am-5pm                  │
│                                                     │
│ RECOMENDACIÓN: Opción 1 (interno)                 │
│ Razón: Instituciónneeds presence on campus        │
│                                                     │
└────────────────────────────────────────────────────┘
```

---

### 1.3 Conclusión Técnica

```
╔════════════════════════════════════════════════════╗
║  FACTIBILIDAD TÉCNICA: SISTEMA DE MATRÍCULA       ║
║  CONCLUSIÓN: ✓ FACTIBLE                           ║
╚════════════════════════════════════════════════════╝

REQUERIMIENTOS BÁSICOS:
┌────────────────────────────────────────────────────┐
│ ✓ Hardware Actual: CUMPLE (aunque borderline)     │
│ ✓ Tecnología Disponible: EXISTE Y ES ESTABLE      │
│ ✓ Conectividad: SUFICIENTE                         │
│ ✓ Licencias: ECONÓMICAS O GRATUITAS               │
│ ✓ Personal técnico: CONSEGIBLE                     │
└────────────────────────────────────────────────────┘

INVERSIÓN TÉCNICA INICIAL:
┌────────────────────────────────────────────────────┐
│ Upgrade Computadoras (i7): ~$3,000                │
│ Servidor (no aplica, usar Cloud): $0             │
│ Herramientas desarrollo: $0 (Open Source)         │
│ Capacitación técnica: ~$500                       │
│                                                    │
│ TOTAL INVERSIÓN: ~$3,500 (una sola vez)           │
└────────────────────────────────────────────────────┘

COSTOS RECURRENTES (Anuales):
┌────────────────────────────────────────────────────┐
│ Azure Cloud: $1,800/año                           │
│ Técnico de soporte: $4,800-6,000/año             │
│ Mantenimiento/actualizaciones: $1,200/año         │
│                                                    │
│ TOTAL RECURRENTE: ~$8,000/año                     │
└────────────────────────────────────────────────────┘

RIESG TÉCNICOS IDENTIFICADOS:
┌────────────────────────────────────────────────────┐
│ RIESGO | PROBABILIDAD | SOLUCIÓN                  │
│─────────────────────────────────────────────────────│
│ Caída servidor | Media | Respaldo Azure           │
│ Pérdida datos | Baja | Backup automático          │
│ Lentitud acceso | Baja | Upgrade de internet      │
│ Incompatibilidad navegador | Baja | Testing      │
│ Falta técnico soporte | Media | Capacitación      │
└────────────────────────────────────────────────────┘

RECOMENDACIONES:
1. ✓ Hacer UPGRADE a procesadores i7 ANTES de lanzar
2. ✓ Usar Azure Cloud en lugar de servidor local
3. ✓ Contratar técnico de TI dedicado
4. ✓ Configurar respaldos automáticos diarios
5. ✓ Documentar todo el sistema para transferencia
```

---

## 2. EJEMPLO COMPLETO: FACTIBILIDAD OPERATIVA - SISTEMA DE MATRÍCULA

### 2.1 Capacitación de Personal

```
┌────────────────────────────────────────────────────┐
│    PLAN DE CAPACITACIÓN POR GRUPO DE USUARIO      │
├────────────────────────────────────────────────────┤
│                                                     │
│ GRUPO 1: ADMINISTRATIVOS (5 personas)             │
│ ┌────────────────────────────────────────────┐   │
│ │ Rol: Gestionar todo el sistema             │   │
│ │ Experiencia Actual: Media (uso Windows)     │   │
│ │ Horas Capacitación: 20 horas               │   │
│ │                                             │   │
│ │ Modelo de Capacitación:                    │   │
│ │ • 2 sesiones presenciales de 4 horas       │   │
│ │ • 2 sesiones presenciales de 3 horas       │   │
│ │ • 6 horas práctica independiente            │   │
│ │                                             │   │
│ │ Temas:                                      │   │
│ │ 1. Crear período de matrícula (2 hrs)      │   │
│ │ 2. Gestionar cupos por asignatura (3 hrs)  │   │
│ │ 3. Crear oferta académica (2 hrs)          │   │
│ │ 4. Generar reportes (2 hrs)                │   │
│ │ 5. Resolver problemas estudiantes (6 hrs)  │   │
│ │ 6. Mantenimiento básico (3 hrs)            │   │
│ │ 7. Práctica intensiva (2 hrs)              │   │
│ │                                             │   │
│ │ Responsable: Proveedor del software        │   │
│ │ Formato: Presencial en institución         │   │
│ │ Cronograma: 2 semanas antes de lanzar      │   │
│ └────────────────────────────────────────────┘   │
│                                                     │
│ GRUPO 2: DOCENTES (25 personas)                  │
│ ┌────────────────────────────────────────────┐   │
│ │ Rol: Ver estudiantes matriculados          │   │
│ │ Experiencia: Variable (baja a media)        │   │
│ │ Horas Capacitación: 4 horas                │   │
│ │                                             │   │
│ │ Modelo de Capacitación:                    │   │
│ │ • 1 sesión presencial de 2 horas           │   │
│ │ • Video tutorial de 15 minutos              │   │
│ │ • FAQ en web                                │   │
│ │ • Soporte por email                         │   │
│ │                                             │   │
│ │ Temas:                                      │   │
│ │ 1. Acceder al sistema (1 hr)               │   │
│ │ 2. Ver mis estudiantes (1 hr)              │   │
│ │ 3. Descargar lista de asistencia (30 min)  │   │
│ │ 4. Preguntas frecuentes (30 min)           │   │
│ │                                             │   │
│ │ Responsable: Administrativo senior          │   │
│ │ Formato: Presencial (2 sesiones de 15)     │   │
│ │           O virtuales si lo prefieren       │   │
│ │ Cronograma: 1 semana antes de lanzar       │   │
│ └────────────────────────────────────────────┘   │
│                                                     │
│ GRUPO 3: ESTUDIANTES (450 personas)              │
│ ┌────────────────────────────────────────────┐   │
│ │ Rol: Matricularse en asignaturas           │   │
│ │ Experiencia: Media (internet natives)       │   │
│ │ Horas Capacitación: 1-2 horas              │   │
│ │                                             │   │
│ │ Modelo de Capacitación:                    │   │
│ │ • Video tutorial paso a paso (10 min)       │   │
│ │ • Infografía PDF descargable                │   │
│ │ • Sesión de Q&A en auditorio (30 min)      │   │
│ │ • FAQ interactivo en web                    │   │
│ │ • Soporte por email/WhatsApp                │   │
│ │                                             │   │
│ │ Temas:                                      │   │
│ │ 1. Acceder con matrícula+contraseña (2')   │   │
│ │ 2. Ver oferta disponible (2')              │   │
│ │ 3. Seleccionar y confirmar (3')            │   │
│ │ 4. Descargar constancia (2')               │   │
│ │ 5. Preguntas frecuentes (4')               │   │
│ │                                             │   │
│ │ Responsable: Equipo administrativo          │   │
│ │ Formato: Videos + Web + Soporte             │   │
│ │ Cronograma: 1 semana antes + durante       │   │
│ └────────────────────────────────────────────┘   │
│                                                     │
│ GRUPO 4: JEFES DE CARRERA (5 personas)           │
│ ┌────────────────────────────────────────────┐   │
│ │ Rol: Supervisar matrícula, verreportes     │   │
│ │ Experiencia: Media-Alta                     │   │
│ │ Horas Capacitación: 3 horas                │   │
│ │                                             │   │
│ │ Modelo: Sesión privada con proyecto manager │   │
│ │ Tópicos: Todo lo de administrativos         │   │
│ │          + análisis de datos/reportes       │   │
│ │                                             │   │
│ │ Cronograma: 3-4 semanas antes de lanzar    │   │
│ └────────────────────────────────────────────┘   │
│                                                     │
└────────────────────────────────────────────────────┘
```

### 2.2 Materiales de Capacitación

```
┌────────────────────────────────────────────────────┐
│       MATERIALES QUE SE CREARÁN/NECESITAN         │
├────────────────────────────────────────────────────┤
│                                                     │
│ PARA ADMINISTRATIVOS:                             │
│ ✓ Manual PDF (30 páginas)                         │
│ ✓ Video tutorial 45 minutos                       │
│ ✓ Guía de troubleshooting                         │
│ ✓ Tablas de configuración                         │
│ ✓ Procesos en FlowChart diagramas                 │
│ ✓ Checklist de inicio semestre                    │
│                                                     │
│ PARA DOCENTES:                                    │
│ ✓ Video 15 minutos (procedimiento)                │
│ ✓ Guía una página (imprimible)                    │
│ ✓ FAQ (5-10 preguntas)                           │
│ ✓ Screenshot anotados de pantallas               │
│                                                     │
│ PARA ESTUDIANTES:                                 │
│ ✓ Video animado 10 minutos                        │
│ ✓ Infografía paso a paso                         │
│ ✓ FAQ interactivo en web                          │
│ ✓ Chatbot para preguntas básicas                  │
│ ✓ Video adicionales para problemas comunes        │
│                                                     │
│ PARA JEFES DE CARRERA:                            │
│ ✓ Presentación ejecutiva 20 slides                │
│ ✓ Manual técnico                                  │
│ ✓ Dashboard de ejemplo                            │
│ ✓ Datos de prueba para análisis                   │
│                                                     │
└────────────────────────────────────────────────────┘
```

### 2.3 Cambios de Procesos

```
┌────────────────────────────────────────────────────┐
│         COMPARACIÓN: ANTES vs DESPUÉS              │
├────────────────────────────────────────────────────┤
│                                                     │
│ PROCESO 1: Matricularse en Asignaturas            │
│                                                     │
│ ANTES (Manual):                                   │
│ 1. Ir a oficina de registro                       │
│ 2. Hacer fila (30-60 minutos)                     │
│ 3. Llenar formulario en papel                     │
│ 4. Pagar matrícula                                │
│ 5. Recibir constancia impresa                     │
│ 6. Archivador guarda datos                        │
│ TIEMPO: ~90 minutes × 450 estudiantes = 675 hrs! │
│ ERROR: Errores escritura, papeles perdidos        │
│ COST: 1 administrativo tiempo completo            │
│                                                     │
│ DESPUÉS (Online):                                 │
│ 1. Entrar a sistema desde casa                    │
│ 2. Seleccionar asignaturas (5 minutos)           │
│ 3. Confirmar matrícula                            │
│ 4. Descargar constancia PDF                       │
│ 5. Sistema guarda datos automáticamente           │
│ TIEMPO: ~5 minutos × 450 estudiantes = 37.5 hrs! │
│ ERROR: Validaciones automáticas previenen errores │
│ COST: 0.5 administrativos (parte tiempo)          │
│                                                     │
│ IMPACTO: 637.5 horas ahorradas + menos errores   │
│                                                     │
│ ─────────────────────────────────────────────────│
│                                                     │
│ PROCESO 2: Aprobar Matrícula (Administrativo)    │
│                                                     │
│ ANTES (Manual):                                   │
│ 1. Revisar documento en papel                     │
│ 2. Verificar cupos disponibles (manual)           │
│ 3. Anotar en libro mayor                          │
│ 4. Archivar documentos                            │
│ TIEMPO: 10 min × 450 = 4,500 minutos = 75 horas │
│ ERROR: Conflictos de cupos, sobrecapacidad        │
│                                                     │
│ DESPUÉS (Online):                                 │
│ 1. Sistema valida automáticamente                 │
│ 2. Cupos se verifican en tiempo real              │
│ 3. Datos se guardan en BD                         │
│ 4. Reporte automático cada día                    │
│ TIEMPO: Sistema hace todo automáticamente        │
│ ERROR: Control de calidad automático              │
│                                                     │
│ IMPACTO: 75 horas ahorradas + cero errores       │
│                                                     │
└────────────────────────────────────────────────────┘
```

### 2.4 Resistencia al Cambio

```
┌────────────────────────────────────────────────────┐
│         ANÁLISIS DE RESISTENCIA AL CAMBIO         │
├────────────────────────────────────────────────────┤
│                                                     │
│ GRUPO: ADMINISTRATIVOS                            │
│ Resistencia: MEDIA-ALTA                           │
│ ┌──────────────────────────────────────────────┐  │
│ │ RAZÓN: Están acostumbrados a forma manual    │  │
│ │        Miedo a perder control del proceso    │  │
│ │        Temor a que la tecnología les reempl │  │
│ │                                              │  │
│ │ MITIGACIÓN:                                  │  │
│ │ • Involucrar en diseño del sistema           │  │
│ │ • Mostrar que FACILITA su trabajo            │  │
│ │ • Capacitación extra (20 hrs vs 4-3 otros)  │  │
│ │ • Designar "power users" que lideren cambio │  │
│ │ • Itinerario: 1 mes de transición gradual    │  │
│ │ • Soporte dedicado durante cambio            │  │
│ └──────────────────────────────────────────────┘  │
│                                                     │
│ GRUPO: DOCENTES                                   │
│ Resistencia: MEDIA                                │
│ ┌──────────────────────────────────────────────┐  │
│ │ RAZÓN: Algunos no son tech-savvy             │  │
│ │        Temen complicaciones                  │  │
│ │        Aún no ven beneficio claro            │  │
│ │                                              │  │
│ │ MITIGACIÓN:                                  │  │
│ │ • Demostración vívida: "Ahora es tan fácil"  │  │
│ │ • Enfoque en beneficios: acceso rápido       │  │
│ │ • Capacitación breve (4 horas)               │  │
│ │ • Soporte por teléfono para dudas            │  │
│ │ • Manual impreso como referencia             │  │
│ │ • Perión de transición: 2-3 semanas         │  │
│ └──────────────────────────────────────────────┘  │
│                                                     │
│ GRUPO: ESTUDIANTES                                │
│ Resistencia: BAJA                                 │
│ ┌──────────────────────────────────────────────┐  │
│ │ RAZÓN: Generación digital, acostumbrados a   │  │
│ │        plataformas online                    │  │
│ │        Esperan esto como normal              │  │
│ │                                              │  │
│ │ MITIGACIÓN:                                  │  │
│ │ • Campañas en redes sociales                 │  │
│ │ • Videos divertidos, no aburridos            │  │
│ │ • Beta testing con estudiantes líderes       │  │
│ │ • FAQ en web + WhatsApp support              │  │
│ │ • Período de transición: 1 semana            │  │
│ └──────────────────────────────────────────────┘  │
│                                                     │
│ GRUPO: JEFES DE CARRERA                           │
│ Resistencia: BAJA-MEDIA                           │
│ ┌──────────────────────────────────────────────┐  │
│ │ RAZÓN: Pueden ver el valor en datos/reportes │  │
│ │        Pero preocupación por transición      │  │
│ │                                              │  │
│ │ MITIGACIÓN:                                  │  │
│ │ • Mostrar dashboards y reportes              │  │
│ │ • Involucrar en definición de reportes       │  │
│ │ • Sesiones privadas de capacitación          │  │
│ │ • Acceso a datos de prueba                   │  │
│ └──────────────────────────────────────────────┘  │
│                                                     │
└────────────────────────────────────────────────────┘
```

### 2.5 Soporte Técnico

```
┌────────────────────────────────────────────────────┐
│          PLAN DE SOPORTE TÉCNICO                  │
├────────────────────────────────────────────────────┤
│                                                     │
│ FASE 1: DURANTE IMPLEMENTACIÓN (3 meses)         │
│                                                     │
│ Equipo de Soporte:                                │
│ • 1 Técnico Senior (Proveedor)                    │
│ • 1 Técnico Local (Institución)                   │
│ • 1 Project Manager                               │
│                                                     │
│ Horario: Lunes-Viernes 7am-6pm                   │
│ Canales:                                          │
│ • Teléfono: Ext. 105                             │
│ • Email: soporte@universidad.edu.ni               │
│ • Presencial: Oficina informatica (9am-5pm)      │
│                                                     │
│ SLA (Service Level Agreement):                    │
│ • Nivel 1 (Error crítico): Respuesta en 15 min   │
│ • Nivel 2 (Error mayor): Respuesta en 1 hora     │
│ • Nivel 3 (Error menor): Respuesta en 4 horas    │
│                                                     │
│ ─────────────────────────────────────────────────│
│                                                     │
│ FASE 2: MANTENIMIENTO (Permanente)               │
│                                                     │
│ Equipo:                                           │
│ • 1 Técnico Local de TI                           │
│ • Soporte remoto del Proveedor (contratos)       │
│                                                     │
│ Horario: 7am-5pm, emergencias 24/7               │
│ Canales:                                          │
│ • Teléfono: Ext. 105                             │
│ • Email: soporte@universidad.edu.ni               │
│ • Ticketing system en web                         │
│                                                     │
│ SLA (Mantenimiento):                              │
│ • Crítico: 1 hora máximo                          │
│ • Mayor: 4 horas máximo                           │
│ • Menor: 1 día hábil                              │
│                                                     │
│ ─────────────────────────────────────────────────│
│                                                     │
│ CATEGORÍAS DE PROBLEMAS:                          │
│                                                     │
│ ✗ CRÍTICO: Sistema completo caído                 │
│   → Impact: Nadie puede matricularse              │
│   → Duración: <30 minutos                         │
│   → Ejemplo: DB Server offline                    │
│                                                     │
│ ✗ MAYOR: Funcionalidad central no funciona       │
│   → Impact: Algunos usuarios afectados            │
│   → Duración: <4 horas                            │
│   → Ejemplo: No se guardan matrículas             │
│                                                     │
│ ✗ MENOR: Funcionalidad limitada/cosmético        │
│   → Impact: Molestia pero no bloquea trabajo      │
│   → Duración: <24 horas                           │
│   → Ejemplo: Reporte mal formateado               │
│                                                     │
│ ✗ SOLICITUD: Nueva función o pregunta            │
│   → Impact: Ninguno                               │
│   → Duración: 1-2 semanas                         │
│   → Ejemplo: ¿Cómo…?                             │
│                                                     │
│ ─────────────────────────────────────────────────│
│                                                     │
│ BASE DE CONOCIMIENTO:                             │
│ • 50+ artículos FAQ                               │
│ • Procedimientos paso-a-paso                      │
│ • Videos tutoriales                               │
│ • Troubleshooting guide                           │
│ • Disponible en intranet                          │
│                                                     │
└────────────────────────────────────────────────────┘
```

### 2.6 Seguridad e Interfaz

```
┌────────────────────────────────────────────────────┐
│       SEGURIDAD Y DISEÑO DE INTERFAZ               │
├────────────────────────────────────────────────────┤
│                                                     │
│ SEGURIDAD DE INFORMACIÓN                          │
│                                                     │
│ Autenticación:                                    │
│ • Cada usuario: Matrícula + Contraseña           │
│ • Contraseñas: Hasheadas con bcrypt              │
│ • Sesión: Timeout 30 minutos inactividad          │
│ • Botón Logout: Cierra sesión completamente       │
│                                                     │
│ Autorización (por rol):                           │
│ ┌────────────────────────────────────────────┐   │
│ │ ESTUDIANTE: Puede ver su matrícula solo;   │   │
│ │            No puede cambiar notas           │   │
│ │            No puede ver otros estudiantes   │   │
│ │                                             │   │
│ │ DOCENTE: Puede ver sus estudiantes;        │   │
│ │          Puede ver asistencia;             │   │
│ │          No puede cambiar matrículas       │   │
│ │                                             │   │
│ │ ADMIN: Acceso completo al sistema;         │   │
│ │        Todos los reportes;                 │   │
│ │        Gestión completa de datos           │   │
│ │                                             │   │
│ │ JEFE CARRERA: Ve su carrera solo;         │   │
│ │               Reportes de sus estudiantes;  │   │
│ │               No puede editar matrículas;  │   │
│ │               Lectura solamente             │   │
│ └────────────────────────────────────────────┘   │
│                                                     │
│ Encriptación:                                     │
│ • HTTPS: Todo comunic. encriptada                 │
│ • Certificado SSL: De autoridad certificada       │
│ • Base datos: Datos sensibles encriptados         │
│                                                     │
│ Auditoría:                                        │
│ • Log de accesos: Quién, cuándo, qué hizo        │
│ • Registro cambios: Quién modificó datos          │
│ • Reporte diario: Actividades sospechosas         │
│                                                     │
│ Backup y Recuperación:                            │
│ • Backup diario: 11pm cada noche                  │
│ • Respaldo en 3 ubicaciones                       │
│ • RPO (Recovery Point Objective): 1 día máximo    │
│ • RTO (Recovery Time Objective): 2 horas máximo   │
│                                                     │
│ ─────────────────────────────────────────────────│
│                                                     │
│ INTERFAZ DE USUARIO (UI/UX)                      │
│                                                     │
│ Diseño Responsivo:                                │
│ • Desktop: 1920x1080 (pantalla normal)            │
│ • Tablet: 1024x768 (iPad)                         │
│ • Mobile: 375x667 (iPhone)                        │
│ • Todos auto-ajustan al tamaño                    │
│                                                     │
│ Usabilidad:                                       │
│ ✓ Menú claro y sencillo                           │
│ ✓ Colores consistentes                            │
│ ✓ Accionables claros (botones grandes)            │
│ ✓ Confirmaciones útiles                           │
│ ✓ Mensajes de error claros                        │
│ ✓ Accesibilidad: Para discapacitados              │
│ ✓ Velocidad: Carga de página < 3 segundos        │
│                                                     │
│ Compatibilidad de Navegadores:                    │
│ ✓ Chrome 90+                                       │
│ ✓ Firefox 88+                                      │
│ ✓ Safari 14+                                       │
│ ✓ Edge 90+                                         │
│                                                     │
│ Testing de Interfaz:                              │
│ • Grupo de prueba (50 estudiantes) prepara        │
│ • Feedback recogido                               │
│ • Mejoras implementadas                           │
│ • Beta testing de 1 semana                        │
│                                                     │
└────────────────────────────────────────────────────┘
```

### 2.7 Conclusión Operativa

```
╔═════════════════════════════════════════════════╗
║ FACTIBILIDAD OPERATIVA: SISTEMA DE MATRÍCULA   ║
║ CONCLUSIÓN: ✓ FACTIBLE                         ║
╚═════════════════════════════════════════════════╝

RESUMEN:
┌───────────────────────────────────────────────────┐
│ ✓ Capacitación: Planable y estructurada          │
│ ✓ Personal: Disponible (técnico TI)               │
│ ✓ Procesos: Mejoran significativamente           │
│ ✓ Resistencia: Manejable con estrategia          │
│ ✓ Soporte: Modelo definido y viable              │
│ ✓ Seguridad: Medidas adecuadas identificadas     │
│ ✓ Interfaz: Diseño amigable y testeable          │
└───────────────────────────────────────────────────┘

INVERSIÓN EN OPERACIÓN:

FASE 1 (Implementación - 3 meses):
$40,000 (salarios técnicos, capacitación)

FASE 2 (Operación Anual):
$8,000/año = soporte técnico

BENEFICIO OPERATIVO:
• 637 horas ahorradas en matrícula anual
• ~$12,000 en costos evitados
• Reducción de errores: 100x
• Satisfacción usuario: Estimada 90%+

RIESGOS OPERATIVOS MITIGADOS:
1. Resistencia personal: Con capacitación intensiva
2. Falta de soporte: Con técnico dedicado
3. Inseguridad de datos: Con controles implementados
4. Usabilidad: Con testing extensivo
```

---

## 3. EJEMPLO COMPLETO: FACTIBILIDAD ECONÓMICA - SISTEMA DE MATRÍCULA

### Contexto
**Institución:** Universidad Nacional Centro
**Estudiantes:** 450
**Administrativos:** 5
**Docentes:** 25
**Escenario:** La institución desarrolla el sistema internamente

### 3.1 Costos de Desarrollo

#### Personal

```
┌──────────────────────────────────────────────────────┐
│         COSTOS DE PERSONAL (AÑO 0)                  │
├──────────────────────────────────────────────────────┤
│                                                       │
│ Desarrolladores Backend:                            │
│ • Cantidad: 2 personas                              │
│ • Salario: $400/mes cada uno                        │
│ • Duración: 18 meses                                │
│ • Subtotal: 2 × $400 × 18 = $14,400                │
│                                                       │
│ Diseñador UI/UX:                                    │
│ • Cantidad: 1 persona                               │
│ • Salario: $300/mes                                 │
│ • Duración: 12 meses                                │
│ • Subtotal: 1 × $300 × 12 = $3,600                 │
│                                                       │
│ Project Manager:                                    │
│ • Cantidad: 1 persona                               │
│ • Salario: $450/mes                                 │
│ • Duración: 18 meses                                │
│ • Subtotal: 1 × $450 × 18 = $8,100                 │
│                                                       │
│ QA/Testing:                                         │
│ • Cantidad: 1 persona                               │
│ • Salario: $250/mes                                 │
│ • Duración: 6 meses                                 │
│ • Subtotal: 1 × $250 × 6 = $1,500                  │
│                                                       │
│ ────────────────────────────────────────────────     │
│ TOTAL PERSONAL: $27,600                             │
│                                                       │
└──────────────────────────────────────────────────────┘
```

#### Hardware y Software

```
┌──────────────────────────────────────────────────────┐
│    HARDWARE Y SOFTWARE PARA DESARROLLO              │
├──────────────────────────────────────────────────────┤
│                                                       │
│ Licencias Visual Studio Enterprise:                 │
│ • Para 2 desarrolladores: 2 × $500 = $1,000        │
│                                                       │
│ Servidor de pruebas (hardware):                     │
│ • 1 servidor físico o VM: $1,500                    │
│                                                       │
│ Software de gestión de proyectos (Jira):            │
│ • Licencia anual: $500                              │
│                                                       │
│ ────────────────────────────────────────────────     │
│ TOTAL HARDWARE/SW: $3,000                           │
│                                                       │
└──────────────────────────────────────────────────────┘
```

#### Otros Gastos

```
| Concepto | Monto |
|----------|-------|
| Capacitación de equipo | $500 |
| Viáticos y reuniones | $300 |
| Documentación | $200 |
| Otros | $100 |
| **TOTAL OTROS** | **$1,100** |
```

**COSTO TOTAL AÑO 0 (DESARROLLO): $31,700**

---

### 3.2 Costos Anuales de Mantenimiento (Año 1 en adelante)

```
┌──────────────────────────────────────────────────────┐
│    COSTOS OPERACIONALES ANUALES                     │
├──────────────────────────────────────────────────────┤
│                                                       │
│ Servidor Azure Cloud (Standard D2s v3):             │
│ • Máquina virtual: $100/mes = $1,200/año           │
│ • Base de datos: $60/mes = $720/año                │
│ • Almacenamiento backup: $40/mes = $480/año        │
│ • Subtotal: $2,400/año                              │
│                                                       │
│ Técnico de Soporte TI:                              │
│ • 1 técnico local dedicado: $400/mes = $4,800/año  │
│                                                       │
│ Actualizaciones y Parches:                          │
│ • Mantenimiento preventivo: $100/mes = $1,200/año  │
│                                                       │
│ Licencias (renovación anual):                       │
│ • Visual Studio (1 licencia): $500/año              │
│                                                       │
│ ────────────────────────────────────────────────     │
│ TOTAL MANTENIMIENTO/AÑO: $8,900                     │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 3.3 Beneficios Esperados

```
┌──────────────────────────────────────────────────────┐
│         BENEFICIOS CUANTITATIVOS                    │
├──────────────────────────────────────────────────────┤
│                                                       │
│ BENEFICIO 1: Ahorro en Matrícula (UC3)             │
│ ─────────────────────────────────────────────        │
│ • Antes: 450 estudiantes × 90 min = 675 horas     │
│ • Después: 450 estudiantes × 5 min = 37.5 horas   │
│ • Ahorro: 637.5 horas por semestre                 │
│ • Anual: 637.5 × 2 semestres = 1,275 horas       │
│ • Costo de hora (admin): $30                        │
│ • Beneficio: 1,275 × $30 = $38,250/año             │
│                                                       │
│ BENEFICIO 2: Generación de Reportes (UC7)         │
│ ─────────────────────────────────────────────        │
│ • Reportes/mes: 5                                   │
│ • Tiempo antiguo: 2 horas/reporte = 10 res/mes    │
│ • Tiempo nuevo: 0.1 horas/reporte = 0.5 hrs/mes   │
│ • Ahorro: 9.5 horas/mes × 12 = 114 horas/año     │
│ • Beneficio: 114 × $30 = $3,420/año                │
│                                                       │
│ BENEFICIO 3: Reducción de Errores                  │
│ ─────────────────────────────────────────────        │
│ • Errores manuales: ~10% (45 estudiantes)          │
│ • Tiempo corrección: 1 hora cada uno = 45 horas   │
│ • Costo: 45 × $30 = $1,350 por semestre           │
│ • Anual: $1,350 × 2 = $2,700/año                   │
│ • Con sistema: 0 errores = $0                       │
│ • Beneficio: $2,700/año                             │
│                                                       │
│ BENEFICIO 4: Mejor Servicio a Estudiantes         │
│ ─────────────────────────────────────────────        │
│ • Satisfacción +20%                                 │
│ • Reducción quejas: 50%                             │
│ • Valor: Retención de estudiantes                   │
│ • Estimado: $5,000/año (reducción pérdida)         │
│                                                       │
│ ────────────────────────────────────────────────     │
│ TOTAL BENEFICIOS ANUALES: $49,370/año              │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 3.4 Proyección Financiera (5 años)

```
┌──────────────────────────────────────────────────────────────────────┐
│                    ANÁLISIS FINANCIERO 5 AÑOS                        │
├──────────────────────────────────────────┼───┬───┬───┬───┬──────────┤
│ CONCEPTO                 │ Año 0 │ Año 1  │ Año 2  │ Año 3  │ Año 4  │
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ INGRESOS                 │       │        │        │        │        │
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ Beneficios operacionales │ $0    │ $49,370│ $49,370│ $49,370│ $49,370│
│ (ahorro + eficiencia)    │       │        │        │        │        │
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ TOTAL INGRESOS           │ $0    │ $49,370│ $49,370│ $49,370│ $49,370│
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ COSTOS                   │       │        │        │        │        │
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ Desarrollo inicial       │ -$31,700 │ $0  │ $0     │ $0     │ $0     │
│ Mantenimiento/año        │ $0    │ -$8,900│ -$8,900│ -$8,900│ -$8,900│
│ Soporte técnico          │ $0    │ -$4,800│ -$4,800│ -$4,800│ -$4,800│
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ TOTAL COSTOS             │ -$31,700 │ -$13,700 │ -$13,700 │ -$13,700│
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ FLUJO DE CAJA            │ -$31,700│ $35,670│ $35,670│ $35,670│ $35,670│
├──────────────────────────┼───────┼────────┼────────┼────────┼────────┤
│ FLUJO ACUMULADO          │ -$31,700│ $3,970 │ $39,640│ $75,310│ $110,980│
└──────────────────────────┴───────┴────────┴────────┴────────┴────────┘
```

---

### 3.5 Indicadores Financieros

```
┌──────────────────────────────────────────────────────┐
│           CÁLCULOS FINANCIEROS                      │
├──────────────────────────────────────────────────────┤
│                                                       │
│ VAN (Valor Actual Neto) - Tasa descuento: 10%      │
│                                                       │
│ VAN = Σ(Flujo de Caja / (1+r)^n) - Inversión       │
│ VAN = (-31,700) + (35,670/(1.1)^1) +               │
│       (35,670/(1.1)^2) + (35,670/(1.1)^3) +         │
│       (35,670/(1.1)^4)                              │
│                                                       │
│ VAN = -31,700 + 32,427 + 29,479 + 26,799 +         │
│       24,362                                         │
│ VAN = $81,367 ✓ POSITIVO                            │
│                                                       │
│ ─────────────────────────────────────────────        │
│                                                       │
│ TIR (Tasa Interna de Retorno)                      │
│                                                       │
│ Se calcula cuando VAN = 0                          │
│ Resultado: TIR ≈ 89% ✓ MUY ALTA                    │
│                                                       │
│ (Mucho mayor que tasa de descuento 10%)             │
│                                                       │
│ ─────────────────────────────────────────────        │
│                                                       │
│ Payback Period (Recuperación de inversión)         │
│                                                       │
│ Año 0: -$31,700 (todo invertido en desarrollo)     │
│ Año 1: -$31,700 + $35,670 = $3,970 ✓               │
│                                                       │
│ Recuperación ocurre durante el AÑO 1                │
│ Plazo exacto: 31,700 / 35,670 = 0.89 años        │
│ = ~10.7 meses                                        │
│                                                       │
│ ─────────────────────────────────────────────        │
│                                                       │
│ ROI (Retorno sobre inversión) - Año 5               │
│                                                       │
│ ROI = (Ganancia neta / Inversión inicial) × 100     │
│ ROI = ((110,980) / 31,700) × 100                    │
│ ROI = 350% ✓ EXCELENTE                              │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 3.6 Análisis de Sensibilidad

**¿Qué pasa si los beneficios son menores o mayores?**

```
┌──────────────────────────────────────────────────────┐
│        ESCENARIOS ALTERNATIVOS                      │
├──────────────────────────────────────────────────────┤
│                                                       │
│ ESCENARIO PESIMISTA (30% menos beneficios)         │
│ ──────────────────────────────────────────          │
│ • Beneficios reales: $49,370 × 0.7 = $34,559      │
│ • Flujo Año 1: $34,559 - $13,700 = $20,859        │
│ • Payback: 31,700 / 20,859 = 1.52 años            │
│ • VAN (5 años): ~$45,200 (positivo aún)            │
│ • TIR: ~56% (aún mayor que 10% tasa)               │
│ • CONCLUSIÓN: Viable incluso con este escenario     │
│                                                       │
│ ESCENARIO PROBABLE (100% beneficios)               │
│ ──────────────────────────────────────────          │
│ • (Este es el del análisis anterior)                │
│ • Payback: 0.89 años (~11 meses)                   │
│ • VAN: $81,367                                      │
│ • TIR: 89%                                          │
│ • CONCLUSIÓN: MUY RENTABLE                          │
│                                                       │
│ ESCENARIO OPTIMISTA (30% más beneficios)           │
│ ──────────────────────────────────────────          │
│ • Beneficios reales: $49,370 × 1.3 = $64,181      │
│ • Flujo Año 1: $64,181 - $13,700 = $50,481        │
│ • Payback: 31,700 / 50,481 = 0.63 años            │
│ • VAN (5 años): ~$145,000 (muy positivo)           │
│ • TIR: ~145% (excelente)                           │
│ • CONCLUSIÓN: ALTAMENTE RENTABLE                    │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 3.7 Conclusión Económica

```
╔═════════════════════════════════════════════════╗
║ FACTIBILIDAD ECONÓMICA: SISTEMA DE MATRÍCULA   ║
║ CONCLUSIÓN: ✓✓ MUY VIABLE                      ║
╚═════════════════════════════════════════════════╝

INDICADORES FINANCIEROS:
┌─────────────────────────────────────────┐
│ VAN (5 años): $81,367 ✓ POSITIVO       │
│ TIR: 89% ✓ EXCELENTE (vs 10% requerido)│
│ Payback: 0.89 años ✓ MENOS DE 1 AÑO    │
│ ROI (5 años): 350% ✓ MUY ALTO          │
│ En escenario pesimista aún es viable   │
└─────────────────────────────────────────┘

RESUMEN FINANCIERO:
• Inversión inicial: $31,700 (una sola vez)
• Beneficio anual: $49,370
• Payback: ~11 meses
• En 5 años: $110,980 de ganancia neta
• VEREDICTO: Proyecto altamente rentable
```

---

## 4. EJEMPLO COMPLETO: FACTIBILIDAD LEGAL - SISTEMA DE MATRÍCULA

### 4.1 Análisis de Leyes Aplicables

```
┌──────────────────────────────────────────────────────┐
│      LEYES DE PROTECCIÓN DE DATOS                   │
├──────────────────────────────────────────────────────┤
│                                                       │
│ Contexto: Nicaragua (país de la institución)        │
│                                                       │
│ LEYES APLICABLES:                                   │
│                                                       │
│ 1. Ley de Protección de Datos Personales de        │
│    Nicaragua (Decreto No. 3-2008)                   │
│    ✓ Aplica: SÍ (recopila datos estudiantes)       │
│    Impacto: Requiere políticas de privacidad       │
│    Requisito: Consentimiento informado              │
│                                                       │
│ 2. Regulaciones de Privacidad de Educación         │
│    (Ministerio de Educación)                        │
│    ✓ Aplica: SÍ (datos académicos)                 │
│    Impacto: Acceso restringido a datos             │
│    Requisito: Auditoría de acceso                   │
│                                                       │
│ 3. GDPR (General Data Protection Regulation)       │
│    ✗ Aplica: NO (aplica solo UE)                   │
│                                                       │
│ 4. Ley de Contraloría General                      │
│    ✓ Aplica: SÍ (institución pública)             │
│    Impacto: Transparencia en datos                  │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 4.2 Datos Personales Manejados

```
┌──────────────────────────────────────────────────────┐
│      INVENTARIO DE DATOS PERSONALES                 │
├──────────────────────────────────────────────────────┤
│                                                       │
│ ESTUDIANTES (450 personas):                         │
│ • Nombre completo (dato sensible)                   │
│ • Número de cédula (dato sensible)                  │
│ • Email y teléfono                                  │
│ • Carrera y semestre                                │
│ • Calificaciones (dato sensible)                    │
│ • Asignaturas matriculadas                          │
│ • Historial académico completo                      │
│ • Domicilio                                         │
│                                                       │
│ ADMINISTRATIVOS (5 personas):                       │
│ • Nombre y cédula                                   │
│ • Email y teléfono de trabajo                       │
│ • Rol en sistema (admin, moderador, etc)            │
│                                                       │
│ DOCENTES (25 personas):                             │
│ • Nombre y cédula                                   │
│ • Email institucional                               │
│ • Especialidades/materias enseñadas                 │
│ • Horarios                                          │
│                                                       │
│ Volumen total: ~480 personas × 8-12 campos         │
│ Total registros: ~5,000 campos de datos            │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 4.3 Medidas de Protección de Datos

```
┌──────────────────────────────────────────────────────┐
│      CÓMO SE PROTEGEN LOS DATOS                     │
├──────────────────────────────────────────────────────┤
│                                                       │
│ 1. AUTENTICACIÓN                                    │
│    └─ Usuario + Contraseña                          │
│       • Contraseñas hasheadas con bcrypt            │
│       • No se guardan en texto plano                │
│       • Cambio de contraseña cada 90 días           │
│                                                       │
│ 2. AUTORIZACIÓN (Por Rol)                           │
│    ├─ Estudiante:                                   │
│    │  ✓ Ver solo sus propios datos                  │
│    │  ✗ No puede ver otros estudiantes              │
│    │  └─ Único acceso: calificaciones, matrícula    │
│    │                                                 │
│    ├─ Docente:                                      │
│    │  ✓ Ver estudiantes de sus clases               │
│    │  ✓ Ver asistencia                              │
│    │  ✗ No puede modificar calificaciones           │
│    │                                                 │
│    ├─ Administrativo:                               │
│    │  ✓ Acceso completo a todos datos              │
│    │  ✓ Puede modificar con auditoría               │
│    │                                                 │
│    └─ Jefe de Carrera:                              │
│       ✓ Ver datos de su carrera solo                │
│       ✓ Ver reportes agregados                      │
│       ✗ No puede editar datos                       │
│                                                       │
│ 3. ENCRIPTACIÓN                                     │
│    ├─ En tránsito: HTTPS/SSL                        │
│    │  • Certificado SSL válido                      │
│    │  • Todas las conexiones cifradas               │
│    │                                                 │
│    └─ En reposo (base de datos):                    │
│       • Datos sensibles encriptados (AES-256)       │
│       • Contraseñas hasheadas (no recuperables)     │
│                                                       │
│ 4. AUDITORÍA Y REGISTRO                             │
│    ├─ Log de todos los accesos                      │
│    │  • Quién accedió                               │
│    │  • Cuándo accedió                              │
│    │  • Qué datos vio                               │
│    │  • Qué cambios hizo                            │
│    │                                                 │
│    └─ Revisión diaria de logs                       │
│       • Buscar accesos sospechosos                  │
│       • Alertas automáticas                         │
│                                                       │
│ 5. BACKUP Y RECUPERACIÓN                            │
│    ├─ Respaldo diario: 11:00 PM                     │
│    ├─ Ubicación: 3 centros de datos                 │
│    ├─ RPO (máximo a perder): 1 día                  │
│    └─ RTO (tiempo recuperación): 2 horas máximo     │
│                                                       │
│ 6. CONTROL DE ACCESO FÍSICO                         │
│    ├─ Servidor en datacenter con seguridad          │
│    └─ O en Azure (Microsoft maneja seguridad)       │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 4.4 Derechos de Propiedad Intelectual

```
┌──────────────────────────────────────────────────────┐
│         ¿QUIÉN ES DUEÑO DEL SISTEMA?                │
├──────────────────────────────────────────────────────┤
│                                                       │
│ PROPIEDAD DEL CÓDIGO:                               │
│ └─ Dueño: Universidad Nacional Centro               │
│    • Desarrolladores fueron empleados de la uni     │
│    • Código fue desarrollado en horario laboral     │
│    • Según ley: propiedad es de la institución      │
│                                                       │
│ COPYRIGHT (Derecho de Autor):                       │
│ ├─ Registrado: Sí, ante DNDA (Dirección            │
│ │             Nacional de Derechos de Autor)       │
│ ├─ Número de registro: [Pendiente de tramitar]      │
│ ├─ Protección: Válida por 70 años post-muerte      │
│ │             del autor o 70 años para empresa     │
│ │                                                   │
│ └─ Implicaciones:                                   │
│    • Nadie puede copiar el código sin permiso       │
│    • La universidad puede vender licencias          │
│    • Terceros no pueden distribuir                  │
│                                                       │
│ PATENTE:                                            │
│ └─ Aplicable: NO (no es invención patentable)      │
│    • Es un software de gestión estándar             │
│    • Las ideas base no son novedosas                │
│    • Costo/complejidad no justifica                 │
│                                                       │
│ SECRETO COMERCIAL:                                  │
│ └─ Aplica: PARCIALMENTE                             │
│    • Algoritmos específicos (si los hay)            │
│    • Configuración de seguridad                     │
│    • Datos de la institución                        │
│    • Base de datos con información estudiantes      │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 4.5 Licencias de Software Utilizadas

```
┌──────────────────────────────────────────────────────┐
│      LICENCIAS DE SOFTWARE UTILIZADAS               │
├──────────────────────────────────────────────────────┤
│                                                       │
│ .NET Framework 8.0:                                 │
│ • Licencia: MIT License (Open Source)               │
│ • Costo: GRATUITO                                   │
│ • Uso permitido: Comercial, privado, modificación   │
│ • Requisito: Incluir copyright/licencia             │
│ • CUMPLIMIENTO: ✓ SENCILLO                          │
│                                                       │
│ ASP.NET Core:                                       │
│ • Licencia: MIT License (Open Source)               │
│ • Costo: GRATUITO                                   │
│ • Requisito: Incluir copyright/licencia             │
│ • CUMPLIMIENTO: ✓ SENCILLO                          │
│                                                       │
│ React (Frontend):                                   │
│ • Licencia: BSD License (Open Source)               │
│ • Costo: GRATUITO                                   │
│ • Requisito: Incluir copyright/licencia             │
│ • CUMPLIMIENTO: ✓ SENCILLO                          │
│                                                       │
│ SQL Server Express (Base Datos):                    │
│ • Licencia: Gratuita con restricciones              │
│ • Límite: 1 GB RAM, 10 GB DB, no cluster           │
│ • Para 450 estudiantes: ✓ SUFICIENTE                │
│ • Costo: GRATUITO (si < 10 GB)                     │
│ • Upgrade a Standard: $3,500 si crece               │
│ • CUMPLIMIENTO: ✓ ACTUAL ESTÁ OK                    │
│                                                       │
│ Visual Studio Community:                            │
│ • Licencia: Gratuita para educación                 │
│ • Costo: GRATUITO                                   │
│ • CUMPLIMIENTO: ✓ GRATUITO                          │
│                                                       │
│ Azure Cloud:                                        │
│ • Licencia: Acuerdos de servicio Microsoft          │
│ • Costo: Pago por uso ($150-200/mes)               │
│ • CUMPLIMIENTO: ✓ LICENCIA COMERCIAL OK             │
│                                                       │
│ ────────────────────────────────────────────────     │
│ TOTAL CUMPLIMIENTO DE LICENCIAS: ✓ EXCELENTE        │
│ • Todas las librerías respetan términos             │
│ • Licencias open-source son permisivas              │
│ • No hay conflictos legales                         │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 4.6 Contratos Necesarios

```
┌──────────────────────────────────────────────────────┐
│      DOCUMENTOS LEGALES REQUERIDOS                  │
├──────────────────────────────────────────────────────┤
│                                                       │
│ 1. POLÍTICA DE PRIVACIDAD ✓                        │
│    ├─ Describe: Qué datos recopilamos               │
│    ├─ Cómo los usamos                               │
│    ├─ Medidas de seguridad                          │
│    ├─ Derechos del usuario (acceso, corrección)     │
│    ├─ Tiempo de retención                           │
│    │  (Estudiantes actuales: Indefinido)            │
│    │  (Estudiantes egresados: 10 años)              │
│    ├─ Contacto: dpo@universidad.edu.ni              │
│    └─ Ubicación: www.universidad.edu.ni/privacidad  │
│                                                       │
│ 2. TÉRMINOS DE SERVICIO ✓                          │
│    ├─ Disponibilidad del sistema                    │
│    │  (99.5% uptime garantizado)                    │
│    ├─ Responsabilidades usuario                     │
│    ├─ Responsabilidades institución                 │
│    ├─ Penalizaciones por mal uso                    │
│    ├─ Limitación de responsabilidad                 │
│    ├─ Ley aplicable: Nicaragua                      │
│    └─ Jurisdicción: Cortes de Nicaragua             │
│                                                       │
│ 3. ACUERDO DE CONFIDENCIALIDAD (NDA) ✓            │
│    ├─ Firmado por: Personal administrativo          │
│    │               Personal de desarrollo (if hired) │
│    ├─ Define: Qué es información confidencial       │
│    ├─ Período: 5 años post-empleo                   │
│    ├─ Penalizaciones: Por violación                 │
│    └─ Excepciones: Información pública, requerida  │
│                                                       │
│ 4. CONTRATO DE DESARROLLO ✓                        │
│    (Si fue externo, incluye:)                       │
│    ├─ Alcance del proyecto                          │
│    ├─ Costos y cronograma                           │
│    ├─ Entregables específicos                       │
│    ├─ Propiedad del código (sí es universidad)      │
│    ├─ Garantías de funcionamiento                   │
│    ├─ Soporte post-implementación                   │
│    └─ Cláusulas de resolución                       │
│                                                       │
│ 5. ACUERDO DE NIVEL DE SERVICIO (SLA) ✓           │
│    ├─ Disponibilidad garantizada: 99.5%             │
│    ├─ Tiempo de respuesta soporte: 1 hora           │
│    ├─ Tiempo de resolución: 4 horas                 │
│    ├─ Backup: Diarios                               │
│    ├─ Penalizaciones si no cumple                   │
│    └─ Revisión: Trimestral                          │
│                                                       │
│ 6. CONSENTIMIENTO DE ESTUDIANTES ✓                 │
│    ├─ Formulario: Aceptar Términos y Privacidad    │
│    ├─ Recopilado: En primera matrícula              │
│    ├─ Archivado: En expediente estudiante           │
│    └─ Renovación: Cada año académico                │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 4.7 Riesgos Legales Identificados

```
┌──────────────────────────────────────────────────────┐
│          RIESGOS LEGALES Y MITIGACIÓN               │
├──────────────────────────────────────────────────────┤
│                                                       │
│ RIESGO 1: Fuga de Datos Personales                 │
│ ─────────────────────────────────────────          │
│ Probabilidad: MEDIA                                 │
│ Severidad: ALTA (multas + reputación)               │
│ Prevención:                                         │
│ • Encriptación AES-256 en BD                        │
│ • HTTPS para todas las conexiones                   │
│ • Auditoría de accesos diaria                       │
│ • Firewall y WAF                                    │
│ • Pruebas de penetración anual                      │
│ Penalidad legal: Multa + cierre del sistema        │
│                                                       │
│ RIESGO 2: Acceso No Autorizado                     │
│ ─────────────────────────────────────────          │
│ Probabilidad: BAJA                                  │
│ Severidad: MEDIA                                    │
│ Prevención:                                         │
│ • 4 niveles distintos de acceso                     │
│ • Log de acceso para auditoría                      │
│ • Cambio de contraseña cada 90 días                 │
│ • Alert de múltiples fallos de login                │
│ Penalidad: Acceso indebido a información            │
│                                                       │
│ RIESGO 3: Violación de Copyright                   │
│ ─────────────────────────────────────────          │
│ Probabilidad: BAJA                                  │
│ Severidad: MEDIA                                    │
│ Prevención:                                         │
│ • Código 100% original                              │
│ • Copyright registrado                              │
│ • Documentación de desarrollo                       │
│ • No se copia código externo sin licencia            │
│ Penalidad: Demanda civil + daños                    │
│                                                       │
│ RIESGO 4: Incumplimiento Ley Datos Personales     │
│ ─────────────────────────────────────────          │
│ Probabilidad: BAJA (con medidas)                    │
│ Severidad: MUY ALTA                                 │
│ Prevención:                                         │
│ • Política privacidad publicada                     │
│ • Consentimiento estudiantes firmado                │
│ • Protección de datos implementada                  │
│ • DPO designado (Data Protection Officer)           │
│ • Auditoría externa anual                           │
│ Penalidad: Multa hasta 10% ingresos o $500k nic   │
│                                                       │
│ RIESGO 5: Cambio de Regulaciones Futuras          │
│ ─────────────────────────────────────────          │
│ Probabilidad: MEDIA (ley sigue evolucionando)      │
│ Severidad: BAJA (tiempo para adaptarse)             │
│ Prevención:                                         │
│ • Monitorear regulaciones nuevas                    │
│ • Sistema flexible para cambios                     │
│ • Consulta legal periódica                          │
│ • Auditoría de cumplimiento anual                   │
│ Penalidad: Multa + tiempo para cumplir              │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

### 4.8 Conclusión Legal

```
╔═════════════════════════════════════════════════╗
║ FACTIBILIDAD LEGAL: SISTEMA DE MATRÍCULA       ║
║ CONCLUSIÓN: ✓ FACTIBLE                         ║
╚═════════════════════════════════════════════════╝

EVALUACIÓN POR ASPECTO:

✓ Protección de Datos:
  • Medidas implementadas
  • Política privacidad clara
  • Cumple ley local (Nicaragua)
  • ESTADO: CONFORME

✓ Propiedad Intelectual:
  • Código: Propiedad de universidad (100%)
  • Copyright: Registrado
  • Licencias open-source: Respetadas
  • ESTADO: PROTEGIDO

✓ Licencias de Software:
  • Todas las librerías con licencias válidas
  • Open-source con términos claros
  • Costo: Bajo/gratuito
  • ESTADO: CUMPLIDO

✓ Contratos:
  • Todos los documentos requeridos preparados
  • Términos claros y justos
  • SLA definido
  • ESTADO: EN ORDEN

✓ Riesgos Legales:
  • Identificados
  • Mitigados con medidas específicas
  • Monitoreo continuo
  • ESTADO: CONTROLADO

VEREDICTO FINAL:
El proyecto es LEGALMENTE FACTIBLE con todas
las medidas de protección y documentación adecuadas.
