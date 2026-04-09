# ========================================
# GALERÍA DE ARTE DIGITAL - VERSIÓN 1
# Landing Page Simple
# ========================================

import streamlit as st

# ===== ENCABEZADO PRINCIPAL =====
# Título principal de nuestra galería
st.title(' Galería de Arte Digital')

# Subtítulo con descripción
st.header('Explora el Arte Contemporáneo')

# ===== SECCIÓN DE BIENVENIDA =====
# Usamos markdown para crear contenido con formato rico
st.markdown("""
Bienvenido a nuestra colección exclusiva de arte digital. Aquí encontrarás:

-  **Obras únicas** de artistas emergentes
-  **Variedad de estilos** desde abstracto hasta realismo
-  **Alta calidad** en cada pieza
-  **Artistas internacionales** de todos los continentes
""")

# Separador visual
st.divider()

# ===== OBRA DESTACADA =====
st.subheader('Obra Destacada del Día')

# Mostramos una imagen destacada
st.image(
    'https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?w=800',
    caption='"Explosión de Color" - Arte Digital Abstracto por Artista Moderno',
    use_container_width=True  # La imagen ocupará todo el ancho disponible
)

# Descripción de la obra
st.write("""
Esta pieza representa la fusión de colores y formas en el arte digital moderno. 
Creada completamente con herramientas digitales, es un ejemplo perfecto de cómo 
la tecnología expande las fronteras del arte.
""")

# Separador
st.divider()

# ===== INFORMACIÓN ADICIONAL =====
st.subheader('¿Sabías que?')

# Cita inspiradora
st.markdown("""
> "El arte digital no reemplaza al arte tradicional, lo complementa y expande 
> las posibilidades creativas de los artistas."

*- Experto en Arte Digital*
""")

# ===== PIE DE PÁGINA =====
st.divider()

# Información de contacto y créditos
st.text('Galería de Arte Digital © 2024')
st.text('Creado con Streamlit')
