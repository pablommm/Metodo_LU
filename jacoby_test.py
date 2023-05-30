import numpy as np
import pprint

print('MÉTODO DE JACOBI',end="\n\n")

'''
La siguiente función en Python recibe la matriz de coeficientes  a  y el vector de constantes b  de un sistema lineal.
Adicionalmente recibe un vector inicial  x, la estimación del error "e" y el máximo de iteraciones permitidas m. Esta 
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

A = np.zeros([m,m]) # defino la matriz original
D = np.zeros([m,m]) # defino la matriz diagonal
D_inversa= np.zeros([m,m]) # defino la matriz diagonal inversa
L = np.zeros([m,m]) # defino la matriz inferior
U = np.zeros([m,m]) # defino la matriz superior
b = np.array([[0],[0],[0]],float) # defino el vector solucion
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

#--------------------------------------------------------------------------------
print("\nUsted ingreso la matriz A")
print(A)

print("\nUsted ingreso el vector b")
print(b)

for  r  in  range(m):
    for  c  in  range(m):
        if (r==c):
            
            D[r,c] = A[r,c]
            #print("vamos formando la matriz diagonal")
            #print(D)
        if(r<c):
            
            U[r,c] = A[r,c]
            #print("vamos armando la matriz superior")
            #print(U)
        if(r>c):
            
            L[r,c] = A[r,c]
            #print("vamos armando la matriz inferior")
            #print(L)
            

print("\nAsi quedo la diagonal D")
print(D)
print("\nAsi quedo la inferior L")
print(L)
print("\nAsi quedo la superior U")
print(U)
            
print("\nCalculamos la inversa de la diagonal")
for  r  in  range(m):
    for  c  in  range(m):
        if (r==c):
            D_inversa[r,c]=np.around((1/A[r,c]),2)
            
print(D_inversa)
suma_matriz= np.zeros([m,m])
print("\nSuma de matriz U + L")
for  r  in  range(m):
    for  c  in  range(m):
        suma_matriz[r,c]=L[r,c]+ U[r,c]
        
print(suma_matriz)

print("\nLa diagonal inversa multiplicada con la suma de L+U nos da: ")
result = np.dot(D_inversa,suma_matriz)
print(result)

print("\nLa diagonal inversa multiplicada con el vector b nos da: ")
result = np.dot(D_inversa,b)
print(result)



"""
print("\n aqui comienzan las iteraciones")

def jacobi(a,b,x): 
	n=len(x) 
	t=x.copy()
	for  i  in  range(n): 
		s=0
		for j in range(n): 			
			if i!=j:
				
				print("\nen la matriz fila",i+1,"en al columna",j+1,"tiene el valor",a[i,j])
				print("esta siendo multiplicado la columna",j+1,"del vector valiendo",t[j])
				s=s+a[i,j]*t[j]
				print("da como resultado de s es",s)
				print("")
				print("al vector b, en posicion",i+1,"con valor",b[i])
				print("le restamos el valor s",s+1)
				print("esto lo dividimos por la diagonal de la matriz en la posicion",i+1,i+1, "siendo",a[i,i])
				x[i]=(b[i]-s)/a[i,i]
				print("\nnos da como resultado",x[i])
	return x

def jacobim(a,b,x,e,m): 
	n=len(x)  
	t=x.copy()
	for  k  in  range(m): 
		x=jacobi(a,b,x)
		d=np.linalg.norm(np.array(x)-np.array(t),np.inf) # este es el calculo del margen de error
		print ("\nPara la iteración "+str(k+1)+": X = "+str(np.transpose(x.round(2)))+"\tError: "+str(abs(d)))
		if d<e:
			return [x,k] 
		else:
			t=x.copy() 
	return [[],m]


# X es la solución y k las iteraciones
[x,k]=jacobim(A,b,x,1.e-1,maxite)

if(k==maxite):
	print("\nEl método diverge o no converge para la cota de error pedido")

else: 
	print("\nEl vector 'x' es:")
	print(x)

	print("\nEl numero de iteraciones es: "+str(k+1))
 
print("\nEl valor de x es:", x[0])
print("\nEl valor de y es:", x[1])
print("\nEl valor de z es:", x[2],"\n")

"""