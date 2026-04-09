"""
Funciones auxiliares y utilidades generales
"""
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from functools import wraps


def format_pokemon_id(pokemon_id: int) -> str:
    """
    Formatea el ID del Pokémon con ceros a la izquierda
    
    Args:
        pokemon_id: ID numérico del Pokémon
        
    Returns:
        String formateado como #001, #025, etc.
    """
    try:
        # Si es string numérico o int/float
        return f"#{int(float(pokemon_id)):03d}"
    except (ValueError, TypeError):
        # Si es texto no numérico (ej: nombre)
        return str(pokemon_id)


def calculate_stat_total(stats: Dict[str, int]) -> int:
    """
    Calcula el total de estadísticas base
    
    Args:
        stats: Diccionario con estadísticas base
        
    Returns:
        Suma total de todas las estadísticas
    """
    return sum(stats.values())


def get_stat_category(total: int) -> str:
    """
    Categoriza el total de estadísticas
    
    Args:
        total: Total de estadísticas
        
    Returns:
        Categoría: 'Legendary', 'Very Strong', 'Strong', 'Average', o 'Weak'
    """
    if total >= 600:
        return 'Legendario'
    elif total >= 520:
        return 'Muy Fuerte'
    elif total >= 450:
        return 'Fuerte'
    elif total >= 350:
        return 'Promedio'
    else:
        return 'Débil'


def load_json_file(filepath: str) -> Dict[str, Any]:
    """
    Carga un archivo JSON de forma segura
    
    Args:
        filepath: Ruta al archivo JSON
        
    Returns:
        Diccionario con los datos del archivo, o dict vacío si falla
    """
    try:
        path = Path(filepath)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error al cargar {filepath}: {e}")
    return {}


def save_json_file(filepath: str, data: Dict[str, Any]) -> bool:
    """
    Guarda datos en un archivo JSON de forma segura
    
    Args:
        filepath: Ruta donde guardar el archivo
        data: Datos a guardar
        
    Returns:
        True si se guardó exitosamente, False en caso contrario
    """
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error al guardar {filepath}: {e}")
        return False


def retry_on_failure(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorador para reintentar una función en caso de fallo
    
    Args:
        max_attempts: Número máximo de intentos
        delay: Segundos de espera entre intentos
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Intento {attempt + 1} falló: {e}. Reintentando...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator


def normalize_search_term(term: str) -> str:
    """
    Normaliza un término de búsqueda
    
    Args:
        term: Término a normalizar
        
    Returns:
        Término en minúsculas sin espacios extra
    """
    return term.lower().strip()


def is_valid_pokemon_id(pokemon_id: Any) -> bool:
    """
    Valida si un ID de Pokémon es válido
    
    Args:
        pokemon_id: ID a validar
        
    Returns:
        True si es un número entre 1 y 1025, False en caso contrario
    """
    try:
        id_num = int(pokemon_id)
        return 1 <= id_num <= 1025
    except (ValueError, TypeError):
        return False


def get_generation_from_id(pokemon_id: int) -> Optional[int]:
    """
    Obtiene el número de generación a partir del ID del Pokémon
    
    Args:
        pokemon_id: ID del Pokémon
        
    Returns:
        Número de generación (1-9) o None si no es válido
    """
    from utils.constants import GENERATIONS
    
    for gen, (start, end) in GENERATIONS.items():
        if start <= pokemon_id <= end:
            return gen
    return None


def format_evolution_chain(evolutions: List[str]) -> str:
    """
    Formatea la cadena evolutiva para mostrar
    
    Args:
        evolutions: Lista de nombres de evoluciones
        
    Returns:
        String formateado con flechas: "Bulbasaur → Ivysaur → Venusaur"
    """
    if not evolutions:
        return "No evoluciona"
    return " → ".join([evo.title() for evo in evolutions])


def get_type_effectiveness(attacker_type: str, defender_types: List[str]) -> Dict[str, float]:
    """
    Calcula la efectividad de tipos (simplificado)
    
    Args:
        attacker_type: Tipo del atacante
        defender_types: Lista de tipos del defensor
        
    Returns:
        Diccionario con multiplicadores de daño
    """
    # Tabla simplificada de efectividad de tipos
    effectiveness = {
        'fire': {'grass': 2.0, 'ice': 2.0, 'bug': 2.0, 'steel': 2.0, 'water': 0.5, 'fire': 0.5, 'rock': 0.5, 'dragon': 0.5},
        'water': {'fire': 2.0, 'ground': 2.0, 'rock': 2.0, 'water': 0.5, 'grass': 0.5, 'dragon': 0.5},
        'grass': {'water': 2.0, 'ground': 2.0, 'rock': 2.0, 'fire': 0.5, 'grass': 0.5, 'poison': 0.5, 'flying': 0.5, 'bug': 0.5, 'dragon': 0.5, 'steel': 0.5},
        'electric': {'water': 2.0, 'flying': 2.0, 'electric': 0.5, 'grass': 0.5, 'dragon': 0.5, 'ground': 0.0},
    }
    
    multiplier = 1.0
    for defender_type in defender_types:
        if attacker_type in effectiveness:
            multiplier *= effectiveness[attacker_type].get(defender_type, 1.0)
    
    return {'multiplier': multiplier, 'effectiveness': 'Super efectivo' if multiplier > 1 else 'No muy efectivo' if multiplier < 1 else 'Normal'}
