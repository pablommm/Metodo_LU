import matplotlib.pyplot as plt
import numpy as np
import random
import sympy as sym



def graficacion(valores_en_x,valores_en_y,funcion):
    x = sym.Symbol('x')
    print("\n---------------------------------------------")
    print("\n ahora graficaremos lo obtenido ")
    print("\n---------------------------------------------")

    #print("valor en y es ", valor_en_y)
    a= min(valores_en_x)
    #print("El valor minimo de x es: ",a)
    b= max(valores_en_x)
    #print("El valor maximo de x es: ",b)

    #fun_legrange_al_reves = sym.lambdify(x,resultado_legrange_al_reves)
    pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
    pyi = funcion(pxi)# los valores de Y son los valores en X valuados en el polinomio
    #plt.plot(pxi,pyi,color='blue')

    #fun_newton = sym.lambdify(x,funcion)
    pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
    pyi = funcion(pxi)# los valores de Y son los valores en X valuados en el polinomio
    #plt.plot(pxi,pyi,color='red')

    plt.plot(pxi,pyi,color='blue')
    plt.plot(pxi,pyi,color='red')
    plt.title('usamos la escala de forma exponencial')
    plt.scatter(valores_en_x,valores_en_y) #los puntos
    plt.grid()
    for i, j in zip(valores_en_x, valores_en_y):
        plt.annotate(f'({i}, {j})', (i, j), textcoords="offset points", xytext=(0,10), ha='center')
    plt.yscale('symlog')
    plt.show()
    

def graficacion_con_raiz(valores_en_x,valores_en_y,funcion,raiz):
    x = sym.Symbol('x')
    print("\n---------------------------------------------")
    print("\n ahora graficaremos lo obtenido ")
    print("\n---------------------------------------------")

    #print("valor en y es ", valor_en_y)
    a= min(valores_en_x)
    #print("El valor minimo de x es: ",a)
    b= max(valores_en_x)
    #print("El valor maximo de x es: ",b)

    #fun_legrange_al_reves = sym.lambdify(x,resultado_legrange_al_reves)
    pxi = np.linspace(a,b,200)# tomamos el valor "a" mas chico de las X, el valor "b" mas alto, como limitees y hacemos un muestro de 200 puntos
    pyi = funcion(pxi)# los valores de Y son los valores en X valuados en el polinomio
    #plt.plot(pxi,pyi,color='blue')


    plt.plot(pxi,pyi,color='red')
    plt.title('usamos la escala de forma exponencial ')
    plt.scatter(valores_en_x,valores_en_y) #los puntos
    plt.scatter(raiz, funcion(raiz), color='green', label='la raiz encontrada')
    plt.grid()
    for i, j in zip(valores_en_x, valores_en_y):
        plt.annotate(f'({i}, {j})', (i, j), textcoords="offset points", xytext=(0,10), ha='center')
    plt.yscale('symlog')
    plt.show()