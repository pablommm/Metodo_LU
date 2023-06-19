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

for i in range (5):
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

#GENERAR LOS VALORES DE INICIO
pn_1 = 0
pn = 0
pn_str = ""
c = 0
lista_x = []
denominador = 1
denominador_str = ""

#FUNCION OBTENER C
def obtener_c(yn, yn_1, xn, lista_x, pn_str):
    primero = True
    denominador = ""
    denominador_str = ""
    for k in lista_x:
        if(primero):
            denominador += "( " + str(xn) + " - " + str(k) + " )"
            denominador_str += "( x - " + str(k) + " )"
            primero = False
        else:
            denominador += " * ( " + str(xn1) + " - " + str(k) + " )"
            denominador_str += " * ( x - " + str(k) + " )"
    #print("denominador: ", denominador)
    #print("resultado del numerador: ", (yn - yn_1))
    #print("resultado denominador: ", eval(denominador))
    #print("el valor de denominador es ", denominador)
    eval_denominador = eval(denominador)
    cn = (yn - yn_1)/eval_denominador
    pn_str += " + " + str(cn) + " * " + denominador_str
    return cn, pn_str, denominador_str, denominador







for j in range (len(lista_de_numeros)):
    print("me encuentro en el paso ", j)
    time.sleep(1)
    if(j == 0):
        pn_1 = lista_de_numeros[0][1]
        xn = lista_de_numeros[0][0]
        xn1 = lista_de_numeros[j+1][0]
        pn_str = str(pn_1)
        print("p(", j, ") = ", pn_1)
    else:
        xn  = lista_de_numeros[j-1][0] 
        lista_x.append(xn)
        xn1 = lista_de_numeros[j][0] 
        print(lista_x)
        pn_1 = lista_de_numeros[j - 1][1]
        pn = lista_de_numeros[j][1]
        c, pn_str, denominador_str, denominador = obtener_c(pn, pn_1, xn1, lista_x, pn_str)
        denominador = ""
        #print("p(", j - 1, ") = ", pn_1)
        #print("p(", j, ") = ", pn)
        pn_1 = pn
        print("p(", j, ") = ", pn_str)
        print("\n-----------------------------------------")
        time.sleep(1)     
    
    
        
    
            




# la graficacion

print("primero graficamos solo los puntos: ")
valores_en_x = []
valores_en_y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==0):
            valores_en_x.append(lista_de_numeros[i][j])
        else:
            valores_en_y.append(lista_de_numeros[i][j])

print("esta es la lista de valores en x",valores_en_x)
print("esta es la lista de valores en y",valores_en_y)

plt.scatter(valores_en_x, valores_en_y)

plt.show()


















