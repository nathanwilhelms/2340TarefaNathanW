import numpy as np
import matplotlib.pyplot as plt

# TAREFA 3 - QUESTAO 3 ITEM A
# f(x) = 4x - 1.8x^2 + 1.2x^3 - 0.3x^4
# grafico da funcao

# definicao da funcao original
def f(x):
    return 4*x - 1.8*x**2 + 1.2*x**3 - 0.3*x**4

# definicao da derivada
def df(x):
    return 4 - 3.6*x + 3.6*x**2 - 1.2*x**3

# METODO GRAFICO
x = np.linspace(-2, 4, 1000)
plt.figure()
plt.plot(x, f(x))
plt.axhline(0, color='k')
plt.title("Questao 3: 4x - 1.8x^2 + 1.2x^3 - 0.3x^4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# valores nas extremidades e no meio do intervalo
print("f(-2) =", f(-2))
print("f(0) =", f(0))
print("f(2) =", f(2))
print("f(4) =", f(4))

# a derivada troca de sinal uma unica vez, entao o intervalo e unimodal
print("df(-2) =", df(-2))
print("df(2) =", df(2))
print("df(4) =", df(4))

# BUSCA INCREMENTAL NA DERIVADA, PARA LOCALIZAR O MAXIMO
n = 10000
m = np.linspace(-2, 4, n)
intervalos = []

for i in range(n-1):
    if df(m[i])*df(m[i+1]) < 0:
        intervalos.append([m[i], m[i+1]])

matriz_intervalos = np.array(intervalos)
print("Matriz de Intervalos [xl, xu] onde df troca de sinal:")
print(matriz_intervalos)
print("Numero de pontos otimos no intervalo:", len(matriz_intervalos))
