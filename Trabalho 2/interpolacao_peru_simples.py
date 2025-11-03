import numpy as np

pesos, tempos = np.array([3.0, 5.0, 7.0, 9.0]), np.array([83, 146, 197, 243])
peso_peru = 6.22

def lagrange(x_dados, y_dados, x):
    n, resultado = len(x_dados), 0.0
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x - x_dados[j]) / (x_dados[i] - x_dados[j])
        resultado += y_dados[i] * L_i
    return resultado

def newton(x_dados, y_dados, x):
    n = len(x_dados)
    F = np.zeros((n, n))
    F[:, 0] = y_dados
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x_dados[i+j] - x_dados[i])
    resultado, produto = F[0, 0], 1.0
    for i in range(1, n):
        produto *= (x - x_dados[i-1])
        resultado += F[0, i] * produto
    return resultado

r_l, r_n = lagrange(pesos, tempos, peso_peru), newton(pesos, tempos, peso_peru)
h, m = int(r_l // 60), int(r_l % 60)

print("="*60)
print("METODOS NUMERICOS - TRABALHO 2")
print(f"Tempo para assar peru de {peso_peru} kg")
print("="*60)
print(f"\nLagrange: {r_l:.2f} min = {h}h {m:02d}min")
print(f"Newton:   {r_n:.2f} min = {h}h {m:02d}min")
print(f"Diferenca: {abs(r_l-r_n):.10f} min")
print("\nVERIFICACAO:")
for p, t in zip(pesos, tempos):
    calc = lagrange(pesos, tempos, p)
    print(f"P({p}) = {calc:.2f} (esperado: {t}) {'OK' if abs(calc-t) < 1e-10 else 'ERRO'}")
print(f"\nRESULTADO FINAL: {h}h {m:02d}min ({r_l:.2f} minutos)")
print("="*60)
