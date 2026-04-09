"""
GENERADOR DE DATOS DE EJEMPLO PARA PRUEBAS
Crea archivos con datos de ciudades para probar la aplicación
"""
import random

def create_sample_data(filename="sample_cities.txt", num_cities=10):
    """
    CREAR DATOS DE EJEMPLO PARA TSP
    Genera coordenadas aleatorias de ciudades en un área definida
    
    Args:
        filename (str): Nombre del archivo de salida
        num_cities (int): Número de ciudades a generar
    """
    sample_cities = [
        (0, 0),      # Ciudad 0 - Punto de partida
        (10, 20),    # Ciudad 1
        (30, 15),    # Ciudad 2  
        (25, 5),     # Ciudad 3
        (40, 30),    # Ciudad 4
        (15, 35),    # Ciudad 5
        (35, 40),    # Ciudad 6
        (5, 25),     # Ciudad 7
        (20, 10),    # Ciudad 8
        (45, 15)     # Ciudad 9
    ]
    
    # Si se piden más ciudades, generar aleatorias
    if num_cities > 10:
        sample_cities = [(0, 0)]  # Siempre empezar con (0,0)
        for i in range(1, num_cities):
            x = random.randint(5, 50)
            y = random.randint(5, 50)
            sample_cities.append((x, y))
    
    # Guardar en archivo
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for x, y in sample_cities:
                f.write(f"{x},{y}\n")
        
        print(f"Datos de ejemplo creados en: {filename}")
        print(f"Número de ciudades generadas: {len(sample_cities)}")
        print("Coordenadas generadas:")
        for i, (x, y) in enumerate(sample_cities):
            print(f"  Ciudad {i}: ({x}, {y})")
            
    except Exception as e:
        print(f"Error creando datos de ejemplo: {e}")

def create_clustered_data(filename="clustered_cities.txt"):
    """
    CREAR DATOS AGRUPADOS (CLUSTERED)
    Genera ciudades agrupadas en regiones para problemas más realistas
    """
    cities = []
    
    # Cluster 1: Región noroeste
    for i in range(5):
        x = random.randint(5, 15)
        y = random.randint(30, 40)
        cities.append((x, y))
    
    # Cluster 2: Región noreste  
    for i in range(5):
        x = random.randint(35, 45)
        y = random.randint(25, 35)
        cities.append((x, y))
    
    # Cluster 3: Región central
    for i in range(5):
        x = random.randint(15, 30)
        y = random.randint(10, 20)
        cities.append((x, y))
    
    # Guardar en archivo
    with open(filename, 'w', encoding='utf-8') as f:
        for x, y in cities:
            f.write(f"{x},{y}\n")
    
    print(f"Datos agrupados creados en: {filename}")

if __name__ == "__main__":
    # Ejecutar cuando se llama directamente
    print("Generador de Datos de Ejemplo para TSP Solver")
    print("=" * 50)
    
    # Crear datos básicos
    create_sample_data("sample_cities.txt", 10)
    
    # Crear datos más grandes
    create_sample_data("large_cities.txt", 20)
    
    # Crear datos agrupados
    create_clustered_data("clustered_cities.txt")
    
    print("\nInstrucciones para usar los datos:")
    print("1. Ejecuta la aplicación: python main.py")
    print("2. Usa el ejemplo_data.py para cargar las ciudades")