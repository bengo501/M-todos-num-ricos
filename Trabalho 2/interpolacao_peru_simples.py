"""
Métodos Numéricos - Trabalho 2
Interpolação para tempo de assar peru
Dona Selma precisa saber quanto tempo assar um peru de 6.22 kg
"""

import numpy as np

# ============================================================================
# DADOS DO PROBLEMA
# ============================================================================

# Pesos dos perus (em kg)
pesos = np.array([3.0, 5.0, 7.0, 9.0])

# Tempos de cozimento (convertidos para minutos)
# 1h 23min = 83 min
# 2h 26min = 146 min
# 3h 17min = 197 min
# 4h 03min = 243 min
tempos_minutos = np.array([83, 146, 197, 243])

# Peso do peru deste ano
peso_peru = 6.22

print("=" * 70)
print("METODOS NUMERICOS - TRABALHO 2")
print("Interpolacao para Tempo de Assar Peru")
print("=" * 70)

print("\nDADOS DE REFERENCIA:")
print("-" * 70)
print(f"{'Peso (kg)':<15} {'Tempo':<20} {'Tempo (min)':<15}")
print("-" * 70)
for i, (peso, tempo_min) in enumerate(zip(pesos, tempos_minutos)):
    horas = tempo_min // 60
    minutos = tempo_min % 60
    print(f"{peso:<15.1f} {int(horas)}h {int(minutos):02d}min{'':<10} {tempo_min:<15}")
print("-" * 70)
print(f"\nPeso do peru deste ano: {peso_peru} kg")


# ============================================================================
# INTERPOLAÇÃO DE LAGRANGE (Implementação Manual)
# ============================================================================

def lagrange_interpolation(x_dados, y_dados, x):
    """
    Implementação manual da interpolação de Lagrange
    
    L(x) = Σ(y_i * L_i(x))
    onde L_i(x) = Π((x - x_j)/(x_i - x_j)) para j ≠ i
    """
    n = len(x_dados)
    resultado = 0.0
    
    for i in range(n):
        # Calcular L_i(x)
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x - x_dados[j]) / (x_dados[i] - x_dados[j])
        
        # Adicionar termo y_i * L_i(x)
        resultado += y_dados[i] * L_i
    
    return resultado


print("\n" + "=" * 70)
print("METODO: INTERPOLACAO DE LAGRANGE")
print("=" * 70)

valor_lagrange = lagrange_interpolation(pesos, tempos_minutos, peso_peru)

# Converter resultado para horas e minutos
horas_resultado = int(valor_lagrange // 60)
minutos_resultado = int(valor_lagrange % 60)

print(f"\nResultado para peru de {peso_peru} kg:")
print(f"   Tempo: {valor_lagrange:.2f} minutos")
print(f"   Tempo: {horas_resultado}h {minutos_resultado:02d}min")

# Verificação: testar nos pontos conhecidos
print(f"\nVerificacao nos pontos conhecidos:")
print(f"{'Peso (kg)':<15} {'Tempo real (min)':<20} {'Tempo interp. (min)':<25} {'Erro (min)':<15}")
print("-" * 75)
for peso, tempo_real in zip(pesos, tempos_minutos):
    tempo_interp = lagrange_interpolation(pesos, tempos_minutos, peso)
    erro = abs(tempo_interp - tempo_real)
    print(f"{peso:<15.1f} {tempo_real:<20} {tempo_interp:<25.6f} {erro:<15.10f}")


# ============================================================================
# INTERPOLAÇÃO DE NEWTON (Diferenças Divididas)
# ============================================================================

def diferencas_divididas(x, y):
    """Calcula as diferenças divididas para interpolação de Newton"""
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x[i+j] - x[i])
    
    return F


def newton_interpolation(x_dados, y_dados, x):
    """Interpolação de Newton usando diferenças divididas"""
    n = len(x_dados)
    F = diferencas_divididas(x_dados, y_dados)
    
    resultado = F[0, 0]
    produto = 1.0
    
    for i in range(1, n):
        produto *= (x - x_dados[i-1])
        resultado += F[0, i] * produto
    
    return resultado


print("\n" + "=" * 70)
print("METODO: INTERPOLACAO DE NEWTON")
print("=" * 70)

valor_newton = newton_interpolation(pesos, tempos_minutos, peso_peru)

horas_newton = int(valor_newton // 60)
minutos_newton = int(valor_newton % 60)

print(f"\nResultado para peru de {peso_peru} kg:")
print(f"   Tempo: {valor_newton:.2f} minutos")
print(f"   Tempo: {horas_newton}h {minutos_newton:02d}min")

# Comparação entre métodos
print(f"\n" + "=" * 70)
print("COMPARACAO DOS METODOS")
print("=" * 70)
print(f"Lagrange: {valor_lagrange:.4f} minutos ({horas_resultado}h {minutos_resultado:02d}min)")
print(f"Newton:   {valor_newton:.4f} minutos ({horas_newton}h {minutos_newton:02d}min)")
print(f"Diferenca: {abs(valor_lagrange - valor_newton):.10f} minutos")
print("\nObservacao: Ambos os metodos devem dar o mesmo resultado!")


# ============================================================================
# RESULTADO FINAL
# ============================================================================

print("\n" + "=" * 70)
print("RESULTADO FINAL")
print("=" * 70)
print(f"\nPara assar um peru de {peso_peru} kg a 230C:")
print(f"   Tempo necessario: {horas_resultado}h {minutos_resultado:02d}min")
print(f"   Valor em minutos: {valor_lagrange:.2f} minutos")
print(f"\nRecomendacao: Comece a assar o peru {horas_resultado}h {minutos_resultado:02d}min antes")
print(f"   do horario previsto para servir!")

print("\n" + "=" * 70)
print("ANALISE TECNICA")
print("=" * 70)
print(f"""
Tipo de Interpolacao: Polinomial de grau 3
Numero de pontos: {len(pesos)}
Metodos utilizados: Lagrange e Newton (ambos identicos)
Ponto interpolado: {peso_peru} kg (interpolacao, nao extrapolacao)

Observacoes:
   - O ponto 6.22 kg esta entre 5.0 kg e 7.0 kg (interpolacao)
   - Para 5.0 kg: 2h 26min (146 min)
   - Para 7.0 kg: 3h 17min (197 min)
   - Interpolacao linear simples: ~{146 + (197-146)*(6.22-5.0)/(7.0-5.0):.1f} min
   - Nossa interpolacao polinomial: {valor_lagrange:.2f} min
   
A interpolacao polinomial considera todos os 4 pontos, proporcionando
   uma estimativa mais precisa que uma simples interpolacao linear.
""")

print("=" * 70)

