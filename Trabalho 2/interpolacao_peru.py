"""
Métodos Numéricos - Trabalho 2
Interpolação para tempo de assar peru
Dona Selma precisa saber quanto tempo assar um peru de 6.22 kg
"""

import numpy as np
from scipy.interpolate import lagrange
from typing import Tuple

# Tentar importar matplotlib para gráficos (opcional)
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("⚠️ Matplotlib não disponível. Gráficos serão pulados.")

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
print("MÉTODOS NUMÉRICOS - TRABALHO 2")
print("Interpolação para Tempo de Assar Peru")
print("=" * 70)

print("\n📊 DADOS DE REFERÊNCIA:")
print("-" * 70)
print(f"{'Peso (kg)':<15} {'Tempo':<20} {'Tempo (min)':<15}")
print("-" * 70)
for i, (peso, tempo_min) in enumerate(zip(pesos, tempos_minutos)):
    horas = tempo_min // 60
    minutos = tempo_min % 60
    print(f"{peso:<15.1f} {horas}h {minutos:02d}min{'':<10} {tempo_min:<15}")
print("-" * 70)
print(f"\n🎯 Peso do peru deste ano: {peso_peru} kg")


# ============================================================================
# MÉTODO 1: INTERPOLAÇÃO DE LAGRANGE
# ============================================================================

def interpolacao_lagrange(x_dados: np.ndarray, y_dados: np.ndarray, x: float) -> Tuple[float, np.poly1d]:
    """
    Realiza interpolação de Lagrange
    
    Args:
        x_dados: Pontos x conhecidos
        y_dados: Pontos y conhecidos
        x: Ponto onde deseja-se interpolar
    
    Returns:
        Valor interpolado e polinômio de Lagrange
    """
    # Criar polinômio de Lagrange
    poly = lagrange(x_dados, y_dados)
    
    # Avaliar no ponto desejado
    valor = poly(x)
    
    return valor, poly


print("\n" + "=" * 70)
print("MÉTODO 1: INTERPOLAÇÃO DE LAGRANGE")
print("=" * 70)

valor_lagrange, polinomio_lagrange = interpolacao_lagrange(pesos, tempos_minutos, peso_peru)

