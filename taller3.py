import numpy as np

def laplace_solver(N,M, V0, dx_dy, max_iteraciones=10000):
    "genera un pontencial aribitrario de dimensiones N x M"
    V = np.random.rand(N, M) 
    iteraciones = 0
    "Condicional para parar el ciclo (deje un valor alto para que se logre el resultado mas adecuado)"
    while iteraciones < max_iteraciones:
        "copia del pontencial para tener un punto de comparacion"
        V_old = np.copy(V)
        "Ciclo que recorre cada uno de los puntos de el potencial"
        for i in range(1, V.shape[0] - 1):
            for j in range(1, V.shape[1] - 1):
                "funcion encargada de hacer el promedio y reemplazar el valor"
                V[i, j] = 0.25 * (V_old[i+1, j] + V_old[i-1, j] + V_old[i, j+1] + V_old[i, j-1])
        
        "coondiciones de frontera"
        V[:, 0] = V0[:, 0] 
        V[:, -1] = V0[:, -1] 
        V[0, :] = V0[0, :]  
        V[-1, :] = V0[-1, :]  
    
        "Si la diferencia entre la matriz nueva del voltaje y la original es menor al valor de tolerancia se rompe el ciclo"
        if np.max(np.abs(V - V_old)) < dx_dy:
            break
        
        iteraciones += 1
    
    return V
