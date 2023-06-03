
def coeficientes_diferencias_divididas(x, y):
    n = len(x)
    coeficientes = [y[0]]
    
    for i in range(1, n):
        diferencia = y[i]
        for j in range(i):
            diferencia = (diferencia - coeficientes[j]) / (x[i] - x[j])
        coeficientes.append(diferencia)
    
    return coeficientes

def interpolacion_newton(x, y, valor):
    coeficientes = coeficientes_diferencias_divididas(x, y)
    n = len(x)
    interpolacion = coeficientes[0]
    factor = 1
    
    for i in range(1, n):
        factor *= (valor - x[i-1])
        interpolacion += coeficientes[i] * factor
    
    return interpolacion

# Ejemplo de uso
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]
valor_interpolado = interpolacion_newton(x, y, 2.5)
print(valor_interpolado)
