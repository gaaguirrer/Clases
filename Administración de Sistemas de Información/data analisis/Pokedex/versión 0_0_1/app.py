"""
Aplicación Pokédex - Versión 0.1.0
Arquitectura MVC con integración json-server
"""
import streamlit as st
from views.layout import setup_page_config, load_css, render_header, render_footer
from views.pokemon_view import (
    render_pokemon_card,
    render_favorites_sidebar,
    render_history_panel,
    navigate_to_pokemon
)
from controllers.pokemon_controller import (
    manejar_busqueda,
    alternar_favorito,
    pokemon_aleatorio
)
from controllers.chart_controller import crear_grafico_radar
from models.favorites_model import load_favorites, is_favorite
from models.history_model import get_popular_pokemon
from utils.constants import POPULAR_POKEMON


def initialize_session_state():
    """Inicializa el estado de sesión con valores por defecto"""
    defaults = {
        'search_results': [],
        'search_term': '',
        'trigger_search': False,
        'selected_pokemon': None,
        'favorites': load_favorites(),
        'dark_mode': True,
        'current_view': 'search'
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_popular_pokemon_sidebar():
    """Renderiza botones de Pokémon populares en el sidebar"""
    # Intentar obtener populares dinámicos del historial
    popular_list = get_popular_pokemon(5)
    
    # Si no hay suficiente historial, usar estáticos
    if not popular_list:
        popular_list = POPULAR_POKEMON[:5]
        
    with st.sidebar.expander("Popular", expanded=False, icon=":material/star:"):
        for pokemon in popular_list:
            # Manejar diferencias de estructura de datos (dict vs objeto)
            name = pokemon.get('name', pokemon.get('nombre', ''))
            pid = pokemon.get('id')
            
            # Formato consistente: #ID Nombre
            st.button(
                f"#{pid} {name.title()}", 
                width='stretch', 
                key=f"pop_{name}_{pid}", # Key única combinando nombre e ID
                on_click=navigate_to_pokemon,
                args=(name,)
            )


def search_callback():
    """Callback para activar la búsqueda al presionar Enter"""
    st.session_state.trigger_search = True


def render_search_section():
    """Renderiza la sección principal de búsqueda (Layout 2x2)"""
    # Columnas para Inputs (Izq) y Botones (Der)
    # Ajustamos ratio a [2.5, 0.8] ya que los botones sin texto son más pequeños
    col_inputs, col_btns = st.columns([2.5, 0.8], gap="small")
    
    with col_inputs:
        # Fila 1: Input de Búsqueda
        search_term = st.text_input(
            "Buscar",
            value=st.session_state.search_term,
            placeholder="Nombre o ID...",
            key="search_input",
            label_visibility="collapsed",
            on_change=search_callback
        )
        
        # Fila 2: Selector de Tipo (debajo del input)
        from models.pokemon_model import get_all_pokemon_types
        tipos = get_all_pokemon_types()
        type_filter = st.selectbox(
            "Tipo",
            ["Todos"] + [t.title() for t in tipos],
            key="type_selector",
            label_visibility="collapsed"
        )
    
    with col_btns:
        # Fila 1: Botón Buscar (Ancho completo)
        search_button = st.button("", icon=":material/search:", type="primary", key="search_btn", width='stretch', help="Buscar Pokémon")
        
        # Fila 2: Botones Aleatorio y Limpiar
        b_col1, b_col2 = st.columns(2, gap="small")
        with b_col1:
            random_button = st.button("", icon=":material/shuffle:", width='stretch', key="random_btn", help="Pokémon Aleatorio")
        with b_col2:
            clear_button = st.button("", icon=":material/cleaning_services:", width='stretch', key="clear_btn", help="Limpiar Búsqueda")

    # Manejar acciones
    if search_button or st.session_state.trigger_search:
        st.session_state.trigger_search = False
        tipo_val = None if type_filter == "Todos" else type_filter.lower()
        pokemon = manejar_busqueda(search_term, filtro_tipo=tipo_val)
        if pokemon:
            st.session_state.search_results = [pokemon]
            st.session_state.selected_pokemon = pokemon
            st.rerun()
    
    if random_button:
        tipo_val = None if type_filter == "Todos" else type_filter.lower()
        pokemon = pokemon_aleatorio(filtro_tipo=tipo_val)
        if pokemon:
            st.session_state.search_results = [pokemon]
            st.session_state.selected_pokemon = pokemon
            st.rerun()
    
    if clear_button:
        st.session_state.search_results = []
        st.session_state.search_term = ""
        st.session_state.selected_pokemon = None
        st.rerun()


def render_results_section():
    """Renderiza la sección de resultados"""
    if st.session_state.search_results:
        for pokemon in st.session_state.search_results:
            # Renderizar tarjeta
            render_pokemon_card(pokemon)
            st.markdown("---")
    # Eliminado: render_popular_pokemon() - Ahora está en el sidebar


def main():
    """Función principal de la aplicación"""
    # Configuración de página
    setup_page_config()
    load_css()
    
    # Inicializar estado
    initialize_session_state()
    
    # Sidebar
    with st.sidebar:
        # Favoritos
        render_favorites_sidebar()
        st.markdown("---")
        # Pokémon Populares
        render_popular_pokemon_sidebar()
        st.markdown("---")
        # Historial
        render_history_panel()
    
    # Layout Superior: Header (Izq) + Buscador (Der)
    with st.container():
        # Layout de 5 columnas ajustado para evitar saltos de línea y alinear verticalmente:
        # Col 1 (0.5): Margen Izquierdo (X)
        # Col 2 (4.0): Título (Más ancho para que quepa en una línea)
        # Col 3 (1.0): Espacio Central (2X) - Doble del margen (0.5 * 2 = 1.0)
        # Col 4 (4.0): Buscador
        # Col 5 (0.5): Margen Derecho (X)
        # vertical_alignment="center" alinea el título y el buscador al centro verticalmente
        c1, c2, c3, c4, c5 = st.columns([0.5, 4, 1, 4, 0.5], vertical_alignment="center")
        
        with c2:
            render_header()
            
        with c4:
            render_search_section()
    
    st.markdown("---")
    
    # Sección de Resultados (Ancho completo)
    render_results_section()
    
    # Footer
    render_footer()


if __name__ == "__main__":
    main()