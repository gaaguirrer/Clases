"""
Controlador principal para lógica de negocio de Pokémon
Orquesta las interacciones entre modelos y vistas
"""
import streamlit as st
from typing import List, Dict, Optional
from models.pokemon_model import get_pokemon, search_pokemon, get_random_pokemon
from models.favorites_model import add_favorite, remove_favorite, is_favorite
from models.history_model import add_to_history
from utils.helpers import normalize_search_term, is_valid_pokemon_id


def manejar_busqueda(termino_busqueda: str, filtro_tipo: str = None, generacion: int = None) -> Optional[Dict]:
    """
    Maneja una búsqueda de Pokémon
    
    Args:
        termino_busqueda: Término de búsqueda
        filtro_tipo: Filtro de tipo (opcional)
        generacion: Filtro de generación (opcional)
        
    Returns:
        Datos del Pokémon encontrado o None
    """
    if not termino_busqueda or not termino_busqueda.strip():
        st.warning("Por favor ingresa un nombre o número")
        return None
    
    termino_busqueda = normalize_search_term(termino_busqueda)
    
    # Validar si es un ID
    if termino_busqueda.isdigit():
        if not is_valid_pokemon_id(termino_busqueda):
            st.error(f"ID {termino_busqueda} no es válido. Debe estar entre 1 y 1025.")
            return None
    
    # Buscar Pokémon
    with st.spinner('Buscando...'):
        pokemon = get_pokemon(termino_busqueda)
    
    if not pokemon:
        st.error(
            f"❌ **Pokémon no encontrado**\n\n"
            f"No pudimos encontrar a '{termino_busqueda}'. Por favor verifica que el nombre o número sea correcto."
        )
        add_to_history(termino_busqueda, None)
        return None
    
    # Aplicar filtros
    if filtro_tipo and filtro_tipo != "Todos":
        if filtro_tipo.lower() not in [t.lower() for t in pokemon.get('tipos', [])]:
            st.warning(f"{pokemon['nombre_es']} no es de tipo {filtro_tipo}")
            return None
    
    if generacion:
        from utils.helpers import get_generation_from_id
        pokemon_gen = get_generation_from_id(pokemon['id'])
        if pokemon_gen != generacion:
            st.warning(f"{pokemon['nombre_es']} no pertenece a la Generación {generacion}")
            return None
    
    # Agregar al historial
    add_to_history(termino_busqueda, pokemon)
    
    return pokemon


def alternar_favorito(pokemon: Dict) -> None:
    """
    Maneja la acción de agregar/quitar de favoritos
    
    Args:
        pokemon: Datos del Pokémon
    """
    pokemon_id = pokemon['id']
    
    if is_favorite(pokemon_id):
        if remove_favorite(pokemon_id):
            st.success(f"✓ {pokemon['nombre_es']} eliminado de favoritos")
            # Actualizar estado de sesión
            if 'favorites' in st.session_state:
                st.session_state.favorites = [
                    fav for fav in st.session_state.favorites 
                    if fav['id'] != pokemon_id
                ]
    else:
        if add_favorite(pokemon):
            st.success(f"⭐ {pokemon['nombre_es']} añadido a favoritos")
            # Actualizar estado de sesión
            if 'favorites' not in st.session_state:
                st.session_state.favorites = []
            st.session_state.favorites.append(pokemon)


def pokemon_aleatorio(filtro_tipo: str = None) -> Optional[Dict]:
    """
    Obtiene un Pokémon aleatorio, opcionalmente filtrado por tipo
    
    Args:
        filtro_tipo: Tipo de Pokémon (opcional)
        
    Returns:
        Datos del Pokémon aleatorio
    """
    msg = f'Buscando Pokémon aleatorio de tipo {filtro_tipo}...' if filtro_tipo and filtro_tipo != "Todos" else 'Buscando Pokémon aleatorio...'
    
    with st.spinner(msg):
        pokemon = get_random_pokemon(filtro_tipo)
    
    if pokemon:
        add_to_history(f"Aleatorio: {pokemon['nombre_es']}", pokemon)
        st.success(f"¡Encontrado: {pokemon['nombre_es']}!")
    else:
        st.error("Error al obtener Pokémon aleatorio")
    
    return pokemon


def busqueda_avanzada(
    consulta: str = "",
    filtro_tipo: str = None,
    generacion: int = None,
    min_estadisticas: int = None,
    max_estadisticas: int = None,
    ordenar_por: str = "id"
) -> List[Dict]:
    """
    Maneja una búsqueda avanzada con múltiples filtros
    
    Args:
        query: Término de búsqueda
        type_filter: Filtro de tipo
        generation: Filtro de generación
        min_stats: Estadísticas mínimas
        max_stats: Estadísticas máximas
        sort_by: Campo por el cual ordenar
        
    Returns:
        Lista de Pokémon que cumplen los criterios
    """
    with st.spinner('Buscando...'):
        results = search_pokemon(
            query=consulta,
            type_filter=filtro_tipo,
            generation=generacion,
            min_stats=min_estadisticas,
            max_stats=max_estadisticas
        )
    
    if not results:
        st.info("No se encontraron resultados con los filtros aplicados")
        return []
    
    # Ordenar resultados
    if sort_by == "nombre":
        results.sort(key=lambda x: x.get('nombre_es', x.get('nombre', '')))
    elif sort_by == "stats":
        from utils.helpers import calculate_stat_total
        results.sort(key=lambda x: calculate_stat_total(x.get('stats', {})), reverse=True)
    else:  # Por ID (default)
        results.sort(key=lambda x: x.get('id', 0))
    
    return results


def obtener_datos_comparacion(ids_pokemon: List[int]) -> List[Dict]:
    """
    Obtiene datos para comparar múltiples Pokémon
    
    Args:
        pokemon_ids: Lista de IDs de Pokémon a comparar
        
    Returns:
        Lista de datos de Pokémon para comparación
    """
    pokemon_list = []
    
    for pokemon_id in pokemon_ids:
        pokemon = get_pokemon(str(pokemon_id))
        if pokemon:
            pokemon_list.append(pokemon)
    
    return pokemon_list


def validar_entrada_busqueda(termino_busqueda: str) -> bool:
    """
    Valida el input de búsqueda
    
    Args:
        termino_busqueda: Término a validar
        
    Returns:
        True si es válido, False en caso contrario
    """
    if not search_term or not search_term.strip():
        return False
    
    # Permitir letras, números, guiones y espacios
    import re
    if not re.match(r'^[a-zA-Z0-9\s\-]+$', search_term):
        st.error("El término de búsqueda contiene caracteres no válidos")
        return False
    
    return True
