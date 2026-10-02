import numpy as np
import matplotlib.pyplot as plt

# TAREFA 3 - QUESTAO 1 ITEM B
# f(x) = -x^2 + 8x - 12
# verificar se a interpolacao quadratica da o mesmo maximo da derivacao
# aproximacoes iniciais x1 = 0, x2 = 2, x3 = 6

# definicao da funcao original
def f(x):
    return -x**2 + 8*x - 12

# definicao da derivada
def df(x):
    return -2*x + 8

# criterio de parada SCARVOROUGHT, 1966
na = 6
Eppara = 0.5*10**(2-na)
print("Valor de Eppara:", Eppara)

# RESULTADO ANALITICO, PARA COMPARAR DEPOIS
# df(x) = 0 em x = 4
print("Resultado analitico: x =", 4, "f(x) =", f(4))
print("df(4) =", df(4))

# METODO GRAFICO
x = np.linspace(-1, 9, 1000)
plt.figure()
plt.plot(x, f(x))
plt.axhline(0, color='k')
plt.title("Questao 1: -x^2 + 8x - 12")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# INTERPOLACAO QUADRATICA
x1 = 0
x2 = 2
x3 = 6
xold = x2
Epest = 100
i = 0

print("INTERPOLACAO QUADRATICA")
while Epest > Eppara:
    numerador = (x2-x1)**2*(f(x2)-f(x3)) - (x2-x3)**2*(f(x2)-f(x1))
    denominador = (x2-x1)*(f(x2)-f(x3)) - (x2-x3)*(f(x2)-f(x1))
    x4 = x2 - 0.5*numerador/denominador

    Epest = abs((x4-xold)/x4)*100
    xold = x4

    # o problema e de MAXIMO, entao fica o ponto de maior f(x)
    # troca dos pontos para manter os tres que cercam o maximo
    if x4 > x2:
        if f(x4) > f(x2):
            x1 = x2
            x2 = x4
        else:
            x3 = x4
    else:
        if f(x4) > f(x2):
            x3 = x2
            x2 = x4
        else:
            x1 = x4

    i = i + 1
    print(i, x4, f(x4), Epest)

print("Maximo pela interpolacao quadratica: x =", x4)
print("Valor da funcao no maximo: f(x) =", f(x4))
print("Iteracoes:", i)

# a funcao e uma parabola, entao a parabola interpoladora e a propria funcao
# por isso a primeira iteracao ja cai exatamente no maximo
