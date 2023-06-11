import numpy as np
import matplotlib.pyplot as plt
import random
import sympy as sym
import time
time.sleep(1)
print("\n---------------------------------------------")
print ("*********Polinomio interpolador de Newtown*********")
print("\n---------------------------------------------")

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
                #print("se repitio el valor", n)
            banned_x.append(n)
            #print("se baneo el valor", n)
        punto.append(n)
        #print("agregue el valor ",n)
        #print("punto ", punto)
    lista_de_numeros.append(punto)

time.sleep(1)       
print("\nAsi me quedo la lista de vectores ",lista_de_numeros)

# Aqui separamos en valores en X y valores en Y
x = []
y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==0):
            x.append(lista_de_numeros[i][j])
        else:
            y.append(lista_de_numeros[i][j])

print("\nLos valores en x son: ",x)
print("\nLos valores en y son: ",y)
# sacamos el grado del polinomio interpolador (Newton)
grado_newton = len(x) - 1
print("\nEste es el grado del polinomio interpolador en newton:", grado_newton)
time.sleep(1)

print("\n---------------------------------------------")
print("\n Empezamos a calcular las diferencias divididas  ")
print("\n---------------------------------------------")

# Empezamos a calcular las diferencias divididas
# creamos la matriz
diferencias_divididas = np.zeros((grado_newton + 1, grado_newton + 1))
# inicializamos la primer columan de la matriz con los valores en Y
diferencias_divididas[:, 0] = y 

print("\n creamos una matriz de 20x20 para almacenar las diferencias divididas, comenzamos agregando los valores en y: ",diferencias_divididas)
time.sleep(1)

# utilizamos este bucle para calcular el resto de las diferencias divididas
for j in range(1, grado_newton + 1):
    for i in range(j, grado_newton + 1):
        diferencias_divididas[i, j] = (diferencias_divididas[i, j - 1] - diferencias_divididas[i - 1, j - 1]) / (x[i] - x[i - j])
        #print("\n la matriz paso a paso : \n",diferencias_divididas)



# el metodo para construir el polinomio interpolador (Newton)
def polinomio_interpolador_newton(x_eval):
    resultado = diferencias_divididas[0, 0]
    producto = 1
    for i in range(1, grado_newton + 1):
        producto *= (x_eval - x[i - 1])
        resultado += diferencias_divididas[i, i] * producto
    return resultado

time.sleep(1)        

# Graficamos el polinomio interpolador y los pares de datos
x_vals = np.linspace(minimo, maximo, 100)
y_vals = polinomio_interpolador_newton(x_vals)
print("\n Despues de hacer los calculos asi queda la matriz : \n",diferencias_divididas)


plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Polinomio interpolador (Newton)')


plt.scatter(x, y, color='red', label='Pares de datos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación polinómica por el método de Newton')
plt.legend()
plt.grid(True)
plt.show()


print("\n---------------------------------------------")
print("\n Ahora ordenamos los valores al reves \n ")
print("\n---------------------------------------------")
# Ordenamos los pares al revés
x_rev = x[::-1]
y_rev = y[::-1]

print("\nLos valores en x son: ",x_rev)
print("\nLos valores en y son: ",y_rev)
time.sleep(1)

# Calcular el polinomio interpolador con Legange
print("\n---------------------------------------------")
print ("*********Polinomio interpolador de Legrange*********")
print("\n---------------------------------------------")
# el grado del polinomio interpolador 
print("\n el gradro de polinomio es \n", len(x_rev))

# definimos la variable simbolica
x = sym.Symbol('x')
#  inicializamos el polinomio
polinomio = 0

for i in range(len(lista_de_numeros)):
    numerador = 1
    denominador = 1
    for j in range(len(lista_de_numeros)):
        if j!=i:
            numerador = numerador*(x-x_rev[j])
            denominador = denominador * (x_rev[i]- x_rev[j])
    
    time.sleep(1)
    print("\n-----------------------------------------")
    print("Iteracion numero: ",i)
    print("\n-----------------------------------------")
    #print("\nAsi va quedando el numerador: ",numerador)       
    #print("\nAsi va quedando el denominador: ",denominador)
    print("\nAsi va quedando el polinomio: \n", polinomio)
    L = numerador/denominador
    polinomio = polinomio + L * y_rev[i] # aqui vamos almacenando las partes del polinomio que se van almacenando
    
