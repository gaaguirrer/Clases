# ========================================
# GALERÍA DE ARTE DIGITAL - VERSIÓN 2
# Con Navegación y Layouts
# ========================================

import streamlit as st

# ===== CONFIGURACIÓN DE LA PÁGINA =====
st.set_page_config(page_title='Galería de Arte Digital', layout='wide')

# ===== INICIALIZAR SESSION STATE =====
# Mantener el estado de la página actual entre rerenderizados
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Inicio'

# ===== SIDEBAR - MENÚ DE NAVEGACIÓN =====
st.sidebar.title('Galería de Arte Digital')
st.sidebar.write('Menú de Navegación')
st.sidebar.divider()

# Botones de navegación en el sidebar
if st.sidebar.button('Inicio', use_container_width=True):
    st.session_state.pagina = 'Inicio'

if st.sidebar.button('Galería', use_container_width=True):
    st.session_state.pagina = 'Galería'

if st.sidebar.button('Sobre Nosotros', use_container_width=True):
    st.session_state.pagina = 'Sobre Nosotros'

st.sidebar.divider()
st.sidebar.text('Navegación activa')
st.sidebar.info(f'Página actual: {st.session_state.pagina}')

# ===== CONTENIDO SEGÚN LA PÁGINA SELECCIONADA =====

if st.session_state.pagina == 'Inicio':
    # PÁGINA DE INICIO
    st.title('Bienvenido a la Galería de Arte Digital')
    st.header('Explora nuestra colección exclusiva')
    
    # Descripción en columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Nuestra Misión')
        st.write("""
        Promover el arte digital contemporáneo y conectar artistas
        emergentes con amantes del arte en todo el mundo.
        """)
        
    with col2:
        st.subheader('Lo Que Ofrecemos')
        st.write('- Colección curada de arte digital')
        st.write('- Artistas de todo el mundo')
        st.write('- Alta calidad en cada pieza')
        st.write('- Actualizaciones constantes')
    
    st.divider()
    
    # Obra destacada
    st.subheader('Obra Destacada')
    st.image(
        'https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=800',
        caption='Arte Digital Abstracto - Autor Desconocido',
        use_container_width=True
    )

elif st.session_state.pagina == 'Galería':
    # PÁGINA DE GALERÍA
    st.title('Nuestra Colección de Arte')
    
    # Tabs para categorías de arte
    tab1, tab2, tab3 = st.tabs(['Arte Abstracto', 'Arte Moderno', 'Arte Digital'])
    
    with tab1:
        st.subheader('Colección: Arte Abstracto')
        
        # Mostrar obras en un grid de 3 columnas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image('https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=400')
            with st.expander('Ver detalles'):
                st.write('**Título:** Explosión de Color')
                st.write('**Artista:** Desconocido')
                st.write('**Año:** 2023')
                
        with col2:
            st.image('https://images.unsplash.com/photo-1541961017774-22349e4a1262?w=400')
            with st.expander('Ver detalles'):
                st.write('**Título:** Formas en Movimiento')
                st.write('**Artista:** Artista Moderno')
                st.write('**Año:** 2022')
                
        with col3:
            st.image('https://images.unsplash.com/photo-1549887534-1541e9326642?w=400')
            with st.expander('Ver detalles'):
                st.write('**Título:** Geometría Digital')
                st.write('**Artista:** Creador Digital')
                st.write('**Año:** 2024')
    
    with tab2:
        st.subheader('Colección: Arte Moderno')
        st.write('Obras del siglo XX y XXI')
        st.info('Colección en actualización...')
    
    with tab3:
        st.subheader('Colección: Arte Digital')
        st.write('Creaciones completamente digitales')
        st.info('Próximamente más obras...')

elif st.session_state.pagina == 'Sobre Nosotros':
    # PÁGINA SOBRE NOSOTROS
    st.title('Sobre Nuestra Galería')
    
    # Información en expanders
    with st.expander('Historia', expanded=True):
        st.write("""
        Fundada en 2024, nuestra galería nació con la misión de democratizar
        el acceso al arte digital y promover artistas emergentes.
        """)
    
    with st.expander('Equipo'):
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Director:** John Doe')
            st.write('**Curadora:** Jane Smith')
        with col2:
            st.write('**Técnico:** Bob Johnson')
            st.write('**Comunicaciones:** Alice Williams')
    
    with st.expander('Contacto'):
        st.write('Email: contacto@galeria.com')
        st.write('Teléfono: +1 234 567 8900')
        st.write('Dirección: 123 Arte Street, Ciudad')

# ===== PIE DE PÁGINA =====
st.divider()
st.text('Galería de Arte Digital - 2024')
st.text('Creado con Streamlit')
