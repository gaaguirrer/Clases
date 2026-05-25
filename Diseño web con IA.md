# Guía: Crear una Landing Page con Kimi (Sin conocimientos previos)



---



## PASO 1: Iniciar la entrevista con Kimi



1. Ve a la web de Kimi (https://kimi.moonshot.cn)

2. Pega el siguiente prompt y presiona Enter:



&gt; Simula que eres un Diseñador web especialista en landing pages. Vas a hacerme una entrevista de máximo 10 preguntas para entender qué página web necesito. **Importante:** Enfoca todas tus preguntas en aspectos visuales, de contenido y objetivos de negocio de la web. **No hagas preguntas técnicas** (servidores, hosting, código, etc.) porque no tengo conocimientos de informática. Optimiza todo pensando en SEO (posicionamiento en Google). La landing page se hará con Vue, HTML y Tailwind CSS, se alojará en GitHub y se desplegará en Netlify. Si Netlify no soporta Vue, usa React. No usaré bases de datos. La arquitectura debe ser la más simple posible. Solo necesito una landing page informativa, no una aplicación web. Hazme las preguntas de una en una para que pueda responder cómodamente.



3. Responde cada pregunta que te haga Kimi con la mayor información posible sobre tu empresa.



---



## PASO 2: Documentar las preguntas y respuestas



1. Abre Microsoft Word (o cualquier editor de texto).

2. Copia todas las preguntas que hizo Kimi y las respuestas que diste.

3. Guarda el documento como `Entrevista Landing Page.docx` (o el nombre que prefieras).

4. Este documento es tu base; no lo pierdas.



---



## PASO 3: Generar el documento de especificaciones en Markdown



1. Vuelve a Kimi.

2. Pega el siguiente prompt, **incluyendo al final todas las preguntas y respuestas del Paso 2**:



&gt; Redacta un documento en Markdown con todas las especificaciones para mi landing page. Este documento servirá de base para generar mockups en Google Stitch. **No generes código de programación** en ninguna parte del documento. Usa solo texto descriptivo, listas y secciones claras. Recuerda: se desarrollará con Vue, HTML y Tailwind CSS (si Netlify no soporta Vue, usa React). La arquitectura debe ser extremadamente simple porque no tengo conocimientos de informática. No se usarán bases de datos. Se alojará en GitHub y se desplegará en Netlify. Optimiza todo para SEO. Incluye: nombre del proyecto, descripción de la empresa, secciones que debe tener la landing page, textos sugeridos, paleta de colores recomendada, tipografías, imágenes necesarias, estructura de navegación, y recomendaciones para el responsive (que se vea bien en celular). Entrega todo dentro de un único bloque de código Markdown, sin bloques de código internos ni snippets de programación.



[Pega aquí todas las preguntas y respuestas del Paso 2]



3. Copia todo el Markdown que genere Kimi.



---



## PASO 4: Crear la carpeta del proyecto y guardar requerimientos



1. En tu computadora, crea una carpeta nueva llamada **"Pagina Web"** (puedes hacerlo en el escritorio).

2. Dentro de esa carpeta, crea un documento de texto llamado **"Requerimientos"** (puedes usar el Bloc de Notas).

3. Pega todo el Markdown generado en el Paso 3 dentro de ese documento.

4. Guarda y cierra.



---



## PASO 5: Generar el mockup en Google Stitch



1. Ve a Google Stitch (https://stitch.withgoogle.com).

2. Pega el contenido completo del documento "Requerimientos" en el área de trabajo.

3. Pide a Google Stitch que genere el mockup/visualización de tu landing page basado en esas especificaciones.

4. Cuando esté listo, usa la opción **Exportar** → **Copiar código**.

5. Vuelve a tu carpeta **"Pagina Web"**.

6. Crea otro documento de texto y pega ahí el código copiado de Google Stitch.

7. Guarda ese documento con un nombre claro, por ejemplo: **"Mockup Stitch"**.



---



## Resumen de archivos en tu carpeta "Pagina Web"



- `Requerimientos.txt` → Especificaciones en Markdown (Paso 4)

- `Mockup Stitch.txt` → Código exportado de Google Stitch (Paso 5)



---



**Nota importante:** Esta guía llega hasta el Paso 5. Los siguientes pasos (desarrollo real del sitio, subida a GitHub, despliegue en Netlify) se abordarán en una siguiente etapa una vez que tengas listos estos documentos base.

