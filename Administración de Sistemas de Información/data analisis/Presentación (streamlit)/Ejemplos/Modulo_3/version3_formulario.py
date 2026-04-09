# ========================================
# GALERÍA DE ARTE DIGITAL - VERSIÓN 3
# Formulario Interactivo
# ========================================

import streamlit as st

st.set_page_config(page_title='Agregar Obra', layout='centered')

st.title('Registro de Nueva Obra')
st.write('Completa el formulario para registrar tu arte en la galería.')

# Container para el formulario
form_container = st.container()

with form_container:
    col1, col2 = st.columns(2)
    
    with col1:
        titulo = st.text_input('Título de la obra', placeholder='Ej. La Noche Estrellada')
        estilo = st.selectbox('Estilo', ['Abstracto', 'Moderno', 'Clásico', 'Digital', 'Surrealista'])
        precio = st.number_input('Precio Estimado ($)', min_value=0.0, step=50.0)
    
    with col2:
        artista = st.text_input('Nombre del artista', placeholder='Tu nombre o seudónimo')
        fecha = st.date_input('Fecha de creación')
        color_base = st.color_picker('Color predominante', '#1E88E5')

    descripcion = st.text_area('Descripción detallada', height=100)
    
    # Términos y condiciones
    st.divider()
    acepta_terminos = st.checkbox('Confirmo que esta obra es original y tengo los derechos sobre ella.')
    
    # Botón de envío
    enviado = st.button('Registrar Obra', use_container_width=True)
    
    if enviado:
        if not acepta_terminos:
            st.error('Debes aceptar los términos y condiciones para continuar.')
        elif len(titulo) == 0 or len(artista) == 0:
            st.warning('El título y el nombre del artista son obligatorios.')
        else:
            st.success('Exito: La obra ha sido registrada correctamente.')
            
            # Mostrar resumen
            st.info('Resumen del registro:')
            st.write(f"**Título:** {titulo}")
            st.write(f"**Artista:** {artista}")
            st.write(f"**Estilo:** {estilo}")
            st.write(f"**Precio:** ${precio}")
