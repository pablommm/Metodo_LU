# Polinomio interpolador
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt

banned_x = []


print("\n---------------------------------------------")
print ("*********Polinomio interpolador de Newtown*********")
print("\n---------------------------------------------")


print("Debemos geneara 20 numeros al azar")
maximo=int(input("Indique el valor maximo que podra tomar: "))
minimo=int(input("Indique ahora el valor minimo que podra tomar: "))


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


#OBTENER C
def obtener_c(yn, yn1, xn1, lista_x):
    denominador = 1
    for i in lista_x:
        denominador *= (xn1 - i)
    #print("el valor de denominador es ", denominador)
    return ((yn - yn1)/denominador)


#GENERAR LOS P(X)
pn = 0
pn1 = 0
c = 0
lista_x = []
denominador = 1


print("El valor de P0(X) es: ", pn)

for i in range (len(lista_de_numeros) - 1):
    print("me encuentro en el paso ", i)
    time.sleep(1)
    if(i == 0):
        pn = lista_de_numeros[0][1]
    else:
        xn  = lista_de_numeros[i][0] 
        lista_x.append(xn)
        xn1 = lista_de_numeros[i+1][0] 
        c = obtener_c(pn, pn1, xn1, lista_x)
        denominador = 1
        for j in lista_x:
            denominador *= (xn1 - j)
        pn1 = pn + c * denominador
        
    print("p(", i, ") = ", pn)
    print("p(", i + 1, ") = ", pn1)
    print("\n-----------------------------------------")
    time.sleep(1)
    pn = pn1


# la graficacion
"""
print("primero graficamos solo los puntos: ")
valores_en_x = []
valores_en_y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==1):
            valores_en_x.append(lista_de_numeros[i][j])
        else:
            valores_en_y.append(lista_de_numeros[i][j])

print("esta es la lista de valores en x",valores_en_x)
print("esta es la lista de valores en y",valores_en_y)

plt.scatter(valores_en_x, valores_en_y)

plt.show()
"""

















