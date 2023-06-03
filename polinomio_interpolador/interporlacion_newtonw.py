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
    lista_de_numeros.append(random.randrange(minimo,maximo))

print("generemos la siguiente lista de numeros aleatorios")
print(lista_de_numeros)    