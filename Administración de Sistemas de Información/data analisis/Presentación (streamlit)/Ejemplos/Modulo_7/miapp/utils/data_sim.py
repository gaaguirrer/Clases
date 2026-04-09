"""
utils/data_sim.py
Modulo de simulacion de base de datos para la Galeria de Arte Digital.
Provee datos ficticios que imitan lo que vendria de una fuente real.
"""

import pandas as pd
import numpy as np
import time


# ---------------------------------------------------------------------------
# Datos estaticos de obras de arte por estilo
# ---------------------------------------------------------------------------

OBRAS = {
    "Abstraccionismo": [
        {"titulo": "Composicion en Azul", "artista": "Elena Voss", "anio": 2018, "valor_usd": 4500},
        {"titulo": "Ritmo Sincopado",      "artista": "Marco Reyes", "anio": 2020, "valor_usd": 3800},
        {"titulo": "Fragmento No. 7",      "artista": "Sofía Lund",  "anio": 2015, "valor_usd": 6200},
        {"titulo": "Tension Cromatica",    "artista": "David Osei",  "anio": 2022, "valor_usd": 2900},
    ],
    "Realismo Digital": [
        {"titulo": "La Ciudad a las 3am",  "artista": "Carla Mora",  "anio": 2021, "valor_usd": 5500},
        {"titulo": "Retrato de Algoritmo", "artista": "Yuki Tanaka", "anio": 2019, "valor_usd": 7800},
        {"titulo": "Mercado Central",      "artista": "Luis Ponce",  "anio": 2023, "valor_usd": 3100},
    ],
    "Arte Generativo": [
        {"titulo": "Iteracion 42",         "artista": "CodeArtist_X", "anio": 2022, "valor_usd": 1200},
        {"titulo": "Fractal Organico",     "artista": "Neural Co.",   "anio": 2023, "valor_usd": 2400},
        {"titulo": "Simetria Emergente",   "artista": "AlgoStudio",   "anio": 2021, "valor_usd": 1800},
        {"titulo": "patron.exe",           "artista": "CodeArtist_X", "anio": 2020, "valor_usd": 950},
    ],
}


# ---------------------------------------------------------------------------
# Metricas del dashboard principal
# ---------------------------------------------------------------------------

METRICAS = {
    "obras_registradas": {"valor": 847,    "delta": "+23"},
    "artistas_activos":  {"valor": 134,    "delta": "+8"},
    "ventas_mes_usd":    {"valor": 92_400, "delta": "+12.5%"},
    "visitantes_web":    {"valor": 15_320, "delta": "+4.3%"},
}


# ---------------------------------------------------------------------------
# Funcion simulada de carga pesada (para demostrar @st.cache_data)
# ---------------------------------------------------------------------------

def cargar_datos_analisis(seed: int = 42) -> pd.DataFrame:
    """
    Simula una consulta costosa a la base de datos con una pausa artificial.
    En una aplicacion real, aqui iria una llamada a SQL, una API o un archivo CSV.
    """
    time.sleep(2.5)  # Simula latencia de red o procesamiento

    rng = np.random.default_rng(seed)
    meses = pd.date_range("2023-01-01", periods=12, freq="MS")
    df = pd.DataFrame({
        "Mes":               meses,
        "Ventas_USD":        rng.integers(40_000, 120_000, size=12),
        "Obras_Registradas": rng.integers(20, 80, size=12),
        "Visitantes_Web":    rng.integers(8_000, 25_000, size=12),
    })
    df["Mes"] = df["Mes"].dt.strftime("%b %Y")
    return df


# ---------------------------------------------------------------------------
# Opciones de listas desplegables
# ---------------------------------------------------------------------------

ESTILOS_ARTE = list(OBRAS.keys())
TECNICAS = ["Acrilico sobre lienzo", "Oleo digital", "Fotografia procesada",
            "Impresion 3D", "NFT / Arte en cadena", "Acuarela escaneada"]
