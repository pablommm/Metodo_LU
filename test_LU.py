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

print("usted ingreso la siguiente matriz: ")
print(u)


#u = [[ 2, -1,  1.],[ 3,  3,  9.],[ 3,  3,  5]]

time.sleep(1)

#operacion para poner ceros debajo de la diagonal
contadorMatrizU=0
contadorMatrizL=0
for k in range(0,m):
    for r in range(0,m):
        print("\nEstamos en la fila",r+1,"columna",k+1,"con valor ",matriz[r,k])
        contadorMatrizL =contadorMatrizL+1
        if(k==r):
            l[k,r]=1
            print("\nponemos un 1 en esta posicion" )
            print("asi va quedando la funcion l")
            print(l)
        if (k<r):
            print("\ndividiremos", matriz[r,k],"por la posicion",k+1,k+1,"con valor", matriz[k,k] )
            factor=(matriz[r,k]/matriz[k,k])
            print("nos da como resultado de factor",factor)
            l[r,k]=factor
            print("asi va quedando la matriz l")
            print(l)
            
            for c in range(0,m):
                contadorMatrizU =contadorMatrizU+1
                print("\nEstamos en la fila",r+1,"columna",c+1, "con valor ",matriz[r,c])
                print("calculamos ",matriz[r,c]," menos (",factor,"por",matriz[k,c],")")
                matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
                print("nos da como resultado",matriz[r,c])
                u[r,c]=matriz[r,c]
                print("asi va quedando la matriz U ")
                print(u)
                

                
print("resultados")
print("matriz l")
print(l)

print("en total se necesitarion ",contadorMatrizL,"operaciones elementales para despejar L")
print("\n---------------------------------------------")
print("resultados")
print("matriz u")
print(u)


print("\n---------------------------------------------")
"""
#comprobacion
matrizr=np.zeros([m,m])
for r in range (0,m):
    for c in range(0,m):
        for k in range (0,m):
            matrizr[r,c] +=(l[r,k]*u[k,c])

print("comprobacion")            
print(matrizr)
a=np.dot(l,u)
print("\n---------------------------------------------")
print(a)                

"""