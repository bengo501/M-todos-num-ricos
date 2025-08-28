"""
Métodos Numéricos - Sistemas Lineares
Solução completa dos exercícios do exlab2.txt
"""

import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt

# ============================================================================
# EXERCÍCIO 1: Problema do Parquinho
# ============================================================================

def exercicio1():
    """
    Resolve o problema do parquinho com 4 brinquedos
    """
    print("=== EXERCÍCIO 1: PROBLEMA DO PARQUINHO ===")
    print("Um parquinho tem 4 brinquedos: A, B, C e D")
    print("\nInformações:")
    print("(a) 20 pessoas/hora chegam pelo portão principal → brinquedo A")
    print("(b) 10 pessoas/hora chegam pelo portão secundário → brinquedo C")
    print("(c) Pessoas vão primeiro para o brinquedo mais próximo")
    print("(d) Depois do primeiro brinquedo:")
    print("    - Metade vai para B")
    print("    - 1/3 vai embora")
    print("    - 1/6 vai para cada um dos outros dois brinquedos")
    print("(e) Depois de B ou D, pessoas se dividem igualmente entre A, C e D")
    
    # Vamos modelar o sistema de equações
    # Seja x_A, x_B, x_C, x_D o número de pessoas em cada brinquedo
    
    print("\n=== MODELAGEM DO SISTEMA ===")
    print("Vamos analisar o fluxo de pessoas:")
    
    # Pessoas que chegam diretamente
    chegada_A = 20  # pessoas/hora
    chegada_C = 10  # pessoas/hora
    
    print(f"Chegadas diretas: A = {chegada_A}, C = {chegada_C}")
    
    # Vamos calcular o fluxo passo a passo
    print("\n=== CÁLCULO DO FLUXO ===")
    
    # Passo 1: Pessoas que vão de A para outros brinquedos
    # Das 20 pessoas que chegam em A:
    # - 10 vão para B (metade)
    # - 3.33 vão embora (1/3)
    # - 3.33 vão para C (1/6)
    # - 3.33 vão para D (1/6)
    
    fluxo_A_para_B = chegada_A * 0.5  # 10
    fluxo_A_para_embora = chegada_A * (1/3)  # 6.67
    fluxo_A_para_C = chegada_A * (1/6)  # 3.33
    fluxo_A_para_D = chegada_A * (1/6)  # 3.33
    
    print(f"Fluxo de A: B={fluxo_A_para_B}, embora={fluxo_A_para_embora:.2f}, C={fluxo_A_para_C:.2f}, D={fluxo_A_para_D:.2f}")
    
    # Passo 2: Pessoas que vão de C para outros brinquedos
    # Das 10 pessoas que chegam em C:
    # - 5 vão para B (metade)
    # - 1.67 vão embora (1/3)
    # - 1.67 vão para A (1/6)
    # - 1.67 vão para D (1/6)
    
    fluxo_C_para_B = chegada_C * 0.5  # 5
    fluxo_C_para_embora = chegada_C * (1/3)  # 3.33
    fluxo_C_para_A = chegada_C * (1/6)  # 1.67
    fluxo_C_para_D = chegada_C * (1/6)  # 1.67
    
    print(f"Fluxo de C: B={fluxo_C_para_B}, embora={fluxo_C_para_embora:.2f}, A={fluxo_C_para_A:.2f}, D={fluxo_C_para_D:.2f}")
    
    # Passo 3: Pessoas que vão de B para outros brinquedos
    # Das pessoas que chegam em B (10 + 5 = 15):
    # - 5 vão para A (1/3)
    # - 5 vão para C (1/3)
    # - 5 vão para D (1/3)
    
    total_em_B = fluxo_A_para_B + fluxo_C_para_B  # 15
    fluxo_B_para_A = total_em_B * (1/3)  # 5
    fluxo_B_para_C = total_em_B * (1/3)  # 5
    fluxo_B_para_D = total_em_B * (1/3)  # 5
    
    print(f"Fluxo de B: A={fluxo_B_para_A}, C={fluxo_B_para_C}, D={fluxo_B_para_D}")
    
    # Passo 4: Pessoas que vão de D para outros brinquedos
    # Das pessoas que chegam em D (3.33 + 1.67 + 5 = 10):
    # - 3.33 vão para A (1/3)
    # - 3.33 vão para C (1/3)
    # - 3.33 vão para D (1/3)
    
    total_em_D = fluxo_A_para_D + fluxo_C_para_D + fluxo_B_para_D  # 10
    fluxo_D_para_A = total_em_D * (1/3)  # 3.33
    fluxo_D_para_C = total_em_D * (1/3)  # 3.33
    fluxo_D_para_D = total_em_D * (1/3)  # 3.33 (permanecem em D)
    
    print(f"Fluxo de D: A={fluxo_D_para_A:.2f}, C={fluxo_D_para_C:.2f}, D={fluxo_D_para_D:.2f}")
    
    # Agora vamos calcular o número final de pessoas em cada brinquedo
    print("\n=== CÁLCULO FINAL ===")
    
    # Pessoas em A:
    # - Chegam diretamente: 20
    # - Vêm de C: 1.67
    # - Vêm de B: 5
    # - Vêm de D: 3.33
    # - Vão embora: 6.67 + 3.33 + 5 + 3.33 = 18.33
    pessoas_A = chegada_A + fluxo_C_para_A + fluxo_B_para_A + fluxo_D_para_A
    pessoas_A -= (fluxo_A_para_embora + fluxo_C_para_embora + fluxo_B_para_A + fluxo_D_para_A)
    
    # Pessoas em B:
    # - Vêm de A: 10
    # - Vêm de C: 5
    # - Vão embora: 5 + 5 + 5 = 15
    pessoas_B = fluxo_A_para_B + fluxo_C_para_B
    pessoas_B -= (fluxo_B_para_A + fluxo_B_para_C + fluxo_B_para_D)
    
    # Pessoas em C:
    # - Chegam diretamente: 10
    # - Vêm de A: 3.33
    # - Vêm de B: 5
    # - Vêm de D: 3.33
    # - Vão embora: 3.33 + 1.67 + 5 + 3.33 = 13.33
    pessoas_C = chegada_C + fluxo_A_para_C + fluxo_B_para_C + fluxo_D_para_C
    pessoas_C -= (fluxo_A_para_C + fluxo_C_para_embora + fluxo_B_para_C + fluxo_D_para_C)
    
    # Pessoas em D:
    # - Vêm de A: 3.33
    # - Vêm de C: 1.67
    # - Vêm de B: 5
    # - Vêm de D: 3.33 (permanecem)
    # - Vão embora: 3.33 + 1.67 + 5 + 3.33 = 13.33
    pessoas_D = fluxo_A_para_D + fluxo_C_para_D + fluxo_B_para_D + fluxo_D_para_D
    pessoas_D -= (fluxo_A_para_D + fluxo_C_para_D + fluxo_B_para_D + fluxo_D_para_D)
    
    # Na verdade, vamos resolver isso de forma mais sistemática
    print("\n=== RESOLUÇÃO SISTEMÁTICA ===")
    
    # Sistema de equações em estado estacionário:
    # A = 20 + (1/6)C + (1/3)B + (1/3)D - (1/3)A - (1/6)A
    # B = (1/2)A + (1/2)C - (1/3)B - (1/3)B - (1/3)B
    # C = 10 + (1/6)A + (1/3)B + (1/3)D - (1/6)C - (1/3)C
    # D = (1/6)A + (1/6)C + (1/3)B + (1/3)D - (1/3)D
    
    # Simplificando:
    # A = 20 + (1/6)C + (1/3)B + (1/3)D - (1/2)A
    # B = (1/2)A + (1/2)C - B
    # C = 10 + (1/6)A + (1/3)B + (1/3)D - (1/2)C
    # D = (1/6)A + (1/6)C + (1/3)B
    
    # Reorganizando:
    # (3/2)A - (1/3)B - (1/6)C - (1/3)D = 20
    # -(1/2)A + 2B - (1/2)C = 0
    # -(1/6)A - (1/3)B + (3/2)C - (1/3)D = 10
    # -(1/6)A - (1/6)C - (1/3)B + D = 0
    
    # Matriz do sistema
    A = np.array([
        [3/2, -1/3, -1/6, -1/3],
        [-1/2, 2, -1/2, 0],
        [-1/6, -1/3, 3/2, -1/3],
        [-1/6, -1/6, -1/3, 1]
    ])
    
    b = np.array([20, 0, 10, 0])
    
    print("Matriz do sistema:")
    print(A)
    print(f"\nVetor independente: {b}")
    
    # Resolvendo o sistema
    try:
        solucao = np.linalg.solve(A, b)
        print(f"\nSolução do sistema:")
        print(f"A = {solucao[0]:.2f} pessoas")
        print(f"B = {solucao[1]:.2f} pessoas")
        print(f"C = {solucao[2]:.2f} pessoas")
        print(f"D = {solucao[3]:.2f} pessoas")
        
        print(f"\nTotal de pessoas no parque: {sum(solucao):.2f}")
        
    except np.linalg.LinAlgError:
        print("Sistema não tem solução única")
    
    return solucao

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
    
    print("\n=== SISTEMA DE EQUAÇÕES ===")
    print("Para cada ponto (x, y): ax³ + bx² + cx + d = y")
    
    # Construindo a matriz do sistema
    A = []
    b = []
    
    for x, y in pontos:
        linha = [x**3, x**2, x, 1]  # coeficientes de a, b, c, d
        A.append(linha)
        b.append(y)
        print(f"Para ({x}, {y}): {x**3}a + {x**2}b + {x}c + d = {y}")
    
    A = np.array(A)
    b = np.array(b)
    
    print(f"\nMatriz do sistema:")
    print(A)
    print(f"\nVetor independente: {b}")
    
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
        
        # Plotando o polinômio
        x_vals = np.linspace(-1.5, 2.5, 100)
        y_vals = a*x_vals**3 + b_coef*x_vals**2 + c*x_vals + d
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, 'b-', label='Polinômio p(x)')
        plt.plot([x for x, y in pontos], [y for x, y in pontos], 'ro', markersize=8, label='Pontos dados')
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Polinômio de Terceiro Grau')
        plt.legend()
        plt.savefig('polinomio_terceiro_grau.png', dpi=300, bbox_inches='tight')
        plt.show()
        
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
    print("para obter o composto X")
    
    # Dados do problema
    print("\nComposição do composto X:")
    composicao_X = [26, 19, 31, 24]  # em %
    print(f"Componente a: {composicao_X[0]}%")
    print(f"Componente b: {composicao_X[1]}%")
    print(f"Componente c: {composicao_X[2]}%")
    print(f"Componente d: {composicao_X[3]}%")
    
    print("\nComposição das substâncias puras:")
    # Matriz onde cada linha é uma substância e cada coluna é um componente
    composicao_substancias = np.array([
        [15, 28, 27, 30],  # Substância A
        [36, 11, 36, 17],  # Substância B
        [20, 15, 33, 32],  # Substância C
        [31, 22, 24, 23]   # Substância D
    ])
    
    print("Substância A:", composicao_substancias[0])
    print("Substância B:", composicao_substancias[1])
    print("Substância C:", composicao_substancias[2])
    print("Substância D:", composicao_substancias[3])
    
    print("\n=== SISTEMA DE EQUAÇÕES ===")
    print("Seja x_A, x_B, x_C, x_D as proporções de cada substância")
    print("Então: x_A + x_B + x_C + x_D = 1")
    print("E para cada componente:")
    
    # Sistema de equações
    # x_A * A_a + x_B * B_a + x_C * C_a + x_D * D_a = X_a
    # x_A * A_b + x_B * B_b + x_C * C_b + x_D * D_b = X_b
    # x_A * A_c + x_B * B_c + x_C * C_c + x_D * D_c = X_c
    # x_A * A_d + x_B * B_d + x_C * C_d + x_D * D_d = X_d
    
    A = composicao_substancias.T  # Transposta para ter as equações nas linhas
    b = np.array(composicao_X)
    
    print("Matriz do sistema:")
    print(A)
    print(f"\nVetor independente: {b}")
    
    # Resolvendo o sistema
    try:
        proporcoes = np.linalg.solve(A, b)
        
        print(f"\nSolução:")
        print(f"Proporção de A: {proporcoes[0]:.4f} ({proporcoes[0]*100:.2f}%)")
        print(f"Proporção de B: {proporcoes[1]:.4f} ({proporcoes[1]*100:.2f}%)")
        print(f"Proporção de C: {proporcoes[2]:.4f} ({proporcoes[2]*100:.2f}%)")
        print(f"Proporção de D: {proporcoes[3]:.4f} ({proporcoes[3]*100:.2f}%)")
        
        soma = sum(proporcoes)
        print(f"\nSoma das proporções: {soma:.4f}")
        
        if abs(soma - 1.0) < 1e-10:
            print("✓ Soma igual a 1 (solução válida)")
        else:
            print("⚠ Soma diferente de 1 (solução pode não ser válida)")
        
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
    print("para obter o composto X (com componentes desconhecidos)")
    
    # Dados do problema (versão realista)
    print("\nComposição do composto X (com componentes desconhecidos):")
    composicao_X_real = [24.3, 15.0, 26.2, 21.5]  # em %
    print(f"Componente a: {composicao_X_real[0]}%")
    print(f"Componente b: {composicao_X_real[1]}%")
    print(f"Componente c: {composicao_X_real[2]}%")
    print(f"Componente d: {composicao_X_real[3]}%")
    
    soma_conhecida = sum(composicao_X_real)
    print(f"Soma dos componentes conhecidos: {soma_conhecida:.1f}%")
    print(f"Componentes desconhecidos: {100 - soma_conhecida:.1f}%")
    
    print("\nComposição das substâncias puras (mesma do exercício 3):")
    composicao_substancias = np.array([
        [15, 28, 27, 30],  # Substância A
        [36, 11, 36, 17],  # Substância B
        [20, 15, 33, 32],  # Substância C
        [31, 22, 24, 23]   # Substância D
    ])
    
    print("Substância A:", composicao_substancias[0])
    print("Substância B:", composicao_substancias[1])
    print("Substância C:", composicao_substancias[2])
    print("Substância D:", composicao_substancias[3])
    
    print("\n=== ANÁLISE DO PROBLEMA ===")
    print("Como a soma não é 100%, existem componentes desconhecidos.")
    print("Isso significa que o sistema pode não ter solução exata.")
    print("Vamos tentar diferentes abordagens:")
    
    # Abordagem 1: Resolver o sistema como está
    print("\n--- Abordagem 1: Resolver sistema como está ---")
    A = composicao_substancias.T
    b = np.array(composicao_X_real)
    
    try:
        proporcoes_1 = np.linalg.solve(A, b)
        print("Solução obtida:")
        for i, prop in enumerate(proporcoes_1):
            print(f"Proporção de {chr(65+i)}: {prop:.4f} ({prop*100:.2f}%)")
        
        soma_1 = sum(proporcoes_1)
        print(f"Soma das proporções: {soma_1:.4f}")
        
        # Verificando a solução
        resultado_1 = A @ proporcoes_1
        print("Verificação:")
        for i, (esperado, obtido) in enumerate(zip(composicao_X_real, resultado_1)):
            print(f"Componente {chr(97+i)}: {obtido:.2f}% (esperado: {esperado}%)")
        
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
        
    except Exception as e:
        print(f"Erro na abordagem 2: {e}")
    
    # Abordagem 3: Normalizar para soma = 1
    print("\n--- Abordagem 3: Normalizar para soma = 1 ---")
    try:
        # Resolver o sistema e depois normalizar
        proporcoes_3 = np.linalg.solve(A, b)
        proporcoes_3_normalizadas = proporcoes_3 / sum(proporcoes_3)
        
        print("Solução normalizada:")
        for i, prop in enumerate(proporcoes_3_normalizadas):
            print(f"Proporção de {chr(65+i)}: {prop:.4f} ({prop*100:.2f}%)")
        
        soma_3 = sum(proporcoes_3_normalizadas)
        print(f"Soma das proporções: {soma_3:.4f}")
        
        # Verificando a solução
        resultado_3 = A @ proporcoes_3_normalizadas
        print("Verificação:")
        for i, (esperado, obtido) in enumerate(zip(composicao_X_real, resultado_3)):
            erro = abs(obtido - esperado)
            print(f"Componente {chr(97+i)}: {obtido:.2f}% (esperado: {esperado}%, erro: {erro:.2f}%)")
        
    except np.linalg.LinAlgError:
        print("Sistema não tem solução única")
    
    print("\n=== INTERPRETAÇÃO ===")
    print("A versão realista é mais complexa porque:")
    print("1. Existem componentes desconhecidos (13% do total)")
    print("2. O sistema pode não ter solução exata")
    print("3. As proporções obtidas podem não somar 1")
    print("4. É necessário interpretar os resultados com cuidado")
    print("5. Pode ser necessário usar métodos de otimização")
    
    return proporcoes_2 if 'proporcoes_2' in locals() else None

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def verificar_sistema(A: np.ndarray, b: np.ndarray, x: np.ndarray, nome: str):
    """
    Verifica se a solução x satisfaz o sistema Ax = b
    """
    print(f"\n=== VERIFICAÇÃO DO SISTEMA {nome} ===")
    resultado = A @ x
    erro = np.linalg.norm(resultado - b)
    print(f"Erro da solução: {erro:.2e}")
    
    if erro < 1e-10:
        print("✓ Solução correta!")
    else:
        print("⚠ Solução pode ter erros")
    
    return erro

