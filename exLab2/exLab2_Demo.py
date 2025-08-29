"""
Métodos Numéricos - Sistemas Lineares
Demonstração dos Exercícios do exlab2.txt
"""

import numpy as np

# ============================================================================
# EXERCÍCIO 1: Problema do Parquinho
# ============================================================================

def exercicio1():
    """
    Resolve o problema do parquinho com 4 brinquedos
    """
    print("=== EXERCÍCIO 1: PROBLEMA DO PARQUINHO ===")
    print("Um parquinho tem 4 brinquedos: A, B, C e D")
    
    # Sistema de equações em estado estacionário
    # A = 20 + (1/6)C + (1/3)B + (1/3)D - (1/2)A
    # B = (1/2)A + (1/2)C - B
    # C = 10 + (1/6)A + (1/3)B + (1/3)D - (1/2)C
    # D = (1/6)A + (1/6)C + (1/3)B
    
    # Reorganizando:
    # (3/2)A - (1/3)B - (1/6)C - (1/3)D = 20
    # -(1/2)A + 2B - (1/2)C = 0
    # -(1/6)A - (1/3)B + (3/2)C - (1/3)D = 10
    # -(1/6)A - (1/6)C - (1/3)B + D = 0
    
    A = np.array([
        [3/2, -1/3, -1/6, -1/3],
        [-1/2, 2, -1/2, 0],
        [-1/6, -1/3, 3/2, -1/3],
        [-1/6, -1/6, -1/3, 1]
    ])
    
    b = np.array([20, 0, 10, 0])
    
    print("Matriz do sistema:")
    print(A)
    print(f"Vetor independente: {b}")
    
    # Resolvendo o sistema
    try:
        solucao = np.linalg.solve(A, b)
        print(f"\nSolução do sistema:")
        print(f"A = {solucao[0]:.2f} pessoas")
        print(f"B = {solucao[1]:.2f} pessoas")
        print(f"C = {solucao[2]:.2f} pessoas")
        print(f"D = {solucao[3]:.2f} pessoas")
        print(f"Total: {sum(solucao):.2f} pessoas")
        
        return solucao
        
    except np.linalg.LinAlgError:
        print("Sistema não tem solução única")
        return None

# ============================================================================
# EXERCÍCIO 2: Polinômio de Terceiro Grau
# ============================================================================

def exercicio2():
    """
    Encontra o polinômio de terceiro grau que passa pelos pontos dados
    """
    print("\n=== EXERCÍCIO 2: POLINÔMIO DE TERCEIRO GRAU ===")
    print("Encontrar polinômio p(x) = ax³ + bx² + cx + d que passa pelos pontos:")
    pontos = [(-1, -3), (0, -1), (1, 2), (2, -2)]
    
    for i, (x, y) in enumerate(pontos):
        print(f"Ponto {i+1}: ({x}, {y})")
    
    # Construindo a matriz do sistema
    A = []
    b = []
    
    for x, y in pontos:
        linha = [x**3, x**2, x, 1]  # coeficientes de a, b, c, d
        A.append(linha)
        b.append(y)
    
    A = np.array(A)
    b = np.array(b)
    
    print(f"\nMatriz do sistema:")
    print(A)
    print(f"Vetor independente: {b}")
    
    # Resolvendo o sistema
    try:
        coeficientes = np.linalg.solve(A, b)
        a, b_coef, c, d = coeficientes
        
        print(f"\nSolução:")
        print(f"a = {a:.6f}")
        print(f"b = {b_coef:.6f}")
        print(f"c = {c:.6f}")
        print(f"d = {d:.6f}")
        
        print(f"\nPolinômio: p(x) = {a:.6f}x³ + {b_coef:.6f}x² + {c:.6f}x + {d:.6f}")
        
        # Verificando a solução
        print(f"\nVerificação:")
        for x, y in pontos:
            p_x = a*x**3 + b_coef*x**2 + c*x + d
            print(f"p({x}) = {p_x:.6f} (esperado: {y})")
        
        return coeficientes
        
    except np.linalg.LinAlgError:
        print("Sistema não tem solução única")
        return None

# ============================================================================
# EXERCÍCIO 3: Análise Química - Composição de Substâncias
# ============================================================================

def exercicio3():
    """
    Resolve o problema de composição química (versão ideal)
    """
    print("\n=== EXERCÍCIO 3: ANÁLISE QUÍMICA (VERSÃO IDEAL) ===")
    print("Determinar como as substâncias A, B, C e D foram misturadas")
    
    # Dados do problema
    composicao_X = [26, 19, 31, 24]  # em %
    print(f"Composição do composto X: {composicao_X}")
    
    # Matriz onde cada linha é uma substância e cada coluna é um componente
    composicao_substancias = np.array([
        [15, 28, 27, 30],  # Substância A
        [36, 11, 36, 17],  # Substância B
        [20, 15, 33, 32],  # Substância C
        [31, 22, 24, 23]   # Substância D
    ])
    
    print("Composição das substâncias puras:")
    print("A:", composicao_substancias[0])
    print("B:", composicao_substancias[1])
    print("C:", composicao_substancias[2])
    print("D:", composicao_substancias[3])
    
    A = composicao_substancias.T  # Transposta para ter as equações nas linhas
    b = np.array(composicao_X)
    
    print(f"\nMatriz do sistema:")
    print(A)
    print(f"Vetor independente: {b}")
    
    # Resolvendo o sistema
    try:
        proporcoes = np.linalg.solve(A, b)
        
        print(f"\nSolução:")
        print(f"Proporção de A: {proporcoes[0]:.4f} ({proporcoes[0]*100:.2f}%)")
        print(f"Proporção de B: {proporcoes[1]:.4f} ({proporcoes[1]*100:.2f}%)")
        print(f"Proporção de C: {proporcoes[2]:.4f} ({proporcoes[2]*100:.2f}%)")
        print(f"Proporção de D: {proporcoes[3]:.4f} ({proporcoes[3]*100:.2f}%)")
        
        soma = sum(proporcoes)
        print(f"Soma das proporções: {soma:.4f}")
        
        # Verificando a solução
        print(f"\nVerificação:")
        resultado = A @ proporcoes
        for i, (esperado, obtido) in enumerate(zip(composicao_X, resultado)):
            print(f"Componente {chr(97+i)}: {obtido:.2f}% (esperado: {esperado}%)")
        
        return proporcoes
        
    except np.linalg.LinAlgError:
        print("Sistema não tem solução única")
        return None

