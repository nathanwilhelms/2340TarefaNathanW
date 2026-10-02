import numpy as np
import matplotlib.pyplot as plt

# TAREFA 3 - QUESTAO 3 ITEM B
# f(x) = 4x - 1.8x^2 + 1.2x^3 - 0.3x^4
# maximo pela busca da razao aurea, com xl = -2 e xu = 4

# definicao da funcao original
def f(x):
    return 4*x - 1.8*x**2 + 1.2*x**3 - 0.3*x**4

# criterio de parada SCARVOROUGHT, 1966
na = 6
Eppara = 0.5*10**(2-na)
print("Valor de Eppara:", Eppara)

# razao aurea, raiz positiva de phi^2 - phi - 1 = 0
phi = (1 + np.sqrt(5))/2
print("Valor de phi:", phi)

# BUSCA DA RAZAO AUREA
xl = -2
xu = 4
Ea = 100
i = 0

print("BUSCA DA RAZAO AUREA")
while Ea > Eppara:
    d = (phi - 1)*(xu - xl)
    x1 = xl + d
    x2 = xu - d

    # o problema e de MAXIMO, entao fica o ponto de maior f(x)
    if f(x1) > f(x2):
        xotm = x1
        xl = x2
    else:
        xotm = x2
        xu = x1

    Ea = (2 - phi)*abs((xu - xl)/xotm)*100
    i = i + 1
    print(i, xl, xu, xotm, f(xotm), Ea)

print("Maximo pela razao aurea: x =", xotm)
print("Valor da funcao no maximo: f(x) =", f(xotm))
print("Iteracoes:", i)

# grafico com o ponto encontrado
x = np.linspace(-2, 4, 1000)
plt.figure()
plt.plot(x, f(x))
plt.plot(xotm, f(xotm), 'ro')
plt.title("Questao 3b: maximo pela razao aurea")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
