# Ejercicio 2:


# Crear matriz 3x3 con numpy


import numpy as np


A = np.array([
            [2, 1, 3],
            [1, 0, 2],
            [4, 1, 8]
            ])


print( "Matriz A: ")
print(A)


# Calcular determinante con scipy


from scipy.linalg import det


detA = det(A)


print("Determinante: ")
print(detA)
   
# Derivar función dada con SymPy


import sympy as sp


x = sp.symbols( "x")  # declaramos la variable
f = x**2 + 3*x + 2    # función definida
df = sp.diff(f, x)    # derivada respecto de x


print("f(x) = ", f)
print("f´(x) = ", df)
