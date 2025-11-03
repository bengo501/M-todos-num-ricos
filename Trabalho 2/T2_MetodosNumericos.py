import numpy as np

pesos, tempos = np.array([3.0, 5.0, 7.0, 9.0]), np.array([83, 146, 197, 243])
pesoDoPeru = 6.22

def metodoLagrange(x, y, ponto_desejado):
    tamanho, resultado = len(x), 0.0
    for i in range(tamanho):
        polinomioBase = 1.0
        for j in range(tamanho):
            if i != j:
                polinomioBase *= (ponto_desejado - x[j]) / (x[i] - x[j])
        resultado += y[i] * polinomioBase
    return resultado

def metodoNewton(x, y, ponto_desejado):
    tamanho = len(x)
    F = np.zeros((tamanho, tamanho))
    F[:, 0] = y
    for j in range(1, tamanho):
        for i in range(tamanho - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x[i+j] - x[i])
    resultado, produto = F[0, 0], 1.0
    for i in range(1, tamanho):
        produto *= (ponto_desejado - x[i-1])
        resultado += F[0, i] * produto
    return resultado

resultadoLagrange, resultadoNewton = metodoLagrange(pesos, tempos, pesoDoPeru), metodoNewton(pesos, tempos, pesoDoPeru)
horas, minutos = int(resultadoLagrange // 60), int(resultadoLagrange % 60)

print("=" * 70)
print("METODOS NUMERICOS - TRABALHO 2")
print(f"Tempo para assar peru de {pesoDoPeru} kg")
print("=" * 70)
print(f"\nLagrange: {resultadoLagrange:.2f} min = {horas}h {minutos:02d}min")
print(f"Newton:   {resultadoNewton:.2f} min = {horas}h {minutos:02d}min")
print(f"Diferenca: {abs(resultadoLagrange - resultadoNewton):.10f} min")
print("\nVERIFICACAO:")
for p, t in zip(pesos, tempos):
    calc = metodoLagrange(pesos, tempos, p)
    print(f"P({p}) = {calc:.2f} (esperado: {t}) {'OK' if abs(calc-t) < 1e-10 else 'ERRO'}")
print(f"\nRESULTADO FINAL: {horas}h {minutos:02d}min ({resultadoLagrange:.2f} minutos)")
print("=" * 70)
