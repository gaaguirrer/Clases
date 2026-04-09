"""
Sistema de layout y configuración de la aplicación
Maneja la configuración de página, carga de CSS y temas
"""
import streamlit as st
import textwrap
from pathlib import Path
from utils.constants import APP_CONFIG


def setup_page_config():
    """
    Configura la página de Streamlit con los ajustes apropiados
    """
    st.set_page_config(
        page_title=APP_CONFIG['PAGE_TITLE'],
        page_icon=APP_CONFIG['PAGE_ICON'],
        layout=APP_CONFIG['LAYOUT'],
        initial_sidebar_state="expanded"
    )


def load_css():
    """
    Carga el archivo CSS personalizado de forma segura
    """
    # Buscar el archivo CSS en múltiples ubicaciones posibles
    possible_paths = [
        Path('templates/styles.css'),
        Path('Templates/styles.css'),
        Path('templates/Styles.css'),
        Path('Templates/Styles.css')
    ]
    
    css_loaded = False
    for css_path in possible_paths:
        if css_path.exists():
            try:
                with open(css_path, 'r', encoding='utf-8') as f:
                    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
                css_loaded = True
                break
            except Exception as e:
                print(f"Error al cargar CSS desde {css_path}: {e}")
    
    if not css_loaded:
        st.warning("No se pudo cargar el archivo de estilos CSS")


def render_header():
    """
    Renderiza el encabezado de la aplicación con Pokébola dinámica
    """
    # Determinar si hay un Pokémon seleccionado
    has_pokemon = (
        'selected_pokemon' in st.session_state and 
        st.session_state.selected_pokemon is not None
    )
    
    # Clase CSS de la Pokébola (abierta o cerrada)
    pokeball_class = "pokeball-logo open" if has_pokemon else "pokeball-logo"
    
    html = f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />
    <div style="text-align: center; padding: 0.5rem 0; margin-bottom: 0;">
        <h1 style="color: #4cc9f0; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); display: flex; align-items: center; justify-content: center; gap: 15px; font-size: 3.2rem;">
            <div class="{pokeball_class}"></div> Pokédex App
        </h1>
        <p style="color: #e6e6e6; margin: 0.2rem 0 0 0; font-size: 1.15rem;">
            Tu enciclopedia Pokémon completa
        </p>
    </div>
    """
    st.markdown(html.replace('\n', ''), unsafe_allow_html=True)


def render_footer():
    """
    Renderiza el pie de página
    """
    html = """
    <div style="text-align: center; padding: 2rem 0 1rem 0; margin-top: 3rem; 
                border-top: 1px solid rgba(255,255,255,0.1);">
        <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; margin: 0;">
            Datos proporcionados por <a href="https://pokeapi.co" target="_blank" 
            style="color: #4cc9f0; text-decoration: none;">PokéAPI</a>
        </p>
        <p style="color: rgba(255,255,255,0.4); font-size: 0.75rem; margin: 0.5rem 0 0 0;">
            Versión 0.1.0 | Desarrollado con Streamlit
        </p>
    </div>
    """
    st.markdown(html.replace('\n', ''), unsafe_allow_html=True)


def apply_theme(is_dark_mode: bool = True):
    """
    Aplica el tema oscuro o claro
    
    Args:
        is_dark_mode: True para modo oscuro, False para modo claro
    """
    theme_attr = "" if is_dark_mode else "light"
    
    html = f"""
    <script>
        document.documentElement.setAttribute('data-theme', '{theme_attr}');
    </script>
    """
    st.markdown(html.replace('\n', ''), unsafe_allow_html=True)
