"""
pages/01_Galeria_Interactiva.py
Galeria de Arte Digital — Modulo 7, Streamlit

Pagina 1: Galeria Interactiva
Demuestra el uso de st.tabs, st.slider, columnas y tarjetas HTML/CSS personalizadas.
"""

import pathlib
import sys
import streamlit as st

# --- Configuracion de pagina ---
st.set_page_config(page_title="Galeria Interactiva", layout="wide")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_BASE = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(_BASE))

def _cargar_css() -> None:
    css_path = _BASE / "utils" / "estilos.css"
    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

_cargar_css()

from utils.data_sim import OBRAS  # noqa: E402

# ---------------------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown(
        '<div class="titulo-pagina" style="font-size:1.3rem;">Galeria de Arte Digital</div>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.caption("Pagina 1 de 3")

# ---------------------------------------------------------------------------
# Cabecera
# ---------------------------------------------------------------------------

st.markdown('<div class="titulo-pagina">Galeria Interactiva</div>', unsafe_allow_html=True)

# --- Slider de filtro por año ---
anio_min, anio_max = 2014, 2024
rango = st.slider(
    "Filtrar obras por rango de año de creacion",
    min_value=anio_min,
    max_value=anio_max,
    value=(2015, 2023),
    step=1,
)

st.markdown("---")

# ---------------------------------------------------------------------------
# Pestanas por estilo artistico
# ---------------------------------------------------------------------------

pestanas = st.tabs(list(OBRAS.keys()))

for tab, (estilo, lista_obras) in zip(pestanas, OBRAS.items()):
    with tab:
        obras_filtradas = [o for o in lista_obras if rango[0] <= o["anio"] <= rango[1]]

        if not obras_filtradas:
            st.markdown(
                '<div class="alerta-info">No hay obras registradas en el rango de años seleccionado.</div>',
                unsafe_allow_html=True,
            )
        else:
            # Mostrar tarjetas en columnas de 2
            pares = [obras_filtradas[i: i + 2] for i in range(0, len(obras_filtradas), 2)]
            for par in pares:
                cols = st.columns(2)
                for col, obra in zip(cols, par):
                    with col:
                        st.markdown(
                            f'<div class="my-card">'
                            f"<h3>{obra['titulo']}</h3>"
                            f"<p><strong>Artista:</strong> {obra['artista']}</p>"
                            f"<p><strong>Año:</strong> {obra['anio']}</p>"
                            f"<p><strong>Valor estimado:</strong> ${obra['valor_usd']:,} USD</p>"
                            f"</div>",
                            unsafe_allow_html=True,
                        )

        with st.expander("Acerca del estilo: " + estilo):
            descripciones = {
                "Abstraccionismo": (
                    "El abstraccionismo prescinde de la representacion literal de la realidad, "
                    "priorizando colores, formas y composiciones que evocan emociones directas."
                ),
                "Realismo Digital": (
                    "El realismo digital combina tecnicas clasicas de representacion fiel "
                    "con herramientas digitales de alta precision para capturar la vida cotidiana."
                ),
                "Arte Generativo": (
                    "El arte generativo utiliza algoritmos, sistemas autonomos y aleatoriedad "
                    "controlada para producir obras donde el codigo es el pincel del artista."
                ),
            }
            st.write(descripciones.get(estilo, "Descripcion no disponible."))
