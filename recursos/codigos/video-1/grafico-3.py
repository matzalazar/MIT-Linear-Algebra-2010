import plotly.graph_objects as go

# Definir los vectores
A_col1 = [2, -1]  # Primera columna de la matriz
A_col2 = [-1, 2]  # Segunda columna de la matriz
b = [0, 3]        # Vector resultado

# Punto intermedio
intermediate = [1, 1]

# Crear la figura
fig = go.Figure()

# Agregar los vectores columna
fig.add_trace(go.Scatter(
    x=[0, A_col1[0]], y=[0, A_col1[1]],
    mode='lines+markers',
    marker=dict(size=6),
    line=dict(width=2, color='blue'),
    name='x * [2, -1]'
))

fig.add_trace(go.Scatter(
    x=[0, A_col2[0]], y=[0, A_col2[1]],
    mode='lines+markers',
    marker=dict(size=6),
    line=dict(width=2, color='green'),
    name='y * [-1, 2]'
))

# Agregar el vector b
fig.add_trace(go.Scatter(
    x=[0, b[0]], y=[0, b[1]],
    mode='lines+markers',
    marker=dict(size=6),
    line=dict(width=2, color='red'),
    name='b = [0, 3]'
))

# Agregar el vector punteado desde el extremo de x hasta b, pasando por un punto intermedio
fig.add_trace(go.Scatter(
    x=[A_col1[0], intermediate[0], b[0]],  # Puntos: extremo de x, intermedio, extremo de b
    y=[A_col1[1], intermediate[1], b[1]],
    mode='lines+markers',
    marker=dict(size=6, symbol='circle'),
    line=dict(width=2, color='purple', dash='dot'),  # Línea punteada
    name='Combinación lineal (punteada)'
))

# Configurar el diseño
fig.update_layout(
    title="Representación de vectores con trayectoria combinada",
    xaxis=dict(title="x", zeroline=True, range=[-3, 3]),
    yaxis=dict(title="y", zeroline=True, range=[-3, 3]),
    showlegend=True,
    width=600,
    height=600
)

# Mostrar la figura
fig.show()
