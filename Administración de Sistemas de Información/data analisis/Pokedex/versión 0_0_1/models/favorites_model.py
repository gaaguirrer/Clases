"""
Modelo de datos para gestión de favoritos
Maneja la persistencia de Pokémon favoritos del usuario
"""
import streamlit as st
from pathlib import Path
from typing import List, Dict, Optional
from utils.helpers import load_json_file, save_json_file


FAVORITES_FILE = "data/favorites.json"


def load_favorites() -> List[Dict]:
    """
    Carga la lista de favoritos desde el archivo JSON
    
    Returns:
        Lista de Pokémon favoritos
    """
    data = load_json_file(FAVORITES_FILE)
    return data.get('favorites', [])


def save_favorites(favorites: List[Dict]) -> bool:
    """
    Guarda la lista de favoritos en el archivo JSON
    
    Args:
        favorites: Lista de Pokémon favoritos
        
    Returns:
        True si se guardó exitosamente, False en caso contrario
    """
    data = {'favorites': favorites}
    return save_json_file(FAVORITES_FILE, data)


def add_favorite(pokemon: Dict) -> bool:
    """
    Añade un Pokémon a favoritos
    
    Args:
        pokemon: Diccionario con datos del Pokémon
        
    Returns:
        True si se añadió exitosamente, False si ya existía o hubo error
    """
    from utils.constants import APP_CONFIG
    
    favorites = load_favorites()
    
    # Verificar si ya existe
    if any(fav['id'] == pokemon['id'] for fav in favorites):
        return False
    
    # Verificar límite máximo
    if len(favorites) >= APP_CONFIG['MAX_FAVORITES']:
        st.warning(f"Límite de {APP_CONFIG['MAX_FAVORITES']} favoritos alcanzado")
        return False
    
    favorites.append(pokemon)
    return save_favorites(favorites)


def remove_favorite(pokemon_id: int) -> bool:
    """
    Elimina un Pokémon de favoritos por su ID
    
    Args:
        pokemon_id: ID del Pokémon a eliminar
        
    Returns:
        True si se eliminó exitosamente, False si no se encontró o hubo error
    """
    favorites = load_favorites()
    initial_len = len(favorites)
    
    favorites = [fav for fav in favorites if fav['id'] != pokemon_id]
    
    if len(favorites) == initial_len:
        return False  # No se encontró el Pokémon
    
    return save_favorites(favorites)


def is_favorite(pokemon_id: int) -> bool:
    """
    Verifica si un Pokémon está en favoritos
    
    Args:
        pokemon_id: ID del Pokémon a verificar
        
    Returns:
        True si está en favoritos, False en caso contrario
    """
    favorites = load_favorites()
    return any(fav['id'] == pokemon_id for fav in favorites)


def get_all_favorites() -> List[Dict]:
    """
    Obtiene todos los Pokémon favoritos
    
    Returns:
        Lista completa de favoritos
    """
    return load_favorites()


def clear_favorites() -> bool:
    """
    Elimina todos los favoritos
    
    Returns:
        True si se eliminaron exitosamente
    """
    return save_favorites([])


def get_favorites_count() -> int:
    """
    Obtiene el número de favoritos
    
    Returns:
        Cantidad de Pokémon en favoritos
    """
    return len(load_favorites())
