import numpy as np
import matplotlib.pyplot as plt
import taller3 as ta

"Aqui definimos las funciones analiticas para poder graficarlas"
def f(x):
    respuesta = np.sin(np.pi*x/2)
    return respuesta
def g(y):
    respuesta = np.cos(np.pi*y/2) + 2*((np.cos(np.pi/4))**2/np.sin(np.pi/2))*np.sin(np.pi*y/2)
    return respuesta

def V(x,y):
    respuesta = f(x)*g(y)
    return respuesta

n = 50
m = 50

x = np.linspace(0,n-1,n)
y = np.linspace(0,m-1,m)
X, Y = np.meshgrid(x,y)
Z = V(X,Y)
plt.contourf(X, Y, Z)
plt.colorbar()
plt.title("Mapa del valor del potencial")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
