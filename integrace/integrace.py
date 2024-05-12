import numpy as np
from scipy import integrate
import sympy as sp

# Definice funkcí
x = sp.symbols('x')
f = 2*x**3 - 3*x**2 + 4*x - 1
g = sp.sin(x)
h = sp.exp(x)

# Definice intervalu integrace
a = 0
b = np.pi/2

# Analytické řešení
F_analytic = sp.integrate(f, (x, a, b))
G_analytic = sp.integrate(g, (x, a, b))
H_analytic = sp.integrate(h, (x, a, b))

# Numerické řešení pomocí scipy
F_numeric_scipy, _ = integrate.quad(lambda x: 2*x**3 - 3*x**2 + 4*x - 1, a, b)
G_numeric_scipy, _ = integrate.quad(np.sin, a, b)
H_numeric_scipy, _ = integrate.quad(np.exp, a, b)

# Výsledky
print("Polynomická funkce:")
print("Analytické řešení:", F_analytic)
print("Numerické řešení (scipy):", F_numeric_scipy)
print()

print("Harmonická funkce:")
print("Analytické řešení:", G_analytic)
print("Numerické řešení (scipy):", G_numeric_scipy)
print()

print("Exponenciální funkce:")
print("Analytické řešení:", H_analytic)
print("Numerické řešení (scipy):", H_numeric_scipy)
