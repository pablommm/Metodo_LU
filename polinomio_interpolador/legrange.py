# Polinomio interpolador

import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

"""
print("\n---------------------------------------------")
print ("*********Polinomio interpolador de Legrange*********")
print("\n---------------------------------------------")
# en esta seccion definimos las cotas
print("Generaremos 20 numeros al azar, ahora necesitaremos establecer las cotas")
maximo=int(input("Indique el valor maximo que podran tomar: "))
minimo=int(input("Indique ahora el valor minimo que podran tomar: "))
banned_x = []#  aqui almacenamos los valores en x que ya se tomaron para que no se repitan

lista_de_numeros = [] # almacenamos los vectores que usaremos
print("\n---------------------------------------------")

for i in range (20):
    punto=[]
    for r in range(2):
        n=random.randrange(minimo,maximo)
        if(r == 0):
            while(banned_x.count(n) > 0):
                n=random.randrange(minimo,maximo)
                print("Se repitio el valor: ", n)
            banned_x.append(n)
            print("Se baneo el valor: ", n)
        punto.append(n)
        print("Agregue el valor: ",n)
        print("Se agrego el punto: ", punto)
    lista_de_numeros.append(punto)

time.sleep(1)# hacemos una pausa para mostrar la lista de puntos
lista_de_numeros = sorted(lista_de_numeros)
#lista_de_numeros = [[37, 25], [40, 2], [11, 34], [12, 9], [46, 9], [1, 49], [31, 20]]
print("\nAsi quedo la lista de vectores \n",lista_de_numeros)

# aqui separamos en valores en X y valores en Y
valores_en_x = []
valores_en_y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==0):
            valores_en_x.append(lista_de_numeros[i][j])
        else:
            valores_en_y.append(lista_de_numeros[i][j])


time.sleep(1) # hacemos una pausa para mostrar los valores por separado

lista_numeros_descendente = lista_de_numeros.copy()
lista_numeros_ascendente = lista_de_numeros.copy()

def myFunc(e):
  return e[0]

lista_numeros_descendente.sort(reverse=False, key=myFunc)
lista_numeros_ascendente.sort(reverse=True, key=myFunc)

xi=valores_en_x
print("\nLos valores en x son: ",xi)
fi=valores_en_y
print("\nLos valores en y son: ",fi)
"""



def intepolacion_legrange(lista_de_numeros):
    """
    print("\n---------------------------------------------")
    print("\n Empezamos a calcular por el metodo de legrange  ")
    print("\n---------------------------------------------")
    """
    # aqui separamos en valores en X y valores en Y
    valores_en_x = []
    valores_en_y = []
    for i in range(len(lista_de_numeros)):
        for j in range (2):
            if(j==0):
                valores_en_x.append(lista_de_numeros[i][j])
            else:
                valores_en_y.append(lista_de_numeros[i][j])
    
    xi=valores_en_x
    fi=valores_en_y
    ################################ aqui comenzamos a calcular ################################


    # definimos la variable simbolica
    x = sym.Symbol('x')
    #  inicializamos el polinomio
    polinomio = 0
    """
    f = sym.Symbol('x')
    polinomio = sym.Poly(2*f**3 + 4*f**2 - 5*f + 1, f)
    grado = polinomio.degree()
    """

    for i in range(len(lista_de_numeros)):
        numerador = 1
        denominador = 1
        for j in range(len(lista_de_numeros)):
            if j!=i:
                numerador = numerador*(x-xi[j])
                denominador = denominador * (xi[i]- xi[j])
        
        time.sleep(1)
        print("\n-----------------------------------------")
        print("Iteracion numero: ",i)
        print("\n-----------------------------------------")
        #print("\nAsi va quedando el numerador: ",numerador)       
        #print("\nAsi va quedando el denominador: ",denominador)
        print("\nAsi va quedando el polinomio: \n", polinomio)
        L = numerador/denominador
        #print("asi va quedando L: ", L)
        polinomio = polinomio + L * fi[i] # aqui vamos almacenando las partes del polinomio que se van almacenando
        

            
    time.sleep(2)
    #print("El polinomio con legrange sin simplificar es ",polinomio)
    polisimp = polinomio.expand()
    print("\n-----------------------------------------")
    print("\nEsta es la forma final del polinomio: \n",polisimp)
    print("\n-----------------------------------------")

    cualquiera = sym.Poly(polinomio)

    print("\nEl grado del polinomio es: ", cualquiera.degree())

    ################################ aqui comenzamos a graficar ################################
    """
    pol_legrange = sym.lambdify(x,polisimp)

    valor_en_y = cualquiera.subs(x,0)
    #print("valor en y es ", valor_en_y)
    a= min(xi)
    #print("El valor minimo de x es: ",a)
    b= max(xi)
    #print("El valor maximo de x es: ",b)
    pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
    pyi = pol_legrange(pxi)# los valores de Y son los valores en X valuados en el polinomio
    plt.title('Interpolación de Lagrange pero usamos la escala de forma exponencial')
    plt.scatter(xi,fi)#los puntos
    plt.plot(pxi,pyi,color='red')
    plt.grid()
    for i, j in zip(xi, fi):
        plt.annotate(f'({i}, {j})', (i, j), textcoords="offset points", xytext=(0,10), ha='center')
    plt.yscale('symlog')
    plt.show()
    """
def polinomio_legrange(lista_de_numeros):

    # aqui separamos en valores en X y valores en Y
    valores_en_x = []
    valores_en_y = []
    for i in range(len(lista_de_numeros)):
        for j in range (2):
            if(j==0):
                valores_en_x.append(lista_de_numeros[i][j])
            else:
                valores_en_y.append(lista_de_numeros[i][j])
    
    xi=valores_en_x
    fi=valores_en_y
    ################################ aqui comenzamos a calcular ################################

    # definimos la variable simbolica
    x = sym.Symbol('x')
    #  inicializamos el polinomio
    polinomio = 0

    for i in range(len(lista_de_numeros)):
        numerador = 1
        denominador = 1
        for j in range(len(lista_de_numeros)):
            if j!=i:
                numerador = numerador*(x-xi[j])
                denominador = denominador * (xi[i]- xi[j])
        L = numerador/denominador
        polinomio = polinomio + L * fi[i] # aqui vamos almacenando las partes del polinomio que se van almacenando

    #print("El polinomio con legrange sin simplificar es ",polinomio)
    #polisimp = polinomio.expand()
    funcion = sym.lambdify(x,polinomio)
    #polinomio = sym.Poly(polinomio)
    return funcion
    