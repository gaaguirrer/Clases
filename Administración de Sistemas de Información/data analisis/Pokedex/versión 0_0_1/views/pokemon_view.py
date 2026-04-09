"""
Componentes visuales para Pokémon
Incluye tarjetas, barras de estadísticas, badges, etc.
"""
import streamlit as st
import textwrap
from typing import Dict, List
from utils.constants import TYPE_COLORS, TYPE_ICONS, TYPE_NAMES_ES
from utils.helpers import format_pokemon_id, calculate_stat_total, get_stat_category
from models.favorites_model import is_favorite, load_favorites, get_all_favorites
from controllers.pokemon_controller import alternar_favorito


def render_stat_bar(value: int, max_value: int = 255) -> str:
    """
    Renderiza una barra de estadística con animación
    """
    percentage = min(100, int((value / max_value) * 100))
    return f'<div class="stat-bar-container"><div class="stat-bar" style="width: {percentage}%; animation: fillBar 0.5s ease-out;"></div></div>'


def render_type_badge(tipo: str) -> str:
    """
    Renderiza un badge de tipo de Pokémon
    """
    color = TYPE_COLORS.get(tipo.lower(), '#777')
    icon = TYPE_ICONS.get(tipo.lower(), '<span class="material-symbols-rounded" style="font-size: 1rem; vertical-align: middle;">star</span>')
    nombre_es = TYPE_NAMES_ES.get(tipo.lower(), tipo.title())
    
    return f'<span class="type-badge" style="background-color: {color};">{icon} {nombre_es}</span>'


def render_skeleton_loader() -> None:
    """
    Renderiza un skeleton loader mientras se cargan los datos
    """
    html = """
    <div class="pokemon-card-compact skeleton-loader">
        <div class="skeleton-header"></div>
        <div class="skeleton-content">
            <div class="skeleton-image"></div>
            <div class="skeleton-stats">
                <div class="skeleton-stat"></div>
                <div class="skeleton-stat"></div>
                <div class="skeleton-stat"></div>
            </div>
        </div>
    </div>
    """
    st.markdown(html.replace('\n', ''), unsafe_allow_html=True)


from typing import Dict, List, Union

def navigate_to_pokemon(identifier: Union[int, str]):
    """Callback para navegar a un Pokémon específico"""
    st.session_state.search_term = str(identifier)
    st.session_state.search_input = str(identifier)
    st.session_state.trigger_search = True

