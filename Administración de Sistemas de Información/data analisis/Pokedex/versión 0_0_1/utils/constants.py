"""
Constantes y configuraciones globales para la aplicación Pokédex
"""

# Configuración de API y servidor
API_CONFIG = {
    'JSON_SERVER_URL': 'http://localhost:3000',
    'POKEAPI_URL': 'https://pokeapi.co/api/v2',
    'TIMEOUT': 5,
    'MAX_RETRIES': 3,
    'CACHE_TTL': 3600
}

# Colores por tipo de Pokémon
TYPE_COLORS = {
    'fire': '#ff7402',
    'water': '#4592c4',
    'grass': '#9bcc50',
    'electric': '#eed535',
    'psychic': '#f366b9',
    'ice': '#51c4e7',
    'dragon': '#53a4cf',
    'dark': '#707070',
    'fairy': '#fdb9e9',
    'normal': '#a4acaf',
    'fighting': '#d56723',
    'flying': '#3dc7ef',
    'poison': '#b97fc9',
    'ground': '#f7de3f',
    'rock': '#a38c21',
    'bug': '#729f3f',
    'ghost': '#7b62a3',
    'steel': '#9eb7b8'
}

# Iconos de tipo (Google Material Symbols)
TYPE_ICONS = {
    'fire': '<span class="material-symbols-rounded" style="vertical-align: middle;">local_fire_department</span>',
    'water': '<span class="material-symbols-rounded" style="vertical-align: middle;">water_drop</span>',
    'grass': '<span class="material-symbols-rounded" style="vertical-align: middle;">eco</span>',
    'electric': '<span class="material-symbols-rounded" style="vertical-align: middle;">bolt</span>',
    'psychic': '<span class="material-symbols-rounded" style="vertical-align: middle;">psychology</span>',
    'ice': '<span class="material-symbols-rounded" style="vertical-align: middle;">ac_unit</span>',
    'dragon': '<span class="material-symbols-rounded" style="vertical-align: middle;">auto_awesome</span>',
    'dark': '<span class="material-symbols-rounded" style="vertical-align: middle;">dark_mode</span>',
    'fairy': '<span class="material-symbols-rounded" style="vertical-align: middle;">auto_fix_high</span>',
    'normal': '<span class="material-symbols-rounded" style="vertical-align: middle;">radio_button_checked</span>',
    'fighting': '<span class="material-symbols-rounded" style="vertical-align: middle;">sports_martial_arts</span>',
    'flying': '<span class="material-symbols-rounded" style="vertical-align: middle;">air</span>',
    'poison': '<span class="material-symbols-rounded" style="vertical-align: middle;">skull</span>',
    'ground': '<span class="material-symbols-rounded" style="vertical-align: middle;">terrain</span>',
    'rock': '<span class="material-symbols-rounded" style="vertical-align: middle;">landscape</span>',
    'bug': '<span class="material-symbols-rounded" style="vertical-align: middle;">pest_control</span>',
    'ghost': '<span class="material-symbols-rounded" style="vertical-align: middle;">visibility_off</span>',
    'steel': '<span class="material-symbols-rounded" style="vertical-align: middle;">shield</span>'
}

# Rangos de generaciones
GENERATIONS = {
    1: (1, 151),
    2: (152, 251),
    3: (252, 386),
    4: (387, 493),
    5: (494, 649),
    6: (650, 721),
    7: (722, 809),
    8: (810, 905),
    9: (906, 1025)
}

# Nombres de estadísticas en español
STAT_NAMES_ES = {
    'hp': 'PS',
    'attack': 'Ataque',
    'defense': 'Defensa',
    'special-attack': 'Ataque Esp.',
    'special-defense': 'Defensa Esp.',
    'speed': 'Velocidad'
}

# Nombres de tipos en español
TYPE_NAMES_ES = {
    'normal': 'Normal',
    'fire': 'Fuego',
    'water': 'Agua',
    'grass': 'Planta',
    'electric': 'Eléctrico',
    'ice': 'Hielo',
    'fighting': 'Lucha',
    'poison': 'Veneno',
    'ground': 'Tierra',
    'flying': 'Volador',
    'psychic': 'Psíquico',
    'bug': 'Bicho',
    'rock': 'Roca',
    'ghost': 'Fantasma',
    'dragon': 'Dragón',
    'dark': 'Siniestro',
    'steel': 'Acero',
    'fairy': 'Hada'
}

# Pokémon populares para inicio rápido
# Pokémon populares para inicio rápido (Nombre, ID)
POPULAR_POKEMON = [
    {'name': 'pikachu', 'id': 25},
    {'name': 'charizard', 'id': 6},
    {'name': 'bulbasaur', 'id': 1},
    {'name': 'squirtle', 'id': 7},
    {'name': 'eevee', 'id': 133},
    {'name': 'mewtwo', 'id': 150},
    {'name': 'gengar', 'id': 94},
    {'name': 'dragonite', 'id': 149},
    {'name': 'snorlax', 'id': 143},
    {'name': 'lucario', 'id': 448}
]

# Configuración de la aplicación
APP_CONFIG = {
    'PAGE_TITLE': 'Pokédex App',
    'PAGE_ICON': None,
    'LAYOUT': 'wide',
    'MAX_FAVORITES': 50,
    'MAX_HISTORY': 20,
    'RESULTS_PER_PAGE': 20
}
