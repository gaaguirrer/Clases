"""
CAPA DE GESTIÓN DE DATOS
Maneja operaciones de entrada/salida y persistencia de datos
"""
class TSPDataManager:
    """
    GESTOR DE DATOS PARA LA APLICACIÓN TSP
    Proporciona métodos estáticos para guardar y cargar datos
    """
    
    @staticmethod
    def save_solution(route, statistics, filename="tsp_solution.txt"):
        """
        GUARDAR SOLUCIÓN EN ARCHIVO
        Propósito: Persistir los resultados para análisis posterior
        
        Args:
            route (list): Ruta óptima encontrada
            statistics (dict): Métricas de la solución
            filename (str): Nombre del archivo de salida
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("SOLUCIÓN TSP - VECINO MÁS CERCANO\n")
                f.write("=" * 50 + "\n")
                f.write(f"Ruta: {' -> '.join(map(str, route))}\n")
                f.write(f"Distancia Total: {statistics['total_distance']:.2f}\n")
                f.write(f"Número de Ciudades: {statistics['num_cities']}\n")
                f.write(f"Distancia Promedio: {statistics['average_distance']:.2f}\n")
                f.write(f"Distancia Máxima: {statistics['max_distance']:.2f}\n")
                f.write(f"Distancia Mínima: {statistics['min_distance']:.2f}\n")
                f.write(f"Desviación Estándar: {statistics['std_distance']:.2f}\n")
            print(f"Solución guardada en: {filename}")
        except Exception as e:
            print(f"Error guardando solución: {e}")
    
    @staticmethod
    def load_cities_from_file(filename):
        """
        CARGAR CIUDADES DESDE ARCHIVO
        Propósito: Leer datos de ciudades desde archivo de texto
        
        Args:
            filename (str): Ruta del archivo a cargar
            
        Returns:
            list: Lista de tuplas (x, y) con coordenadas
        """
        cities = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if line and ',' in line:
                        try:
                            x, y = map(float, line.split(','))
                            cities.append((x, y))
                        except ValueError:
                            print(f"Línea {line_num} ignorada (formato inválido): {line}")
            print(f"Cargadas {len(cities)} ciudades desde: {filename}")
        except FileNotFoundError:
            print(f"Archivo no encontrado: {filename}")
        except Exception as e:
            print(f"Error cargando archivo: {e}")
        return cities
    
    @staticmethod
    def export_route_to_csv(route, cities, filename="tsp_route.csv"):
        """
        EXPORTAR RUTA A FORMATO CSV
        Propósito: Generar archivo CSV para análisis externo
        
        Args:
            route (list): Ruta óptima
            cities (list): Coordenadas de ciudades
            filename (str): Nombre del archivo CSV
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Orden,Ciudad,Coordenada_X,Coordenada_Y\n")
                for i, city_idx in enumerate(route):
                    x, y = cities[city_idx]
                    f.write(f"{i+1},{city_idx},{x},{y}\n")
            print(f"Ruta exportada a: {filename}")
        except Exception as e:
            print(f"Error exportando a CSV: {e}")