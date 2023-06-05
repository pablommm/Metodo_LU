# Polinomio interpolador

import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sympy

print("\n---------------------------------------------")
print ("*********Polinomio interpolador de Newtown*********")
print("\n---------------------------------------------")

print("Debemos geneara 20 numeros al azar")
maximo=int(input("Indique el valor maximo que podra tomar: "))
minimo=int(input("Indique ahora el valor minimo que podra tomar: "))
banned_x = []

lista_de_numeros = []
print("\n---------------------------------------------")

for i in range (20):
    punto=[]
    for r in range(2):
        n=random.randrange(minimo,maximo)
        if(r == 0):
            while(banned_x.count(n) > 0):
                n=random.randrange(minimo,maximo)
                print("se repitio el valor", n)
            banned_x.append(n)
            print("se baneo el valor", n)
        punto.append(n)
        print("agregue el valor ",n)
        print("punto ", punto)
    lista_de_numeros.append(punto)
        
print("asi me quedo la lista de vectoes ",lista_de_numeros)

valores_en_x = []
valores_en_y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==1):
            valores_en_x.append(lista_de_numeros[i][j])
        else:
            valores_en_y.append(lista_de_numeros[i][j])

xi=valores_en_x
fi=valores_en_y

x = sympy.Symbol('x')
polinomio = 0
n = len(xi) 

for i in range(0,n,1):
    numerador = 1
    denominador = 1
    for j in range(0,n,1):
        if j!=1:
            numerador = numerador*(x-xi[j])
            denominador = denominador * (xi[i]- xi[j])
        L = numerador/denominador
        polinomio = polinomio + L * fi[i]

print("el polinimog con legrange sin simplificar es ",L)
polinomio_simplificado = polinomio.expand()
print("el polinimio simplificado queda asi: ",polinomio_simplificado)
"""
# Interpolacion de Lagrange
# Polinomio en forma simbólica
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

print('INTERPOLACIÓN POLINÓMICA DE LAGRANJE',end="\n\n")

print("Es una forma de presentar el polinomio que interpola un conjunto de puntos dado. ",end="\n\n")

# INGRESO , Datos de prueba

# Datos de X
xi = np.array([-1.5, -0.75, 0, 0.75, 1.5])

# Datos de F(X)
fi = np.array([-14.1014, -0.931596, 0, 0.931596, 14.1014])

# PROCEDIMIENTO
n = len(xi)
x = sym.Symbol('x')
# Polinomio
polinomio = 0
for i in range(0,n,1):
    # Termino de Lagrange
    termino = 1
    for j  in range(0,n,1):
        if (j!=i):
            termino = termino*(x-xi[j])/(xi[i]-xi[j])
    print("El L(",i,") es :", termino)
    polinomio = polinomio + termino*fi[i]
# Expande el polinomio
px = polinomio.expand()
# para evaluacion numérica
pxn = sym.lambdify(x,polinomio)

# Puntos para la gráfica
a = np.min(xi)
b = np.max(xi)
muestras = 101
xi_p = np.linspace(a,b,muestras)
fi_p = pxn(xi_p)

# Salida
print('\nPolinomio de Lagrange, expresiones:')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(px)

# Gráfica
plt.title('Interpolación Lagrange')
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(xi_p,fi_p, label = 'Polinomio')
plt.legend()
plt.show()
"""