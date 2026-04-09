"""
Controlador para generación de gráficos y visualizaciones
Utiliza Plotly para crear gráficos interactivos
"""
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List
from utils.helpers import calculate_stat_total
from utils.constants import TYPE_COLORS


def crear_grafico_radar(pokemon: Dict) -> go.Figure:
    """
    Crea un gráfico radar de las estadísticas de un Pokémon
    
    Args:
        pokemon: Datos del Pokémon
        
    Returns:
        Figura de Plotly con el gráfico radar
    """
    stats = pokemon.get('stats', {})
    
    # Preparar datos
    categories = ['HP', 'Ataque', 'Defensa', 'At. Esp.', 'Def. Esp.', 'Velocidad']
    values = [
        stats.get('hp', 0),
        stats.get('ataque', 0),
        stats.get('defensa', 0),
        stats.get('ataque_especial', 0),
        stats.get('defensa_especial', 0),
        stats.get('velocidad', 0)
    ]
    
    # Crear gráfico
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=pokemon.get('nombre_es', pokemon.get('nombre', '')),
        line=dict(color='#4cc9f0', width=2),
        fillcolor='rgba(76, 201, 240, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 255],
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='white', size=10)
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.1)',
                tickfont=dict(color='white', size=12)
            ),
            bgcolor='rgba(0, 0, 0, 0.1)'
        ),
        showlegend=False,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(color='white'),
        margin=dict(l=40, r=40, t=40, b=40),
        height=350
    )
    
    return fig


def create_comparison_chart(pokemon_list: List[Dict]) -> go.Figure:
    """
    Crea un gráfico de barras comparativo para múltiples Pokémon
    
    Args:
        pokemon_list: Lista de Pokémon a comparar (máx 3)
        
    Returns:
        Figura de Plotly con el gráfico comparativo
    """
    if not pokemon_list:
        return go.Figure()
    
    stats_names = ['HP', 'Ataque', 'Defensa', 'At. Esp.', 'Def. Esp.', 'Velocidad']
    stats_keys = ['hp', 'ataque', 'defensa', 'ataque_especial', 'defensa_especial', 'velocidad']
    
    fig = go.Figure()
    
    colors = ['#4cc9f0', '#f72585', '#7209b7']
    
    for idx, pokemon in enumerate(pokemon_list[:3]):
        stats = pokemon.get('stats', {})
        values = [stats.get(key, 0) for key in stats_keys]
        
        fig.add_trace(go.Bar(
            name=pokemon.get('nombre_es', pokemon.get('nombre', '')),
            x=stats_names,
            y=values,
            marker=dict(color=colors[idx % len(colors)]),
            text=values,
            textposition='auto',
            textfont=dict(color='white', size=11)
        ))
    
    fig.update_layout(
        barmode='group',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0.1)',
        font=dict(color='white'),
        xaxis=dict(
            gridcolor='rgba(255, 255, 255, 0.1)',
            title='Estadística',
            titlefont=dict(size=14)
        ),
        yaxis=dict(
            gridcolor='rgba(255, 255, 255, 0.1)',
            range=[0, 255],
            title='Valor Base',
            titlefont=dict(size=14)
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(0, 0, 0, 0.3)'
        ),
        margin=dict(l=40, r=40, t=80, b=40),
        height=400
    )
    
    return fig


def create_stats_bar_chart(pokemon: Dict) -> go.Figure:
    """
    Crea un gráfico de barras simple para estadísticas de un Pokémon
    
    Args:
        pokemon: Datos del Pokémon
        
    Returns:
        Figura de Plotly con el gráfico de barras
    """
    stats = pokemon.get('stats', {})
    
    stats_names = ['HP', 'Ataque', 'Defensa', 'At. Esp.', 'Def. Esp.', 'Velocidad']
    stats_keys = ['hp', 'ataque', 'defensa', 'ataque_especial', 'defensa_especial', 'velocidad']
    values = [stats.get(key, 0) for key in stats_keys]
    
    # Colores gradientes
    colors = ['#4cc9f0', '#4895ef', '#4361ee', '#3f37c9', '#4895ef', '#f72585']
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=stats_names,
        y=values,
        marker=dict(
            color=colors,
            line=dict(color='white', width=1)
        ),
        text=values,
        textposition='outside',
        textfont=dict(color='white', size=12)
    ))
    
    total = calculate_stat_total(stats)
    
    fig.update_layout(
        title=dict(
            text=f'Total: {total}',
            x=0.5,
            xanchor='center',
            font=dict(size=16, color='#4cc9f0')
        ),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0.1)',
        font=dict(color='white'),
        xaxis=dict(
            showgrid=False,
            title='Estadística'
        ),
        yaxis=dict(
            gridcolor='rgba(255, 255, 255, 0.1)',
            range=[0, max(values) + 20],
            title='Valor Base'
        ),
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40),
        height=350
    )
    
    return fig


def create_type_distribution_chart(pokemon_list: List[Dict]) -> go.Figure:
    """
    Crea un gráfico de distribución de tipos
    
    Args:
        pokemon_list: Lista de Pokémon para analizar
        
    Returns:
        Figura de Plotly con gráfico de pie
    """
    if not pokemon_list:
        return go.Figure()
    
    # Contar tipos
    type_count = {}
    for pokemon in pokemon_list:
        for tipo in pokemon.get('tipos', []):
            type_count[tipo] = type_count.get(tipo, 0) + 1
    
    # Ordenar por frecuencia
    sorted_types = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
    
    tipos = [t[0] for t in sorted_types]
    counts = [t[1] for t in sorted_types]
    colors = [TYPE_COLORS.get(t, '#777777') for t in tipos]
    
    fig = go.Figure()
    
    fig.add_trace(go.Pie(
        labels=[t.title() for t in tipos],
        values=counts,
        marker=dict(colors=colors, line=dict(color='white', width=2)),
        textfont=dict(size=12, color='white'),
        hole=0.3
    ))
    
    fig.update_layout(
        title=dict(
            text='Distribución de Tipos',
            x=0.5,
            xanchor='center',
            font=dict(size=16, color='white')
        ),
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05,
            bgcolor='rgba(0, 0, 0, 0.3)'
        ),
        margin=dict(l=20, r=20, t=60, b=20),
        height=400
    )
    
    return fig
