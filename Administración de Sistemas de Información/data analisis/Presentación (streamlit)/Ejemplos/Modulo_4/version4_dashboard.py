# ========================================
# GALERÍA DE ARTE DIGITAL - VERSIÓN 4
# Dashboard Analítico
# ========================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='Dashboard Galería', layout='wide')
st.title('Panel de Control Analítico')
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Visitas Totales", "25,000", "5,000", delta_color="normal")
col2.metric("Nuevos Usuarios", "1,200", "50", delta_color="normal")
col3.metric("Obras Vendidas", "45", "-2", delta_color="inverse")
col4.metric("Ingresos", "$24,500", "$1,400", delta_color="normal")
st.divider()

dias = pd.date_range(start="2024-01-01", periods=30)
datos_ventas = pd.DataFrame({
    'Fecha': dias,
    'Abstracto': np.random.randint(5, 50, size=30),
    'Digital': np.random.randint(10, 80, size=30),
}).set_index('Fecha')

col_izq, col_der = st.columns([2, 1])
with col_izq:
    st.subheader('Ventas últimos 30 días')
    st.line_chart(datos_ventas)

    # Plotly Interactivo extraído de la teoría
    st.subheader("Gráfico Interactivo (Plotly)")
    df_arte = pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
        'Ventas Abstracto': [12, 19, 15, 25, 22],
        'Ventas Clásico': [5, 8, 4, 10, 15]
    })
    fig = px.bar(
        df_arte, 
        x='Mes', 
        y=['Ventas Abstracto', 'Ventas Clásico'],
        title="Comparativa de Ventas por Lote",
        barmode='group',
        color_discrete_sequence=['#1E88E5', '#FFD166']
    )
    st.plotly_chart(fig, use_container_width=True)

with col_der:
    st.subheader('Inventario')
    inventario = pd.DataFrame({
        'Categoría': ['Abstracto', 'Digital', 'Moderno', 'Clásico'],
        'Stock Real': [120, 200, 45, 12]
    })
    # Tablas interactivas vs Estáticas
    st.write("Explorador de Datos:")
    st.dataframe(inventario, use_container_width=True, hide_index=True)
