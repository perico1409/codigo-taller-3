import taller3 as ta
import numpy as np
n = 5
m = 5
V0 = np.zeros((n, m))
"le di un valor de 2 a V_0 y de -2 a -V_0"
V0[:, 0] = -2  
V0[:, -1] = 2  
V0[0, :] = 0  
V0[-1, :] = 0  
V_solucion= ta.laplace_solver(n,m, V0,1e-4)
print(V_solucion)
