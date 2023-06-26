import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import time
import sympy as sym
import numpy as np

#print(os.getcwd())
data = pd.read_csv('./Regresion/ACUMULADOS_vs_DIAS.csv')
#excel = pd.read_excel('./Regresion/ACUMULADOS_vs_DIAS.xlsx')
print(len(data))

n = len(data)
exi = sum(data.dia)
eyi = sum(data.acumulados)
sigma_xi2 = 0
for i in range(len(data.dia)):
    sigma_xi2 += (data.dia[i]*data.dia[i])

sigma_xi_yi = 0
for i in range(len(data.dia)):
    sigma_xi_yi += (data.dia[i]*data.acumulados[i])



def obtener_a(df1, df2):
    n= len(df1)
    exi = sum(df1)
    eyi = sum(df2)
    sigma_xi2 = 0
    sigma_xi_yi = 0

    for i in range(len(df1)):
        current1 = int(df1[i])
        current2 = int(df2[i])
        sigma_xi_yi += (df1[i]*df2[i])
        sigma_xi2 += (df1[i]*df1[i])

    numerador = (n * sigma_xi_yi) - (exi*eyi)
    denominador = (n * sigma_xi2) - (exi * exi)
    a = numerador / denominador

    return a

def obtener_b(df1, df2, a):
    n= len(df1)
    exi = sum(df1)
    eyi = sum(df2)
    numerador = eyi - (a * exi)
    b = numerador / n
    return b

def rse_lineal(df1, df2, a, b):
    exi = sum(df1)
    eyi = sum(df2)
    rse = 0
    for i in range(len(df1)):
        rse += (a*df1[i] + b - df2[i])**2
    return rse





a_obtenido = obtener_a(data.dia, data.acumulados)
print("El valor de a es: ", a_obtenido )
b_obtenido = obtener_b(data.dia, data.acumulados, a_obtenido)
print("El valor de b es: ", b_obtenido)
recta = "y = " + str(a_obtenido) + "*x + " + str(b_obtenido)
print("La recta obtenida es: ", recta)
error_cuadrado = rse_lineal(data.dia, data.acumulados, a_obtenido, b_obtenido)
print("El error obtenido es: ", error_cuadrado)

x = sym.Symbol("x")
funcion_1 = lambda x: 1406.5942618467504*x -62138.47083685545

def calcular_r(x, y):
    """ std_x = np.std(x)
    std_y = np.std(y)
    xy = 0
    for i in range(len(x)):
        xy += x[i]*y[i]
    sum_x = sum(x)
    sum_y = sum(y)
    numerador = xy - (sum_x * sum_y)
    denominador = std_x * std_y
    r = numerador / denominador """

    n = len(x)
    sigma_xi = sum(x)
    sigma_yi = sum(y)
    sigma_xi2 = 0
    sigma_xi_yi = 0

    for i in range(len(x)):
        sigma_xi_yi += (x[i]*y[i])
        sigma_xi2 += (x[i]*x[i])

    numerador = (n * sigma_xi_yi) - (sigma_xi * sigma_yi)
    denominador = 1
    r = 0

    return r

#r_obtenido = calcular_r(data.acumulados, funcion(data.dia))
r_obtenido, _ = pearsonr(data.acumulados, funcion_1(data.dia))

print("El r obtenido es de: ", r_obtenido)

b = 1
a = 1
y = b*x**a

p = np.polyfit(data.dia, np.log(y), 1)
#p = np.polyfit(data.dia, data.acumulados, 1)


plt.scatter(data.dia, data.acumulados)
plt.plot(data.dia, funcion_1(data.dia))
plt.show()

