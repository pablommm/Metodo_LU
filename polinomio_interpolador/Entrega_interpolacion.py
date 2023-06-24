import numpy as np
import matplotlib.pyplot as plt
import random
import sympy as sym
import time
import math
from legrange import intepolacion_legrange
from legrange import polinomio_legrange
from newton import polinomio_newton
from MetodoSecante import secante

time.sleep(1)

print("\n---------------------------------------------")
print ("**************** Interpolacion ****************")
print("\n---------------------------------------------")

print("Aqui vamos a genearar 20 numeros al azar")
maximo=int(input("Indique el valor maximo que podra tomar: "))
minimo=int(input("Indique ahora el valor minimo que podra tomar: "))
banned_x = []
lista_de_numeros = []
tolerancia = 0.0000001
x = sym.Symbol('x')
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
valores_en_x = []
valores_en_y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==0):
            valores_en_x.append(lista_de_numeros[i][j])
        else:
            valores_en_y.append(lista_de_numeros[i][j])

lista_numeros_descendente = lista_de_numeros.copy()
lista_numeros_ascendente = lista_de_numeros.copy()

def myFunc(e):
  return e[0]

lista_numeros_descendente.sort(reverse=False, key=myFunc)
lista_numeros_ascendente.sort(reverse=True, key=myFunc)

print("\nLos valores en x son: ",valores_en_x)
print("\nLos valores en y son: ",valores_en_y)

time.sleep(1)

print("\n---------------------------------------------")
print("\n Empezamos a calcular el polinomio segun el metodo de newton  ")
print("\n---------------------------------------------")

resultado_newton = polinomio_newton(lista_de_numeros)

print("\nLa forma final del polinomio de newton es :\n",resultado_newton)

time.sleep(1)

print("\n---------------------------------------------")
print("\n Empezamos a calcular con el metodo de Legrange con la lista de numeros al reves  ")
print("\n---------------------------------------------")

lista_numeros_al_reves = lista_de_numeros[::-1]
print("\nEsta es la lista de numeros al reves ",lista_numeros_al_reves)

intepolacion_legrange(lista_numeros_al_reves)
resultado_legrange_al_reves = polinomio_legrange(lista_numeros_al_reves)
time.sleep(1)

print("\n---------------------------------------------")
print("\n Empezamos a calcular con el metodo de Legrange con la lista de numeros desordenados  ")
print("\n---------------------------------------------")

lista_numeros_desordenados = random.sample(lista_de_numeros,len(lista_de_numeros))
print("\nEsta es la lista de numeros desordenados ",lista_numeros_desordenados)

#intepolacion_legrange(lista_numeros_desordenados)

time.sleep(1)
print("\n---------------------------------------------")
print("\n Ahora calcularemos una raiz de este polinomio con el metodo secante ")
print("\n---------------------------------------------")

#secante(polinomio_legrange(lista_de_numeros),x[0],x[1],tolerancia)
print("\n---------------------------------------------")
print("\n ahora graficaremos lo obtenido ")
print("\n---------------------------------------------")
# graficamos




#print("valor en y es ", valor_en_y)
a= min(valores_en_x)
#print("El valor minimo de x es: ",a)
b= max(valores_en_x)
#print("El valor maximo de x es: ",b)

#fun_legrange_al_reves = sym.lambdify(x,resultado_legrange_al_reves)
pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
pyi = resultado_legrange_al_reves(pxi)# los valores de Y son los valores en X valuados en el polinomio
#plt.plot(pxi,pyi,color='blue')

fun_newton = sym.lambdify(x,resultado_newton)
pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
pyi = fun_newton(pxi)# los valores de Y son los valores en X valuados en el polinomio
#plt.plot(pxi,pyi,color='red')

plt.plot(pxi,pyi,color='blue')
plt.plot(pxi,pyi,color='red')
plt.title('ahora graficaremos lo obtenido')
plt.scatter(valores_en_x,valores_en_y) #los puntos
plt.grid()
for i, j in zip(valores_en_x, valores_en_y):
    plt.annotate(f'({i}, {j})', (i, j), textcoords="offset points", xytext=(0,10), ha='center')
plt.yscale('symlog')
plt.show()
