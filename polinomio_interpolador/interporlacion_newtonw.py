# Polinomio interpolador
import math
import time
import random
import numpy as np

print("\n---------------------------------------------")
print ("*********Polinomio interpolador de Newtown*********")
print("\n---------------------------------------------")


print("Debemos geneara 20 numeros al azar")
maximo=int(input("Indique el valor maximo que podra tomar: "))
minimo=int(input("Indique ahora el valor minimo que podra tomar: "))


lista_de_numeros = ([])
print("\n---------------------------------------------")

for i in range (20):
    punto=([])
    for r in range(2):
        n=random.randrange(minimo,maximo)
        punto.append(n)
        print("agregue el valor ",n)
        print("punto ", punto)
    lista_de_numeros.append(punto)
        
print("asi me quedo la lista de vectoes ",lista_de_numeros)
         