time.sleep(1)
#print("El polinomio con legrange sin simplificar es ",polinomio)
polisimp = polinomio.expand()
print("\n-----------------------------------------")
print("\nEsta es la forma final del polinomio con Lagrange: \n",polisimp)
print("\n-----------------------------------------")

################################ aqui comenzamos a graficar ################################

pol = sym.lambdify(x,polisimp)

a= min(x_rev)
#print("El valor minimo de x es: ",a)
b= max(x_rev)
#print("El valor maximo de x es: ",b)

pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
pyi = pol(pxi)# los valores de Y son los valores en X valuados en el polinomio

plt.figure()
plt.scatter(x_rev,y_rev)#los puntos
for i, j in zip(x_rev, y_rev):
    plt.annotate(f'({i}, {j})', (i, j), textcoords="offset points", xytext=(0,10), ha='center')
plt.plot(pxi,pyi,color='red')
plt.grid()
plt.show()


print("\n---------------------------------------------")
print("\n Ahora desordenamos los valores  \n ")
print("\n---------------------------------------------")
random.shuffle(lista_de_numeros)

print("\nLista de numeros desordenada",lista_de_numeros)

polinomio = 0

for i in range(len(lista_de_numeros)):
    numerador = 1
    denominador = 1
    for j in range(len(lista_de_numeros)):
        if j!=i:
            numerador = numerador*(x-x_rev[j])
            denominador = denominador * (x_rev[i]- x_rev[j])
    
    time.sleep(1)
    print("\n-----------------------------------------")
    print("Iteracion numero: ",i)
    print("\n-----------------------------------------")
    #print("\nAsi va quedando el numerador: ",numerador)       
    #print("\nAsi va quedando el denominador: ",denominador)
    print("\nAsi va quedando el polinomio: \n", polinomio)
    L = numerador/denominador
    polinomio = polinomio + L * y_rev[i] # aqui vamos almacenando las partes del polinomio que se van almacenando
    
time.sleep(1)
#print("El polinomio con legrange sin simplificar es ",polinomio)
polisimp = polinomio.expand()
print("\n-----------------------------------------")
print("\nEsta es la forma final del polinomio con Lagrange: \n",polisimp)
print("\n-----------------------------------------")

################################ aqui comenzamos a graficar ################################

pol = sym.lambdify(x,polisimp)

a= min(x_rev)
#print("El valor minimo de x es: ",a)
b= max(x_rev)
#print("El valor maximo de x es: ",b)

pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
pyi = pol(pxi)# los valores de Y son los valores en X valuados en el polinomio

plt.figure()
plt.scatter(x_rev,y_rev)#los puntos
for i, j in zip(x_rev, y_rev):
    plt.annotate(f'({i}, {j})', (i, j), textcoords="offset points", xytext=(0,10), ha='center')
plt.plot(pxi,pyi,color='red')
plt.grid()
plt.show()

# Función para encontrar una raíz del polinomio interpolador por el método de Newton

"""
def encontrar_raiz_newton(polinomio, x_inicial, tolerancia=1e-6, max_iter=100):
    x_actual = x_inicial
    iteracion = 0

    while np.abs(polinomio(x_actual)) > tolerancia and iteracion < max_iter:
        x_actual = x_actual - polinomio(x_actual) / polinomio_interpolador_newton(x_actual)
        iteracion += 1

    if np.abs(polinomio(x_actual)) <= tolerancia:
        return x_actual
    else:
        return None

# Encontrar una raíz del polinomio interpolador (Newton)
raiz = encontrar_raiz_newton(polinomio_interpolador_newton, x[0])
print("Raíz del polinomio interpolador (Newton):", raiz)
"""