# Converter resultado para horas e minutos
horas_resultado = int(valor_lagrange // 60)
minutos_resultado = int(valor_lagrange % 60)

print(f"\n📐 Polinômio de Lagrange (coeficientes):")
coeffs = polinomio_lagrange.coef
grau = len(coeffs) - 1
print(f"Grau do polinômio: {grau}")
print("Coeficientes (do maior para menor grau):")
for i, coef in enumerate(coeffs):
    exp = grau - i
    if exp == 0:
        print(f"  {coef:.6f}")
    elif exp == 1:
        print(f"  {coef:.6f}x")
    else:
        print(f"  {coef:.6f}x^{exp}")

print(f"\n✅ Resultado para peru de {peso_peru} kg:")
print(f"   Tempo: {valor_lagrange:.2f} minutos")
print(f"   Tempo: {horas_resultado}h {minutos_resultado:02d}min")

# Verificação: testar nos pontos conhecidos
print(f"\n🔍 Verificação nos pontos conhecidos:")
print(f"{'Peso (kg)':<15} {'Tempo real (min)':<20} {'Tempo interp. (min)':<25} {'Erro (min)':<15}")
print("-" * 75)
for peso, tempo_real in zip(pesos, tempos_minutos):
    tempo_interp = polinomio_lagrange(peso)
    erro = abs(tempo_interp - tempo_real)
    print(f"{peso:<15.1f} {tempo_real:<20} {tempo_interp:<25.2f} {erro:<15.6f}")


# ============================================================================
# MÉTODO 2: INTERPOLAÇÃO DE NEWTON (Forma de Newton)
# ============================================================================

def diferencas_divididas(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula as diferenças divididas para interpolação de Newton
    
    Returns:
        Matriz de diferenças divididas
    """
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x[i+j] - x[i])
    
    return F


def interpolacao_newton(x_dados: np.ndarray, y_dados: np.ndarray, x: float) -> Tuple[float, dict]:
    """
    Realiza interpolação de Newton usando diferenças divididas
    
    Returns:
        Valor interpolado e dicionário com diferenças divididas
    """
    n = len(x_dados)
    F = diferencas_divididas(x_dados, y_dados)
    
    # Construir o polinômio
    resultado = F[0, 0]
    produto = 1.0
    
    for i in range(1, n):
        produto *= (x - x_dados[i-1])
        resultado += F[0, i] * produto
    
    # Coletar diferenças divididas para exibição
    diff_divididas = {f'f[x_{i}]': F[0, i] for i in range(n)}
    
    return resultado, diff_divididas


print("\n" + "=" * 70)
print("MÉTODO 2: INTERPOLAÇÃO DE NEWTON")
print("=" * 70)

valor_newton, diffs = interpolacao_newton(pesos, tempos_minutos, peso_peru)

horas_newton = int(valor_newton // 60)
minutos_newton = int(valor_newton % 60)

print(f"\n📐 Diferenças Divididas:")
for i, (key, value) in enumerate(diffs.items()):
    print(f"  {key} = {value:.6f}")

print(f"\n✅ Resultado para peru de {peso_peru} kg:")
print(f"   Tempo: {valor_newton:.2f} minutos")
print(f"   Tempo: {horas_newton}h {minutos_newton:02d}min")

# Comparação entre métodos
print(f"\n" + "=" * 70)
print("COMPARAÇÃO DOS MÉTODOS")
print("=" * 70)
print(f"Lagrange: {valor_lagrange:.4f} minutos ({horas_resultado}h {minutos_resultado:02d}min)")
print(f"Newton:   {valor_newton:.4f} minutos ({horas_newton}h {minutos_newton:02d}min)")
print(f"Diferença: {abs(valor_lagrange - valor_newton):.10f} minutos")
print("\n💡 Observação: Ambos os métodos devem dar o mesmo resultado!")


# ============================================================================
# VISUALIZAÇÃO
# ============================================================================

def plotar_interpolacao():
    """Cria gráfico da interpolação"""
    if not HAS_MATPLOTLIB:
        print("⚠️ Matplotlib não disponível. Pulando criação do gráfico.")
        return
    
    # Criar intervalo para plotagem
    x_plot = np.linspace(2.5, 9.5, 1000)
    y_plot = polinomio_lagrange(x_plot)
    
    # Criar figura
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plotar polinômio interpolador
    ax.plot(x_plot, y_plot, 'b-', linewidth=2, label='Polinômio Interpolador')
    
    # Plotar pontos conhecidos
    ax.plot(pesos, tempos_minutos, 'ro', markersize=10, label='Pontos Conhecidos')
    
    # Plotar ponto interpolado
    ax.plot(peso_peru, valor_lagrange, 'g*', markersize=15, label=f'Interpolação: {peso_peru} kg')
    
    # Adicionar linhas de referência
    ax.axvline(peso_peru, color='g', linestyle='--', alpha=0.5)
    ax.axhline(valor_lagrange, color='g', linestyle='--', alpha=0.5)
    
    # Formatação
    ax.set_xlabel('Peso do Peru (kg)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tempo de Cozimento (minutos)', fontsize=12, fontweight='bold')
    ax.set_title('Interpolação: Tempo de Assar Peru', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    
    # Adicionar anotações
    for peso, tempo in zip(pesos, tempos_minutos):
        horas = int(tempo // 60)
        minutos = int(tempo % 60)
        ax.annotate(f'{peso} kg\n{horas}h {minutos:02d}min', 
                   xy=(peso, tempo), 
                   xytext=(10, 10), 
                   textcoords='offset points',
                   fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5))
    
    # Anotar resultado
    horas_res = int(valor_lagrange // 60)
    minutos_res = int(valor_lagrange % 60)
    ax.annotate(f'Resultado:\n{peso_peru} kg\n{horas_res}h {minutos_res:02d}min',
               xy=(peso_peru, valor_lagrange),
               xytext=(30, -30),
               textcoords='offset points',
               fontsize=11,
               fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8),
               arrowprops=dict(arrowstyle='->', color='green', lw=2))
    
    plt.tight_layout()
    plt.savefig('grafico_interpolacao.png', dpi=300, bbox_inches='tight')
    print(f"\n📊 Gráfico salvo em: grafico_interpolacao.png")
    plt.close()


print("\n" + "=" * 70)
print("GERANDO VISUALIZAÇÃO")
print("=" * 70)
plotar_interpolacao()


# ============================================================================
# RESULTADO FINAL
# ============================================================================

print("\n" + "=" * 70)
print("RESULTADO FINAL")
print("=" * 70)
print(f"\n🎯 Para assar um peru de {peso_peru} kg a 230°C:")
print(f"   ⏱️  Tempo necessário: {horas_resultado}h {minutos_resultado:02d}min")
print(f"   📊 Valor em minutos: {valor_lagrange:.2f} minutos")
print(f"\n💡 Recomendação: Comece a assar o peru {horas_resultado}h {minutos_resultado:02d}min antes")
print(f"   do horário previsto para servir!")

print("\n" + "=" * 70)
print("ANÁLISE TÉCNICA")
print("=" * 70)
print(f"""
📐 Tipo de Interpolação: Polinomial de grau {grau}
📊 Número de pontos: {len(pesos)}
✅ Métodos utilizados: Lagrange e Newton (ambos idênticos)
🎯 Ponto interpolado: {peso_peru} kg (interpolação, não extrapolação)

📈 Observações:
   - O ponto 6.22 kg está entre 5.0 kg e 7.0 kg (interpolação)
   - Para 5.0 kg: 2h 26min (146 min)
   - Para 7.0 kg: 3h 17min (197 min)
   - Interpolação linear simples: ~{146 + (197-146)*(6.22-5.0)/(7.0-5.0):.1f} min
   - Nossa interpolação polinomial: {valor_lagrange:.2f} min
   
💡 A interpolação polinomial considera todos os 4 pontos, proporcionando
   uma estimativa mais precisa que uma simples interpolação linear.
""")

print("=" * 70)

