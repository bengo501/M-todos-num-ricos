"""
Métodos Numéricos - Sistemas Lineares
Solução dos exercícios da Lista 1
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve, lu_factor, lu_solve
import math

# ============================================================================
# EXERCÍCIO 1: Problema do parquinho
# ============================================================================

def exercicio1():
    """
    Resolve o problema do parquinho com 4 brinquedos
    """
    print("=== EXERCÍCIO 1: PROBLEMA DO PARQUINHO ===")
    
    print("Um parquinho tem 4 brinquedos: A, B, C e D")
    print("Informações:")
    print("- 20 pessoas/hora chegam pelo portão principal (próximo ao brinquedo A)")
    print("- 10 pessoas/hora chegam pelo portão secundário (próximo ao brinquedo C)")
    print("- As pessoas vão primeiro para o brinquedo mais perto do portão por onde entraram")
    print("- Depois do primeiro brinquedo, metade vai para B, o resto se divide em 3 partes:")
    print("  * 1/3 vai embora")
    print("  * 1/3 vai para um dos outros dois brinquedos")
    print("  * 1/3 vai para o outro brinquedo")
    print("- Depois de B ou D, as pessoas se dividem igualmente entre A, C e D")
    
    # Definir variáveis: x1, x2, x3, x4 = pessoas em A, B, C, D respectivamente
    print("\nSistema de equações:")
    print("x1 = 20 + (1/3)(x2/2) + (1/3)(x4/2) + (1/3)(x2/2) + (1/3)(x4/2)")
    print("x2 = (1/2)(x1) + (1/2)(x3)")
    print("x3 = 10 + (1/3)(x2/2) + (1/3)(x4/2)")
    print("x4 = (1/3)(x2/2) + (1/3)(x4/2)")
    
    # Simplificar as equações
    print("\nSimplificando:")
    print("x1 = 20 + (1/3)x2 + (1/3)x4")
    print("x2 = (1/2)x1 + (1/2)x3")
    print("x3 = 10 + (1/3)x2 + (1/3)x4")
    print("x4 = (1/3)x2 + (1/3)x4")
    
    # Forma matricial: Ax = b
    A = np.array([
        [1, -1/3, 0, -1/3],
        [-1/2, 1, -1/2, 0],
        [0, -1/3, 1, -1/3],
        [0, -1/3, 0, 2/3]
    ])
    
    b = np.array([20, 0, 10, 0])
    
    print(f"\nMatriz A:")
    print(A)
    print(f"\nVetor b:")
    print(b)
    
    # Resolver o sistema
    try:
        x = solve(A, b)
        print(f"\nSolução:")
        print(f"x1 (brinquedo A) = {x[0]:.2f} pessoas")
        print(f"x2 (brinquedo B) = {x[1]:.2f} pessoas")
        print(f"x3 (brinquedo C) = {x[2]:.2f} pessoas")
        print(f"x4 (brinquedo D) = {x[3]:.2f} pessoas")
        
        # Verificar se a solução faz sentido
        total = sum(x)
        print(f"\nTotal de pessoas no parque: {total:.2f}")
        print(f"Pessoas que chegam por hora: 30")
        
        if abs(total - 30) < 1e-10:
            print("✓ A solução está correta!")
        else:
            print("⚠️ Verificar a solução")
            
    except np.linalg.LinAlgError:
        print("Erro: Sistema singular ou mal condicionado")

# ============================================================================
# EXERCÍCIO 2: Métodos de Gauss-Jacobi e Gauss-Seidel
# ============================================================================

def gauss_jacobi(A, b, x0, tol=1e-10, max_iter=100):
    """
    Implementa o método de Gauss-Jacobi
    """
    n = len(b)
    x = x0.copy()
    iteracoes = []
    
    for k in range(max_iter):
        x_anterior = x.copy()
        
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma += A[i, j] * x_anterior[j]
            x[i] = (b[i] - soma) / A[i, i]
        
        erro = np.linalg.norm(x - x_anterior)
        iteracoes.append((k+1, x.copy(), erro))
        
        if erro < tol:
            break
    
    return x, iteracoes

def gauss_seidel(A, b, x0, tol=1e-10, max_iter=100):
    """
    Implementa o método de Gauss-Seidel
    """
    n = len(b)
    x = x0.copy()
    iteracoes = []
    
    for k in range(max_iter):
        x_anterior = x.copy()
        
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma += A[i, j] * x[j]
            x[i] = (b[i] - soma) / A[i, i]
        
        erro = np.linalg.norm(x - x_anterior)
        iteracoes.append((k+1, x.copy(), erro))
        
        if erro < tol:
            break
    
    return x, iteracoes

def exercicio2():
    """
    Resolve sistema usando Gauss-Jacobi e Gauss-Seidel
    """
    print("=== EXERCÍCIO 2: MÉTODOS DE GAUSS-JACOBI E GAUSS-SEIDEL ===")
    
    # Sistema dado no exercício
    A = np.array([
        [8, 2, 4, 5],
        [-1, -3, 1, 2],
        [3, -3, -4, 3],
        [2, -2, -1, 3]
    ])
    
    b = np.array([-7, 10, -4, -3])
    x0 = np.array([1, 1, 1, 1])  # Estimativa inicial
    
    print("Sistema:")
    print("8x + 2y + 4z + 5w = -7")
    print("-x - 3y + z + 2w = 10")
    print("3x - 3y - 4z + 3w = -4")
    print("2x - 2y - z + 3w = -3")
    
    print(f"\nMatriz A:")
    print(A)
    print(f"\nVetor b:")
    print(b)
    print(f"\nEstimativa inicial: {x0}")
    
    # Verificar se a matriz é diagonalmente dominante
    print(f"\nVerificação de convergência:")
    for i in range(len(A)):
        diag = abs(A[i, i])
        soma_linha = sum(abs(A[i, j]) for j in range(len(A)) if j != i)
        print(f"Linha {i+1}: |a{i+1}{i+1}| = {diag:.2f}, Σ|a{i+1}j| = {soma_linha:.2f}")
        if diag > soma_linha:
            print(f"  ✓ Linha {i+1} é diagonalmente dominante")
        else:
            print(f"  ⚠️ Linha {i+1} não é diagonalmente dominante")
    
    # Método de Gauss-Jacobi
    print(f"\n" + "="*60)
    print("MÉTODO DE GAUSS-JACOBI")
    print("="*60)
    
    x_jacobi, iteracoes_jacobi = gauss_jacobi(A, b, x0)
    
    print(f"Solução encontrada: {x_jacobi}")
    print(f"\nIterações:")
    print("k\tx1\t\tx2\t\tx3\t\tx4\t\tErro")
    print("-" * 80)
    
    for k, x, erro in iteracoes_jacobi[:10]:  # Mostrar apenas as primeiras 10
        print(f"{k}\t{x[0]:.6f}\t{x[1]:.6f}\t{x[2]:.6f}\t{x[3]:.6f}\t{erro:.2e}")
    
    if len(iteracoes_jacobi) > 10:
        print(f"... ({len(iteracoes_jacobi) - 10} iterações omitidas)")
    
    # Método de Gauss-Seidel
    print(f"\n" + "="*60)
    print("MÉTODO DE GAUSS-SEIDEL")
    print("="*60)
    
    x_seidel, iteracoes_seidel = gauss_seidel(A, b, x0)
    
    print(f"Solução encontrada: {x_seidel}")
    print(f"\nIterações:")
    print("k\tx1\t\tx2\t\tx3\t\tx4\t\tErro")
    print("-" * 80)
    
    for k, x, erro in iteracoes_seidel[:10]:  # Mostrar apenas as primeiras 10
        print(f"{k}\t{x[0]:.6f}\t{x[1]:.6f}\t{x[2]:.6f}\t{x[3]:.6f}\t{erro:.2e}")
    
    if len(iteracoes_seidel) > 10:
        print(f"... ({len(iteracoes_seidel) - 10} iterações omitidas)")
    
    # Comparação
    print(f"\n" + "="*60)
    print("COMPARAÇÃO DOS MÉTODOS")
    print("="*60)
    
    print(f"Gauss-Jacobi: {len(iteracoes_jacobi)} iterações")
    print(f"Gauss-Seidel: {len(iteracoes_seidel)} iterações")
    
    if len(iteracoes_seidel) < len(iteracoes_jacobi):
        print("✓ Gauss-Seidel convergiu mais rapidamente!")
    else:
        print("⚠️ Gauss-Jacobi convergiu mais rapidamente")
    
    # Verificar solução exata
    try:
        x_exato = solve(A, b)
        print(f"\nSolução exata: {x_exato}")
        
        erro_jacobi = np.linalg.norm(x_jacobi - x_exato)
        erro_seidel = np.linalg.norm(x_seidel - x_exato)
        
        print(f"Erro Gauss-Jacobi: {erro_jacobi:.2e}")
        print(f"Erro Gauss-Seidel: {erro_seidel:.2e}")
        
    except np.linalg.LinAlgError:
        print("Não foi possível calcular a solução exata")

# ============================================================================
# EXERCÍCIO 3: Polinômio de terceiro grau por sistema linear
# ============================================================================

def exercicio3():
    """
    Encontra polinômio de terceiro grau que passa pelos pontos dados
    """
    print("=== EXERCÍCIO 3: POLINÔMIO DE TERCEIRO GRAU ===")
    
    # Pontos dados: (-1, -3), (0, -1), (1, 2), (2, -2)
    pontos = [(-1, -3), (0, -1), (1, 2), (2, -2)]
    
    print("Pontos: (-1, -3), (0, -1), (1, 2), (2, -2)")
    print("Polinômio: p(x) = ax³ + bx² + cx + d")
    
    # Construir sistema linear
    A = np.zeros((4, 4))
    b = np.zeros(4)
    
    for i, (x, y) in enumerate(pontos):
        A[i, 0] = x**3  # coeficiente de a
        A[i, 1] = x**2  # coeficiente de b
        A[i, 2] = x     # coeficiente de c
        A[i, 3] = 1     # coeficiente de d
        b[i] = y
    
    print(f"\nSistema linear:")
    print("a(-1)³ + b(-1)² + c(-1) + d = -3")
    print("a(0)³ + b(0)² + c(0) + d = -1")
    print("a(1)³ + b(1)² + c(1) + d = 2")
    print("a(2)³ + b(2)² + c(2) + d = -2")
    
    print(f"\nMatriz A:")
    print(A)
    print(f"\nVetor b:")
    print(b)
    
    # Resolver o sistema
    try:
        coeficientes = solve(A, b)
        a, b_coef, c, d = coeficientes
        
        print(f"\nCoeficientes encontrados:")
        print(f"a = {a:.6f}")
        print(f"b = {b_coef:.6f}")
        print(f"c = {c:.6f}")
        print(f"d = {d:.6f}")
        
        print(f"\nPolinômio: p(x) = {a:.6f}x³ + {b_coef:.6f}x² + {c:.6f}x + {d:.6f}")
        
        # Verificar se o polinômio passa pelos pontos
        print(f"\nVerificação:")
        for x, y_esperado in pontos:
            y_calculado = a*x**3 + b_coef*x**2 + c*x + d
            erro = abs(y_calculado - y_esperado)
            print(f"p({x}) = {y_calculado:.6f} (esperado: {y_esperado}), erro: {erro:.2e}")
        
    except np.linalg.LinAlgError:
        print("Erro: Sistema singular ou mal condicionado")

# ============================================================================
# EXERCÍCIO 4: Análise química - composição de substâncias
# ============================================================================

def exercicio4():
    """
    Resolve problema de análise química - versão básica
    """
    print("=== EXERCÍCIO 4: ANÁLISE QUÍMICA - COMPOSIÇÃO DE SUBSTÂNCIAS ===")
    
    print("Composto X pode ser constituído de 4 substâncias: A, B, C e D")
    print("Cada substância é constituída de componentes: a, b, c, d")
    print("Tabela de proporções:")
    print("Componente\tem X\tem A\tem B\tem C\tem D")
    print("a\t\t26%\t15%\t36%\t20%\t31%")
    print("b\t\t19%\t28%\t11%\t15%\t22%")
    print("c\t\t31%\t27%\t36%\t33%\t24%")
    print("d\t\t24%\t30%\t17%\t32%\t23%")
    
    # Matriz de coeficientes (proporções de cada componente em cada substância)
    A = np.array([
        [15, 36, 20, 31],  # componente a
        [28, 11, 15, 22],  # componente b
        [27, 36, 33, 24],  # componente c
        [30, 17, 32, 23]   # componente d
    ])
    
    # Vetor de resultados (proporções encontradas em X)
    b = np.array([26, 19, 31, 24])
    
    print(f"\nSistema linear:")
    print("15x₁ + 36x₂ + 20x₃ + 31x₄ = 26")
    print("28x₁ + 11x₂ + 15x₃ + 22x₄ = 19")
    print("27x₁ + 36x₂ + 33x₃ + 24x₄ = 31")
    print("30x₁ + 17x₂ + 32x₃ + 23x₄ = 24")
    print("onde x₁, x₂, x₃, x₄ são as proporções de A, B, C, D em X")
    
    # Resolver o sistema
    try:
        x = solve(A, b)
        
        print(f"\nSolução:")
        print(f"Proporção de A em X: {x[0]:.4f} = {x[0]*100:.2f}%")
        print(f"Proporção de B em X: {x[1]:.4f} = {x[1]*100:.2f}%")
        print(f"Proporção de C em X: {x[2]:.4f} = {x[2]*100:.2f}%")
        print(f"Proporção de D em X: {x[3]:.4f} = {x[3]*100:.2f}%")
        
        total = sum(x)
        print(f"\nTotal: {total:.4f} = {total*100:.2f}%")
        
        if abs(total - 1.0) < 0.01:
            print("✓ A solução faz sentido (total próximo de 100%)")
        else:
            print("⚠️ Verificar a solução (total deveria ser 100%)")
        
        # Verificar se as proporções são positivas
        if all(xi >= 0 for xi in x):
            print("✓ Todas as proporções são positivas")
        else:
            print("⚠️ Algumas proporções são negativas")
        
    except np.linalg.LinAlgError:
        print("Erro: Sistema singular ou mal condicionado")

# ============================================================================
# EXERCÍCIO 5: Análise química - versão mais realista
# ============================================================================

def exercicio5():
    """
    Resolve problema de análise química - versão mais realista
    """
    print("=== EXERCÍCIO 5: ANÁLISE QUÍMICA - VERSÃO MAIS REALISTA ===")
    
    print("Composto X pode ser constituído de 4 substâncias: A, B, C e D")
    print("Existem outras substâncias desconhecidas em X")
    print("Tabela de proporções (não soma 100%):")
    print("Componente\tem X\tem A\tem B\tem C\tem D")
    print("a\t\t24.3%\t15%\t36%\t20%\t31%")
    print("b\t\t15%\t28%\t11%\t15%\t22%")
    print("c\t\t26.2%\t27%\t36%\t33%\t24%")
    print("d\t\t21.5%\t30%\t17%\t32%\t23%")
    
    # Matriz de coeficientes
    A = np.array([
        [15, 36, 20, 31],  # componente a
        [28, 11, 15, 22],  # componente b
        [27, 36, 33, 24],  # componente c
        [30, 17, 32, 23]   # componente d
    ])
    
    # Vetor de resultados
    b = np.array([24.3, 15.0, 26.2, 21.5])
    
    print(f"\nSistema linear:")
    print("15x₁ + 36x₂ + 20x₃ + 31x₄ = 24.3")
    print("28x₁ + 11x₂ + 15x₃ + 22x₄ = 15.0")
    print("27x₁ + 36x₂ + 33x₃ + 24x₄ = 26.2")
    print("30x₁ + 17x₂ + 32x₃ + 23x₄ = 21.5")
    
    # Resolver usando mínimos quadrados (sistema sobredeterminado)
    try:
        # Usar mínimos quadrados para resolver Ax ≈ b
        x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        
        print(f"\nSolução por mínimos quadrados:")
        print(f"Proporção de A em X: {x[0]:.4f} = {x[0]*100:.2f}%")
        print(f"Proporção de B em X: {x[1]:.4f} = {x[1]*100:.2f}%")
        print(f"Proporção de C em X: {x[2]:.4f} = {x[2]*100:.2f}%")
        print(f"Proporção de D em X: {x[3]:.4f} = {x[3]*100:.2f}%")
        
        total = sum(x)
        print(f"\nTotal: {total:.4f} = {total*100:.2f}%")
        
        # Calcular resíduos
        b_calculado = A @ x
        residuo_total = np.linalg.norm(b - b_calculado)
        print(f"\nResíduo total: {residuo_total:.6f}")
        
        print(f"\nComparação:")
        print("Componente\tEsperado\tCalculado\tDiferença")
        print("-" * 50)
        for i, comp in enumerate(['a', 'b', 'c', 'd']):
            print(f"{comp}\t\t{b[i]:.1f}%\t\t{b_calculado[i]:.1f}%\t\t{b[i] - b_calculado[i]:.1f}%")
        
        print(f"\nINTERPRETAÇÃO:")
        print("Como o sistema é sobredeterminado e há substâncias desconhecidas,")
        print("a solução por mínimos quadrados fornece a melhor aproximação.")
        print("O resíduo indica o erro de ajuste do modelo.")
        
    except np.linalg.LinAlgError:
        print("Erro: Sistema singular ou mal condicionado")

# ============================================================================
# EXERCÍCIO 6: Análise química - versão ainda mais realista
# ============================================================================

def exercicio6():
    """
    Resolve problema de análise química - versão ainda mais realista
    """
    print("=== EXERCÍCIO 6: ANÁLISE QUÍMICA - VERSÃO AINDA MAIS REALISTA ===")
    
    print("Composto X pode ser constituído de 4 substâncias: A, B, C e D")
    print("Existem outras substâncias desconhecidas em A, B, C e D também")
    print("Tabela de proporções (não soma 100% em nenhuma coluna):")
    print("Componente\tem X\tem A\tem B\tem C\tem D")
    print("a\t\t8%\t5%\t6%\t11%\t17%")
    print("b\t\t7%\t8%\t11%\t5%\t6%")
    print("c\t\t12%\t7%\t16%\t13%\t14%")
    print("d\t\t2%\t12%\t11%\t12%\t14%")
    
    # Matriz de coeficientes
    A = np.array([
        [5, 6, 11, 17],   # componente a
        [8, 11, 5, 6],    # componente b
        [7, 16, 13, 14],  # componente c
        [12, 11, 12, 14]  # componente d
    ])
    
    # Vetor de resultados
    b = np.array([8, 7, 12, 2])
    
    print(f"\nSistema linear:")
    print("5x₁ + 6x₂ + 11x₃ + 17x₄ = 8")
    print("8x₁ + 11x₂ + 5x₃ + 6x₄ = 7")
    print("7x₁ + 16x₂ + 13x₃ + 14x₄ = 12")
    print("12x₁ + 11x₂ + 12x₃ + 14x₄ = 2")
    
    # Resolver usando mínimos quadrados
    try:
        x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        
        print(f"\nSolução por mínimos quadrados:")
        print(f"Proporção de A em X: {x[0]:.4f} = {x[0]*100:.2f}%")
        print(f"Proporção de B em X: {x[1]:.4f} = {x[1]*100:.2f}%")
        print(f"Proporção de C em X: {x[2]:.4f} = {x[2]*100:.2f}%")
        print(f"Proporção de D em X: {x[3]:.4f} = {x[3]*100:.2f}%")
        
        total = sum(x)
        print(f"\nTotal: {total:.4f} = {total*100:.2f}%")
        
        # Calcular resíduos
        b_calculado = A @ x
        residuo_total = np.linalg.norm(b - b_calculado)
        print(f"\nResíduo total: {residuo_total:.6f}")
        
        print(f"\nComparação:")
        print("Componente\tEsperado\tCalculado\tDiferença")
        print("-" * 50)
        for i, comp in enumerate(['a', 'b', 'c', 'd']):
            print(f"{comp}\t\t{b[i]:.1f}%\t\t{b_calculado[i]:.1f}%\t\t{b[i] - b_calculado[i]:.1f}%")
        
        print(f"\nINTERPRETAÇÃO:")
        print("Esta é a versão mais realista, onde há incertezas em todas as")
        print("medições. A solução por mínimos quadrados fornece a melhor")
        print("aproximação possível, mas deve ser interpretada com cuidado.")
        print("O resíduo alto indica que o modelo pode não ser adequado.")
        
        # Verificar se as proporções fazem sentido
        if any(xi < 0 for xi in x):
            print("\n⚠️ ATENÇÃO: Algumas proporções são negativas!")
            print("Isso pode indicar que o modelo não é adequado ou")
            print("que há erros nas medições.")
        
    except np.linalg.LinAlgError:
        print("Erro: Sistema singular ou mal condicionado")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Sistemas Lineares
    """
    print("MÉTODOS NUMÉRICOS - SISTEMAS LINEARES")
    print("=" * 60)
    
    # Executar exercícios
    print("\n" + "="*60)
    exercicio1()
    
    print("\n" + "="*60)
    exercicio2()
    
    print("\n" + "="*60)
    exercicio3()
    
    print("\n" + "="*60)
    exercicio4()
    
    print("\n" + "="*60)
    exercicio5()
    
    print("\n" + "="*60)
    exercicio6()
    
    print("\n" + "="*60)
    print("EXECUÇÃO CONCLUÍDA!")
    print("Todos os exercícios de Sistemas Lineares foram resolvidos.")

if __name__ == "__main__":
    main()
