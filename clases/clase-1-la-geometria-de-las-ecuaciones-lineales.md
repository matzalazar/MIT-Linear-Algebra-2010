# La geometría de las ecuaciones lineales.  

Problema fundamental del álgebra lineal: resolver sistema de ecuaciones lineales.

## Ejemplo con dos incógnitas.

Asumamos que tenemos un sistema lineal de $n$ ecuaciones con $n$ incógnitas. Es decir, la misma cantidad de ecuaciones que de incógnitas. 

### Presentación por filas.

$$
\begin{aligned}
2x - y &= 0 \\
-x + 2y &= 3
\end{aligned}
$$

Tomamos una ecuación a la vez y dibujamos las rectas que representan en un sistema de ejes cartesianos.

![Gráfico del sistema de ecuaciones](/recursos/imagenes/video-1/grafico-1.png)

(El código utilizando la librería `plotly` se puede descargar [acá](/recursos/codigo/video-1/grafico-1.py)).

La intersección de las rectas es la resolución del sistema. $x=1, y=2$. Satisface ambas ecuaciones.

### Presentación por columnas.

Esta presentación opera con vectores para obtener el mismo resultado. Veamos cómo:

$$
x
\begin{bmatrix}
2 \\
-1
\end{bmatrix} +
y
\begin{bmatrix}
-1 \\
2
\end{bmatrix} =
\begin{bmatrix}
0 \\
3
\end{bmatrix}
$$

Cada una de las columnas podemos pensarla como vectores.

![Gráfico del sistema como vectores](/recursos/imagenes/video-1/grafico-2.png)

(El código utilizando la librería `plotly` se puede descargar [acá](/recursos/codigo/video-1/grafico-2.py)).

Necesitamos encontrar la **combinación lineal** de términos $x$ e $y$ que me permitan obtener el vector resultado. 

![Gráfico del sistema como combinación vectorial](/recursos/imagenes/video-1/grafico-3.png)

(El código utilizando la librería `plotly` se puede descargar [acá](/recursos/codigo/video-1/grafico-3.py)).

Notemos que llegamos al resultado $b$ mediante la suma de vectores. El punto $(1, 1)$ señala la primera suma del vector $y$ al vector $x$, pero debemos sumarle dos veces $y$. De ese modo, llegamos a $b$, con extremo en el punto $(0, 3)$.

$$
1
\begin{bmatrix}
2 \\
-1
\end{bmatrix} +
2
\begin{bmatrix}
-1 \\
2
\end{bmatrix} =
\begin{bmatrix}
0 \\
3
\end{bmatrix}
$$

### Matriz.

Podemos rápidamente identificar la matriz de coeficientes $A$.

$$
A =
\begin{bmatrix}
2 & -1 \\
-1 & 2
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
0 \\
3
\end{bmatrix}
$$

De modo que llegamos a la forma:

$A * \mathbf{x} = b$, donde $\mathbf{x}$ y $b$ son vectores.

## Ejemplo con tres incógnitas.

$$
\begin{aligned}
  2x &- y     &&= 0 \\
 -x  &+ 2y - z &&= -1 \\
     &- 3y + 4z &&= 4
\end{aligned}
$$

### Forma matricial.

$$
A =
\begin{bmatrix}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -3 & 4 \\
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} =
\begin{bmatrix}
0 \\
-1 \\
4
\end{bmatrix}
$$

![Gráfico del sistema como tres planos](/recursos/imagenes/video-1/grafico-4.png)

(El código utilizando la librería `plotly` se puede descargar [acá](/recursos/codigo/video-1/grafico-4.py))

_Nota_: Si tuviéramos sólo dos ecuaciones en un espacio de tres dimensiones, la solución será una recta. La recta en la que ambos planos se interceptan. Con tres planos, si los parámetros lo permiten, los tres planos se interceptarán en un punto.

### Presentación por columnas.

$$
x
\begin{bmatrix}
2 \\
-1 \\
0
\end{bmatrix} +
y
\begin{bmatrix}
-1 \\
2 \\
-3
\end{bmatrix} +
z
\begin{bmatrix}
0 \\
-1 \\
4
\end{bmatrix} =
\begin{bmatrix}
0 \\
-1 \\
4
\end{bmatrix}
$$

Del lado izquierdo tenemos una **combinación lineal** de tres vectores. Cada uno de los vectores es tridimensional. ¿Qué combinación de los tres vectores produce $b$?

De este modo, la solución surge a la vista: el vector asociado a $z$ es igual a $b$; de modo que $x=0, y=0$ y la solución será: $(0, 0, 1)$.

**Cambiemos el $b$**.

$$
x
\begin{bmatrix}
2 \\
-1 \\
0
\end{bmatrix} +
y
\begin{bmatrix}
-1 \\
2 \\
-3
\end{bmatrix} +
z
\begin{bmatrix}
0 \\
-1 \\
4
\end{bmatrix} =
\begin{bmatrix}
1 \\
1 \\
-3
\end{bmatrix}
$$

Nuevamente, observamos que la única solución posible es $x=1, y=1, z=0$ en tanto:

para $x$: $1*(2)+1*(-1)+0=1$
para $y$: $1*(-1)+1*(2)+0=1$
para $z$: $1*(0)+1*(-3)+0=-3$

¿La combinación lineal de las columnas llenan el espacio tridimensional?

O, lo que es lo mismo:

**¿Podemos resolver cualquier $A\mathbf{x}=b$ para cualquier $b$?**

En el caso particular estudiado: sí. La matriz es no-singular, es invertible. 

**¿Cuándo la respuesta será no?**

Si las columnas están en el mismo plano, entonces sus combinaciones estarán en el mismo plano.

Estaremos entonces frente a un caso singular. La matriz no será invertible. 

## Multiplicación de una matriz por un vector.

Dada la forma:

$A\mathbf{x}=b$

Siendo $A$ una matriz y $\mathbf{x}$ un vector. ¿Cómo se multiplican? Hay dos formas de hacerlo.

**1) Por columnas.**

$$
\begin{bmatrix}
2 & 5 \\
1 & 3
\end{bmatrix}
\begin{bmatrix}
1 \\
2 
\end{bmatrix} =
1
\begin{bmatrix}
2 \\
1
\end{bmatrix} +
2
\begin{bmatrix}
5 \\
3 
\end{bmatrix} =
\begin{bmatrix}
2 \\
1
\end{bmatrix} +
\begin{bmatrix}
10 \\
6 
\end{bmatrix} =
\begin{bmatrix}
12 \\
7
\end{bmatrix} 
$$

**2. Por filas.**

$$
\begin{bmatrix}
2 & 5 \\
1 & 3
\end{bmatrix}
\begin{bmatrix}
1 \\
2 
\end{bmatrix} =
\begin{bmatrix}
(2 * 1)+(5 * 2) \\
(1 * 1)+(3 * 2) 
\end{bmatrix} =
\begin{bmatrix}
12 \\
7
\end{bmatrix} 
$$
