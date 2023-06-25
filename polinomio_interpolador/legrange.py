# Polinomio interpolador

import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


def interpolacion_legrange(lista_de_numeros): # este muestra mensajes pero no devuelve nada
    
    print("\n---------------------------------------------")
    print("\n Aqui comienza legrange ")
    print("\n---------------------------------------------")
    
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
        

            
    time.sleep(1)
    #print("El polinomio con legrange sin simplificar es ",polinomio)
    polisimp = polinomio.expand()
    print("\n-----------------------------------------")
    print("\nEsta es la forma final del polinomio: \n",polisimp)
    print("\n-----------------------------------------")

    cualquiera = sym.Poly(polinomio)

 
def polinomio_legrange(lista_de_numeros): # este no muesta mensajes pero devuelve un polinomio

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
    return polinomio
    