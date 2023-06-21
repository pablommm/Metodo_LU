import sympy as sym

def derivada(funcion):
    x = sym.Symbol("x")
    return sym.Derivative(funcion).doit()

expresion = input("ingrese una funcion f(x):")
print("Su derivada es: ", derivada(expresion))