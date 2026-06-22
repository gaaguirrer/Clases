#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera UDIII OPII Gober_Cripto.html a partir del markdown usando la plantilla y estilos.
"""

import re
import markdown
from pathlib import Path

BASE = Path(r"C:\Users\ingga\OneDrive\Documentos\Nueva carpeta\Clases")
MD_FILE = BASE / r"Optativa profesional II (gobernanza y Criptografía)\Unidades\UDIII OPII Gober_Cripto.md"
OUTPUT = BASE / r"Optativa profesional II (gobernanza y Criptografía)\Unidades\UDIII OPII Gober_Cripto.html"

# ---- Leer markdown ----
md_text = MD_FILE.read_text(encoding="utf-8")

# ---- Extraer título ----
title_match = re.search(r"^# (.+)$", md_text, re.MULTILINE)
TITLE = title_match.group(1) if title_match else "Unidad Didáctica"

# ---- Extensiones de markdown ----
extensions = [
    "markdown.extensions.extra",
    "markdown.extensions.tables",
    "markdown.extensions.fenced_code",
    "markdown.extensions.smarty",
    "markdown.extensions.nl2br",
]

# ---- Reusable SVG logo ----
LOGO_SVG = '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <g id="rayo">
            <path d="M49 26 L51 26 L56 3 C56 2 54 1 50 1 C46 1 44 2 44 3 L49 26 Z" class="ray"/>
        </g>
    </defs>
    <use href="#rayo" transform="rotate(0, 50, 50)" />
    <use href="#rayo" transform="rotate(22.5, 50, 50)" />
    <use href="#rayo" transform="rotate(45, 50, 50)" />
    <use href="#rayo" transform="rotate(67.5, 50, 50)" />
    <use href="#rayo" transform="rotate(90, 50, 50)" />
    <use href="#rayo" transform="rotate(112.5, 50, 50)" />
    <use href="#rayo" transform="rotate(135, 50, 50)" />
    <use href="#rayo" transform="rotate(157.5, 50, 50)" />
    <use href="#rayo" transform="rotate(180, 50, 50)" />
    <use href="#rayo" transform="rotate(202.5, 50, 50)" />
    <use href="#rayo" transform="rotate(225, 50, 50)" />
    <use href="#rayo" transform="rotate(247.5, 50, 50)" />
    <use href="#rayo" transform="rotate(270, 50, 50)" />
    <use href="#rayo" transform="rotate(292.5, 50, 50)" />
    <use href="#rayo" transform="rotate(315, 50, 50)" />
    <use href="#rayo" transform="rotate(337.5, 50, 50)" />
    <g transform="translate(37, 39)">
        <polygon points="0,0 11,6 11,22 0,18" class="book-left" />
        <polygon points="11,6 14,6 14,23 11,22" class="book-spine" />
        <polygon points="14,6 26,0 26,18 14,23" class="book-right" />
    </g>
    <circle cx="50" cy="40" r="3.5" class="dot-yellow" />
</svg>'''


def preprocess_markdown(text):
    """Pre-process markdown before conversion."""
    # Remove the first img line (logo handled by template)
    text = re.sub(r'^<img[^>]*>\n?', '', text)
    # Convert **Término:** text → use for glossary later
    return text


def section_header(text):
    return f'''<div class="section-header">
    <span class="header-text">{text}</span>
    <div class="bar-container">
        <div class="block-red"></div>
        <div class="bar-gap"></div>
        <div class="block-blue"></div>
    </div>
</div>'''


def md_to_html(md_section):
    """Convert markdown to HTML."""
    if not md_section.strip():
        return ""
    return markdown.markdown(md_section, extensions=extensions)


def postprocess_html(html, section_type=None):
    """Apply CSS classes and improve HTML structure."""
    # Blockquotes → styled divs
    html = re.sub(
        r'<blockquote>\s*<p><strong>(Caso de éxito[：:]\s*.*?)</strong>(.*?)</p>\s*</blockquote>',
        r'<div class="caso-exito"><strong>\1</strong>\2</div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p><strong>(Caso de [Ff]allo[：:]\s*.*?)</strong>(.*?)</p>\s*</blockquote>',
        r'<div class="caso-fallo"><strong>\1</strong>\2</div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p><strong>(.*?[Rr]eflexi[óo]n[：:].*?)</strong>(.*?)</p>\s*</blockquote>',
        r'<div class="reflexion"><strong>\1</strong>\2</div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p><strong>(.*?[Cc]onsejo.*?)</strong>(.*?)</p>\s*</blockquote>',
        r'<div class="highlight"><strong>\1</strong>\2</div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p><strong>(.*?[Rr]egla.*?)</strong>(.*?)</p>\s*</blockquote>',
        r'<div class="highlight"><strong>\1</strong>\2</div>',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'<blockquote>\s*<p><strong>(.*?[Ll]ecci[óo]n.*?)</strong>(.*?)</p>\s*</blockquote>',
        r'<div class="highlight"><strong>\1</strong>\2</div>',
        html, flags=re.DOTALL
    )
    # Remaining blockquotes
    html = re.sub(
        r'<blockquote>(.*?)</blockquote>',
        r'<div class="highlight">\1</div>',
        html, flags=re.DOTALL
    )
    # Convert h3 sections → topic-header
    html = re.sub(
        r'<h3>(.*?)</h3>',
        r'<h3 class="topic-header">\1</h3>',
        html
    )
    # Hr → styled
    html = re.sub(r'<hr\s*/?>', r'<hr>', html)
    # Checkbox lists
    html = html.replace('- [ ] ', '☐ ')
    html = html.replace('- [x] ', '☑ ')
    
    if section_type == "glosario":
        html = glossary_to_dl(html)
    
    if section_type == "autoevaluacion":
        html = html.replace('<ol>', '<ol>\n')
    
    return html


def glossary_to_dl(html):
    """Convert glossary paragraph format to dl/dt/dd."""
    # Pattern: <p><strong>Term:</strong> Definition</p>
    def replace_glossary(m):
        term = m.group(1).strip().rstrip(':')
        definition = m.group(2).strip()
        # Remove leading : or space
        definition = re.sub(r'^[:\s]+', '', definition)
        return f'<dt><strong>{term}</strong></dt>\n<dd>{definition}</dd>'
    
    html = re.sub(
        r'<p><strong>([^<]+?)</strong>\s*[：:]\s*(.*?)</p>',
        replace_glossary,
        html
    )
    html = f'<div class="glosario">\n<dl>\n{html}\n</dl>\n</div>'
    return html


def parse_structure(text):
    """Parse markdown into sections."""
    text = preprocess_markdown(text)
    lines = text.split('\n')
    sections = []
    current_level = 0
    current_title = ""
    current_content = []
    
    for line in lines:
        header_match = re.match(r'^(#{1,4})\s+(.+)$', line)
        if header_match:
            if current_content or current_title:
                sections.append({
                    'level': current_level,
                    'title': current_title,
                    'content': current_content
                })
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            current_level = level
            current_title = title
            current_content = []
        else:
            current_content.append(line)
    
    if current_content or current_title:
        sections.append({
            'level': current_level,
            'title': current_title,
            'content': current_content
        })
    return sections


def build_html(sections):
    """Build the complete HTML document."""
    html_parts = []
    
    # ---- HEAD ----
    html_parts.append(f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unidad III - {TITLE}</title>
    <link rel="stylesheet" href="../../estilos/unidades.css">
    <link rel="stylesheet" href="../../estilos/logo.css">
    <link rel="stylesheet" href="../../estilos/portada.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;800&display=swap" rel="stylesheet">
    <style>
        body {{ counter-reset: page 0; }}
    </style>
</head>
<body>''')
    
    # ---- COVER PAGE ----
    html_parts.append(f'''<!-- PORTADA -->
<div class="page-letter">
    <div class="logo-container">
        <div class="logo-icon">
            {LOGO_SVG}
        </div>
        <div class="logo-text">
            <h1 class="acronym">UNHSJM</h1>
            <div class="line-red-only"></div>
            <div class="full-name">
                UNIVERSIDAD NACIONAL<br>
                HÉROES DE SAN JOSÉ DE LAS MULAS
            </div>
        </div>
    </div>
    <div class="center-content">
        <div class="title-group">
            <h1 class="title-main">Unidad Didáctica</h1>
            <div class="decoration-lines">
                <div class="line-blue-cover"></div>
                <div class="line-red-cover"></div>
            </div>
        </div>
        <div class="subtitle-cover">
            {TITLE}<br>
            Unidad III
        </div>
    </div>
</div>''')
    
    # ---- BUILD PAGES FROM SECTIONS ----
    # Filter sections for content
    # h1 = title (skip)
    # h2 = major sections (introduccion, desarrollo, autoeval, bibliografia, glosario)
    # h3 = subsections within desarrollo
    
    all_content_sections = [s for s in sections if s['level'] >= 2 and s['title']]
    
    # Generate TOC
    toc_pages = {}
    page_counter = 2
    for s in all_content_sections:
        if s['level'] == 2:
            t = s['title']
            if 'índice' not in t.lower() and 'contenido' not in t.lower():
                toc_pages[t] = page_counter
                page_counter += 1
    
    def make_slug(title):
        slug = title.lower()
        slug = re.sub(r'[^a-záéíóúñ0-9\s-]', '', slug)
        slug = slug.replace(' ', '-')
        slug = re.sub(r'-+', '-', slug)
        return slug
    
    # TOC page
    toc_items = []
    for s in all_content_sections:
        if s['level'] == 2:
            t = s['title']
            if 'índice' in t.lower() or 'contenido' in t.lower():
                continue
            slug = make_slug(t)
            pg = toc_pages.get(t, '?')
            toc_items.append(f'<li><a href="#{slug}">{t}</a><span class="page-ref">{pg}</span>')
            # Add h3 subsections under this h2
            sub_items = []
            for s2 in all_content_sections:
                if s2['level'] == 3 and _is_subsection_of(s2, s, all_content_sections):
                    sub_slug = make_slug(s2['title'])
                    sub_items.append(f'<li><a href="#{sub_slug}">{s2["title"]}</a><span class="page-ref">{pg}</span></li>')
                    pg += 1
                elif s2['level'] == 3 and sub_items:
                    break
            if sub_items:
                toc_items[-1] += '\n<ul>\n' + '\n'.join(sub_items) + '\n</ul>'
            toc_items[-1] += '</li>'
    
    toc_html = section_header("Índice de Contenido")
    toc_html += f'''<div class="toc"><ul>{"".join(toc_items)}</ul></div>
    <div class="page-number"></div>'''
    html_parts.append(f'<!-- ÍNDICE -->\n<div class="page-content">\n{toc_html}\n</div>')
    
    # Content pages
    page_num = 2
    for i, sec in enumerate(all_content_sections):
        title = sec['title']
        level = sec['level']
        
        if 'índice' in title.lower() and 'contenido' in title.lower():
            continue
        
        md_text = '\n'.join(sec['content'])
        body_html = md_to_html(md_text)
        
        # Determine section type
        sec_type = None
        if title == "Introducción":
            sec_header = "Introducción"
        elif title == "Autoevaluación" or title.startswith("Autoevaluación"):
            sec_header = "Autoevaluación"
            sec_type = "autoevaluacion"
        elif title == "Bibliografía" or title.startswith("Bibliografía"):
            sec_header = "Bibliografía y Webgrafía"
        elif title == "Glosario":
            sec_header = "Glosario"
            sec_type = "glosario"
        else:
            sec_header = "Desarrollo de Contenidos"
        
        body_html = postprocess_html(body_html, section_type=sec_type)
        
        if not body_html.strip():
            continue
        
        page_html = section_header(sec_header)
        
        if level == 3:
            slug = make_slug(title)
            page_html += f'<h3 class="topic-header" id="{slug}">{title}</h3>'
        
        page_html += body_html
        page_html += '\n    <div class="page-number"></div>'
        
        html_parts.append(f'<!-- PÁGINA {page_num}: {title} -->\n<div class="page-content">\n{page_html}\n</div>')
        page_num += 1
    
    html_parts.append('''</body>
</html>''')
    
    return '\n\n'.join(html_parts)


def _is_subsection_of(h3_sec, h2_sec, all_secs):
    """Check if h3 section belongs under h2 section."""
    h2_idx = None
    h3_idx = None
    for idx, s in enumerate(all_secs):
        if s == h2_sec:
            h2_idx = idx
        if s == h3_sec:
            h3_idx = idx
    if h2_idx is not None and h3_idx is not None:
        # h3 should come after h2 but before the next h2
        for s in all_secs[h2_idx+1:h3_idx]:
            if s['level'] == 2:
                return False
        return True
    return False


# ---- Main ----
sections = parse_structure(md_text)
output_html = build_html(sections)
OUTPUT.write_text(output_html, encoding="utf-8")
print(f"Generado: {OUTPUT}")
print(f"Secciones procesadas: {len([s for s in sections if s['level'] >= 2])}")
