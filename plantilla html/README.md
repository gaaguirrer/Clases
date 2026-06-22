# Plantilla HTML para Unidades Didácticas

Esta carpeta contiene un archivo `plantilla.html` listo para usar como base para crear unidades didácticas con formato de libro (tamaño carta). Incluye todos los estilos CSS y la estructura HTML necesaria en un solo archivo autónomo.

---

## Estructura del documento

Cada unidad se compone de páginas individuales, cada una representada por un `<div>` con clase específica:

| Clase            | Propósito                                   |
|------------------|---------------------------------------------|
| `page-letter`    | Portada del documento (sin número de página)|
| `page-content`   | Páginas de contenido (numeradas automáticamente) |

### Portada

Contiene el logotipo UNHSJM (SVG), el nombre de la universidad, el título de la unidad y dos barras decorativas. La portada no lleva número de página.

> **⚠️ REGLA: NO MODIFICAR EL LOGO INSTITUCIONAL**  
> El bloque completo de la portada —SVG del escudo, texto "UNHSJM", línea roja divisoria, y texto "UNIVERSIDAD NACIONAL HÉROES DE SAN JOSÉ DE LAS MULAS"— forma parte de la identidad institucional y **no debe modificarse, eliminarse ni alterarse** de ninguna forma. Cualquier cambio requiere aprobación del área de comunicación institucional. Solo se permite cambiar el título y subtítulo de la unidad.

### Páginas de contenido

Cada página mide exactamente 21.59 cm × 27.94 cm (tamaño carta). El contenido que excede esa altura se oculta (`overflow: hidden`), por lo que debe dividirse manualmente en páginas separadas.

---

## Encabezado de sección

Todas las secciones importantes llevan un encabezado con el siguiente diseño:

```
[Texto del encabezado] [▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌ barra roja 29%] [   ] [▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌ barra azul 69%]
```

Se implementa así:

- Un contenedor `.section-header` con `display: flex`.
- El texto `.header-text` ocupa su ancho natural (`flex-shrink: 0`).
- Un contenedor `.bar-container` con `flex: 1` ocupa el resto del ancho.
- Dentro de `.bar-container`:
  - `.block-red` con `flex: 29` (barra roja, 29 % del espacio restante).
  - `.bar-gap` con `flex: 2` (separador invisible, 2 % del espacio restante).
  - `.block-blue` con `flex: 69` (barra azul, 69 % del espacio restante).

Las secciones que deben usar este encabezado: **Índice**, **Introducción**, **Desarrollo de Contenidos**, **Autoevaluación**, **Bibliografía**, **Glosario**.

### Regla importante

Cuando una sección ocupa varias páginas (como Desarrollo de Contenidos), el encabezado debe repetirse en la parte superior de cada página.

---

## Temas y subtemas

Dentro de Desarrollo de Contenidos, los temas principales se resaltan con la clase `.topic-header`:

- Borde izquierdo rojo de 5 px (`#c52f2b`).
- Fondo gris claro (`#f5f5f5`).
- Fuente Times New Roman, 20 px, negrita, color azul institucional (`#193a6f`).

---

## Número de página

Cada `.page-content` incrementa automáticamente un contador CSS. El número se muestra al pie de la página, alineado a la derecha, encima de una línea divisoria.

- El contador se inicializa con `body { counter-reset: page 0; }` para que la portada (clase `page-letter`) no cuente.
- La portada no tiene la clase `page-content`, por lo que no participa en el contador.
- El número se genera con el pseudoelemento `.page-number::after { content: counter(page); }`.

---

## Reglas de partición de contenido

1. Cada página de contenido tiene una altura fija de 27.94 cm y oculta el desbordamiento.
2. El contenido debe dividirse manualmente entre páginas.
3. **Ningún párrafo debe quedar cortado entre dos páginas.** Si el espacio disponible en una página no alcanza para un párrafo completo, ese párrafo debe moverse completo a la siguiente página.
4. **El número de página debe ser siempre visible.** Si la línea divisoria y el número de página (`.page-number`) quedan más allá del alto de la página (ocultos por `overflow: hidden`), el último elemento completo de la página (párrafo, tabla, bloque de caso, lista, etc.) debe moverse a la siguiente página, incluso si ese elemento cabe visualmente en la página actual.
5. **Compactación vertical:** Cuando una página tiene espacio disponible después de su contenido, puede recibir el primer elemento completo de la siguiente página, siempre que:
   - El elemento completo quepa íntegramente en el espacio restante.
   - Después de moverlo, el número de página siga siendo visible.
6. **Doble verificación:** Los pasos 4 y 5 deben aplicarse al menos dos veces sobre el documento completo después de cada cambio estructural (añadir, quitar o reordenar contenido). En la primera pasada se corrigen desbordamientos evidentes; en la segunda se aprovecha espacio sobrante y se verifican de nuevo los números de página.
7. **Elementos que no deben particionarse:** Además de párrafos, los siguientes elementos deben mantenerse completos dentro de una misma página: tablas completas, bloques `.caso-exito`, `.caso-fallo`, `.highlight`, `.reflexion`, listas de 3 o más elementos, y bloques `.autoeval` completos.

---

## Colores institucionales UNHSJM

| Color        | Código   | Uso                                    |
|--------------|----------|----------------------------------------|
| Azul oscuro  | `#193a6f`| Barras, títulos, texto del logo        |
| Rojo         | `#c52f2b`| Barras decorativas, borde de subtemas  |
| Azul claro   | `#0a3d62`| Títulos h1, h2, encabezados de tabla   |

---

## Bloques de destaque

| Clase          | Color borde | Fondo      | Propósito                     |
|----------------|-------------|------------|-------------------------------|
| `.highlight`   | Naranja     | Naranja claro | Recomendaciones o conclusiones |
| `.caso-exito`  | Verde       | Verde claro | Casos de éxito                |
| `.caso-fallo`  | Rojo        | Rojo claro  | Casos de fracaso o advertencia |
| `.reflexion`   | Púrpura     | Púrpura claro | Reflexiones o análisis crítico |
| `.autoeval`    | Azul        | Azul claro  | Bloque de autoevaluación      |
| `.glosario`    | —           | —           | Lista de definiciones (`<dl>`) |

---

## Barras decorativas de la portada

- `line-blue-cover`: 69 % de ancho, color rojo (`#c52f2b`), colocada a la izquierda.
- `line-red-cover`: 29 % de ancho, color azul (`#193a6f`), colocada a la derecha.

Los nombres de las clases (`blue`/`red`) no corresponden al color real; se heredaron de una versión anterior donde los colores estaban alineados con el nombre.

---

## Impresión y PDF

Para generar un PDF correctamente:

1. Abrir el HTML en Chrome o Edge.
2. Presionar Ctrl+P.
3. En la configuración de impresión:
   - **Papel**: Carta (21.59 cm × 27.94 cm).
   - **Márgenes**: Ninguno.
   - **Gráficos de fondo**: Activado.
4. Guardar como PDF.

Las reglas `@media print` se encargan de:
- Eliminar sombras y bordes redondeados.
- Agregar `page-break-after: always` en cada página de contenido.
- Ajustar el padding a 0.5 pulgadas.
- Configurar `@page { margin: 0; size: letter portrait; }`.

---

## Archivos

| Archivo          | Descripción                                   |
|------------------|-----------------------------------------------|
| `plantilla.html` | Plantilla autónoma con todo incluido.         |
| `README.md`      | Este documento.                               |
