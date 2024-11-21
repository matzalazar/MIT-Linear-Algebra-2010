import numpy as np
import plotly.graph_objects as go

# Definir los planos
def plano1(x, y):
    return 2 * x - y

def plano2(x, y):
    return x - 2 * y - 1

def plano3(x, y):
    return (3 * y + 4) / 4

# Definir el espacio
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Calcular el valor de z para cada plano
z1 = plano1(x, y)
z2 = plano2(x, y)
z3 = plano3(x, y)

# Crear la figura
fig = go.Figure()

fig.add_trace(go.Surface(z=z1, x=x, y=y, opacity=0.8, colorscale='Blues', name='Plane 1'))
fig.add_trace(go.Surface(z=z2, x=x, y=y, opacity=0.8, colorscale='Reds', name='Plane 2'))
fig.add_trace(go.Surface(z=z3, x=x, y=y, opacity=0.8, colorscale='Greens', name='Plane 3'))

# Configurar el diseño
fig.update_layout(
    title="Intersección de planos",
    scene=dict(
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        zaxis_title="Z-axis"
    ),
    showlegend=True
)

# Guardar la figura como imagen
fig.write_image("grafico-4.png")

# Mostrar la figura
fig.show()
