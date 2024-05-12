import numpy as np
import time
import matplotlib.pyplot as plt

def create_random_matrix(size):
    return np.random.randint(2, size=(size, size))

def check_satisfiability(matrix):
    n = matrix.shape[0]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                return True
    return False

def direct_method(matrix):
    return np.linalg.det(matrix)

def iterative_method(matrix):
    n = matrix.shape[0]
    for i in range(2, n+1):
        submatrix = matrix[:i, :i]
        if np.linalg.det(submatrix) != 0:
            return True
    return False

def measure_time(func, matrix):
    start_time = time.time()
    func(matrix)
    end_time = time.time()
    return end_time - start_time

matrix_sizes = list(range(2, 101))
direct_times = []
iterative_times = []

for size in matrix_sizes:
    matrix = create_random_matrix(size)
    direct_time = measure_time(direct_method, matrix)
    iterative_time = measure_time(iterative_method, matrix)
    direct_times.append(direct_time)
    iterative_times.append(iterative_time)

plt.plot(matrix_sizes, direct_times, label='Přímá metoda')
plt.plot(matrix_sizes, iterative_times, label='Iterativní metoda')
plt.xlabel('Velikost matice')
plt.ylabel('Průměrný čas v sekundách')
plt.title('Porovnání metod')
plt.legend()
plt.grid(True)
plt.show()
