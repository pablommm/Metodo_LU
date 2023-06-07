# Polinomio interpolador

import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

print("\n---------------------------------------------")
print ("*********Polinomio interpolador de Legrange*********")
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
                print("Se repitio el valor", n)
            banned_x.append(n)
            print("Se baneo el valor", n)
        punto.append(n)
        print("agregue el valor ",n)
        print("punto ", punto)
    lista_de_numeros.append(punto)

 
#lista_de_numeros = [[9, 15], [17, 17], [5, 14], [12, 11], [14, 9]] 
print("Asi quedo la lista de vectores ",lista_de_numeros)

valores_en_x = []
valores_en_y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==1):
            valores_en_y.append(lista_de_numeros[i][j])
        else:
            valores_en_x.append(lista_de_numeros[i][j])

xi=valores_en_x
print("Los valores en x son: ",xi)
fi=valores_en_y
print("Los valores en y son: ",fi)

x = sym.Symbol('x')
polinomio = 0
n = len(xi) 

for i in range(len(lista_de_numeros)):
    numerador = 1
    denominador = 1
    for j in range(len(lista_de_numeros)):
        if j!=i:
            numerador = numerador*(x-xi[j])
            #print("El numerador va tomando el valor: ",numerador)
            denominador = denominador * (xi[i]- xi[j])
            #print("El denominador va tomando el valor: ",numerador)
    L = numerador/denominador
    polinomio = polinomio + L * fi[i] # aqui vamos almacenando las partes del polinomio que se van almacenando
        

#print("El polinomio con legrange sin simplificar es ",polinomio)
polisimp = polinomio.expand()

print("El polinomio simplificado queda asi: ",polisimp)

#graficamos

pol = sym.lambdify(x,polisimp)

a= min(xi)
print("El valor minimo de x es: ",a)
b= max(xi)
print("El valor maximo de x es: ",b)

pxi = np.linspace(a,b,200)
pyi = pol(pxi)# los valores de Y son los valores en X valuados en el polinomio

plt.figure()
plt.scatter(xi,fi)#los puntos
plt.plot(pxi,pyi,color='red')
plt.grid()
plt.show()
