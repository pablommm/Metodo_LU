import math
import time
from legrange import polinomio_legrange
#from Entrega_interpolacion import lista_de_numeros,x

# funcion original
#funcion = polinomio_legrange(lista_de_numeros)
lista_de_numeros_aux= [[31, 54], [72, 91], [80, 59], [27, 70]]
x_test = [31, 72, 80, 27]
#punto de partida
#x1 = x_test[1]
#x2 = x_test[2]
#criterio de parada con margen de error
#tolerancia = 0.000001
#funcion = polinomio_legrange(lista_de_numeros_aux)

# funcion = lambda x: x**3 + 4*(x**2) -10
# x = sym.Symbol('x')
# polinomio = sym.Poly(polinomio)
# f = polinomio_legrange(lista_de_numeros_aux)

def secante (f,x1,x2,tolerancia):
    
    error =10000
    n = 0
    x3 = 0
    
    while error > tolerancia:
        if((f(x2)-f(x1))==0):
            x2 = x2 + 5
        
        x3 = x2 - (f(x2)*(x2-x1)/ (f(x2)-f(x1)))
        x1 = x2
        x2 = x3
        error = abs(f(x3))
        n += 1
        
        print("error:",error)
        print("valor x3:",x3)
        print("Valor n:",n)
        
        time.sleep(1)
    print("solucion aproxiamada : {: .4f}".format(x3))
    print("numero de iteracion : {:d}".format(n))
    print("la tolerancia usada es de: ",tolerancia)
          
#secante(polinomio_legrange(lista_de_numeros_aux),x1,x2,tolerancia)