def render_pokemon_card(pokemon: Dict, show_details: bool = True) -> None:
    """
    Renderiza una tarjeta de Pokémon con diseño dividido y pestañas (Imagen Izq | Tabs Der)
    """
    # Contenedor principal
    with st.container():
        # Layout: ajuste fino para centrar el nombre entre las tarjetas
        # Usamos columnas simétricas para asegurar que el nombre esté perfectamente centrado
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col1:
            # ID alineado verticalmente al centro
            st.markdown(f'<div style="display: flex; align-items: center; justify-content: flex-end; height: 60px;"><span class="pokemon-id">{format_pokemon_id(pokemon.get("id", 0))}</span></div>', unsafe_allow_html=True)
        
        with col2:
            # Nombre centrado vertical y horizontalmente
            st.markdown(f'<div style="display: flex; align-items: center; justify-content: center; height: 60px;"><h3 class="pokemon-name" style="font-size: 2.5rem; margin: 0;">{pokemon.get("nombre_es", pokemon.get("nombre", "Desconocido")).title()}</h3></div>', unsafe_allow_html=True)
        
        with col3:
            # Botón centrado verticalmente usando CSS en la columna
            st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
            is_fav = is_favorite(pokemon['id'])
            # Usar iconos Material para el botón de favoritos
            fav_icon = ":material/favorite:" if is_fav else ":material/favorite_border:"
            if st.button("", icon=fav_icon, key=f"header_fav_{pokemon['id']}", help="Añadir/Quitar de Favoritos"):
                alternar_favorito(pokemon)
                st.session_state.favorites = load_favorites()
                st.rerun()

        # Separador visual sutil
        st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)
        
        # Cuerpo de la tarjeta (Split Layout)
        col_left, col_right = st.columns([1, 1], gap="large")
        
        # COLUMNA IZQUIERDA: Tarjeta Visual
        with col_left:
            type_badges = "".join([render_type_badge(t) for t in pokemon.get('tipos', [])])
            altura = pokemon.get('altura', 0)
            peso = pokemon.get('peso', 0)
            
            # Evoluciones (Integradas en la tarjeta izquierda)
            evoluciones = pokemon.get('evoluciones', [])
            evo_html = ""
            if evoluciones:
                evo_text = " ➝ ".join([e.title() for e in evoluciones[:3]])
                evo_html = f"""
                <div class="evolution-chain-internal">
                    <div style="font-size: 0.8rem; text-transform: uppercase; opacity: 0.6; margin-bottom: 0.5rem; letter-spacing: 1px;">Evoluciones</div>
                    {evo_text}
                </div>
                """
            
            # Calcular IDs anterior y siguiente
            try:
                current_id = int(pokemon.get('id', 1))
            except (ValueError, TypeError):
                current_id = 1
                
            prev_id = 1025 if current_id == 1 else current_id - 1
            next_id = 1 if current_id == 1025 else current_id + 1
            
            # Estilo CSS específico para esta columna (simular tarjeta)
            st.markdown("""
            <style>
            /* Selector específico para la columna izquierda de la tarjeta */
            div[data-testid="stHorizontalBlock"]:has(div.pokemon-image-container-compact) > div[data-testid="column"]:nth-child(1) > div[data-testid="stVerticalBlock"] {
                background: var(--card-bg);
                backdrop-filter: blur(12px);
                border: var(--glass-border);
                border-radius: 24px;
                padding: 2rem;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                height: 100%;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Layout de Navegación: [ < ] [ Imagen ] [ > ]
            nav_c1, nav_c2, nav_c3 = st.columns([1, 4, 1], vertical_alignment="center")
            
            with nav_c1:
                st.button("", icon=":material/arrow_back_ios:", key=f"prev_{current_id}", help="Anterior Pokémon", on_click=navigate_to_pokemon, args=(prev_id,))
            
            with nav_c2:
                st.markdown(f"""
                <div class="pokemon-image-container-compact" style="margin: 0 auto; width: 100%; height: 250px;">
                    <img class="pokemon-image" src="{pokemon.get("imagen", "")}" alt="{pokemon.get("nombre", "")}" loading="lazy" style="max-height: 100%;">
                </div>
                """, unsafe_allow_html=True)
            
            with nav_c3:
                st.button("", icon=":material/arrow_forward_ios:", key=f"next_{current_id}", help="Siguiente Pokémon", on_click=navigate_to_pokemon, args=(next_id,))
            
            # Resto del contenido (Badges, Stats) - Evoluciones removidas de aquí
            content_html = f"""
            <div style="display: flex; flex-direction: column; justify-content: center;">
                <div class="type-badges" style="margin-top: 1rem;">{type_badges}</div>
                <div style="text-align: center; font-size: 1rem; opacity: 0.8; margin-top: 1.5rem; display: flex; justify-content: center; gap: 2rem;">
                    <span style="display: inline-flex; align-items: center; gap: 4px;"><span class="material-symbols-rounded" style="font-size: 1.2rem;">straighten</span> {altura}m</span>
                    <span style="display: inline-flex; align-items: center; gap: 4px;"><span class="material-symbols-rounded" style="font-size: 1.2rem;">weight</span> {peso}kg</span>
                </div>
            </div>
            """
            st.markdown(content_html.replace('\n', ''), unsafe_allow_html=True)
            
            # Evoluciones Interactivas (Botones)
            if evoluciones:
                st.markdown('<div style="font-size: 0.8rem; text-transform: uppercase; opacity: 0.6; margin: 1.5rem 0 0.5rem 0; text-align: center; letter-spacing: 1px;">Evoluciones</div>', unsafe_allow_html=True)
                
                # Calcular columnas: Botón - Flecha - Botón ...
                num_evos = len(evoluciones)
                if num_evos > 1:
                    # Crear lista de ratios: [3, 1, 3, 1, 3] etc.
                    cols_config = []
                    for i in range(num_evos):
                        cols_config.append(3) # Botón
                        if i < num_evos - 1:
                            cols_config.append(1) # Flecha
                    
                    cols = st.columns(cols_config, vertical_alignment="center")
                    
                    col_idx = 0
                    for i, evo_name in enumerate(evoluciones):
                        # Columna del Botón
                        with cols[col_idx]:
                            # Verificar si es el Pokémon actual
                            is_current = evo_name.lower() == pokemon.get('nombre', '').lower()
                            
                            st.button(
                                evo_name.title(), 
                                key=f"evo_btn_{evo_name}_{pokemon['id']}", 
                                on_click=navigate_to_pokemon, 
                                args=(evo_name,),
                                use_container_width=True,
                                disabled=is_current,
                                type="secondary" if is_current else "primary"
                            )
                        col_idx += 1
                        
                        # Columna de la Flecha (si no es el último)
                        if i < num_evos - 1:
                            with cols[col_idx]:
                                st.markdown('<div style="text-align: center; color: var(--text-color); opacity: 0.5;"><span class="material-symbols-rounded">arrow_forward</span></div>', unsafe_allow_html=True)
                            col_idx += 1
                else:
                    # Solo una evolución (raro pero posible)
                    cols = st.columns([1, 2, 1])
                    with cols[1]:
                         is_current = evoluciones[0].lower() == pokemon.get('nombre', '').lower()
                         st.button(
                            evoluciones[0].title(), 
                            key=f"evo_btn_{evoluciones[0]}_{pokemon['id']}", 
                            on_click=navigate_to_pokemon, 
                            args=(evoluciones[0],),
                            use_container_width=True,
                            disabled=is_current,
                            type="secondary" if is_current else "primary"
                        )
            else:
                st.markdown('<div style="font-size: 0.8rem; text-transform: uppercase; opacity: 0.6; margin: 1.5rem 0 0.5rem 0; text-align: center; letter-spacing: 1px;">Evoluciones</div>', unsafe_allow_html=True)
                st.markdown('<div style="text-align: center; font-size: 0.9rem; opacity: 0.7; font-style: italic;">Sin evoluciones conocidas hasta ahora</div>', unsafe_allow_html=True)
            
        # COLUMNA DERECHA: Tabs (Estilo aplicado por CSS)
        with col_right:
            # Tabs sin emojis, solo texto
            tab_stats, tab_chart = st.tabs(["Estadísticas", "Gráfico"])
            
            with tab_stats:
                # Preparar estadísticas
                stats_order = ['hp', 'ataque', 'defensa', 'ataque_especial', 'defensa_especial', 'velocidad']
                stats = pokemon.get('stats', {})
                stats_html = ""
                for stat_key in stats_order:
                    value = stats.get(stat_key, 0)
                    label = stat_key.replace('_', ' ').replace('especial', 'esp.').title()
                    stats_html += f'<div class="stat-item-compact"><div class="stat-label">{label}</div><div class="stat-value">{value}</div>{render_stat_bar(value)}</div>'
                
                total = calculate_stat_total(stats)
                category = get_stat_category(total)
                
                stats_content = f"""
                <div class="stats-container-compact">
                    {stats_html}
                    <div class="total-score">
                        <strong style="color: var(--accent-color); font-size: 1.1rem;">Total: {total}</strong>
                        <div style="font-size: 0.8rem; opacity: 0.7; margin-top: 0.1rem;">{category}</div>
                    </div>
                </div>
                """
                st.markdown(stats_content.replace('\n', ''), unsafe_allow_html=True)
                
            with tab_chart:
                from controllers.chart_controller import crear_grafico_radar
                fig = crear_grafico_radar(pokemon)
                st.plotly_chart(fig, width='stretch', config={'displayModeBar': False})


def render_pokemon_grid(pokemon_list: List[Dict], columns: int = 3) -> None:
    """
    Renderiza múltiples Pokémon en una cuadrícula
    
    Args:
        pokemon_list: Lista de Pokémon
        columns: Número de columnas
    """
    if not pokemon_list:
        st.info("No hay Pokémon para mostrar")
        return
    
    cols = st.columns(columns)
    
    for idx, pokemon in enumerate(pokemon_list):
        with cols[idx % columns]:
            render_pokemon_card(pokemon, show_details=False)


def render_comparison_view(pokemon_list: List[Dict]) -> None:
    """
    Renderiza vista de comparación lado a lado
    
    Args:
        pokemon_list: Lista de 2-3 Pokémon para comparar
    """
    if len(pokemon_list) < 2:
        st.warning("Selecciona al menos 2 Pokémon para comparar")
        return
    
    st.markdown("### Comparación de Pokémon")
    
    # Mostrar tarjetas lado a lado
    cols = st.columns(len(pokemon_list))
    
    for idx, pokemon in enumerate(pokemon_list):
        with cols[idx]:
            render_pokemon_card(pokemon)
    
    # Mostrar gráfico comparativo
    st.markdown("---")
    from controllers.chart_controller import create_comparison_chart
    
    fig = create_comparison_chart(pokemon_list)
    st.plotly_chart(fig, width='stretch')


def render_search_filters() -> Dict:
    """
    Renderiza panel de filtros avanzados de búsqueda
    
    Returns:
        Diccionario con los filtros seleccionados
    """
    with st.expander("🔧 Filtros Avanzados", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            from models.pokemon_model import get_all_pokemon_types
            tipos = get_all_pokemon_types()
            
            type_filter = st.selectbox(
                "Tipo",
                ["Todos"] + [t.title() for t in tipos],
                key="filter_type"
            )
            
            from utils.constants import GENERATIONS
            gen_options = ["Todas"] + [f"Gen {g}" for g in GENERATIONS.keys()]
            generation = st.selectbox(
                "Generación",
                gen_options,
                key="filter_gen"
            )
        
        with col2:
            min_stats = st.number_input(
                "Stats mínimas",
                min_value=0,
                max_value=800,
                value=0,
                step=50,
                key="filter_min_stats"
            )
            
            max_stats = st.number_input(
                "Stats máximas",
                min_value=0,
                max_value=800,
                value=800,
                step=50,
                key="filter_max_stats"
            )
        
        sort_by = st.radio(
            "Ordenar por",
            ["ID", "Nombre", "Estadísticas"],
            horizontal=True,
            key="filter_sort"
        )
    
    # Convertir valores
    gen_value = None
    if generation != "Todas":
        gen_value = int(generation.split()[1])
    
    type_value = None if type_filter == "Todos" else type_filter.lower()
    
    sort_map = {"ID": "id", "Nombre": "nombre", "Estadísticas": "stats"}
    
    return {
        'type': type_value,
        'generation': gen_value,
        'min_stats': min_stats if min_stats > 0 else None,
        'max_stats': max_stats if max_stats < 800 else None,
        'sort_by': sort_map[sort_by]
    }


def render_favorites_sidebar() -> None:
    """
    Renderiza el panel de favoritos en el sidebar
    """
    favorites = get_all_favorites()
    
    # Expander colapsable sin contador, con icono Material Design
    with st.sidebar.expander("Favoritos", expanded=False, icon=":material/favorite:"):
        if favorites:
            for fav in favorites:
                # Formato consistente: #ID Nombre
                # Formato consistente: #ID Nombre
                st.button(
                    f"#{fav.get('id', '')} {fav.get('nombre_es', fav.get('nombre', ''))}",
                    key=f"sidebar_fav_{fav['id']}",
                    width='stretch',
                    on_click=navigate_to_pokemon,
                    args=(fav.get('nombre', ''),)
                )
        else:
            st.sidebar.info("No tienes favoritos aún")


def render_history_panel() -> None:
    """
    Renderiza el panel de historial de búsquedas
    """
    from models.history_model import get_recent_searches, clear_history
    
    # Expander sin ícono de papelera en el título, con icono Material Design
    with st.sidebar.expander("Historial", expanded=False, icon=":material/history:"):
        recent = get_recent_searches(10)
        
        if recent:
            # Botón para borrar historial con ícono Material Design
            if st.button("Borrar todo", key="clear_history_btn", width='stretch', help="Borrar Historial", type="secondary", icon=":material/delete:"):
                clear_history()
                st.rerun()
            
            st.markdown("---")
            
            for entry in recent:
                # Mostrar formato consistente con favoritos: Nombre #ID
                pokemon_name = entry.get('pokemon_name')
                pokemon_id = entry.get('pokemon_id')
                search_term = entry.get('search_term')
                
                # Si tenemos datos del Pokémon, mostrar formato "#ID Nombre"
                if pokemon_name and pokemon_id:
                    button_label = f"#{pokemon_id} {pokemon_name}"
                else:
                    # Si no hay datos del Pokémon, mostrar el término de búsqueda
                    button_label = search_term
                
                st.button(
                    button_label, 
                    key=f"history_{search_term}_{pokemon_id}", 
                    width='stretch',
                    on_click=navigate_to_pokemon,
                    args=(search_term,)
                )
        else:
            st.info("No hay búsquedas recientes")
