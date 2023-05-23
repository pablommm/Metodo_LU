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
b=np.zeros([m])

print("ingrese los elementos de la matriz")
# r es fila/renglon c es columna
for r in range(0,m):
    for c in range(0,m):
        matriz [r,c]=(input("elemento a["+str(r+1)+","+str(c+1)+"]: "))
        matriz [r,c]=float(matriz[r,c])
        u[r,c]=matriz[r,c]


print("usted ingreso la siguiente matriz: ")
print(u)
time.sleep(1)

print("\n---------------------------------------------")
print("Ahora ingrese el vector b = (b1, b2, b3)")
for r in range(0,m):
    b[r] = input("ingrese el valor de b" + str(r + 1) + ": ") 

print("usted ingreso el siguiente vector b: ")
print(b)
time.sleep(1)

print("\nPor lo tanto su sistema Ax = b quedo de la siguiente manera:")
for i in range(m):
    print(str(matriz[i,0]) + "x + " + str(matriz[i,1]) + "y + " + str(matriz[i,2]) + "z = " + str(b[i]))
time.sleep(1)

#u = [[ 2, -1,  1.],[ 3,  3,  9.],[ 3,  3,  5]]

time.sleep(1)

#operacion para poner ceros debajo de la diagonal

# k es fila/renglon r es columna
for k in range(0,m):
    for j in range(0,m):
        print("\nEstamos en la fila",j+1,"columna",k+1,"con valor ",matriz[j,k])
        
        if(k==j):
            l[k,j]=1
            print("\nponemos un 1 en esta posicion" )
            print("asi va quedando la funcion l")
            print(l)
        if(k>j):
            print("dejamos este valor")    
        if (k<j):
            print("\ndividiremos", matriz[j,k],"por la posicion",k+1,k+1,"con valor", matriz[k,k] )
            factor=(matriz[j,k]/matriz[k,k])
            print("nos da como resultado de factor",factor)
            l[j,k]=factor
            print("asi va quedando la matriz l")
            print(l)
            
            for c in range(0,m): #aca j se convierte en fila/renglon y c se usa como columna
                
                print("\nEstamos en la fila",j+1,"columna",c+1, "con valor ",matriz[j,c])
                print("calculamos ",matriz[j,c]," menos (",factor,"por",matriz[k,c],")")
                matriz[j,c]=matriz[j,c]-(factor*matriz[k,c])
                print("nos da como resultado",matriz[j,c])
                u[j,c]=matriz[j,c]
                print("asi va quedando la matriz U ")
                print(u)
                

print("\n---------------------------------------------")               
print("resultados")
print("matriz l")
print(l)

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