import matplotlib.pyplot as plt
import numpy as np
import random


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
        
print("asi me quedo la lista de vectores ",lista_de_numeros)


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

# aca aplico un sorted y los organiza por default en base al valor de x
print("ahora ordenados",sorted(lista_de_numeros)) 

plt.scatter(valores_en_x, valores_en_y)

# Muestra la gráfica
plt.show()