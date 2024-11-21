import numpy as np
import plotly.graph_objects as go

# Definir las ecuaciones
x = np.linspace(-5, 5, 500)  # Rango de valores de x

# Ecuación 1: 2x - y = 0 => y = 2x
y1 = 2 * x

# Ecuación 2: -x + 2y = 3 => y = (x + 3) / 2
y2 = (x + 3) / 2

# Crear la figura
fig = go.Figure()

# Agregar la primera recta
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='2x - y = 0'))

# Agregar la segunda recta
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='-x + 2y = 3'))

# Marcar un punto específico (ejemplo: (1, 2))
fig.add_trace(go.Scatter(
    x=[1], y=[2],  # Coordenadas del punto
    mode='markers+text',
    marker=dict(size=10, color='red'),  # Tamaño y color del marcador
    name='Punto (1, 2)',
    text=["(1, 2)"],  # Etiqueta del punto
    textposition="top center"  # Posición del texto
))

# Configurar el diseño del gráfico
fig.update_layout(
    title="Sistema de ecuaciones en el plano cartesiano",
    xaxis=dict(
        title="x",
        zeroline=True,
        showgrid=True,  # Mostrar cuadrícula en el eje x
        range=[-5, 5]
    ),
    yaxis=dict(
        title="y",
        zeroline=True,
        showgrid=True,  # Mostrar cuadrícula en el eje y
        range=[-5, 5]
    ),
    showlegend=True
)

# Mostrar la figura
fig.show()
