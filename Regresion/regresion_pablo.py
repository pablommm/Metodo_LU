import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import time
import sympy as sym
import numpy as np

#print(os.getcwd())
#data = pd.read_csv('./Regresion/examenpablo.csv')
#excel = pd.read_excel('./Regresion/ACUMULADOS_vs_DIAS.xlsx')

Column1 = [1.4927, 2.3176, 3.6188, 5.501, 5.8783, 6.6045, 8.4761, 9.1068, 10.3936, 10.9286, 11.1492, 11.1832, 11.2378, 12.1908, 13.5584, 14.068, 14.3787, 14.4876, 14.6319, 16.1367, 18.2721, 19.636, 20.2288, 20.7735, 21.0639, 21.8052, 22.0969, 22.3531, 22.4005, 22.8825, 23.1419, 23.8467, 25.3743, 25.393, 25.6063, 26.0081, 26.3574, 26.4314, 27.6371, 29.0726, 29.6923, 30.9215, 31.0805, 31.158, 34.8474, 34.9041, 35.4072, 35.5457, 35.5978, 36.0091, 36.4324, 36.8717, 37.6147, 38.5328, 39.3757, 40.5328, 41.3176, 41.3821, 41.9941, 42.1716, 42.8473, 43.4209, 43.6772, 46.2263, 47.5888, 47.6776, 48.5267, 51.5735, 51.9138, 52.1955, 54.5424, 56.017, 56.8023, 56.896, 57.5044, 58.1495, 59.6137, 60.3835, 61.2471, 62.6827, 64.1986, 64.3228, 64.924, 65.9885, 69.3317, 70.621, 76.8084, 77.4724, 77.5238, 80.5694, 83.3859, 83.9469, 87.5221, 89.2309, 92.1858, 93.8075, 94.0878, 96.9785, 98.6619, 98.8893]
Column2 = [31.4652, 31.2994, 31.4438, 30.7364, 30.6469, 31.6485, 30.674, 31.1342, 30.8784, 30.0875, 30.726, 30.6351, 30.7428, 30.1169, 30.0042, 30.1684, 30.7231, 30.0479, 29.8198, 30.9286, 30.5167, 30.0825, 30.4136, 30.4474, 30.09, 30.2429, 30.1619, 30.4453, 30.9862, 30.2048, 29.8864, 29.974, 30.7928, 31.2364, 29.2587, 30.3127, 30.042, 30.0261, 30.2872, 30.6292, 30.2884, 29.6798, 30.046, 29.6139, 29.9835, 29.1709, 30.5228, 30.6692, 29.7704, 30.1849, 30.6393, 29.7087, 30.4654, 28.8012, 30.4324, 30.2214, 29.4398, 30.2693, 30.3336, 29.5708, 30.9444, 30.066, 30.0446, 30.2709, 30.4189, 30.4149, 29.1737, 30.3848, 29.8345, 29.4167, 29.9806, 30.2833, 29.75, 29.8091, 30.3556, 30.3819, 28.8859, 29.0476, 30.2833, 29.5108, 29.8888, 30.3764, 30.4338, 29.7479, 30.2246, 29.8823, 29.8378, 29.2151, 29.8021, 29.5442, 29.9422, 29.5573, 30.9442, 30.2117, 29.8154, 29.0354, 29.5872, 29.9995, 29.5404, 30.2186]

#print(data)

n = len(Column1)
exi = sum(Column1)
eyi = sum(Column2)
sigma_xi2 = 0
for i in range(len(Column1)):
    sigma_xi2 += (Column1[i]*Column1[i])

sigma_xi_yi = 0
for i in range(len(Column1)):
    sigma_xi_yi += (Column1[i]*Column2[i])


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





a_obtenido = obtener_a(Column1, Column2)
print("El valor de a es: ", a_obtenido )
b_obtenido = obtener_b(Column1, Column2, a_obtenido)
print("El valor de b es: ", b_obtenido)
recta = "y = " + str(a_obtenido) + "*x + " + str(b_obtenido)
print("La recta obtenida es: ", recta)
error_cuadrado = rse_lineal(Column1, Column2, a_obtenido, b_obtenido)
print("El error obtenido es: ", error_cuadrado)

x = sym.Symbol("x")


#nueva_funcion = lambda x:  -0.010829872456535638*x + 30.611219343708736
nueva_funcion = eval("lambda x: " + recta.split(" = ")[1])

#print("esto es una prueba",nueva_funcion(5))
lista_y = []
def aplicar_funcion(columna):
    
    for i in range(len(columna)):
        valor = nueva_funcion(columna[i])
        lista_y.append(valor)
    return lista_y

aplicar_funcion(Column1)
#print ("otro test",lista_y)

def calcular_r(x, y):
    std_x = np.std(x)
    std_y = np.std(y)
    xy = 0
    for i in range(len(x)):
        xy += x[i]*y[i]
    sum_x = sum(x)
    sum_y = sum(y)
    numerador = xy - (sum_x * sum_y)
    denominador = std_x * std_y
    r = numerador / denominador 

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

#r_obtenido = calcular_r(Column2, lista_y)
r_obtenido, _ = pearsonr(Column2, lista_y)

print("El r obtenido es de: ", r_obtenido)

b = 1
a = 1
y = b*x**a

#p = np.polyfit(data.dia, np.log(y), 1)
p = np.polyfit(Column1, Column2, 1)


plt.scatter(Column1, Column2)
plt.plot(Column1, lista_y)
# Set x-axis range
plt.xlim(0,100)
# Set y-axis range
plt.ylim(0,100)
plt.show()
