"""
Modelo de datos para Pokémon
Integra json-server local con fallback a PokeAPI
"""
import requests
import streamlit as st
from typing import Dict, List, Optional
from utils.constants import API_CONFIG, GENERATIONS
from utils.helpers import retry_on_failure, normalize_search_term, is_valid_pokemon_id


@st.cache_data(ttl=API_CONFIG['CACHE_TTL'])
def get_pokemon_from_json_server(identifier: str) -> Optional[Dict]:
    """
    Obtiene un Pokémon desde el servidor JSON local
    
    Args:
        identifier: ID o nombre del Pokémon
        
    Returns:
        Diccionario con datos del Pokémon o None si no se encuentra
    """
    try:
        # Intentar por ID
        if str(identifier).isdigit():
            url = f"{API_CONFIG['JSON_SERVER_URL']}/pokemon/{identifier}"
        else:
            # Buscar por nombre
            url = f"{API_CONFIG['JSON_SERVER_URL']}/pokemon?nombre={identifier}"
        
        response = requests.get(url, timeout=API_CONFIG['TIMEOUT'])
        response.raise_for_status()
        
        data = response.json()
        
        # Si es una lista (búsqueda por nombre), tomar el primero
        if isinstance(data, list):
            return data[0] if data else None
        
        return data
        
    except Exception as e:
        print(f"Error al consultar json-server: {e}")
        return None


@st.cache_data(ttl=API_CONFIG['CACHE_TTL'])
@retry_on_failure(max_attempts=API_CONFIG['MAX_RETRIES'])
def get_pokemon_from_pokeapi(identifier: str) -> Optional[Dict]:
    """
    Obtiene un Pokémon desde PokeAPI (fallback)
    
    Args:
        identifier: ID o nombre del Pokémon
        
    Returns:
        Diccionario con datos del Pokémon transformados al formato local
    """
    try:
        identifier = normalize_search_term(str(identifier))
        
        # Primera llamada para datos básicos
        response = requests.get(
            f"{API_CONFIG['POKEAPI_URL']}/pokemon/{identifier}",
            timeout=API_CONFIG['TIMEOUT']
        )
        response.raise_for_status()
        data = response.json()
        
        # Segunda llamada para datos de especie
        species_response = requests.get(data['species']['url'], timeout=API_CONFIG['TIMEOUT'])
        species_response.raise_for_status()
        species_data = species_response.json()
        
        # Obtener nombre en español
        nombre_es = next(
            (n['name'] for n in species_data['names'] if n['language']['name'] == 'es'),
            data['name']
        )
        
        # Descripción en español
        descripcion_es = next(
            (entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
             for entry in species_data['flavor_text_entries']
             if entry['language']['name'] == 'es'),
            ''
        )
        
        # Obtener cadena evolutiva
        evolution_response = requests.get(species_data['evolution_chain']['url'], timeout=API_CONFIG['TIMEOUT'])
        evolution_response.raise_for_status()
        evolution_data = evolution_response.json()
        
        def procesar_evoluciones(chain):
            evolves_to = []
            current = chain['species']['name']
            if chain['evolves_to']:
                for evolution in chain['evolves_to']:
                    evolves_to.append(evolution['species']['name'])
                    evolves_to.extend(procesar_evoluciones(evolution))
            return [current] + evolves_to
        
        evoluciones = list(set(procesar_evoluciones(evolution_data['chain'])))
        evoluciones = [e for e in evoluciones if e != data['name']][:3]
        
        # Habilidades
        abilities = [
            {
                'name': ability['ability']['name'],
                'is_hidden': ability['is_hidden']
            }
            for ability in data['abilities']
        ]
        
        return {
            'id': data['id'],
            'nombre': data['name'],
            'nombre_es': nombre_es,
            'descripcion': descripcion_es,
            'imagen': data['sprites'].get('other', {}).get('official-artwork', {}).get('front_default')
                       or data['sprites']['front_default'],
            'imagen_shiny': data['sprites'].get('other', {}).get('official-artwork', {}).get('front_shiny'),
            'tipos': [t['type']['name'] for t in data['types']],
            'altura': data['height'] / 10,
            'peso': data['weight'] / 10,
            'stats': {
                'hp': data['stats'][0]['base_stat'],
                'ataque': data['stats'][1]['base_stat'],
                'defensa': data['stats'][2]['base_stat'],
                'ataque_especial': data['stats'][3]['base_stat'],
                'defensa_especial': data['stats'][4]['base_stat'],
                'velocidad': data['stats'][5]['base_stat']
            },
            'habilidades': abilities,
            'evoluciones': evoluciones,
            'generacion': species_data['generation']['name'].split('-')[-1]
        }
        
    except requests.exceptions.HTTPError as e:
        # 404 (No encontrado) o 400 (Bad Request - ID inválido)
        if e.response.status_code in [404, 400]:
            # No mostrar error aquí, dejar que el controlador maneje el "No encontrado"
            return None
        else:
            st.error(f"Error de conexión con la API: {e}")
        return None
    except Exception as e:
        st.error(f"Error al obtener datos: {e}")
        return None


