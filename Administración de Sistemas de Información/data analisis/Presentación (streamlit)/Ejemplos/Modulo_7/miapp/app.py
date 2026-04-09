"""
app.py — Panel de Control Principal
Galeria de Arte Digital — Modulo 7, Streamlit

Este es el entrypoint de la aplicacion multipagina.
Muestra las metricas clave del negocio en un dashboard ejecutivo.
"""

import streamlit as st
import pathlib
import sys

# --- Configuracion de pagina ---
st.set_page_config(
    page_title="Galeria de Arte Digital",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Funcion auxiliar: cargar CSS externo
# ---------------------------------------------------------------------------

def cargar_css(path: pathlib.Path) -> None:
    """Lee un archivo CSS y lo inyecta en la aplicacion."""
    if path.exists():
        with open(path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Ruta absoluta al CSS (relativa a este archivo)
_BASE = pathlib.Path(__file__).parent
cargar_css(_BASE / "utils" / "estilos.css")

# Asegurar que el paquete utils sea importable
sys.path.insert(0, str(_BASE))

# ---------------------------------------------------------------------------
# Importaciones de datos
# ---------------------------------------------------------------------------

from utils.data_sim import METRICAS  # noqa: E402

# ---------------------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown(
        '<div class="titulo-pagina" style="font-size:1.3rem;">Galeria de Arte Digital</div>',
        unsafe_allow_html=True,
    )
    st.markdown("Navega entre las secciones del menu para explorar la aplicacion.")
    st.markdown("---")
    st.caption("Modulo 7 — Streamlit Avanzado")

# ---------------------------------------------------------------------------
# Contenido principal
# ---------------------------------------------------------------------------

st.markdown('<div class="titulo-pagina">Panel de Control</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="alerta-info">Bienvenido al sistema de gestion de la galeria. '
    'Los indicadores a continuacion reflejan el estado operativo del presente mes.</div>',
    unsafe_allow_html=True,
)

# --- Metricas en columnas ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Obras Registradas",
        value=f"{METRICAS['obras_registradas']['valor']:,}",
        delta=METRICAS["obras_registradas"]["delta"],
    )
with col2:
    st.metric(
        label="Artistas Activos",
        value=f"{METRICAS['artistas_activos']['valor']:,}",
        delta=METRICAS["artistas_activos"]["delta"],
    )
with col3:
    st.metric(
        label="Ventas del Mes (USD)",
        value=f"${METRICAS['ventas_mes_usd']['valor']:,}",
        delta=METRICAS["ventas_mes_usd"]["delta"],
    )
with col4:
    st.metric(
        label="Visitantes Web",
        value=f"{METRICAS['visitantes_web']['valor']:,}",
        delta=METRICAS["visitantes_web"]["delta"],
    )

st.markdown("---")

# --- Resumen en contenedor ---
with st.container():
    st.subheader("Acerca de esta aplicacion")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown(
            """
            Esta aplicacion multipagina integra las tecnicas cubiertas en los Modulos 1 al 6
            del manual de Streamlit:

            - **Galeria Interactiva** — Pestanas (`st.tabs`), tarjetas HTML/CSS personalizadas y filtro por slider.
            - **Registro de Obras** — Formulario robusto con `st.form` que agrupa los controles y evita
              re-ejecuciones prematuras.
            - **Analisis de Carga** — Demostracion de `@st.cache_data` y `st.spinner` para manejar
              operaciones costosas de manera eficiente.
            """
        )
    with col_b:
        st.markdown(
            '<div class="my-card">'
            "<h3>Tecnologias</h3>"
            "<p>Python 3.10+</p>"
            "<p>Streamlit 1.34+</p>"
            "<p>Pandas / NumPy</p>"
            "<p>CSS personalizado</p>"
            "</div>",
            unsafe_allow_html=True,
        )
