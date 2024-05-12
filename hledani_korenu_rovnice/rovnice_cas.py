import numpy as np
from scipy.optimize import bisect, newton
import matplotlib.pyplot as plt
import time

def logarithmic_function(x):
    return np.log(x)

def cubic_function(x):
    return x**3 - 6*x**2 + 11*x - 6

def trigonometric_function(x):
    return np.sin(x)

log_interval = (0.1, 5)
cubic_interval = (0, 4)
trig_interval = (-2*np.pi, 2*np.pi)

# Metoda půlení intervalu
def bisection_method(f, interval):
    root = bisect(f, *interval)
    return root

# Newtonova metoda
def newton_method(f, interval):
    root = newton(f, np.mean(interval))
    return root

# Funkce pro vizualizaci
def plot_function_and_roots(f, interval, root1, root2, method_name):
    x = np.linspace(interval[0], interval[1], 1000)
    y = f(x)
    plt.plot(x, y, label=f'$f(x)$')
    plt.scatter([root1, root2], [0, 0], color='red', label='kořeny')
    plt.title(f'Funkce a Kořeny (Metoda: {method_name})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Hledání kořenů a porovnání časové náročnosti a přesnosti
def find_and_compare_roots(f, interval, function_name):
    print(f"Nalezení kořenů pro {function_name} funkci:")
    
    # Bisekční metoda
    start_time = time.time()
    bisection_root = bisection_method(f, interval)
    bisection_time = time.time() - start_time
    print(f"Metoda bisekce : Kořen = {bisection_root:.6f}, Čas = {bisection_time:.6f} s")
    
    # Newtonova metoda
    start_time = time.time()
    newton_root = newton_method(f, interval)
    newton_time = time.time() - start_time
    print(f"Newtonova metoda: Kořen = {newton_root:.6f}, Čas = {newton_time:.6f} s")

    # Vizualizace
    plot_function_and_roots(f, interval, bisection_root, newton_root, "Metoda Bisekce a Newtonova metoda")

# Porovnání kořenů pro logaritmickou funkci
find_and_compare_roots(logarithmic_function, log_interval, "Logaritmická funkce")

# Porovnání kořenů pro kubickou funkci
find_and_compare_roots(cubic_function, cubic_interval, "Kubická funkce")

# Porovnání kořenů pro goniometrickou funkci
find_and_compare_roots(trigonometric_function, trig_interval, "Trigoniometrická funkce")
