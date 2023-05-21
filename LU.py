# factorizacion de LU
import math
import time
import numpy as np

print("\n---------------------------------------------")
print ("*********metodo de LU para matrices cuadradas*********")
print("\n---------------------------------------------")
"""
m=int(input("Indique el numero de columnas/filas: "))
print("\n---------------------------------------------")
"""
m=3
matriz= np.zeros([m,m]) # defino la matriz

u=np.zeros([m,m])
l=np.zeros([m,m])

print("ingrese los elementos de la matriz")
# r es fila/renglon c es columna
for r in range(0,m):
    for c in range(0,m):
        matriz [r,c]=(input("elemento a["+str(r+1)+","+str(c+1)+"]: "))
        matriz [r,c]=float(matriz[r,c])
        u[r,c]=matriz[r,c]


#u = [[ 2, -1,  1.],[ 3,  3,  9.],[ 3,  3,  5]]
time.sleep(1)

#operacion para poner ceros debajo de la diagonal
for k in range(0,m):
    for r in range(0,m):
        if(k==r):
            l[k,r]=1
        if (k<r):
            factor=(matriz[r,k]/matriz[k,k])
            l[r,k]=factor
            
            for c in range(0,m):
                matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
                u[r,c]=matriz[r,c]
                
print("resultados")
print("matriz l")
print(l)
print("\n---------------------------------------------")
print("resultados")
print("matriz u")
print(u)
print("\n---------------------------------------------")

#comprobacion
matrizr=np.zeros([m,m])
for r in range (0,m):
    for c in range(0,m):
        for k in range (0,m):
            matrizr[r,c] +=(l[r,k]*u[k,c])
print(matrizr)
a=np.dot(l,u)
print("\n---------------------------------------------")
print(a)                

