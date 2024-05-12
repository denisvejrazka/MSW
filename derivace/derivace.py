import numpy as np
from scipy.misc import derivative
import sympy as sp

def f(x):
    return 3*x**2 - 2*x + 1

def adaptive_derivative(f, x, h=1e-5, tol=1e-6):
    dx = h
    prev_derivative = (f(x + dx) - f(x - dx)) / (2*dx)
    while True:
        dx /= 2
        current_derivative = (f(x + dx) - f(x - dx)) / (2*dx)
        if np.abs(current_derivative - prev_derivative) < tol:
            return current_derivative
        prev_derivative = current_derivative

# Derivace se statickým krokem
def static_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)

# Analytický výpočet derivace pomocí knihovny Simpy
x_sym = sp.Symbol('x')
f_sym = 3*x_sym**2 - 2*x_sym + 1
f_prime_sym = sp.diff(f_sym, x_sym)

# Definice bodu vyhodnocení derivace
x_value = 2.0

analytical_derivative = f_prime_sym.evalf(subs={x_sym: x_value})
numerical_adaptive_derivative = adaptive_derivative(f, x_value)
numerical_static_derivative = static_derivative(f, x_value)

print("Analytická derivace:", analytical_derivative)
print("Numerická derivace s adaptivním krokem:", numerical_adaptive_derivative)
print("Numerická derivace s statickým krokem:", numerical_static_derivative)
