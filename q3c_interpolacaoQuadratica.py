import numpy as np
import matplotlib.pyplot as plt

# TAREFA 3 - QUESTAO 3 ITEM C
# f(x) = 4x - 1.8x^2 + 1.2x^3 - 0.3x^4
# maximo pela interpolacao quadratica, com x1 = 1.75, x2 = 2 e x3 = 2.5

# definicao da funcao original
def f(x):
    return 4*x - 1.8*x**2 + 1.2*x**3 - 0.3*x**4

# criterio de parada SCARVOROUGHT, 1966
na = 6
Eppara = 0.5*10**(2-na)
print("Valor de Eppara:", Eppara)

# INTERPOLACAO QUADRATICA
x1 = 1.75
x2 = 2
x3 = 2.5
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

# grafico com o ponto encontrado
x = np.linspace(1, 3, 1000)
plt.figure()
plt.plot(x, f(x))
plt.plot(x4, f(x4), 'ro')
plt.title("Questao 3c: maximo pela interpolacao quadratica")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
