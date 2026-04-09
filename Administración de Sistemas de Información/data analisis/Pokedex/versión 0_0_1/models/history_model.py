"""
Modelo de datos para gestión de historial de búsquedas
Mantiene un registro de las últimas búsquedas del usuario
"""
from typing import List, Dict
from datetime import datetime
from utils.helpers import load_json_file, save_json_file


HISTORY_FILE = "data/history.json"


def add_to_history(search_term: str, pokemon_data: Dict = None) -> bool:
    """
    Añade una búsqueda al historial
    
    Args:
        search_term: Término buscado
        pokemon_data: Datos del Pokémon encontrado (opcional)
        
    Returns:
        True si se añadió exitosamente
    """
    from utils.constants import APP_CONFIG
    
    history = load_history()
    
    # Crear entrada de historial
    entry = {
        'search_term': search_term,
        'timestamp': datetime.now().isoformat(),
        'pokemon_id': pokemon_data.get('id') if pokemon_data else None,
        'pokemon_name': pokemon_data.get('nombre_es') if pokemon_data else None
    }
    
    # Evitar duplicados consecutivos
    if history and history[0].get('search_term') == search_term:
        return True
    
    # Añadir al principio de la lista
    history.insert(0, entry)
    
    # Mantener solo los últimos N registros
    history = history[:APP_CONFIG['MAX_HISTORY']]
    
    data = {'history': history}
    return save_json_file(HISTORY_FILE, data)


def load_history() -> List[Dict]:
    """
    Carga el historial de búsquedas
    
    Returns:
        Lista de búsquedas recientes (más recientes primero)
    """
    data = load_json_file(HISTORY_FILE)
    return data.get('history', [])


def get_history(limit: int = None) -> List[Dict]:
    """
    Obtiene el historial de búsquedas
    
    Args:
        limit: Número máximo de entradas a devolver
        
    Returns:
        Lista de búsquedas recientes
    """
    history = load_history()
    if limit:
        return history[:limit]
    return history


def clear_history() -> bool:
    """
    Limpia todo el historial
    
    Returns:
        True si se limpió exitosamente
    """
    data = {'history': []}
    return save_json_file(HISTORY_FILE, data)


def get_recent_searches(count: int = 5) -> List[Dict]:
    """
    Obtiene las entradas de búsqueda más recientes con información del Pokémon
    
    Args:
        count: Número de búsquedas a devolver
        
    Returns:
        Lista de entradas de historial completas con pokemon_id y pokemon_name
    """
    history = load_history()
    seen = set()
    recent = []
    
    for entry in history:
        term = entry.get('search_term')
        if term and term not in seen:
            seen.add(term)
            recent.append(entry)  # Devolver entrada completa en lugar de solo el término
            if len(recent) >= count:
                break
    
    return recent


def get_most_searched() -> List[Dict]:
    """
    Obtiene las búsquedas más frecuentes
    
    Returns:
        Lista de diccionarios con término y contador, ordenados por frecuencia
    """
    history = load_history()
    frequency = {}
    
    for entry in history:
        term = entry.get('search_term')
        if term:
            frequency[term] = frequency.get(term, 0) + 1
    
    # Ordenar por frecuencia
    sorted_freq = sorted(
        [{'term': term, 'count': count} for term, count in frequency.items()],
        key=lambda x: x['count'],
        reverse=True
    )
    
    return sorted_freq[:10]  # Top 10


def get_popular_pokemon(limit: int = 5) -> List[Dict]:
    """
    Obtiene los Pokémon más populares basados en el historial de búsqueda
    
    Args:
        limit: Número máximo de Pokémon a devolver
        
    Returns:
        Lista de diccionarios con id, name y count
    """
    history = load_history()
    frequency = {}
    pokemon_info = {}
    
    for entry in history:
        pid = entry.get('pokemon_id')
        name = entry.get('pokemon_name')
        
        if pid and name:
            frequency[pid] = frequency.get(pid, 0) + 1
            # Guardar nombre (sobrescribir para tener el último)
            pokemon_info[pid] = name
            
    # Ordenar por frecuencia
    sorted_popular = sorted(
        [{'id': pid, 'name': pokemon_info[pid], 'count': count} for pid, count in frequency.items()],
        key=lambda x: x['count'],
        reverse=True
    )
    
    return sorted_popular[:limit]