# ============================================================================
# EXERCÍCIO 4: Análise Química - Versão Realista
# ============================================================================

def exercicio4():
    """
    Resolve o problema de composição química (versão realista)
    """
    print("\n=== EXERCÍCIO 4: ANÁLISE QUÍMICA (VERSÃO REALISTA) ===")
    print("Determinar como as substâncias A, B, C e D foram misturadas")
    
    # Dados do problema (versão realista)
    composicao_X_real = [24.3, 15.0, 26.2, 21.5]  # em %
    print(f"Composição do composto X: {composicao_X_real}")
    
    soma_conhecida = sum(composicao_X_real)
    print(f"Soma dos componentes conhecidos: {soma_conhecida:.1f}%")
    print(f"Componentes desconhecidos: {100 - soma_conhecida:.1f}%")
    
    # Mesma matriz do exercício 3
    composicao_substancias = np.array([
        [15, 28, 27, 30],  # Substância A
        [36, 11, 36, 17],  # Substância B
        [20, 15, 33, 32],  # Substância C
        [31, 22, 24, 23]   # Substância D
    ])
    
    A = composicao_substancias.T
    b = np.array(composicao_X_real)
    
    print(f"\nMatriz do sistema:")
    print(A)
    print(f"Vetor independente: {b}")
    
    # Abordagem 1: Resolver o sistema como está
    print("\n--- Abordagem 1: Resolver sistema como está ---")
    try:
        proporcoes_1 = np.linalg.solve(A, b)
        print("Solução obtida:")
        for i, prop in enumerate(proporcoes_1):
            print(f"Proporção de {chr(65+i)}: {prop:.4f} ({prop*100:.2f}%)")
        
        soma_1 = sum(proporcoes_1)
        print(f"Soma das proporções: {soma_1:.4f}")
        
    except np.linalg.LinAlgError:
        print("Sistema não tem solução única")
    
    # Abordagem 2: Mínimos quadrados
    print("\n--- Abordagem 2: Mínimos quadrados ---")
    try:
        proporcoes_2 = np.linalg.lstsq(A, b, rcond=None)[0]
        print("Solução por mínimos quadrados:")
        for i, prop in enumerate(proporcoes_2):
            print(f"Proporção de {chr(65+i)}: {prop:.4f} ({prop*100:.2f}%)")
        
        soma_2 = sum(proporcoes_2)
        print(f"Soma das proporções: {soma_2:.4f}")
        
        # Verificando a solução
        resultado_2 = A @ proporcoes_2
        erro_quadratico = np.sum((resultado_2 - b)**2)
        print(f"Erro quadrático total: {erro_quadratico:.4f}")
        
        print("Verificação:")
        for i, (esperado, obtido) in enumerate(zip(composicao_X_real, resultado_2)):
            erro = abs(obtido - esperado)
            print(f"Componente {chr(97+i)}: {obtido:.2f}% (esperado: {esperado}%, erro: {erro:.2f}%)")
        
        return proporcoes_2
        
    except Exception as e:
        print(f"Erro na abordagem 2: {e}")
        return None

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de sistemas lineares
    """
    print("MÉTODOS NUMÉRICOS - SISTEMAS LINEARES")
    print("Demonstração dos Exercícios do exlab2.txt")
    print("=" * 60)
    
    # Executa todos os exercícios
    resultado1 = exercicio1()
    resultado2 = exercicio2()
    resultado3 = exercicio3()
    resultado4 = exercicio4()
    
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO CONCLUÍDA!")
    print("\nResumo dos resultados:")
    
    if resultado1 is not None:
        print(f"Exercício 1: {resultado1}")
    
    if resultado2 is not None:
        print(f"Exercício 2: Polinômio p(x) = {resultado2[0]:.3f}x³ + {resultado2[1]:.3f}x² + {resultado2[2]:.3f}x + {resultado2[3]:.3f}")
    
    if resultado3 is not None:
        print(f"Exercício 3: Proporções A={resultado3[0]:.3f}, B={resultado3[1]:.3f}, C={resultado3[2]:.3f}, D={resultado3[3]:.3f}")
    
    if resultado4 is not None:
        print(f"Exercício 4: Proporções A={resultado4[0]:.3f}, B={resultado4[1]:.3f}, C={resultado4[2]:.3f}, D={resultado4[3]:.3f}")

if __name__ == "__main__":
    main()
