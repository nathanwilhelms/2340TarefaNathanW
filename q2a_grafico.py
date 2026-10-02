import numpy as np
import matplotlib.pyplot as plt

# TAREFA 3 - QUESTAO 2 ITEM A
# f(x) = -1.5x^6 - 2x^4 + 12x
# grafico da funcao

# definicao da funcao original
def f(x):
    return -1.5*x**6 - 2*x**4 + 12*x

# definicao da derivada
def df(x):
    return -9*x**5 - 8*x**3 + 12

# METODO GRAFICO
x = np.linspace(-2, 2, 1000)
plt.figure()
plt.plot(x, f(x))
plt.axhline(0, color='k')
plt.title("Questao 2: -1.5x^6 - 2x^4 + 12x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

# olhando o grafico, o maximo esta entre x = 0 e x = 2
print("f(0) =", f(0))
print("f(1) =", f(1))
print("f(2) =", f(2))

# a derivada troca de sinal dentro do intervalo, o que confirma o maximo
print("df(0) =", df(0))
print("df(1) =", df(1))

# BUSCA INCREMENTAL NA DERIVADA, PARA LOCALIZAR O MAXIMO
n = 10000
m = np.linspace(0, 2, n)
intervalos = []

for i in range(n-1):
    if df(m[i])*df(m[i+1]) < 0:
        intervalos.append([m[i], m[i+1]])

matriz_intervalos = np.array(intervalos)
print("Matriz de Intervalos [xl, xu] onde df troca de sinal:")
print(matriz_intervalos)
print("Numero de pontos otimos no intervalo:", len(matriz_intervalos))
