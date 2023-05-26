import numpy as np
import pprint

print('MÉTODO DE JACOBI',end="\n\n")

'''
La siguiente función en Python recibe la matriz de coeficientes  a  y el vector de constantes b  de un sistema lineal.
Adicionalmente recibe un vector inicial  x, la estimación del error   e y el máximo de iteraciones permitidas m. Esta 
función utiliza dentro de un ciclo, la función jacobi definida anteriormente. Entrega el vector x calculado y el número 
de iteraciones realizadas k. Si el método no converge, x contendrá un vector nulo.

"a" es la matriz de coeficientes que recibe
"b" es el vector de constantes de un sistema lienal
"x" es el vector inicial
"e" es la estimacion del error
"m" es el maximo de iteracion permitidas
"k" es el numero de interaciones realizadas
"jacobi" entrega el vector "x" ya calculado y "k" las iteraciones

si el metodo converge "x" sera nulo 
'''
m=3
matriz= np.zeros([m,m]) # defino la matriz
A = np.zeros([m,m]) # defino la matriz
b = np.array([[0],[0],[0]],float) # defino el vector
x = np.array([[0],[0],[0]],float) # Vector de Inicio

# Numéro de iteraciones maximo antes de arrojar error
maxite=1000

# Matriz de 3x3 para hacer pruebas
A = np.array([[3,-1,-1],[-1,3,1],[2,1,4],],float)

#aqui se ingresan los valores de la matriz
"""
print("Porfavor ingrese los elementos de la matriz a trabajar con Jacobi\n")
for r in range(0,m):
    for c in range(0,m):
        matriz [r,c]=(input("elemento a["+str(r+1)+","+str(c+1)+"]: "))
        matriz [r,c]=float(matriz[r,c])
        A[r,c]=matriz[r,c]
"""
# Vector Solución para hacer pruebas 
b = np.array([[1],[3],[7],],float)

#aqui se ingresan los valores del vector
"""
print("Porfavor ingrese los elementos del vector\n")
for r in range(0,m):
    b [r]=(input("elemento a["+str(r+1)+"]: "))
"""


def jacobi(a,b,x): 
	n=len(x) 
	t=x.copy()
	for  i  in  range(n): 
		s=0
		for j in range(n): 
			print("\nEstamos en la fila",i+1,"columna",j+1,"con valor ",A[i,j])
			if i==j:
				print("no hago nada")
			if i!=j:
				print("ahora hago el calculo de matriz a en posicion ")
				s=s+a[i,j]*t[j]
				x[i]=(b[i]-s)/a[i,i]
	return x

def jacobim(a,b,x,e,m): 
	n=len(x)  
	t=x.copy()
	for  k  in  range(m): 
		x=jacobi(a,b,x)
		d=np.linalg.norm(np.array(x)-np.array(t),np.inf)
		print ("Para la iteración "+str(k+1)+": X = "+str(np.transpose(x.round(2)))+"\tError: "+str(abs(d)))
		if d<e:
			return [x,k] 
		else:
			t=x.copy() 
	return [[],m]

print ("\nMatriz A:")
pprint.pprint(A)
print ("\nVector b:")
pprint.pprint(b)

print("")

# X es la solución y k las iteraciones
[x,k]=jacobim(A,b,x,1.e-14,maxite)

if(k==maxite):
	print("\nEl método diverge o no converge para la cota de error pedido")

else: 
	print("\nEl vector 'x' es:")
	print(x)

	print("\nEl numero de iteraciones es: "+str(k+1))