def plotar_resultados():
    """
    Cria gráficos para visualizar os resultados
    """
    print("\n=== CRIANDO GRÁFICOS ===")
    
    # Gráfico para o exercício 1
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Exercício 1 - Fluxo de pessoas
    brinquedos = ['A', 'B', 'C', 'D']
    try:
        pessoas = exercicio1()
        axes[0, 0].bar(brinquedos, pessoas)
        axes[0, 0].set_title('Número de Pessoas por Brinquedo')
        axes[0, 0].set_ylabel('Pessoas')
        axes[0, 0].grid(True, alpha=0.3)
    except:
        axes[0, 0].text(0.5, 0.5, 'Exercício 1\n(Não executado)', ha='center', va='center')
        axes[0, 0].set_title('Exercício 1')
    
    # Exercício 2 - Polinômio
    try:
        coefs = exercicio2()
        if coefs is not None:
            x_vals = np.linspace(-1.5, 2.5, 100)
            y_vals = coefs[0]*x_vals**3 + coefs[1]*x_vals**2 + coefs[2]*x_vals + coefs[3]
            pontos = [(-1, -3), (0, -1), (1, 2), (2, -2)]
            
            axes[0, 1].plot(x_vals, y_vals, 'b-', label='Polinômio')
            axes[0, 1].plot([x for x, y in pontos], [y for x, y in pontos], 'ro', label='Pontos')
            axes[0, 1].set_title('Polinômio de Terceiro Grau')
            axes[0, 1].grid(True, alpha=0.3)
            axes[0, 1].legend()
    except:
        axes[0, 1].text(0.5, 0.5, 'Exercício 2\n(Não executado)', ha='center', va='center')
        axes[0, 1].set_title('Exercício 2')
    
    # Exercício 3 - Composição química
    try:
        props = exercicio3()
        if props is not None:
            axes[1, 0].pie(props, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
            axes[1, 0].set_title('Composição do Composto X (Ideal)')
    except:
        axes[1, 0].text(0.5, 0.5, 'Exercício 3\n(Não executado)', ha='center', va='center')
        axes[1, 0].set_title('Exercício 3')
    
    # Exercício 4 - Composição química realista
    try:
        props_real = exercicio4()
        if props_real is not None:
            axes[1, 1].pie(props_real, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')
            axes[1, 1].set_title('Composição do Composto X (Realista)')
    except:
        axes[1, 1].text(0.5, 0.5, 'Exercício 4\n(Não executado)', ha='center', va='center')
        axes[1, 1].set_title('Exercício 4')
    
    plt.tight_layout()
    plt.savefig('resultados_sistemas_lineares.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de sistemas lineares
    """
    print("MÉTODOS NUMÉRICOS - SISTEMAS LINEARES")
    print("Solução dos Exercícios do exlab2.txt")
    print("=" * 60)
    
    # Executa todos os exercícios
    resultado1 = exercicio1()
    resultado2 = exercicio2()
    resultado3 = exercicio3()
    resultado4 = exercicio4()
    
    # Cria gráficos
    plotar_resultados()
    
    print("\n" + "=" * 60)
    print("TODOS OS EXERCÍCIOS CONCLUÍDOS!")
    print("Gráficos salvos como:")
    print("- polinomio_terceiro_grau.png")
    print("- resultados_sistemas_lineares.png")

if __name__ == "__main__":
    main()
