"""
TRABALHO 1 - MÉTODOS NUMÉRICOS
Desenvolvimento completo baseado nas referências fornecidas

Tópicos abordados:
1. Padrão IEEE 754 e precisão da máquina
2. Sistemas lineares e métodos de solução
3. Solução de equações não-lineares
4. Interpolação e ajuste de dados
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve, lu
from scipy.optimize import fsolve
from scipy.interpolate import lagrange, interp1d
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("TRABALHO 1 - MÉTODOS NUMÉRICOS")
print("Desenvolvimento Passo a Passo")
print("="*80)

# ============================================================================
# PARTE I: PRECISÃO DA MÁQUINA E PADRÃO IEEE 754
# ============================================================================

def parte1_precisao_maquina():
    """
    Implementa o algoritmo de precisão da máquina baseado no Exercício 1
    das referências sobre padrão IEEE 754
    """
    print("\n" + "="*50)
    print("PARTE I: PRECISÃO DA MÁQUINA (IEEE 754)")
    print("="*50)
    
    print("\n1.1 Algoritmo de Precisão da Máquina")
    print("-" * 40)
    
    aux = 1.0
    iteracoes = 0
    historico = []
    
    print("Executando algoritmo:")
    print("while (1 + aux > 1):")
    print("    aux = aux / 2")
    print("\nIterações:")
    
    while 1 + aux > 1:
        if iteracoes < 10 or iteracoes % 10 == 0:  # Mostra primeiras 10 e múltiplos de 10
            print(f"  Iteração {iteracoes:2d}: aux = {aux:.2e}")
        historico.append(aux)
        aux = aux / 2
        iteracoes += 1
        
        # Proteção contra loop infinito
        if iteracoes > 100:
            break
    
    epsilon_maquina = aux * 2  # O último valor que funcionou
    
    print(f"\n✓ Algoritmo terminou após {iteracoes} iterações")
    print(f"✓ Último valor de aux: {aux:.2e}")
    print(f"✓ Epsilon da máquina (aproximado): {epsilon_maquina:.2e}")
    print(f"✓ Epsilon do NumPy: {np.finfo(float).eps:.2e}")
    
    # Verificação
    print(f"\nVerificação:")
    print(f"  1 + epsilon_maquina = {1 + epsilon_maquina}")
    print(f"  1 + epsilon_maquina > 1? {1 + epsilon_maquina > 1}")
    print(f"  1 + epsilon_maquina/2 = {1 + epsilon_maquina/2}")
    print(f"  1 + epsilon_maquina/2 > 1? {1 + epsilon_maquina/2 > 1}")
    
    return epsilon_maquina, historico

# ============================================================================
# PARTE II: SISTEMAS LINEARES
# ============================================================================

def parte2_sistemas_lineares():
    """
    Demonstra métodos de solução de sistemas lineares baseado nas referências
    """
    print("\n" + "="*50)
    print("PARTE II: SISTEMAS LINEARES")
    print("="*50)
    
    print("\n2.1 Sistema Linear Exemplo")
    print("-" * 30)
    
    # Sistema exemplo: baseado nas referências de sistemas lineares
    A = np.array([
        [4, -1, 0, 1],
        [-1, 4, -1, 0],
        [0, -1, 4, -1],
        [1, 0, -1, 4]
    ], dtype=float)
    
    b = np.array([15, 10, 10, 20], dtype=float)
    
    print("Sistema Ax = b onde:")
    print("A =")
    print(A)
    print(f"b = {b}")
    
    # Método 1: Eliminação Gaussiana (usando scipy)
    print("\n2.2 Solução por Eliminação Gaussiana")
    print("-" * 40)
    
    x_gauss = solve(A, b)
    print(f"Solução: x = {x_gauss}")
    
    # Verificação
    residuo = np.dot(A, x_gauss) - b
    print(f"Verificação Ax - b = {residuo}")
    print(f"Norma do resíduo: {np.linalg.norm(residuo):.2e}")
    
    # Método 2: Fatoração LU
    print("\n2.3 Solução por Fatoração LU")
    print("-" * 35)
    
    P, L, U = lu(A)
    print("Fatoração A = PLU")
    print(f"Matriz L (triangular inferior):")
    print(L)
    print(f"Matriz U (triangular superior):")
    print(U)
    
    # Análise de condicionamento
    print("\n2.4 Análise de Condicionamento")
    print("-" * 38)
    
    cond_A = np.linalg.cond(A)
    det_A = np.linalg.det(A)
    
    print(f"Número de condição: {cond_A:.2f}")
    print(f"Determinante: {det_A:.2f}")
    
    if cond_A < 100:
        print("✓ Sistema bem condicionado (cond < 100)")
    elif cond_A < 10000:
        print("⚠ Sistema moderadamente condicionado (100 ≤ cond < 10⁴)")
    else:
        print("✗ Sistema mal condicionado (cond ≥ 10⁴)")
    
    return x_gauss, cond_A

# ============================================================================
# PARTE III: SOLUÇÃO DE EQUAÇÕES NÃO-LINEARES
# ============================================================================

def parte3_equacoes_nao_lineares():
    """
    Implementa métodos para solução de equações não-lineares
    baseado nas referências de solução de equações
    """
    print("\n" + "="*50)
    print("PARTE III: SOLUÇÃO DE EQUAÇÕES NÃO-LINEARES")
    print("="*50)
    
    # Função exemplo: f(x) = x³ - 2x - 5 (tem raiz em x ≈ 2.094)
    def f(x):
        return x**3 - 2*x - 5
    
    def df_dx(x):
        return 3*x**2 - 2
    
    print("\n3.1 Função Exemplo")
    print("-" * 20)
    print("f(x) = x³ - 2x - 5")
    print("f'(x) = 3x² - 2")
    
    # Método da Bissecção
    print("\n3.2 Método da Bissecção")
    print("-" * 30)
    
    def bisseccao(f, a, b, tol=1e-6, max_iter=100):
        """Implementa método da bissecção"""
        if f(a) * f(b) > 0:
            raise ValueError("f(a) e f(b) devem ter sinais opostos")
        
        historico = []
        for i in range(max_iter):
            c = (a + b) / 2
            fc = f(c)
            historico.append((i+1, a, b, c, fc))
            
            if abs(fc) < tol:
                return c, historico
            
            if f(a) * fc < 0:
                b = c
            else:
                a = c
        
        return c, historico
    
    # Localizar intervalo
    print("Localizando intervalo com mudança de sinal:")
    for x in range(-5, 5):
        if f(x) * f(x+1) < 0:
            print(f"  f({x}) = {f(x):.2f}, f({x+1}) = {f(x+1):.2f}")
            print(f"  Raiz no intervalo [{x}, {x+1}]")
            a_biss, b_biss = x, x+1
            break
    
    raiz_biss, hist_biss = bisseccao(f, a_biss, b_biss)
    print(f"\nResultado da Bissecção:")
    print(f"  Raiz encontrada: x = {raiz_biss:.6f}")
    print(f"  f(x) = {f(raiz_biss):.2e}")
    print(f"  Iterações: {len(hist_biss)}")
    
    # Método de Newton-Raphson
    print("\n3.3 Método de Newton-Raphson")
    print("-" * 35)
    
    def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
        """Implementa método de Newton-Raphson"""
        historico = []
        x = x0
        
        for i in range(max_iter):
            fx = f(x)
            dfx = df(x)
            
            if abs(dfx) < 1e-12:
                raise ValueError("Derivada muito pequena")
            
            x_novo = x - fx / dfx
            historico.append((i+1, x, fx, dfx, x_novo))
            
            if abs(x_novo - x) < tol:
                return x_novo, historico
            
            x = x_novo
        
        return x, historico
    
    x0_newton = 2.0  # Chute inicial próximo à raiz
    raiz_newton, hist_newton = newton_raphson(f, df_dx, x0_newton)
    
    print(f"Chute inicial: x₀ = {x0_newton}")
    print(f"Resultado do Newton-Raphson:")
    print(f"  Raiz encontrada: x = {raiz_newton:.6f}")
    print(f"  f(x) = {f(raiz_newton):.2e}")
    print(f"  Iterações: {len(hist_newton)}")
    
    # Comparação dos métodos
    print(f"\n3.4 Comparação dos Métodos")
    print("-" * 32)
    print(f"{'Método':<15} {'Raiz':<12} {'Iterações':<10} {'Erro':<12}")
    print("-" * 50)
    erro_biss = abs(f(raiz_biss))
    erro_newton = abs(f(raiz_newton))
    print(f"{'Bissecção':<15} {raiz_biss:<12.6f} {len(hist_biss):<10} {erro_biss:<12.2e}")
    print(f"{'Newton-Raphson':<15} {raiz_newton:<12.6f} {len(hist_newton):<10} {erro_newton:<12.2e}")
    
    return raiz_biss, raiz_newton

# ============================================================================
# PARTE IV: INTERPOLAÇÃO E AJUSTE DE DADOS
# ============================================================================

def parte4_interpolacao():
    """
    Demonstra métodos de interpolação baseado nas referências de interpolação
    """
    print("\n" + "="*50)
    print("PARTE IV: INTERPOLAÇÃO E AJUSTE DE DADOS")
    print("="*50)
    
    print("\n4.1 Dados de Exemplo")
    print("-" * 22)
    
    # Dados exemplo (baseados nos exercícios de interpolação das referências)
    x_dados = np.array([1, 2, 3, 4, 5])
    y_dados = np.array([2, 3, 5, 4, 6])
    
    print(f"Pontos: {list(zip(x_dados, y_dados))}")
    
    # Interpolação de Lagrange
    print("\n4.2 Interpolação de Lagrange")
    print("-" * 33)
    
    poly_lagrange = lagrange(x_dados, y_dados)
    print(f"Polinômio de Lagrange (grau {len(x_dados)-1}):")
    
    # Coeficientes do polinômio
    coefs = poly_lagrange.coefficients
    print("p(x) = ", end="")
    for i, coef in enumerate(coefs):
        grau = len(coefs) - 1 - i
        if i > 0:
            print(" + " if coef >= 0 else " - ", end="")
            coef = abs(coef)
        if grau == 0:
            print(f"{coef:.3f}", end="")
        elif grau == 1:
            print(f"{coef:.3f}x", end="")
        else:
            print(f"{coef:.3f}x^{grau}", end="")
    print()
    
    # Verificação da interpolação
    print("\nVerificação:")
    for i, (x, y) in enumerate(zip(x_dados, y_dados)):
        y_calc = poly_lagrange(x)
        print(f"  p({x}) = {y_calc:.6f} (esperado: {y})")
    
    # Ajuste por mínimos quadrados
    print("\n4.3 Ajuste por Mínimos Quadrados")
    print("-" * 38)
    
    # Ajuste linear
    coefs_linear = np.polyfit(x_dados, y_dados, 1)
    poly_linear = np.poly1d(coefs_linear)
    
    print(f"Ajuste linear: y = {coefs_linear[0]:.3f}x + {coefs_linear[1]:.3f}")
    
    # Ajuste quadrático
    coefs_quad = np.polyfit(x_dados, y_dados, 2)
    poly_quad = np.poly1d(coefs_quad)
    
    print(f"Ajuste quadrático: y = {coefs_quad[0]:.3f}x² + {coefs_quad[1]:.3f}x + {coefs_quad[2]:.3f}")
    
    # Cálculo do R²
    def calcular_r2(y_real, y_pred):
        ss_res = np.sum((y_real - y_pred) ** 2)
        ss_tot = np.sum((y_real - np.mean(y_real)) ** 2)
        return 1 - (ss_res / ss_tot)
    
    r2_linear = calcular_r2(y_dados, poly_linear(x_dados))
    r2_quad = calcular_r2(y_dados, poly_quad(x_dados))
    
    print(f"R² do ajuste linear: {r2_linear:.4f}")
    print(f"R² do ajuste quadrático: {r2_quad:.4f}")
    
    # Visualização
    print("\n4.4 Visualização dos Resultados")
    print("-" * 35)
    
    x_plot = np.linspace(0.5, 5.5, 100)
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(x_dados, y_dados, 'ro', label='Dados originais', markersize=8)
    plt.plot(x_plot, poly_lagrange(x_plot), 'b-', label='Interpolação Lagrange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolação de Lagrange')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 2)
    plt.plot(x_dados, y_dados, 'ro', label='Dados originais', markersize=8)
    plt.plot(x_plot, poly_linear(x_plot), 'g-', label=f'Ajuste linear (R²={r2_linear:.3f})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ajuste Linear')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 3)
    plt.plot(x_dados, y_dados, 'ro', label='Dados originais', markersize=8)
    plt.plot(x_plot, poly_quad(x_plot), 'm-', label=f'Ajuste quadrático (R²={r2_quad:.3f})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ajuste Quadrático')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 4)
    plt.plot(x_dados, y_dados, 'ro', label='Dados originais', markersize=8)
    plt.plot(x_plot, poly_lagrange(x_plot), 'b-', label='Lagrange', alpha=0.7)
    plt.plot(x_plot, poly_linear(x_plot), 'g--', label='Linear', alpha=0.7)
    plt.plot(x_plot, poly_quad(x_plot), 'm:', label='Quadrático', alpha=0.7)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparação dos Métodos')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('trabalho1_interpolacao.png', dpi=300, bbox_inches='tight')
    print("✓ Gráficos salvos em 'trabalho1_interpolacao.png'")
    
    return poly_lagrange, r2_linear, r2_quad

# ============================================================================
# PARTE V: ANÁLISE INTEGRADA E CONCLUSÕES
# ============================================================================

def parte5_analise_integrada():
    """
    Análise integrada de todos os métodos estudados
    """
    print("\n" + "="*50)
    print("PARTE V: ANÁLISE INTEGRADA E CONCLUSÕES")
    print("="*50)
    
    print("\n5.1 Resumo dos Resultados Obtidos")
    print("-" * 36)
    
    print("✓ Precisão da máquina determinada")
    print("✓ Sistema linear resolvido com sucesso")
    print("✓ Equações não-lineares solucionadas")
    print("✓ Interpolação e ajuste implementados")
    
    print("\n5.2 Conexões entre os Métodos")
    print("-" * 32)
    
    print("• Precisão da máquina afeta TODOS os cálculos numéricos")
    print("• Sistemas lineares aparecem em:")
    print("  - Interpolação polinomial (sistema de Vandermonde)")
    print("  - Método de Newton (sistemas jacobiano)")
    print("  - Mínimos quadrados (equações normais)")
    print("• Métodos iterativos requerem critérios de parada baseados em ε")
    print("• Condicionamento afeta estabilidade de todos os métodos")
    
    print("\n5.3 Considerações Práticas")
    print("-" * 30)
    
    print("• Sempre verificar condicionamento de sistemas")
    print("• Usar tolerâncias apropriadas baseadas na precisão da máquina")
    print("• Preferir métodos estáveis numericamente")
    print("• Validar resultados com dados conhecidos")
    print("• Documentar limitações e suposições")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todas as partes do trabalho
    """
    try:
        # Parte I: Precisão da máquina
        epsilon, hist = parte1_precisao_maquina()
        
        # Parte II: Sistemas lineares
        solucao_sistema, condicao = parte2_sistemas_lineares()
        
        # Parte III: Equações não-lineares
        raiz_biss, raiz_newton = parte3_equacoes_nao_lineares()
        
        # Parte IV: Interpolação
        poly, r2_lin, r2_quad = parte4_interpolacao()
        
        # Parte V: Análise integrada
        parte5_analise_integrada()
        
        print("\n" + "="*80)
        print("TRABALHO 1 CONCLUÍDO COM SUCESSO!")
        print("="*80)
        
        print(f"\nResumo dos Principais Resultados:")
        print(f"• Epsilon da máquina: {epsilon:.2e}")
        print(f"• Condicionamento do sistema: {condicao:.2f}")
        print(f"• Raiz por bissecção: {raiz_biss:.6f}")
        print(f"• Raiz por Newton: {raiz_newton:.6f}")
        print(f"• R² ajuste linear: {r2_lin:.4f}")
        print(f"• R² ajuste quadrático: {r2_quad:.4f}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")
        return False

if __name__ == "__main__":
    sucesso = main()
    if sucesso:
        print("\n✅ Todos os métodos executados com sucesso!")
    else:
        print("\n❌ Houve problemas durante a execução.")
