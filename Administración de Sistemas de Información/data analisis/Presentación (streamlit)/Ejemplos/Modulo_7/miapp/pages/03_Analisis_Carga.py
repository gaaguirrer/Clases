"""
pages/03_Analisis_Carga.py
Galeria de Arte Digital — Modulo 7, Streamlit

Pagina 3: Analisis y Gestion de Carga
Demuestra @st.cache_data, st.spinner y visualizaciones con st.bar_chart / st.line_chart.
"""

import pathlib
import sys
import streamlit as st

# --- Configuracion de pagina ---
st.set_page_config(page_title="Analisis de Carga", layout="wide")

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

from utils.data_sim import cargar_datos_analisis  # noqa: E402

# ---------------------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown(
        '<div class="titulo-pagina" style="font-size:1.3rem;">Galeria de Arte Digital</div>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.caption("Pagina 3 de 3")

# ---------------------------------------------------------------------------
# Funcion con cache (envuelta aqui para que Streamlit la registre correctamente)
# ---------------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def obtener_datos_anuales() -> "pd.DataFrame":  # type: ignore[name-defined]  # noqa:F821
    """
    Llama a la funcion costosa de data_sim y almacena el resultado en cache.
    La segunda llamada (y posteriores) devuelve el resultado instantaneamente.
    """
    return cargar_datos_analisis(seed=42)

# ---------------------------------------------------------------------------
# Cabecera
# ---------------------------------------------------------------------------

st.markdown('<div class="titulo-pagina">Analisis de Rendimiento y Carga</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="alerta-info">Esta pagina ilustra el uso de <strong>@st.cache_data</strong> '
    'y <strong>st.spinner</strong>. La primera carga tarda ~2.5 segundos para simular una '
    'consulta costosa; las recargas posteriores son instantaneas.</div>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Carga de datos con spinner
# ---------------------------------------------------------------------------

with st.spinner("Consultando la base de datos anual... Por favor espere."):
    df = obtener_datos_anuales()

st.success("Datos cargados correctamente. (Las recargas subsiguientes son instantaneas gracias al cache.)")

st.markdown("---")

# ---------------------------------------------------------------------------
# Visualizaciones
# ---------------------------------------------------------------------------

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Ventas mensuales (USD)")
    st.bar_chart(df.set_index("Mes")["Ventas_USD"], use_container_width=True, height=280)

with col2:
    st.subheader("Visitantes web por mes")
    st.line_chart(df.set_index("Mes")["Visitantes_Web"], use_container_width=True, height=280)

st.markdown("---")

# --- Tabla de datos completa ---
with st.expander("Ver tabla de datos completa"):
    st.dataframe(
        df.rename(columns={
            "Ventas_USD": "Ventas (USD)",
            "Obras_Registradas": "Obras registradas",
            "Visitantes_Web": "Visitantes web",
        }),
        use_container_width=True,
        hide_index=True,
    )

# --- Metricas derivadas ---
st.markdown("---")
st.subheader("Resumen anual")

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric("Total ventas anuales", f"${df['Ventas_USD'].sum():,.0f} USD")
with col_b:
    st.metric("Total obras registradas", f"{df['Obras_Registradas'].sum():,}")
with col_c:
    st.metric("Total visitantes web", f"{df['Visitantes_Web'].sum():,}")

# ---------------------------------------------------------------------------
# Panel explicativo de st.cache_data
# ---------------------------------------------------------------------------

st.markdown("---")
st.subheader("Como funciona el cache en esta pagina")

st.markdown(
    """
    El decorador `@st.cache_data` serializa el valor de retorno de la funcion
    y lo almacena en memoria (y opcionalmente en disco) indexado por los argumentos
    de entrada. Cuando Streamlit re-ejecuta el script (por cualquier interaccion del
    usuario), detecta que los argumentos no cambiaron y devuelve la copia almacenada
    sin volver a ejecutar la funcion.

    Ventajas principales:

    - Elimina latencia en operaciones costosas (SQL, APIs, procesamiento de archivos).
    - Permite compartir el resultado entre multiples usuarios en la misma sesion de servidor.
    - Se invalida automaticamente si los argumentos cambian o si el TTL configurado expira.

    En esta pagina, `obtener_datos_anuales()` envuelve a `cargar_datos_analisis(seed=42)`
    que incluye un `time.sleep(2.5)` artificial. Solo la primera visita o un recargo forzado
    (`Ctrl+Shift+R`) activara la pausa; el resto de interacciones son inmediatas.
    """
)
