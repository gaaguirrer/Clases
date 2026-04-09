"""
Script para poblar la base de datos JSON con datos de la PokeAPI
Uso: python scripts/populate_db.py --generation 1
"""
import requests
import json
import time
import argparse
import sys
from pathlib import Path
from typing import Dict, List

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


def fetch_pokemon_data(identifier: str) -> Dict:
    """
    Obtiene datos detallados de un Pokémon desde la PokeAPI
    
    Args:
        identifier: Nombre o ID del Pokémon
        
    Returns:
        Diccionario con todos los datos del Pokémon
    """
    try:
        base_url = "https://pokeapi.co/api/v2"
        
        # Obtener datos básicos
        print(f"  Obteniendo datos de {identifier}...")
        response = requests.get(f"{base_url}/pokemon/{identifier}", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Obtener datos de especie
        species_response = requests.get(data['species']['url'], timeout=10)
        species_response.raise_for_status()
        species_data = species_response.json()
        
        # Nombre en español
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
        evolution_response = requests.get(species_data['evolution_chain']['url'], timeout=10)
        evolution_response.raise_for_status()
        evolution_data = evolution_response.json()
        
        def extract_evolution_chain(chain):
            """Extrae la cadena evolutiva completa"""
            evolutions = [chain['species']['name']]
            if chain['evolves_to']:
                for evolution in chain['evolves_to']:
                    evolutions.extend(extract_evolution_chain(evolution))
            return evolutions
        
        evolution_chain = extract_evolution_chain(evolution_data['chain'])
        
        # Habilidades
        abilities = [
            {
                'name': ability['ability']['name'],
                'is_hidden': ability['is_hidden']
            }
            for ability in data['abilities']
        ]
        
        # Construir objeto Pokémon completo
        pokemon = {
            'id': data['id'],
            'nombre': data['name'],
            'nombre_es': nombre_es,
            'descripcion': descripcion_es,
            'imagen': data['sprites'].get('other', {}).get('official-artwork', {}).get('front_default')
                       or data['sprites']['front_default'],
            'imagen_shiny': data['sprites'].get('other', {}).get('official-artwork', {}).get('front_shiny'),
            'tipos': [t['type']['name'] for t in data['types']],
            'altura': data['height'] / 10,  # Convertir a metros
            'peso': data['weight'] / 10,  # Convertir a kg
            'stats': {
                'hp': data['stats'][0]['base_stat'],
                'ataque': data['stats'][1]['base_stat'],
                'defensa': data['stats'][2]['base_stat'],
                'ataque_especial': data['stats'][3]['base_stat'],
                'defensa_especial': data['stats'][4]['base_stat'],
                'velocidad': data['stats'][5]['base_stat']
            },
            'habilidades': abilities,
            'evoluciones': evolution_chain,
            'generacion': species_data['generation']['name'].split('-')[-1]
        }
        
        print(f"  ✓ {nombre_es} obtenido exitosamente")
        return pokemon
        
    except requests.exceptions.RequestException as e:
        print(f"  ✗ Error al obtener {identifier}: {e}")
        return None
    except Exception as e:
        print(f"  ✗ Error inesperado con {identifier}: {e}")
        return None


def populate_database(generation: int = 1, output_file: str = "data/db.json"):
    """
    Puebla la base de datos con Pokémon de una generación específica
    
    Args:
        generation: Número de generación (1-9)
        output_file: Ruta del archivo de salida
    """
    if generation not in GENERATIONS:
        print(f"Generación {generation} no válida. Debe ser 1-9.")
        return
    
    start_id, end_id = GENERATIONS[generation]
    print(f"\n{'='*60}")
    print(f"Poblando base de datos con Pokémon de Generación {generation}")
    print(f"Rango: #{start_id} - #{end_id}")
    print(f"{'='*60}\n")
    
    # Cargar datos existentes si existen
    output_path = Path(output_file)
    if output_path.exists():
        with open(output_path, 'r', encoding='utf-8') as f:
            db = json.load(f)
        print(f"Base de datos existente encontrada con {len(db.get('pokemon', []))} Pokémon\n")
    else:
        db = {
            'pokemon': [],
            'favorites': [],
            'history': []
        }
        print("Creando nueva base de datos\n")
    
    # Obtener IDs ya existentes
    existing_ids = {p['id'] for p in db.get('pokemon', [])}
    
    # Obtener datos de cada Pokémon
    pokemon_list = []
    total = end_id - start_id + 1
    
    for pokemon_id in range(start_id, end_id + 1):
        print(f"[{pokemon_id - start_id + 1}/{total}]", end=" ")
        
        if pokemon_id in existing_ids:
            print(f"Pokémon #{pokemon_id} ya existe en la base de datos, saltando...")
            continue
        
        pokemon = fetch_pokemon_data(pokemon_id)
        if pokemon:
            pokemon_list.append(pokemon)
        
        # Respetar rate limit de la API (máx 100 req/min)
        time.sleep(0.6)
    
    # Agregar nuevos Pokémon a la base de datos
    if pokemon_list:
        db['pokemon'].extend(pokemon_list)
        # Ordenar por ID
        db['pokemon'].sort(key=lambda x: x['id'])
        
        # Guardar en archivo
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
        
        print(f"\n{'='*60}")
        print(f"✓ Base de datos actualizada exitosamente")
        print(f"  Total de Pokémon: {len(db['pokemon'])}")
        print(f"  Nuevos agregados: {len(pokemon_list)}")
        print(f"  Archivo: {output_file}")
        print(f"{'='*60}\n")
    else:
        print("\nNo se agregaron nuevos Pokémon.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Poblar base de datos de Pokémon')
    parser.add_argument(
        '--generation',
        type=int,
        default=1,
        choices=range(1, 10),
        help='Número de generación a poblar (1-9)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='data/db.json',
        help='Archivo de salida para la base de datos'
    )
    
    args = parser.parse_args()
    
    populate_database(generation=args.generation, output_file=args.output)
