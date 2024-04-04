import taller3 as ta
import numpy as np
import matplotlib.pyplot as plt
n = 50
m = 50
V0 = np.zeros((n, m))
"le di un valor de 2 a V_0 y de -2 a -V_0"
V0[:, 0] = -2  
V0[:, -1] = 2  
V0[0, :] = 0  
V0[-1, :] = 0  
V_solucion= ta.laplace_solver(n,m, V0,1e-4)
x = np.linspace(0,n-1,n)
y = np.linspace(0,m-1,m)
X, Y = np.meshgrid(x,y)
plt.contourf(X, Y, V_solucion,  cmap=plt.cm.bone)
plt.colorbar()
plt.title("Mapa del valor del potencial")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

