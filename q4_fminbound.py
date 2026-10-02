import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# TAREFA 3 - QUESTAO 4
# f(x) = 2x + 3/x
# minimo pela funcao fminbound do Python

# definicao da funcao original
def f(x):
    return 2*x + 3/x

# definicao da derivada
def df(x):
    return 2 - 3/x**2

# METODO GRAFICO
x = np.linspace(0.1, 5, 1000)
plt.figure()
plt.plot(x, f(x))
plt.title("Questao 4: 2x + 3/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# a funcao tem uma assintota em x = 0, por isso a busca fica no ramo positivo
# no ramo negativo a funcao cai para menos infinito e nao existe minimo
print("f(0.1) =", f(0.1))
print("f(1) =", f(1))
print("f(5) =", f(5))

# FUNCAO fminbound DO PYTHON
# sintaxe: xmin = scipy.optimize.fminbound(func, x1, x2)
xmin = opt.fminbound(f, 0.1, 5)
print("Minimo pela fminbound: x =", xmin)
print("Valor da funcao no minimo: f(x) =", f(xmin))

# CONFERINDO PELA DERIVADA
# df(x) = 0 em x = sqrt(3/2)
xanalitico = np.sqrt(3/2)
print("Resultado analitico: x =", xanalitico, "f(x) =", f(xanalitico))
print("df no ponto da fminbound:", df(xmin))
