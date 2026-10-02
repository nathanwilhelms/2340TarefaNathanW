import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# TAREFA 3 - QUESTAO 5
# campo de temperaturas T(x,y) = 2x^2 + 3y^2 - 4xy - y - 3x
# item a) curvas de nivel e superficie
# item b) minimo pela funcao minimize do Python

# definicao da funcao de duas variaveis
def T(x, y):
    return 2*x**2 + 3*y**2 - 4*x*y - y - 3*x

# a funcao minimize recebe um unico vetor, entao escrevo a mesma funcao assim
def Tvetor(v):
    x = v[0]
    y = v[1]
    return 2*x**2 + 3*y**2 - 4*x*y - y - 3*x

# MALHA DE PONTOS
n = 200
x = np.linspace(-1, 6, n)
y = np.linspace(-1, 5, n)
X, Y = np.meshgrid(x, y)
Z = T(X, Y)

# ITEM A - CURVAS DE NIVEL
plt.figure()
curvas = plt.contour(X, Y, Z, 30)
plt.clabel(curvas, inline=1, fontsize=8)
plt.title("Questao 5a: curvas de nivel de T(x,y)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

# ITEM A - SUPERFICIE
figura = plt.figure()
eixo = figura.add_subplot(111, projection='3d')
eixo.plot_surface(X, Y, Z, cmap='viridis')
eixo.set_title("Questao 5a: superficie de T(x,y)")
eixo.set_xlabel("x")
eixo.set_ylabel("y")
eixo.set_zlabel("T(x,y)")
plt.show()

# ITEM B - FUNCAO minimize DO PYTHON
# sintaxe: resultado = scipy.optimize.minimize(func, x0)
# o metodo de Nelder-Mead usa somente valores da funcao, sem derivadas
v0 = [0, 0]
resultado = opt.minimize(Tvetor, v0, method='Nelder-Mead')
print("Minimo pela minimize: x =", resultado.x[0], "y =", resultado.x[1])
print("Valor da funcao no minimo: T =", resultado.fun)
print("Numero de avaliacoes da funcao:", resultado.nfev)

# CONFERINDO PELAS DERIVADAS PARCIAIS
# dT/dx = 4x - 4y - 3 = 0 e dT/dy = 6y - 4x - 1 = 0
# resolvendo o sistema, x = 2.75 e y = 2
print("Resultado analitico: x =", 2.75, "y =", 2, "T =", T(2.75, 2))
print("dT/dx no ponto da minimize:", 4*resultado.x[0] - 4*resultado.x[1] - 3)
print("dT/dy no ponto da minimize:", 6*resultado.x[1] - 4*resultado.x[0] - 1)
