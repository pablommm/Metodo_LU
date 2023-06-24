# Polinomio interpolador
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
#from Entrega_interpolacion import lista_de_numeros

banned_x = []

lista_de_numeros = []

print("Debemos geneara 20 numeros al azar")
maximo=int(input("Indique el valor maximo que podra tomar: "))
minimo=int(input("Indique ahora el valor minimo que podra tomar: "))


print("\n---------------------------------------------")

for i in range (5):
    punto=[]
    for r in range(2):
        n=random.randrange(minimo,maximo)
        if(r == 0):
            while(banned_x.count(n) > 0):
                n=random.randrange(minimo,maximo)
                print("se repitio el valor", n)
            banned_x.append(n)
            print("se baneo el valor", n)
        punto.append(n)
        print("agregue el valor ",n)
        print("punto ", punto)
    lista_de_numeros.append(punto)
        
print("asi me quedo la lista de vectores ",lista_de_numeros)

def polinomio_newton(puntos):
    
    print("\n---------------------------------------------")
    print ("*********Polinomio interpolador de Newtown*********")
    print("\n---------------------------------------------")
    # Separate x and y values from the points
    x = [p[0] for p in puntos]
    y = [p[1] for p in puntos]

    # Calculate divided differences
    n = len(x)
    dd = [y]

    for i in range(1, n):
        dd.append([])

        for j in range(n - i):
            diff = (dd[i - 1][j + 1] - dd[i - 1][j]) / (x[j + i] - x[j])
            dd[i].append(diff)

    # Generate the Newton Polynomial Interpolation string
    interpolacion = f'{y[0]}'

    for i in range(1, n):
        termino = ''

        for j in range(i):
            if(j == 0):
                termino += f'(x - {x[j]})'
            else:
                termino += f' * (x - {x[j]})'

        termino += f' * {dd[i][0]}'
        interpolacion += f' + {termino}'
        """ time.sleep(1)
        print("\nEsta es la iteracion numero: ",i)
        print("\nAsi va quedando el polinomio con el metodo de newton :", interpolacion) """
        parseado =sym.parsing.sympy_parser.parse_expr(interpolacion, evaluate=False)
    return parseado

print("El polinomio de newton es: \n", polinomio_newton(lista_de_numeros))

cadena = polinomio_newton(lista_de_numeros)
parseado =sym.parsing.sympy_parser.parse_expr(cadena, evaluate=False)
print("\n El polinomio luego del parseo quedo como: \n", parseado)
#print("RESULTADO: \n", polinomio_newton(lista_de_numeros))

"""
x = sym.Symbol('x') 
resultado = sym.Poly(pn_str) 
grado = resultado.degree()
print("\n-----------------------------------------")  
print(" finalmente obtuve p(", j, ") = \n", resultado)  
print("-----------------------------------------")    
            


plt.title('Interpolación de Newton')
valores_en_x = []
valores_en_y = []
for i in range(len(lista_de_numeros)):
    for j in range (2):
        if(j==0):
            valores_en_x.append(lista_de_numeros[i][j])
        else:
            valores_en_y.append(lista_de_numeros[i][j])
plt.scatter(valores_en_x, valores_en_y)




pol_newton = sym.lambdify(x, resultado.as_expr())
pxi = np.linspace(min(valores_en_x), max(valores_en_x), 200) 
pyi = pol_newton(pxi)



solutions = sym.solve(resultado.as_expr(), x)

print("ENTRO AL AREA DE PRUEBAS")
for d in range(len(valores_en_x)):
    print("\n--------------------------------------")
    print("estoy estudiando el valor: ", valores_en_x[d])
    print("espero el valor: ", valores_en_y[d])
    print("con pol_newton obtuve el valor: ", pol_newton(valores_en_x[d]))
    print("con sym.solve obtuve el valor: ", sym.solve(resultado.as_expr(), valores_en_x[d]))
    print("\n--------------------------------------")
    time.sleep(1)

solutions = sym.solve(resultado.as_expr(), x)

#pyi = sym.solve(resultado.as_expr(), pxi)
plt.plot(pxi, pyi, color='red')
plt.grid()
for i, j in zip(valores_en_x, valores_en_y):
    plt.annotate(f'({i}, {j})', (i, j), textcoords="offset points", xytext=(0,10), ha='center')
plt.yscale('symlog')
plt.show()


"""
