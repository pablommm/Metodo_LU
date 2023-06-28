import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import time
import sympy as sym
import numpy as np
import math

#print(os.getcwd())
data = pd.read_csv('Metodo_LU/Regresion/ACUMULADOS_vs_DIAS.csv')
#excel = pd.read_excel('./Regresion/ACUMULADOS_vs_DIAS.xlsx')

#LINEAL
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
    rse = 0
    for i in range(len(df1)):
        rse += (a*df1[i] + b - df2[i])**2
    return rse

def rse_polinomico(df1, df2, a, b):
    rse = 0
    for i in range(len(df1)):
        rse += (b * df1[i] ** a - df2[i])**2
    return rse

def rse_exponencial(df1, df2, a, b):
    rse = 0
    for i in range(len(df1)):
        #b*e**ax - Y
        rse += (b * math.e ** (a * df1[i]) - df2[i])**2
    return rse







print("----------------------------------------------------------")
print("------------------MODELO LINEAL---------------------------")
print("----------------------------------------------------------")
a_obtenido = obtener_a(data.dia, data.acumulados)
print("El valor de a es: ", a_obtenido )
b_obtenido = obtener_b(data.dia, data.acumulados, a_obtenido)
print("El valor de b es: ", b_obtenido)
recta = "y = " + str(a_obtenido) + " * x + " + str(b_obtenido)
print("La recta obtenida es: ", recta)
error_cuadrado = rse_lineal(data.dia, data.acumulados, a_obtenido, b_obtenido)
print("El error obtenido es: ", error_cuadrado)

x = sym.Symbol("x")

funcion_1 = eval("lambda x: " + recta.split(" = ")[1])

#r_obtenido = calcular_r(data.acumulados, funcion(data.dia))
r_obtenido, _ = pearsonr(data.acumulados, funcion_1(data.dia))

print("El r obtenido es de: ", r_obtenido, "\n")
time.sleep(2)


print("----------------------------------------------------------")
print("------------------MODELO POLINOMICO-----------------------")
print("----------------------------------------------------------")

def regresion_polinomica(x, y):

    # Perform the least squares regression
    log_x = np.log(x)
    log_y = np.log(y)
    coefficients = np.polyfit(log_x, log_y, 1)
    a = coefficients[0]
    b = np.exp(coefficients[1])

    return a, b

a_polinomico, b_polinomico = regresion_polinomica(data.dia, data.acumulados)

funcion_2 = lambda x: b_polinomico * x ** a_polinomico
r_obtenido_polinomico, _ = pearsonr(data.acumulados, funcion_2(data.dia))


print("El valor de a es: ", a_polinomico )
print("El valor de b es: ", b_polinomico)
recta_polinomica = "y = " + str(b_polinomico) + " * x ** " + str(a_polinomico)
print("La recta obtenida es: ", recta_polinomica)
error_cuadrado_polinomico = rse_polinomico(data.dia, data.acumulados, a_polinomico, b_polinomico)
print("El error obtenido es: ", error_cuadrado)
print("El r obtenido es de: ", r_obtenido_polinomico, "\n")
time.sleep(2)

funcion_2 = eval("lambda x: " + recta_polinomica.split(" = ")[1])

print("----------------------------------------------------------")
print("------------------MODELO EXPONENCIAL----------------------")
print("----------------------------------------------------------")

def regresion_exponencial(x , y):

    # Perform the least squares regression
    coefficients = np.polyfit(x, np.log(y), 1)
    a = coefficients[0]
    b = np.exp(coefficients[1])

    return a, b

a_exponencial, b_exponencial = regresion_exponencial(data.dia, data.acumulados)

funcion_3 = lambda x: b_exponencial * math.e ** (a_exponencial * x)
r_obtenido_exponencial, _ = pearsonr(data.acumulados, funcion_3(data.dia))

print("El valor de a es: ", a_exponencial )
print("El valor de b es: ", b_exponencial)
recta_exponencial = "y = " + str(b_exponencial) + " * e ** (" + str(a_polinomico) + " * x)"
print("La recta obtenida es: ", recta_exponencial)
error_cuadrado_exponencial = rse_exponencial(data.dia, data.acumulados, a_exponencial, b_exponencial)
print("El error obtenido es: ", error_cuadrado_exponencial)
print("El r obtenido es de: ", r_obtenido_exponencial, "\n")


b = 1
a = 1
y = b*x**a

#p = np.polyfit(data.dia, np.log(y), 1)
#p = np.polyfit(data.dia, data.acumulados, 1)
plt.figtext(0.15, 0.65, 'R lineal '+str(r_obtenido), fontsize=8, ha='left',color='blue')
plt.figtext(0.15, 0.60, 'R polinomica '+str(r_obtenido_polinomico), fontsize=8, ha='left',color='red')
plt.figtext(0.15, 0.55, 'R exponencial '+str(r_obtenido_exponencial), fontsize=8, ha='left',color='green')
plt.figtext(0.15, 0.50, 'error lineal '+str(error_cuadrado), fontsize=8, ha='left',color='blue')
plt.figtext(0.15, 0.45, 'error polinomica '+str(error_cuadrado_polinomico), fontsize=8, ha='left',color='red')
plt.figtext(0.15, 0.40, 'error exponencial '+str(error_cuadrado_exponencial), fontsize=8, ha='left',color='green')
plt.scatter(data.dia, data.acumulados,color='black' )
plt.plot(data.dia, funcion_1(data.dia),color='blue' )
plt.plot(data.dia, funcion_2(data.dia),color='red' )
plt.plot(data.dia, funcion_3(data.dia),color='green' )
plt.legend(['puntos graficados','funcion lineal', 'funcion polinomica','funcion exponencial'])

plt.show()

