import numpy as np
import matplotlib.pyplot as plt
import random
import sympy as sym
import time
import math
from legrange import intepolacion_legrange
from legrange import polinomio_legrange
from newton import interpolacion_newton
from MetodoSecante import secante

time.sleep(1)

print("\n---------------------------------------------")
print ("********* Interpoladocion *********")
print("\n---------------------------------------------")

print("Aqui vamos a genearar 20 numeros al azar")
maximo=int(input("Indique el valor maximo que podra tomar: "))
minimo=int(input("Indique ahora el valor minimo que podra tomar: "))
banned_x = []
lista_de_numeros = []
tolerancia = 0.0000001

print("\n---------------------------------------------")

for i in range (20):
    punto=[]
    for r in range(2):
        n=random.randrange(minimo,maximo)
        if(r == 0):
            while(banned_x.count(n) > 0):
                n=random.randrange(minimo,maximo)
                #print("se repitio el valor", n)
            banned_x.append(n)
            #print("se baneo el valor", n)
        punto.append(n)
        #print("agregue el valor ",n)
        #print("punto ", punto)
    lista_de_numeros.append(punto)

time.sleep(1)  
     
print("\nAsi me quedo la lista de vectores ",lista_de_numeros)

# Aqui separamos en valores en X y valores en Y
x = []
y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==0):
            x.append(lista_de_numeros[i][j])
        else:
            y.append(lista_de_numeros[i][j])

lista_numeros_descendente = lista_de_numeros.copy()
lista_numeros_ascendente = lista_de_numeros.copy()

def myFunc(e):
  return e[0]

lista_numeros_descendente.sort(reverse=False, key=myFunc)
lista_numeros_ascendente.sort(reverse=True, key=myFunc)

print("\nLos valores en x son: ",x)
print("\nLos valores en y son: ",y)

time.sleep(1)

print("\n---------------------------------------------")
print("\n Empezamos a calcular el polinomio segun el metodo de newton  ")
print("\n---------------------------------------------")

interpolacion_newton(lista_de_numeros)

lista_numeros_al_reves = lista_de_numeros[::-1]
time.sleep(1)
print("\n---------------------------------------------")
print("\n Empezamos a calcular con el metodo de Legrange con la lista de numeros al reves  ")
print("\n---------------------------------------------")
print("\nEsta es la lista de numeros al reves ",lista_numeros_al_reves)
intepolacion_legrange(lista_numeros_al_reves)


lista_numeros_desordenados = random.sample(lista_de_numeros,len(lista_de_numeros))
time.sleep(1)
print("\n---------------------------------------------")
print("\n Empezamos a calcular con el metodo de Legrange con la lista de numeros desordenados  ")
print("\n---------------------------------------------")
print("\nEsta es la lista de numeros desordenados ",lista_numeros_desordenados)
intepolacion_legrange(lista_numeros_desordenados)

#raices = sym.solvers.solve(polinomio_legrange(lista_de_numeros))
time.sleep(1)
print("\n---------------------------------------------")
print("\n Ahora calcularemos una raiz de este polinomio con el metodo secante ")
print("\n---------------------------------------------")
secante(polinomio_legrange(lista_de_numeros),x[0],x[1],tolerancia)