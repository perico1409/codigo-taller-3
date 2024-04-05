import numpy as np
import matplotlib.pyplot as plt
import taller3 as ta
import grafica_analitica as ga

n = 10
m = 10
V0 = np.zeros((n, m))


V0[:, 0] = -1  
V0[:, -1] = 1  
V0[0, :] = 0  
V0[-1, :] = 0  
V_solucion= ta.laplace_solver(n,m, V0,1e-4)


x = np.linspace(0,n-1,n)
y = np.linspace(0,m-1,m)
X, Y = np.meshgrid(x,y)
Z = ga.V(X,Y)
"Damos una matriz que es el error absoluto"
error = abs(V_solucion - Z)
"Graficamos el error en un mapa de calor"
contour = plt.contourf(X, Y, error, cmap='viridis')

cbar = plt.colorbar(contour)
cbar.set_label('error') 

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mapa del error')
plt.show()