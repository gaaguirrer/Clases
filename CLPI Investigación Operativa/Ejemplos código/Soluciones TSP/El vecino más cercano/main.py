#!/usr/bin/env python3

# PUNTO DE ENTRADA PRINCIPAL DE LA APLICACIÓN 
# Propósito: Iniciar la aplicación y manejar la ejecución

import sys 
import os

# Añadir el directorio actual al path para imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """
    FUNCIÓN PRINCIPAL
    Inicia la aplicación de PyForms con la interfaz TSP
    """
    try:
        from pyforms import start_app
        from app_ui import TSPApp
        
        print("=" * 50)
        print("   TSP SOLVER - VECINO MÁS CERCANO")
        print("=" * 50)
        print("Iniciando aplicación...")
        
        # Iniciar la aplicación PyForms
        start_app(TSPApp)
        
    except ImportError as e:
        print(f"Error de importación: {e}")
        print("Verifica que todas las dependencias estén instaladas correctamente.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()