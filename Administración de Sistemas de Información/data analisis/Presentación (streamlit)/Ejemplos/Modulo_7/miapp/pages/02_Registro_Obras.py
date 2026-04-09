"""
pages/02_Registro_Obras.py
Galeria de Arte Digital — Modulo 7, Streamlit

Pagina 2: Registro de Obras
Demuestra el uso de st.form para agrupar controles y evitar re-ejecuciones prematuras.
"""

import pathlib
import sys
from datetime import date
import streamlit as st

# --- Configuracion de pagina ---
st.set_page_config(page_title="Registro de Obras", layout="wide")

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

from utils.data_sim import ESTILOS_ARTE, TECNICAS  # noqa: E402

# ---------------------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown(
        '<div class="titulo-pagina" style="font-size:1.3rem;">Galeria de Arte Digital</div>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.caption("Pagina 2 de 3")

# ---------------------------------------------------------------------------
# Cabecera
# ---------------------------------------------------------------------------

st.markdown('<div class="titulo-pagina">Registro de Obras</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="alerta-info">Complete todos los campos y presione <strong>Registrar Obra</strong>. '
    'El formulario procesa los datos en bloque para evitar actualizaciones parciales.</div>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Formulario con st.form
# ---------------------------------------------------------------------------

with st.form(key="registro_obra", clear_on_submit=True):
    st.subheader("Datos de la obra")

    col1, col2 = st.columns(2)

    with col1:
        titulo = st.text_input(
            "Titulo de la obra",
            placeholder="Ej.: Nocturno en Indigo",
            max_chars=120,
        )
        artista = st.text_input(
            "Nombre del artista",
            placeholder="Ej.: Carmen Rios",
            max_chars=80,
        )
        estilo = st.selectbox("Estilo artistico", options=ESTILOS_ARTE)

    with col2:
        tecnica = st.selectbox("Tecnica utilizada", options=TECNICAS)
        fecha_creacion = st.date_input(
            "Fecha de creacion",
            value=date.today(),
            min_value=date(1900, 1, 1),
            max_value=date.today(),
        )
        valor_usd = st.number_input(
            "Valor estimado (USD)",
            min_value=0,
            max_value=10_000_000,
            step=100,
            value=1_000,
        )

    st.subheader("Descripcion")
    descripcion = st.text_area(
        "Breve descripcion de la obra (opcional)",
        placeholder="Contexto historico, inspiracion, materiales adicionales...",
        max_chars=500,
        height=110,
    )

    enviado = st.form_submit_button("Registrar Obra")

# ---------------------------------------------------------------------------
# Procesamiento del formulario (fuera del bloque with st.form)
# ---------------------------------------------------------------------------

if enviado:
    # Validacion basica
    errores = []
    if not titulo.strip():
        errores.append("El titulo de la obra no puede estar vacio.")
    if not artista.strip():
        errores.append("El nombre del artista no puede estar vacio.")

    if errores:
        for err in errores:
            st.error(err)
    else:
        # Resumen del registro simulado
        st.success(
            f"La obra '{titulo.strip()}' de {artista.strip()} ha sido registrada correctamente."
        )
        with st.container():
            st.subheader("Resumen del registro")
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(
                    f'<div class="my-card">'
                    f"<h3>{titulo.strip()}</h3>"
                    f"<p><strong>Artista:</strong> {artista.strip()}</p>"
                    f"<p><strong>Estilo:</strong> {estilo}</p>"
                    f"<p><strong>Tecnica:</strong> {tecnica}</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
            with col_b:
                st.markdown(
                    f'<div class="my-card">'
                    f"<h3>Datos adicionales</h3>"
                    f"<p><strong>Fecha de creacion:</strong> {fecha_creacion.strftime('%d/%m/%Y')}</p>"
                    f"<p><strong>Valor estimado:</strong> ${valor_usd:,} USD</p>"
                    f"<p><strong>Descripcion:</strong> {descripcion.strip() or 'No proporcionada'}</p>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