def get_pokemon(identifier: str) -> Optional[Dict]:
    """
    Obtiene un Pokémon, intentando primero json-server y luego PokeAPI
    
    Args:
        identifier: ID o nombre del Pokémon
        
    Returns:
        Diccionario con datos del Pokémon o None si no se encuentra
    """
    # Intentar json-server primero
    pokemon = get_pokemon_from_json_server(identifier)
    
    if pokemon:
        return pokemon
    
    # Fallback a PokeAPI
    print(f"json-server no disponible, consultando PokeAPI para {identifier}")
    st.toast(f"⚠️ Base de datos local no disponible. Usando PokeAPI para {identifier}...", icon="🌐")
    return get_pokemon_from_pokeapi(identifier)


@st.cache_data(ttl=API_CONFIG['CACHE_TTL'] * 24)
def get_all_pokemon_types() -> List[str]:
    """
    Obtiene todos los tipos de Pokémon disponibles
    
    Returns:
        Lista de nombres de tipos
    """
    try:
        # Intentar desde json-server primero
        response = requests.get(
            f"{API_CONFIG['JSON_SERVER_URL']}/pokemon",
            timeout=API_CONFIG['TIMEOUT']
        )
        if response.status_code == 200:
            pokemon_list = response.json()
            types = set()
            for p in pokemon_list:
                types.update(p.get('tipos', []))
            return sorted(list(types))
    except:
        pass
    
    # Fallback hardcoded
    return [
        'normal', 'fire', 'water', 'grass', 'electric',
        'ice', 'fighting', 'poison', 'ground', 'flying',
        'psychic', 'bug', 'rock', 'ghost', 'dark',
        'dragon', 'steel', 'fairy'
    ]


def search_pokemon(
    query: str = "",
    type_filter: str = None,
    generation: int = None,
    min_stats: int = None,
    max_stats: int = None
) -> List[Dict]:
    """
    Busca Pokémon con filtros avanzados
    
    Args:
        query: Término de búsqueda (nombre)
        type_filter: Filtrar por tipo
        generation: Filtrar por generación (1-9)
        min_stats: Estadísticas base mínimas totales
        max_stats: Estadísticas base máximas totales
        
    Returns:
        Lista de Pokémon que cumplen los criterios
    """
    try:
        # Construir URL con filtros
        url = f"{API_CONFIG['JSON_SERVER_URL']}/pokemon"
        params = {}
        
        if query:
            params['q'] = query
        
        response = requests.get(url, params=params, timeout=API_CONFIG['TIMEOUT'])
        response.raise_for_status()
        
        results = response.json()
        
        # Aplicar filtros adicionales
        if type_filter:
            results = [p for p in results if type_filter in p.get('tipos', [])]
        
        if generation:
            if generation in GENERATIONS:
                start_id, end_id = GENERATIONS[generation]
                results = [p for p in results if start_id <= p['id'] <= end_id]
        
        if min_stats or max_stats:
            from utils.helpers import calculate_stat_total
            
            filtered = []
            for p in results:
                total = calculate_stat_total(p.get('stats', {}))
                if min_stats and total < min_stats:
                    continue
                if max_stats and total > max_stats:
                    continue
                filtered.append(p)
            results = filtered
        
        return results
        
    except Exception as e:
        print(f"Error en búsqueda: {e}")
        return []


def get_random_pokemon(type_filter: str = None) -> Optional[Dict]:
    """
    Obtiene un Pokémon aleatorio, opcionalmente filtrado por tipo
    
    Args:
        type_filter: Tipo de Pokémon a buscar (opcional)
        
    Returns:
        Diccionario con datos del Pokémon
    """
    import random
    
    # Si hay filtro de tipo, necesitamos obtener la lista de ese tipo primero
    if type_filter and type_filter.lower() != "todos":
        # 1. Intentar primero con búsqueda local (Prioridad Local)
        try:
            local_results = search_pokemon(type_filter=type_filter)
            if local_results:
                print(f"Encontrados {len(local_results)} Pokémon de tipo {type_filter} localmente")
                return random.choice(local_results)
        except Exception as e:
            print(f"Error en búsqueda local aleatoria: {e}")

        # 2. Si no hay locales, intentar obtener de PokeAPI (Fallback)
        try:
            # Intentar obtener de PokeAPI para tener la lista completa
            url = f"{API_CONFIG['POKEAPI_URL']}/type/{type_filter.lower()}"
            response = requests.get(url, timeout=API_CONFIG['TIMEOUT'])
            
            if response.status_code == 200:
                data = response.json()
                pokemon_list = data.get('pokemon', [])
                if pokemon_list:
                    random_entry = random.choice(pokemon_list)
                    pokemon_name = random_entry['pokemon']['name']
                    return get_pokemon(pokemon_name)
        except Exception as e:
            print(f"Error obteniendo lista de tipo {type_filter} de API: {e}")
    
    # Comportamiento por defecto (sin filtro o si falla el filtro)
    # Elegir un ID aleatorio de Gen 1-9
    random_id = random.randint(1, 1025)
    return get_pokemon(str(random_id))


def get_pokemon_by_generation(generation: int) -> List[Dict]:
    """
    Obtiene todos los Pokémon de una generación
    
    Args:
        generation: Número de generación (1-9)
        
    Returns:
        Lista de Pokémon de esa generación
    """
    if generation not in GENERATIONS:
        return []
    
    start_id, end_id = GENERATIONS[generation]
    
    try:
        url = f"{API_CONFIG['JSON_SERVER_URL']}/pokemon"
        response = requests.get(url, timeout=API_CONFIG['TIMEOUT'])
        response.raise_for_status()
        
        all_pokemon = response.json()
        return [p for p in all_pokemon if start_id <= p['id'] <= end_id]
        
    except:
        return []
