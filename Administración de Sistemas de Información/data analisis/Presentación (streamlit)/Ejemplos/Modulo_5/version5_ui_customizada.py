# ========================================
# EJEMPLO MÓDULO 5: ESTILOS CSS y GOOGLE ICONS
# ========================================

import streamlit as st
import os

st.set_page_config(page_title='Componentes con Estilo', layout='centered')

st.title("Diseño Interfaz Avanzada (UI)")
st.write("Combinación de Fuentes externas, Iconos Vectoriales y Componentes CSS puros.")

# 1. Inyectamos Material Symbols de Google
inject_icons = """
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
"""
st.markdown(inject_icons, unsafe_allow_html=True)

st.divider()

# 2. Leemos la Hoja de Estilos (CSS) Externa
# Nos aseguramos de leer el archivo relativo al directorio donde estamos
css_path = os.path.join(os.path.dirname(__file__), 'estilos.css')
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
else:
    st.error(f"No se localiza doc CSS: {css_path}")

# 3. Componentes HTML Simulados (Cards y Google Icons)

st.markdown("""
<div class="my-card">
    <h3 class="my-card-title">
        <span class="material-symbols-outlined" style="vertical-align: sub; color: #FF4B4B;">account_balance</span>
        Resumen Financiero Independiente
    </h3>
    <p class="my-card-text">
        El balance del último trimestre muestra un incremento estable en 
        las operaciones generales, reduciendo costos pasivos en un 14%. 
        <em>(Pase el ratón por encima de esta tarjeta para ver el efecto hover).</em>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="my-card" style="border-left-color: #43A047;">
    <h3 class="my-card-title">
        <span class="material-symbols-outlined" style="vertical-align: sub; color: #43A047;">verified_user</span>
        Seguridad Verificada
    </h3>
    <p class="my-card-text">
        Sus credenciales cumplen con todos los estándares criptográficos solicitados.
    </p>
</div>
""", unsafe_allow_html=True)

st.info("Nota: Revisa el archivo `estilos.css` adyacente para ver cómo se configuran las clases `.my-card` de manera limpia y modular.")
