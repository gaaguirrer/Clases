# ========================================
# EJEMPLO MÓDULO 6: COMPONENTES AVANZADOS
# CONTROL DE FLUJO Y BATCH FORMULARIOS
# ========================================

import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title='Flujo Avanzado', layout='centered')

st.title("Formularios y Caché")
st.write("Explora el control del re-renderizado automático.")

# --- 1. Formularios (Batch Update) ---
st.header("1. Formularios por Lotes (st.form)")

# Inicializamos una variable de estado para guardar nuestros registros
if 'inventario' not in st.session_state:
    st.session_state.inventario = []

# IMPORTANTE: st.form congela el script hasta presionar Form Submit
with st.form(key='registro_avanzado', clear_on_submit=True):
    st.write("Ingresa los datos del nuevo producto:")
    cod_producto = st.text_input("Código SKU")
    descripcion = st.text_area("Descripción Comercial", help="Evitar detalles logísticos")
    
    col1, col2 = st.columns(2)
    with col1:
        categoria = st.selectbox("Categoría", ["Electrónica", "Materiales", "Servicios"])
    with col2:
        stock_minimo = st.number_input("Stock Mínimo Alerta", min_value=1)
        
    # Este es el único botón que puede vivir dentro de un st.form
    submit = st.form_submit_button("Sincronizar Producto")

if submit:
    if len(cod_producto) == 0:
        st.error("Es obligatorio adjuntar un SKU")
    else:
        # Guardamos en Session State
        st.session_state.inventario.append({
            "SKU": cod_producto,
            "Cat": categoria,
            "Stock": stock_minimo
        })
        st.success(f"Producto '{cod_producto}' sincronizado exitosamente.")

st.write("Inventario en Memoria Volátil:")
st.dataframe(pd.DataFrame(st.session_state.inventario))

st.divider()

# --- 2. Caché y Tiempos de Carga ---
st.header("2. Optimización con @st.cache_data")

# Función simulada costosa (Ej. Cargar archivo S3 o Query SQL)
@st.cache_data
def generar_reporte_complejo(anio):
    # Sin el decorador cache_data, cada que oprimas otro botón de la app,
    # el motor de Streamlit tendría que esperar estos 3 segundos extra
    time.sleep(3) 
    return pd.DataFrame({
        "Mes": ["Ene", "Feb", "Mar", "Abr"], 
        "Cierre": [100.5, 150.2, 130.4, 210.9]
    })

if st.button("Ejecutar Consulta Financiera Lenta"):
    with st.spinner('Procesando millones de filas simuladas en el servidor...'):
        df_resultado = generar_reporte_complejo(2024)
        
    st.success("Reporte generado (o extraído inmediatamente de caché).")
    st.line_chart(df_resultado.set_index('Mes'))
    st.info("Presiona el botón de nuevo. Notarás que el retraso de 3 segundos desaparece gracias a la caché.")
