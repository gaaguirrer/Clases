"""
CAPA DE LÓGICA DE NEGOCIO - ALGORITMO TSP
Contiene la implementación del heurístico del vecino más cercano
y cálculos relacionados con el problema del agente viajero.
"""
import numpy as np

class TSPNearestNeighbor:
    """
    CLASE PRINCIPAL DEL SOLVER TSP
    Implementa el algoritmo del vecino más cercano para resolver
    el problema del agente viajero de manera aproximada.
    """
    
    def __init__(self):
        """
        INICIALIZACIÓN DEL SOLVER
        Propósito: Preparar el estado interno para cálculos
        """
        self.distances = None      # Matriz de distancias (no usada actualmente)
        self.cities = None         # Lista de coordenadas de ciudades
        self.route = []            # Ruta óptima encontrada
        self.total_distance = 0    # Distancia total de la ruta
        
    def calculate_distance(self, city1, city2):
        """
        CÁLCULO DE DISTANCIA EUCLIDIANA
        Propósito: Calcular la distancia entre dos puntos en 2D
        Fórmula: √((x₂-x₁)² + (y₂-y₁)²)
        
        Args:
            city1 (tuple): Tupla (x, y) de la primera ciudad
            city2 (tuple): Tupla (x, y) de la segunda ciudad
            
        Returns:
            float: Distancia euclidiana entre las ciudades
        """
        return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    def nearest_neighbor(self, cities, start_city=0):
        """
        ALGORITMO DEL VECINO MÁS CERCANO
        Propósito: Encontrar una ruta aproximada óptima para el TSP
        Complejidad: O(n²) donde n es el número de ciudades
        
        Args:
            cities (list): Lista de tuplas (x, y) con coordenadas
            start_city (int): Índice de la ciudad de inicio (default: 0)
            
        Returns:
            tuple: (ruta, distancia_total)
                   - ruta: Lista de índices en orden de visita
                   - distancia_total: Suma de todas las distancias del recorrido
        """
        n = len(cities)
        # Conjunto de ciudades no visitadas (todas excepto la inicial)
        unvisited = set(range(n))
        current_city = start_city
        route = [current_city]  # La ruta comienza con la ciudad inicial
        total_distance = 0
        
        # Remover ciudad inicial de no visitadas
        unvisited.remove(current_city)
        
        # BUCLE PRINCIPAL: Visitar todas las ciudades restantes
        while unvisited:
            nearest_city = None
            min_distance = float('inf')  # Inicializar con valor infinito
            
            # BUSCAR LA CIUDAD NO VISITADA MÁS CERCANA
            for city in unvisited:
                # Calcular distancia desde ciudad actual a ciudad candidata
                distance = self.calculate_distance(cities[current_city], cities[city])
                
                # ACTUALIZAR MÍNIMO si encontramos ciudad más cercana
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city
            
            # ACTUALIZAR RUTA Y DISTANCIA con el vecino más cercano
            total_distance += min_distance
            current_city = nearest_city
            route.append(current_city)
            unvisited.remove(current_city)
        
        # CERRAR EL CICLO: Regresar a la ciudad de inicio
        return_distance = self.calculate_distance(cities[route[-1]], cities[route[0]])
        total_distance += return_distance
        route.append(route[0])  # Añadir ciudad inicial al final para completar ciclo
        
        return route, total_distance
    
    def solve(self, cities, start_city=0):
        """
        INTERFAZ PRINCIPAL DE SOLUCIÓN
        Propósito: Ejecutar el algoritmo y almacenar resultados
        
        Args:
            cities (list): Lista de coordenadas de ciudades
            start_city (int): Índice de ciudad de inicio
            
        Returns:
            tuple: (ruta, distancia_total)
        """
        self.cities = cities
        self.route, self.total_distance = self.nearest_neighbor(cities, start_city)
        return self.route, self.total_distance
    
    def get_statistics(self):
        """
        GENERACIÓN DE ESTADÍSTICAS DE LA SOLUCIÓN
        Propósito: Proporcionar métricas de calidad de la ruta encontrada
        
        Returns:
            dict: Diccionario con métricas:
                - total_distance: Distancia total del recorrido
                - average_distance: Distancia promedio entre ciudades
                - max_distance: Distancia máxima entre dos ciudades consecutivas
                - min_distance: Distancia mínima entre dos ciudades consecutivas
                - std_distance: Desviación estándar de las distancias
                - num_cities: Número total de ciudades
        """
        # Validar que existe una ruta calculada
        if not self.route:
            return {}
        
        # CALCULAR DISTANCIAS INDIVIDUALES ENTRE CIUDADES CONSECUTIVAS
        distances = []
        for i in range(len(self.route)-1):
            dist = self.calculate_distance(
                self.cities[self.route[i]], 
                self.cities[self.route[i+1]]
            )
            distances.append(dist)
        
        # CALCULAR MÉTRICAS ESTADÍSTICAS
        return {
            'total_distance': self.total_distance,
            'average_distance': np.mean(distances),
            'max_distance': np.max(distances),
            'min_distance': np.min(distances),
            'std_distance': np.std(distances),
            'num_cities': len(self.cities)
        }