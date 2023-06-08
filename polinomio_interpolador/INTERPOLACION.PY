import numpy as np
import matplotlib.pyplot as plt

# Establecer cotas para los pares (x, y)
cota_inferior = -10
cota_superior = 10

# Generar 20 pares de números aleatorios dentro de las cotas
np.random.seed(42)  # Para reproducibilidad
x = np.sort(np.random.uniform(cota_inferior, cota_superior, size=20))
y = np.random.uniform(cota_inferior, cota_superior, size=20)
print("valores en x son ",x)
print("valores en y son ",y)
# Ordenar los pares según x
indices_ordenados = np.argsort(x)
x = x[indices_ordenados]
y = y[indices_ordenados]

# Obtener el grado del polinomio interpolador (Newton)
grado_newton = len(x) - 1
#print("Grado del polinomio interpolador por el método de Newton:", grado_newton)

# Calcular las diferencias divididas
diferencias_divididas = np.zeros((grado_newton + 1, grado_newton + 1))
diferencias_divididas[:, 0] = y
print()

for j in range(1, grado_newton + 1):
    for i in range(j, grado_newton + 1):
        diferencias_divididas[i, j] = (diferencias_divididas[i, j - 1] - diferencias_divididas[i - 1, j - 1]) / (x[i] - x[i - j])

# Construir el polinomio interpolador (Newton)
def polinomio_interpolador_newton(x_eval):
    resultado = diferencias_divididas[0, 0]
    producto = 1
    for i in range(1, grado_newton + 1):
        producto *= (x_eval - x[i - 1])
        resultado += diferencias_divididas[i, i] * producto
    return resultado

# Graficar el polinomio interpolador y los pares de datos
x_vals = np.linspace(cota_inferior, cota_superior, 1000)
y_vals = polinomio_interpolador_newton(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Polinomio interpolador (Newton)')
plt.scatter(x, y, color='red', label='Pares de datos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación polinómica por el método de Newton')
plt.legend()
plt.grid(True)
plt.show()

# Ordenar los pares al revés y obtener otro polinomio interpolador
x_rev = x[::-1]
y_rev = y[::-1]

# Obtener el grado del polinomio interpolador (al revés)
grado_newton_rev = len(x_rev) - 1
print("Grado del polinomio interpolador (al revés):", grado_newton_rev)

# Calcular las diferencias divididas para el polinomio al revés
diferencias_divididas_rev = np.zeros((grado_newton_rev + 1, grado_newton_rev + 1))
diferencias_divididas_rev[:, 0] = y_rev


for j in range(1, grado_newton_rev + 1):
    for i in range(j, grado_newton_rev + 1):
        diferencias_divididas_rev[i, j] = (diferencias_divididas_rev[i, j - 1] - diferencias_divididas_rev[i - 1, j - 1]) / (x_rev[i] - x_rev[i - j])
        #print("estas son las diferencias divididas",diferencias_divididas_rev)
# Construir el polinomio interpolador (al revés)
def polinomio_interpolador_newton_rev(x_eval):
    resultado = diferencias_divididas_rev[0, 0]
    producto = 1
    for i in range(1, grado_newton_rev + 1):
        producto *= (x_eval - x_rev[i - 1])
        resultado += diferencias_divididas_rev[i, i] * producto
    return resultado

# Graficar el polinomio interpolador (al revés) y los pares de datos
y_vals_rev = polinomio_interpolador_newton_rev(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals_rev, label='Polinomio interpolador (al revés)')
plt.scatter(x_rev, y_rev, color='red', label='Pares de datos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación polinómica (al revés)')
plt.legend()
plt.grid(True)
plt.show()

# Función para encontrar una raíz del polinomio interpolador por el método de Newton
def encontrar_raiz_newton(polinomio, x_inicial, tolerancia=1e-6, max_iter=100):
    x_actual = x_inicial
    iteracion = 0

    while np.abs(polinomio(x_actual)) > tolerancia and iteracion < max_iter:
        x_actual = x_actual - polinomio(x_actual) / polinomio_interpolador_newton(x_actual)
        iteracion += 1

    if np.abs(polinomio(x_actual)) <= tolerancia:
        return x_actual
    else:
        return None

# Encontrar una raíz del polinomio interpolador (Newton)
raiz = encontrar_raiz_newton(polinomio_interpolador_newton, x[0])
print("Raíz del polinomio interpolador (Newton):", raiz)
