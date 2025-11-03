import numpy as np

pesos, tempos = np.array([3.0, 5.0, 7.0, 9.0]), np.array([83, 146, 197, 243])#pesos e tempos em kg e minutos 
pesoDoPeru = 6.22

def metodoLagrange(x_dados, y_dados, x):
    n, resultado = len(x_dados), 0.0 # n é o numero de pontos e resultado é o resultado do metodo de lagrange
    for i in range(n): 
        L_i = 1.0 # L_i é o polinomio de lagrange
        for j in range(n):
            if i != j: # se i for diferente de j, então L_i é o polinomio de lagrange
                L_i *= (x - x_dados[j]) / (x_dados[i] - x_dados[j]) # L_i é o polinomio de lagrange
        resultado += y_dados[i] * L_i # resultado é o resultado do metodo de lagrange
    return resultado

def metodoNewton(x_dados, y_dados, x):
    n = len(x_dados) # n é o numero de pontos
    F = np.zeros((n, n)) # F é a matriz de diferenças divididas
    F[:, 0] = y_dados
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x_dados[i+j] - x_dados[i])
    resultado, produto = F[0, 0], 1.0 # resultado é o resultado do metodo de newton e produto é o produto dos polinomios de newton
    for i in range(1, n):
        produto *= (x - x_dados[i-1]) # produto é o produto dos polinomios de newton
        resultado += F[0, i] * produto # resultado é o resultado do metodo de newton
    return resultado # resultado é o resultado do metodo de newton

r_l, r_n = metodoLagrange(pesos, tempos, pesoDoPeru), metodoNewton(pesos, tempos, pesoDoPeru) # r_l é o resultado do metodo de lagrange e r_n é o resultado do metodo de newton
h, m = int(r_l // 60), int(r_l % 60) # h são horas e m são minutos 

print(" ============================================== ")
print(" metodos numericos - t2 ")
print(f" tempo para assar: peru com peso de {pesoDoPeru} kg ")
print("===============================================")
print(f"\n metodo lagrange: {r_l:.2f} min = {h}h {m:02d}min ")
print(f" metodo newton:   {r_n:.2f} min = {h}h {m:02d}min ")
print(f" diferenca: {abs(r_l-r_n):.10f} min ")
print(" \nverificacao: ")
for p, t in zip(pesos, tempos): # p é o peso e t é o tempo
    calc = metodoLagrange(pesos, tempos, p) # calc é o resultado do metodo de lagrange
    print(f" p({p}) = {calc:.2f} (esperado: {t}) {'ok' if abs(calc-t) < 1e-10 else 'erro'} ")
print(f" \nresultado: {h}h {m:02d}min ({r_l:.2f} minutos) ")
print(" =============================================== ")
