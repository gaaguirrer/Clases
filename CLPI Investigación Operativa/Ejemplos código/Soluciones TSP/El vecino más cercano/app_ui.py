"""
CAPA DE PRESENTACIÓN - INTERFAZ DE USUARIO
Implementa la interfaz gráfica usando PyForms y principios UX
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Importar componentes de PyForms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText, ControlButton, ControlList
from pyforms.controls import ControlNumber, ControlLabel, ControlCombo, ControlFile

# Importar nuestras clases de negocio y datos
from tsp_solver import TSPNearestNeighbor
from data_manager import TSPDataManager

class TSPApp(BaseWidget):
    """
    CLASE PRINCIPAL DE LA INTERFAZ DE USUARIO
    Coordina todos los componentes visuales y maneja la interacción del usuario
    """
    
    def __init__(self):
        """
        CONSTRUCTOR DE LA APLICACIÓN
        Inicializa la ventana principal y todos los componentes
        """
        super(TSPApp, self).__init__('TSP Solver - Vecino Más Cercano')
        
        # Inicializar el motor de cálculo TSP
        self.solver = TSPNearestNeighbor()
        
        # Configurar la interfaz de usuario
        self._initialize_ui()
        
    def _initialize_ui(self):
        """
        INICIALIZACIÓN COMPLETA DE LA INTERFAZ
        Crea y configura todos los elementos visuales de la aplicación
        """
        # Establecer tamaño mínimo para buena experiencia de usuario
        self.setMinimumSize(1200, 800)
        
        # ===== PANEL DE CONFIGURACIÓN DEL PROBLEMA =====
        self._input_panel = ControlLabel('=== CONFIGURACIÓN DEL PROBLEMA ===')
        
        # Lista de ciudades - permite ver y editar las ciudades ingresadas
        self._cities_list = ControlList('Ciudades (X, Y)')
        self._cities_list.readonly = False  # Permitir edición directa
        
        # ===== CONTROLES PARA AGREGAR NUEVAS CIUDADES =====
        self._city_x = ControlNumber('Coordenada X', default=0, minimum=0, maximum=1000)
        self._city_y = ControlNumber('Coordenada Y', default=0, minimum=0, maximum=1000)
        self._add_city_btn = ControlButton('Agregar Ciudad')
        
        # ===== CONFIGURACIÓN DE LA SOLUCIÓN =====
        self._start_city = ControlCombo('Ciudad de inicio')
        self._solve_btn = ControlButton('Resolver TSP')
        self._clear_btn = ControlButton('Limpiar Todo')
        
        # ===== PANEL DE RESULTADOS =====
        self._results_panel = ControlLabel('=== RESULTADOS ===')
        self._route_display = ControlList('Ruta Óptima')
        self._route_display.readonly = True  # Solo lectura para resultados
        
        # ===== DASHBOARD DE ESTADÍSTICAS =====
        self._stats_label = ControlLabel('Estadísticas:')
        self._total_distance = ControlLabel('Distancia Total: --')
        self._avg_distance = ControlLabel('Distancia Promedio: --')
        self._max_distance = ControlLabel('Distancia Máxima: --')
        self._min_distance = ControlLabel('Distancia Mínima: --')
        self._std_distance = ControlLabel('Desviación Estándar: --')
        self._num_cities = ControlLabel('Número de Ciudades: --')
        
        # ===== COMPONENTE DE GRÁFICOS =====
        self._figure = plt.figure(figsize=(10, 6))
        self._canvas = FigureCanvas(self._figure)
        
        # ===== ORGANIZACIÓN DEL LAYOUT - PRINCIPIO UX DE AGRUPACIÓN =====
        self.formset = [
            # Panel superior: Configuración del problema
            ('_input_panel', 
             ['_cities_list', 
              ['_city_x', '_city_y', '_add_city_btn'], 
              ['_start_city', '_solve_btn', '_clear_btn']]),
            
            # Panel medio: Resultados
            '_results_panel',
            ['_route_display', 
             [['_stats_label'], 
              ['_total_distance'], 
              ['_avg_distance'], 
              ['_max_distance'], 
              ['_min_distance'],
              ['_std_distance'],
              ['_num_cities']]],
            
            # Panel inferior: Gráficos
            '_canvas'
        ]
        
        # ===== CONEXIÓN DE EVENTOS - ENLAZAR ACCIONES CON MÉTODOS =====
        self._add_city_btn.value = self._add_city
        self._solve_btn.value = self._solve_tsp
        self._clear_btn.value = self._clear_all
        self._cities_list.item_selection_changed_event = self._update_start_city_combo
        
        print("Interfaz de usuario inicializada correctamente")

    def _add_city(self):
        """
        MANEJADOR: AGREGAR NUEVA CIUDAD
        Se ejecuta cuando el usuario hace clic en 'Agregar Ciudad'
        """
        # Obtener valores de los campos de entrada
        x = self._city_x.value
        y = self._city_y.value
        
        # Validar que se hayan ingresado valores válidos
        if x is not None and y is not None:
            # Calcular el número de ciudad automáticamente
            city_number = len(self._cities_list.value)
            
            # Agregar nueva ciudad a la lista con formato: (Nombre, X, Y)
            self._cities_list += [(f"Ciudad {city_number}", x, y)]
            
            # Actualizar las opciones de ciudad de inicio
            self._update_start_city_combo()
            
            # PRINCIPIO UX: Limpiar campos después de agregar para facilitar nueva entrada
            self._city_x.value = 0
            self._city_y.value = 0
            
            print(f"Ciudad {city_number} agregada en coordenadas ({x}, {y})")

    def _update_start_city_combo(self):
        """
        ACTUALIZAR OPCIONES DE CIUDAD DE INICIO
        Se ejecuta automáticamente cuando cambia la lista de ciudades
        """
        cities = self._cities_list.value
        self._start_city.clear()  # Limpiar opciones anteriores
        
        # Agregar cada ciudad como opción en el combo box
        for i, city in enumerate(cities):
            display_text = f"Ciudad {i} (X:{city[1]}, Y:{city[2]})"
            self._start_city.add_item(display_text, i)

    def _solve_tsp(self):
        """
        MANEJADOR PRINCIPAL: RESOLVER PROBLEMA TSP
        Coordina la ejecución del algoritmo y visualización de resultados
        """
        # VALIDACIÓN: Verificar que hay suficientes ciudades
        if len(self._cities_list.value) < 3:
            self.warning("Se necesitan al menos 3 ciudades para resolver el TSP")
            return
        
        print("Iniciando cálculo de ruta óptima...")
        
        # EXTRACCIÓN DE DATOS: Convertir datos de UI a formato de coordenadas
        cities = []
        for city_data in self._cities_list.value:
            # city_data tiene formato: (nombre, coordenada_x, coordenada_y)
            cities.append((city_data[1], city_data[2]))
        
        # EJECUCIÓN DEL ALGORITMO: Llamar al solver
        start_city = self._start_city.value
        route, total_distance = self.solver.solve(cities, start_city)
        
        print(f"Ruta calculada: {len(route)} segmentos, Distancia total: {total_distance:.2f}")
        
        # VISUALIZACIÓN DE RESULTADOS
        self._display_route(route, cities)    # Mostrar ruta paso a paso
        self._display_statistics()            # Actualizar estadísticas
        self._plot_solution(route, cities)    # Generar gráficos
        
        # GUARDAR SOLUCIÓN (opcional)
        stats = self.solver.get_statistics()
        TSPDataManager.save_solution(route, stats)

    def _display_route(self, route, cities):
        """
        MOSTRAR RUTA ÓPTIMA EN LA INTERFAZ
        Formatea y muestra la secuencia de ciudades a visitar
        """
        self._route_display.clear()  # Limpiar resultados anteriores
        
        # Generar entrada para cada segmento de la ruta
        for i, city_idx in enumerate(route[:-1]):
            next_city_idx = route[i + 1]
            x1, y1 = cities[city_idx]
            x2, y2 = cities[next_city_idx]
            
            # Calcular distancia de este segmento específico
            distance = self.solver.calculate_distance((x1, y1), (x2, y2))
            
            # Agregar información formateada a la lista de resultados
            self._route_display += [
                f"Paso {i+1}: Ciudad {city_idx} → Ciudad {next_city_idx}",
                f"   Distancia: {distance:.2f}",
                ""  # Línea en blanco para separación visual
            ]

    def _display_statistics(self):
        """
        ACTUALIZAR DASHBOARD DE ESTADÍSTICAS
        Muestra las métricas de calidad de la solución encontrada
        """
        stats = self.solver.get_statistics()
        
        # Actualizar cada etiqueta con las estadísticas calculadas
        self._total_distance.value = f"Distancia Total: {stats['total_distance']:.2f}"
        self._avg_distance.value = f"Distancia Promedio: {stats['average_distance']:.2f}"
        self._max_distance.value = f"Distancia Máxima: {stats['max_distance']:.2f}"
        self._min_distance.value = f"Distancia Mínima: {stats['min_distance']:.2f}"
        self._std_distance.value = f"Desviación Estándar: {stats['std_distance']:.2f}"
        self._num_cities.value = f"Número de Ciudades: {stats['num_cities']}"

    def _plot_solution(self, route, cities):
        """
        GENERAR VISUALIZACIONES GRÁFICAS
        Crea gráficos para representar visualmente la solución
        """
        # Limpiar figura anterior para evitar superposición
        self._figure.clear()
        
        # CREAR SUBPLOTS: 1 fila, 2 columnas
        ax1 = self._figure.add_subplot(121)  # Gráfico izquierdo: Mapa de ruta
        ax2 = self._figure.add_subplot(122)  # Gráfico derecho: Distancias por segmento
        
        # --- GRÁFICO 1: VISUALIZACIÓN DE LA RUTA ---
        
        # Extraer coordenadas en el orden de la ruta
        x_coords = [cities[i][0] for i in route]
        y_coords = [cities[i][1] for i in route]
        
        # DIBUJAR PUNTOS: Ciudades como puntos rojos
        ax1.scatter(x_coords, y_coords, c='red', s=100, zorder=5)
        
        # DIBUJAR LÍNEAS: Ruta como líneas azules conectando ciudades
        ax1.plot(x_coords, y_coords, 'b-', alpha=0.7, linewidth=2, zorder=4)
        
        # ETIQUETAS: Añadir nombres a cada ciudad
        for i, (x, y) in enumerate(cities):
            ax1.annotate(f'Ciudad {i}', (x, y), xytext=(5, 5), 
                        textcoords='offset points', fontsize=8)
        
        # CONFIGURACIÓN DEL GRÁFICO DE RUTA
        ax1.set_xlabel('Coordenada X')
        ax1.set_ylabel('Coordenada Y')
        ax1.set_title('Ruta Óptima TSP')
        ax1.grid(True, alpha=0.3)  # Grid suave para mejor lectura
        
        # --- GRÁFICO 2: ANÁLISIS DE DISTANCIAS POR SEGMENTO ---
        
        segment_distances = []
        segment_labels = []
        
        # CALCULAR DISTANCIAS PARA CADA SEGMENTO DE LA RUTA
        for i in range(len(route)-1):
            dist = self.solver.calculate_distance(
                cities[route[i]], cities[route[i+1]]
            )
            segment_distances.append(dist)
            segment_labels.append(f'{route[i]}→{route[i+1]}')
        
        # CREAR GRÁFICO DE BARRAS
        bars = ax2.bar(segment_labels, segment_distances, alpha=0.7, color='green')
        ax2.set_xlabel('Segmentos de Ruta')
        ax2.set_ylabel('Distancia')
        ax2.set_title('Distancias por Segmento')
        ax2.tick_params(axis='x', rotation=45)  # Rotar etiquetas para mejor lectura
        
        # AÑADIR VALORES NUMÉRICOS SOBRE LAS BARRAS
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=8)
        
        # AJUSTAR ESPACIADO para evitar superposición de elementos
        self._figure.tight_layout()
        
        # ACTUALIZAR CANVAS: Reflejar cambios en la interfaz
        self._canvas.draw()
        
        print("Gráficos generados y actualizados")

    def _clear_all(self):
        """
        MANEJADOR: LIMPIAR TODOS LOS DATOS
        Restablece la aplicación a su estado inicial
        """
        # Limpiar listas de ciudades y resultados
        self._cities_list.clear()
        self._route_display.clear()
        self._start_city.clear()
        
        # Resetear estadísticas a valores por defecto
        self._total_distance.value = 'Distancia Total: --'
        self._avg_distance.value = 'Distancia Promedio: --'
        self._max_distance.value = 'Distancia Máxima: --'
        self._min_distance.value = 'Distancia Mínima: --'
        self._std_distance.value = 'Desviación Estándar: --'
        self._num_cities.value = 'Número de Ciudades: --'
        
        # Limpiar gráficos
        self._figure.clear()
        self._canvas.draw()
        
        print("Todos los datos han sido limpiados")