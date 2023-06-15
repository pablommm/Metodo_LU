import numpy as np
import pprint
import time 
import matplotlib.pyplot as plt

print('MÉTODO DE JACOBI',end="\n\n")

'''
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
n = 0
A = np.zeros([m,m]) # defino la matriz original
D = np.zeros([m,m]) # defino la matriz diagonal
D_inversa= np.zeros([m,m]) # defino la matriz diagonal inversa
L = np.zeros([m,m]) # defino la matriz inferior
U = np.zeros([m,m]) # defino la matriz superior
b = np.array([[0],[0],[0]],float) # defino el vector solucion
x = np.array([[0],[0],[0]],float) # Vector de Inicio
x0 = np.array([[0],[0],[0]],float)
e = 0.00001 # el margen de error
# Numéro de iteraciones maximo antes de arrojar error
maxite = 1000
margen = 1000
array_de_errores = []
# Matriz de 3x3 para hacer pruebas
A = np.array([[3,-1,-1],[-1,3,1],[2,1,4],],float)

#aqui se ingresan los valores de la matriz
"""
print("Porfavor ingrese los elementos de la matriz(3x3) a trabajar con Jacobi\n")
for r in range(0,m):
    for c in range(0,m):
        A [r,c]=(input("elemento a["+str(r+1)+","+str(c+1)+"]: "))
        A [r,c]=float(A[r,c])
"""
# Vector Solución para hacer pruebas 
b = np.array([[1],[3],[7],],float)
"""
#aqui se ingresan los valores del vector
print("Porfavor ingrese los elementos del vector(3)\n")
for r in range(0,m):
    b [r]=(input("elemento a["+str(r+1)+"]: "))
    
"""
#--------------------------------------------------------------------------------
print("\nUsted ingreso la matriz A")
print(A)
time.sleep(1)
print("\nUsted ingreso el vector b")
print(b)
time.sleep(1)
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
time.sleep(2)     
print("\nCalculamos la inversa de la diagonal")
for  r  in  range(m):
    for  c  in  range(m):
        if (r==c):
            D_inversa[r,c]=np.around((1/A[r,c]),2)
            
print(D_inversa)
time.sleep(1)
xk = np.array([[0],[0],[0]],float)

print("El metodo tomara las partes recien vistas para obtener de manera iterativa\n",
       "una aproximacion a la solucion usando la propiedad:\n", 
       "x(k+1) = -D-1 (L+U) x(k) + D-1 b\n",
       "siendo en el primer paso x(k) el vector [0, 0, 0]")
time.sleep(1)
t0 = np.dot(-D_inversa, (L+U))
print("-D-1 (L+U) = \n", t0)
t1 = np.array(np.dot(D_inversa, b))
print("D-1 b = \n", t1)
time.sleep(2)
while(margen > e):
    #X(k+1) = -D-1 (L+U) x(k) + D-1 b
	#t2 = np.array(np.dot(t0, x0))
	print("Estas son mis ecuaciones actuales:")
	xkn = t1[0] + t0[0][1]*x0[1] + t0[0][2]*x0[2]
	ykn = t1[1] + t0[1][0]*x0[0] + t0[1][2]*x0[2]
	zkn = t1[2] + t0[2][0]*x0[0] + t0[2][1]*x0[1]
	print("X(k+1) = ", t1[0], " + ", t0[0][1], "*", x0[1], " + ", t0[0][2], "*", x0[2])
	print("Y(k+1) = ", t1[1], " + ", t0[1][0], "*", x0[0], " + ", t0[1][2], "*", x0[2])
	print("Z(k+1) = ", t1[2], " + ", t0[2][0], "*", x0[0], " + ", t0[2][1], "*", x0[2])
	print("\n-----------------------------------------------------------------------------------")
	print("X(k+1) = ", xkn)
	print("Y(k+1) = ", ykn)
	print("Z(k+1) = ", zkn)
	xk = np.array([xkn, ykn, zkn])
	
	#print("x0 = " + str(x0))
	#print("D(-1) = " + str(D_inversa))
	#print("D(-1)*b = " + str(np.dot(D_inversa, b)))
	#print("L + U = " + str(L + U))
	#print("D(-1)*(L + U) = " + str(np.dot(D_inversa, L + U)))
	#print("D(-1)*(L + U)*x0 = " + str(np.dot(np.dot(D_inversa, (L+U)), x0)))
	
	n += 1
	print("Mi paso actual de X(" + str(n) + ") es igual a:\n" + str(xk))
	if(margen > np.linalg.norm(np.array(xk)-np.array(x0),np.inf)):
		margen = np.linalg.norm(np.array(xk)-np.array(x0),np.inf)
	else:
		print("El sistema ya no converge ya que la norma de x(k+1) - x(k) no tiende a 0")
		quit()
	print("Mi margen de error actual es de:\n" + str(margen))
	array_de_errores.append(margen)
	x0 = xk.copy()
	print("----------------------------------------\n")
	time.sleep(1)


print("\nMi sistema convergio al vector solucion x =\n" + str(xk.round(3)))
print("\nSe requirieron " + str(n) + " pasos para lograrlo")
print("\nEl margen de error actual es de: " + str(margen))
print("La tolerancia usada es de ",e)

print("----------------------------------------")
print("--------------COMPROBACION--------------")
print("----------------------------------------\n")
# comprobacion

primer_ecuacion=0
segunda_ecuacion=0
tercer_ecuacion=0

for  f  in  range(m):
    for  c  in  range(m):
        if(f==0):
            primer_ecuacion = primer_ecuacion + A[f,c]*xk[c] 
        if(f==1):
            segunda_ecuacion = segunda_ecuacion + A[f,c]*xk[c]
        if(f==2):
            tercer_ecuacion = tercer_ecuacion + A[f,c]*xk[c]
            
print("\nAl remplazar los valores obtenidos por jacobi en el sistemas de ecuaciones podemos comprobar si coinciden con el sistema solucion b")
print("\n (los valores estan truncados)")
print("\n el resultado de remplazar ",xk[0]," en la primer ecuacion da como resultado ",primer_ecuacion," y la solucion esperada es ",b[0])
print("\n el resultado de remplazar ",xk[1]," en la segunda ecuacion da como resultado ",segunda_ecuacion," y la solucion esperada es ",b[1])
print("\n el resultado de remplazar ",xk[2]," en la tercer ecuacion da como resultado ",tercer_ecuacion," y la solucion esperada es ",b[2])


# graficacion tendencia del error

plt.figure()
plt.xlabel('pasos de la iteracion')
plt.ylabel('valor del margen')
plt.title('progreso en el margen de error con jacobi')
plt.plot(range(len(array_de_errores)),array_de_errores,color='red')
plt.grid()
plt.show()
