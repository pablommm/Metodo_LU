import numpy as np
import matplotlib.pyplot as plt
import random
import sympy as sym
import time
import math
from legrange import interpolacion_legrange
from legrange import polinomio_legrange
from newton import polinomio_newton
from MetodoSecante import secante
from graficacion import graficacion
from graficacion import graficacion_con_raiz
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
"""
lista_numeros_descendente = lista_de_numeros.copy()
lista_numeros_ascendente = lista_de_numeros.copy()

def myFunc(e):
  return e[0]

lista_numeros_descendente.sort(reverse=False, key=myFunc)
lista_numeros_ascendente.sort(reverse=True, key=myFunc)
"""
print("\nLos valores en x son: ",valores_en_x)
print("\nLos valores en y son: ",valores_en_y)

time.sleep(1)

print("\n----------------------------------------------------------------------------------------")
print("\n Empezamos a calcular el polinomio segun el metodo de newton  ")
print("\n----------------------------------------------------------------------------------------")

resultado_newton = polinomio_newton(lista_de_numeros)
grado_newton = resultado_newton.as_poly().degree()
print("\nLa forma final del polinomio de newton es :\n",resultado_newton)
print("\nEl grado del polinomio obtenido en newton es ", grado_newton)
print("\nMostramos como quedaria el grafico ")
fun_newton = sym.lambdify(x,resultado_newton)
mensaje_newton = "Polinomio obtenido por Newton"
graficacion(valores_en_x,valores_en_y,fun_newton,mensaje_newton)
time.sleep(1)

print("\n----------------------------------------------------------------------------------------")
print("\n Empezamos a calcular con el metodo de Legrange con la lista de numeros al reves  ")
print("\n----------------------------------------------------------------------------------------")

lista_numeros_al_reves = lista_de_numeros[::-1]
print("\nEsta es la lista de numeros al reves ",lista_numeros_al_reves)

interpolacion_legrange(lista_numeros_al_reves)
resultado_legrange_al_reves = polinomio_legrange(lista_numeros_al_reves)
grado_resultado_legrange_al_reves = resultado_legrange_al_reves.as_poly().degree()
funcion_legrange_alreves= sym.lambdify(x,resultado_legrange_al_reves)
print("\nEl grado del polinomio obtenido en legrange es ", grado_resultado_legrange_al_reves)
print("\nMostramos como quedaria el grafico ")
mensaje_legrange_alreves = "polinomio obtenido por legrange, con valores al reves"
graficacion(valores_en_x,valores_en_y,funcion_legrange_alreves,mensaje_legrange_alreves)


time.sleep(1)

print("\n----------------------------------------------------------------------------------------")
print("\n Empezamos a calcular con el metodo de Legrange con la lista de numeros desordenados  ")
print("\n----------------------------------------------------------------------------------------")

lista_numeros_desordenados = random.sample(lista_de_numeros,len(lista_de_numeros))
print("\nEsta es la lista de numeros desordenados ",lista_numeros_desordenados)

interpolacion_legrange(lista_numeros_desordenados)
resultado_legrange_desordenado = polinomio_legrange(lista_numeros_al_reves)
grado_resultado_legrange_desordenado = resultado_legrange_desordenado.as_poly().degree()
funcion_legrange_desordenados= sym.lambdify(x,resultado_legrange_al_reves)
print("\nEl grado del polinomio obtenido en legrange es ", grado_resultado_legrange_desordenado)
print("\nMostramos como quedaria el grafico ")
mensaje_legrange_desordenado = "polinomio obtenido por legrange, con valores desordenados"
graficacion(valores_en_x,valores_en_y,funcion_legrange_desordenados,mensaje_legrange_desordenado)

time.sleep(1)

print("\n*****************************************************************************")
time.sleep(1)

if (grado_newton == grado_resultado_legrange_al_reves):
    print("\nPodemos observar que los todos estos polinomios tienen el mismo grado\n")
else:
    print("\nEstos polinomios no tienen el mismo grado\n")

print("\n*****************************************************************************")

print("\n----------------------------------------------------------------------------------------")
print("\n Ahora calcularemos una raiz del polinomio de legrange con el metodo secante ")
print("\n----------------------------------------------------------------------------------------")

raiz_obtenida = secante(funcion_legrange_alreves,valores_en_x[0],valores_en_x[1],tolerancia)

print("\n----------------------------------------------------------------------------------------")
print("\n ahora graficaremos lo obtenido ")
print("\n----------------------------------------------------------------------------------------")
mensaje_final = "El primero polinomio marcando en verde la raiz obtenida"
graficacion_con_raiz(valores_en_x,valores_en_y,fun_newton,mensaje_final,raiz_obtenida)


print("\n despues de haber calculado el polinomio tanto por el metodo de Legrange como por el metodo de newton, podemos concluir que mientras lo puntos sean los mismos sin importar su orden obtenemos el mismo polinomio ")


print("\n y que a pesar de tener diferencias en las expresiones algebraicas la representacion grafica de estas se vera igual")