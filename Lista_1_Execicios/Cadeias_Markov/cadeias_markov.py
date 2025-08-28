"""
Métodos Numéricos - Cadeias de Markov
Solução dos exercícios da Lista 1
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# ============================================================================
# EXERCÍCIO 1: Sorveteria - pesquisa de satisfação
# ============================================================================

def exercicio1():
    """
    Resolve o problema da sorveteria com pesquisa de satisfação
    """
    print("=== EXERCÍCIO 1: SORVETERIA - PESQUISA DE SATISFAÇÃO ===")
    
    print("Pesquisa de satisfação da sorveteria:")
    print("Pergunta: 'O nosso sorvete de chocolate é melhor do que o das outras sorveterias?'")
    print("\nMatriz de transição (Primeira → Segunda resposta):")
    print("        Sim    Não")
    print("Sim     70%    30%")
    print("Não     60%    40%")
    
    # Matriz de transição
    P = np.array([
        [0.7, 0.3],  # Se respondeu Sim na primeira vez
        [0.6, 0.4]   # Se respondeu Não na primeira vez
    ])
    
    print(f"\nMatriz de transição P:")
    print(P)
    
    # Estado inicial: 1000 clientes
    # Assumindo que inicialmente 50% responderam Sim e 50% Não
    estado_inicial = np.array([500, 500])  # [Sim, Não]
    
    print(f"\nEstado inicial: {estado_inicial} clientes")
    
    # Calcular distribuição após 4 visitas
    estado_4 = estado_inicial @ np.linalg.matrix_power(P, 4)
    
    print(f"\nDistribuição após 4 visitas:")
    print(f"Sim: {estado_4[0]:.0f} clientes ({estado_4[0]/1000*100:.1f}%)")
    print(f"Não: {estado_4[1]:.0f} clientes ({estado_4[1]/1000*100:.1f}%)")
    
    # Calcular distribuição de longo prazo (estado estacionário)
    # Resolver π = πP, ou seja, π(P - I) = 0
    # Como π₁ + π₂ = 1, temos um sistema linear
    
    A = np.array([
        [P[0,0] - 1, P[1,0]],  # π₁(P₁₁ - 1) + π₂P₂₁ = 0
        [1, 1]                  # π₁ + π₂ = 1
    ])
    
    b = np.array([0, 1])
    
    try:
        pi = np.linalg.solve(A, b)
        
        print(f"\nDistribuição de longo prazo (estado estacionário):")
        print(f"Sim: {pi[0]:.4f} = {pi[0]*100:.2f}%")
        print(f"Não: {pi[1]:.4f} = {pi[1]*100:.2f}%")
        
        # Verificar se é realmente um estado estacionário
        pi_calculado = pi @ P
        print(f"\nVerificação: πP = {pi_calculado}")
        print(f"Diferença: {np.linalg.norm(pi - pi_calculado):.2e}")
        
        # Evolução temporal
        print(f"\nEvolução temporal (primeiras 10 visitas):")
        print("Visita\tSim\t\tNão")
        print("-" * 30)
        
        estado_atual = estado_inicial.copy()
        for i in range(11):
            sim_pct = estado_atual[0] / 1000 * 100
            nao_pct = estado_atual[1] / 1000 * 100
            print(f"{i}\t{sim_pct:.1f}%\t\t{nao_pct:.1f}%")
            estado_atual = estado_atual @ P
        
    except np.linalg.LinAlgError:
        print("Erro ao calcular estado estacionário")

# ============================================================================
# EXERCÍCIO 2: Times de futebol - migração de torcedores
# ============================================================================

def exercicio2():
    """
    Resolve o problema dos times de futebol e migração de torcedores
    """
    print("=== EXERCÍCIO 2: TIMES DE FUTEBOL - MIGRAÇÃO DE TORCEDORES ===")
    
    print("Times: Trêmio, Internacional, Cassis")
    print("Probabilidades de migração:")
    print("- Trêmio → Internacional: 12%")
    print("- Internacional → Cassis: 8%")
    print("- Cassis → Trêmio: 11%")
    print("- Internacional → Trêmio: 7%")
    print("- Cassis → Internacional: 9%")
    print("- Trêmio → Cassis: 10%")
    
    # Matriz de transição (Trêmio, Internacional, Cassis)
    P = np.array([
        [0.78, 0.12, 0.10],  # Trêmio
        [0.07, 0.85, 0.08],  # Internacional
        [0.11, 0.09, 0.80]   # Cassis
    ])
    
    print(f"\nMatriz de transição P:")
    print(P)
    
    # Estado inicial
    estado_inicial = np.array([10000, 11000, 6000])  # [Trêmio, Internacional, Cassis]
    
    print(f"\nEstado inicial:")
    print(f"Trêmio: {estado_inicial[0]} torcedores")
    print(f"Internacional: {estado_inicial[1]} torcedores")
    print(f"Cassis: {estado_inicial[2]} torcedores")
    print(f"Total: {sum(estado_inicial)} torcedores")
    
    # Evolução temporal
    print(f"\nEvolução temporal (primeiros 10 anos):")
    print("Ano\tTrêmio\t\tInternacional\tCassis")
    print("-" * 50)
    
    estado_atual = estado_inicial.copy()
    for i in range(11):
        print(f"{i}\t{estado_atual[0]:.0f}\t\t{estado_atual[1]:.0f}\t\t{estado_atual[2]:.0f}")
        estado_atual = estado_atual @ P
    
    # Calcular estado estacionário
    # Resolver π = πP, ou seja, π(P - I) = 0
    # Como π₁ + π₂ + π₃ = 1, temos um sistema linear
    
    A = np.array([
        [P[0,0] - 1, P[1,0], P[2,0]],      # π₁(P₁₁ - 1) + π₂P₂₁ + π₃P₃₁ = 0
        [P[0,1], P[1,1] - 1, P[2,1]],      # π₁P₁₂ + π₂(P₂₂ - 1) + π₃P₃₂ = 0
        [1, 1, 1]                          # π₁ + π₂ + π₃ = 1
    ])
    
    b = np.array([0, 0, 1])
    
    try:
        pi = np.linalg.solve(A, b)
        
        print(f"\nDistribuição de longo prazo (estado estacionário):")
        print(f"Trêmio: {pi[0]:.4f} = {pi[0]*100:.2f}%")
        print(f"Internacional: {pi[1]:.4f} = {pi[1]*100:.2f}%")
        print(f"Cassis: {pi[2]:.4f} = {pi[2]*100:.2f}%")
        
        # Calcular número de torcedores no estado estacionário
        total_torcedores = sum(estado_inicial)
        torcedores_estacionario = pi * total_torcedores
        
        print(f"\nNúmero de torcedores no estado estacionário:")
        print(f"Trêmio: {torcedores_estacionario[0]:.0f} torcedores")
        print(f"Internacional: {torcedores_estacionario[1]:.0f} torcedores")
        print(f"Cassis: {torcedores_estacionario[2]:.0f} torcedores")
        
    except np.linalg.LinAlgError:
        print("Erro ao calcular estado estacionário")

# ============================================================================
# EXERCÍCIO 3: Lobo guará - regiões de caça
# ============================================================================

def exercicio3():
    """
    Resolve o problema do lobo guará e suas regiões de caça
    """
    print("=== EXERCÍCIO 3: LOBO GUARÁ - REGIÕES DE CAÇA ===")
    
    print("Lobo guará caça em 3 regiões: A, B, C")
    print("Regras:")
    print("- Se caça em uma região hoje, 50% de chance de repetir amanhã")
    print("- Se caça em A hoje, amanhã não caça em B")
    print("- Se caça em B ou C hoje, amanhã escolhe uma das outras duas (50% cada)")
    
    # Matriz de transição (A, B, C)
    # Se está em A: 50% fica em A, 0% vai para B, 50% vai para C
    # Se está em B: 50% vai para A, 0% fica em B, 50% vai para C
    # Se está em C: 50% vai para A, 50% vai para B, 0% fica em C
    P = np.array([
        [0.5, 0.0, 0.5],  # A
        [0.5, 0.0, 0.5],  # B
        [0.5, 0.5, 0.0]   # C
    ])
    
    print(f"\nMatriz de transição P:")
    print(P)
    
    # (a) Apresentar a matriz de transições
    print(f"\n(a) Matriz de transições apresentada acima")
    
    # (b) Probabilidade de estar em C na quarta-feira, começando em A na segunda
    print(f"\n(b) Probabilidade de estar em C na quarta-feira:")
    print("Segunda-feira: A")
    print("Quarta-feira: 2 dias depois")
    
    # Calcular P²
    P_quadrado = np.linalg.matrix_power(P, 2)
    print(f"\nP² (probabilidades em 2 dias):")
    print(P_quadrado)
    
    # Probabilidade de ir de A para C em 2 dias
    prob_A_para_C = P_quadrado[0, 2]
    print(f"Probabilidade de A → C em 2 dias: {prob_A_para_C:.4f} = {prob_A_para_C*100:.2f}%")
    
    # (c) Distribuição de longo prazo
    print(f"\n(c) Distribuição de longo prazo:")
    
    # Resolver sistema linear para estado estacionário
    A = np.array([
        [P[0,0] - 1, P[1,0], P[2,0]],
        [P[0,1], P[1,1] - 1, P[2,1]],
        [1, 1, 1]
    ])
    
    b = np.array([0, 0, 1])
    
    try:
        pi = np.linalg.solve(A, b)
        
        print(f"Probabilidade de longo prazo de caçar em B: {pi[1]:.4f} = {pi[1]*100:.2f}%")
        
        print(f"\nDistribuição completa de longo prazo:")
        print(f"Região A: {pi[0]:.4f} = {pi[0]*100:.2f}%")
        print(f"Região B: {pi[1]:.4f} = {pi[1]*100:.2f}%")
        print(f"Região C: {pi[2]:.4f} = {pi[2]*100:.2f}%")
        
    except np.linalg.LinAlgError:
        print("Erro ao calcular estado estacionário")

# ============================================================================
# EXERCÍCIO 4: Mobilidade social - Ricos, Médios e Pobres
# ============================================================================

def exercicio4():
    """
    Resolve o problema de mobilidade social
    """
    print("=== EXERCÍCIO 4: MOBILIDADE SOCIAL - RICOS, MÉDIOS E POBRES ===")
    
    print("Mobilidade social entre Ricos, Médios e Pobres:")
    print("Crianças Ricas:")
    print("- 70% permanecem Ricas")
    print("- 20% passam a ser Médias")
    print("- 10% passam a ser Pobres")
    print("\nCrianças Médias:")
    print("- 70% permanecem Médias")
    print("- 15% passam a ser Ricas")
    print("- 15% passam a ser Pobres")
    print("\nCrianças Pobres:")
    print("- 60% permanecem Pobres")
    print("- 30% tornam-se Médias")
    print("- 10% passam a ser Ricas")
    
    # Matriz de transição (Ricos, Médios, Pobres)
    P = np.array([
        [0.7, 0.2, 0.1],  # Ricos
        [0.15, 0.7, 0.15], # Médios
        [0.1, 0.3, 0.6]    # Pobres
    ])
    
    print(f"\nMatriz de transição P:")
    print(P)
    
    # (a) Apresentar a matriz de transições
    print(f"\n(a) Matriz de transições apresentada acima")
    
    # (b) Probabilidade de uma pessoa Pobre ter netos Ricos
    print(f"\n(b) Probabilidade de uma pessoa Pobre ter netos Ricos:")
    
    # Calcular P²
    P_quadrado = np.linalg.matrix_power(P, 2)
    print(f"\nP² (probabilidades em 2 gerações):")
    print(P_quadrado)
    
    # Probabilidade de ir de Pobres para Ricos em 2 gerações
    prob_pobres_para_ricos = P_quadrado[2, 0]
    print(f"Probabilidade Pobres → Ricos em 2 gerações: {prob_pobres_para_ricos:.4f} = {prob_pobres_para_ricos*100:.2f}%")
    
    # (c) Probabilidade de bisnetos Ricos
    print(f"\n(c) Probabilidade de uma pessoa Pobre ter bisnetos Ricos:")
    
    # Calcular P³
    P_cubo = np.linalg.matrix_power(P, 3)
    print(f"\nP³ (probabilidades em 3 gerações):")
    print(P_cubo)
    
    prob_pobres_para_ricos_3 = P_cubo[2, 0]
    print(f"Probabilidade Pobres → Ricos em 3 gerações: {prob_pobres_para_ricos_3:.4f} = {prob_pobres_para_ricos_3*100:.2f}%")
    
    # (d) Distribuição de longo prazo
    print(f"\n(d) Distribuição de longo prazo:")
    
    # Resolver sistema linear para estado estacionário
    A = np.array([
        [P[0,0] - 1, P[1,0], P[2,0]],
        [P[0,1], P[1,1] - 1, P[2,1]],
        [1, 1, 1]
    ])
    
    b = np.array([0, 0, 1])
    
    try:
        pi = np.linalg.solve(A, b)
        
        print(f"Distribuição de longo prazo:")
        print(f"Ricos: {pi[0]:.4f} = {pi[0]*100:.2f}%")
        print(f"Médios: {pi[1]:.4f} = {pi[1]*100:.2f}%")
        print(f"Pobres: {pi[2]:.4f} = {pi[2]*100:.2f}%")
        
    except np.linalg.LinAlgError:
        print("Erro ao calcular estado estacionário")
    
    # (e) Nova política de redistribuição
    print(f"\n(e) Nova política de redistribuição:")
    print("Crianças Pobres (nova política):")
    print("- 50% permanecem Pobres")
    print("- 40% tornam-se Médias")
    print("- 10% passam a ser Ricas")
    
    # Nova matriz de transição
    P_nova = np.array([
        [0.7, 0.2, 0.1],   # Ricos (inalterado)
        [0.15, 0.7, 0.15], # Médios (inalterado)
        [0.1, 0.4, 0.5]    # Pobres (alterado)
    ])
    
    print(f"\nNova matriz de transição P:")
    print(P_nova)
    
    # Calcular nova distribuição de longo prazo
    A_nova = np.array([
        [P_nova[0,0] - 1, P_nova[1,0], P_nova[2,0]],
        [P_nova[0,1], P_nova[1,1] - 1, P_nova[2,1]],
        [1, 1, 1]
    ])
    
    try:
        pi_nova = np.linalg.solve(A_nova, b)
        
        print(f"\nNova distribuição de longo prazo:")
        print(f"Ricos: {pi_nova[0]:.4f} = {pi_nova[0]*100:.2f}%")
        print(f"Médios: {pi_nova[1]:.4f} = {pi_nova[1]*100:.2f}%")
        print(f"Pobres: {pi_nova[2]:.4f} = {pi_nova[2]*100:.2f}%")
        
        print(f"\nComparação:")
        print("Categoria\tAntes\t\tDepois\t\tDiferença")
        print("-" * 50)
        print(f"Ricos\t\t{pi[0]*100:.2f}%\t\t{pi_nova[0]*100:.2f}%\t\t{(pi_nova[0]-pi[0])*100:+.2f}%")
        print(f"Médios\t\t{pi[1]*100:.2f}%\t\t{pi_nova[1]*100:.2f}%\t\t{(pi_nova[1]-pi[1])*100:+.2f}%")
        print(f"Pobres\t\t{pi[2]*100:.2f}%\t\t{pi_nova[2]*100:.2f}%\t\t{(pi_nova[2]-pi[2])*100:+.2f}%")
        
    except np.linalg.LinAlgError:
        print("Erro ao calcular nova distribuição de longo prazo")

# ============================================================================
# EXERCÍCIO 5: Jogo de dados - Guilherme vs Christian
# ============================================================================

def exercicio5():
    """
    Resolve o problema do jogo de dados entre Guilherme e Christian
    """
    print("=== EXERCÍCIO 5: JOGO DE DADOS - GUILHERME VS CHRISTIAN ===")
    
    print("Regras do jogo:")
    print("Guilherme vence: se tirar um 5 e na próxima jogada tirar outro 5")
    print("Christian vence: se tirar um 5 e na próxima jogada tirar um 6")
    
    # Estados: N5 (não é 5), 5 (tirou 5), G (Guilherme venceu), C (Christian venceu)
    # Probabilidades: P(5) = 1/6, P(6) = 1/6, P(N5) = 4/6 = 2/3
    
    print(f"\nProbabilidades:")
    print(f"P(5) = 1/6 = {1/6:.4f}")
    print(f"P(6) = 1/6 = {1/6:.4f}")
    print(f"P(N5) = 4/6 = {4/6:.4f}")
    
    # Matriz de transição (N5, 5, G, C)
    P = np.array([
        [2/3, 1/6, 0, 0],    # N5 → N5, N5 → 5
        [2/3, 0, 1/6, 1/6],  # 5 → N5, 5 → G (5), 5 → C (6)
        [0, 0, 1, 0],        # G → G (estado absorvente)
        [0, 0, 0, 1]         # C → C (estado absorvente)
    ])
    
    print(f"\nMatriz de transição P:")
    print(P)
    
    # Calcular probabilidades de absorção
    # Estados transientes: N5, 5
    # Estados absorventes: G, C
    
    # Matriz Q (transientes para transientes)
    Q = np.array([
        [2/3, 1/6],
        [2/3, 0]
    ])
    
    # Matriz R (transientes para absorventes)
    R = np.array([
        [0, 0],
        [1/6, 1/6]
    ])
    
    # Matriz fundamental N = (I - Q)^(-1)
    I = np.eye(2)
    N = np.linalg.inv(I - Q)
    
    # Probabilidades de absorção B = N * R
    B = N @ R
    
    print(f"\nMatriz fundamental N:")
    print(N)
    
    print(f"\nProbabilidades de absorção B:")
    print(B)
    
    # Interpretar resultados
    print(f"\nProbabilidades de vitória:")
    print(f"Começando em N5:")
    print(f"  Guilherme vence: {B[0, 0]:.4f} = {B[0, 0]*100:.2f}%")
    print(f"  Christian vence: {B[0, 1]:.4f} = {B[0, 1]*100:.2f}%")
    
    print(f"\nComeçando em 5:")
    print(f"  Guilherme vence: {B[1, 0]:.4f} = {B[1, 0]*100:.2f}%")
    print(f"  Christian vence: {B[1, 1]:.4f} = {B[1, 1]*100:.2f}%")
    
    # Verificar se as probabilidades somam 1
    print(f"\nVerificação (soma das probabilidades):")
    print(f"N5: {B[0, 0] + B[0, 1]:.4f}")
    print(f"5: {B[1, 0] + B[1, 1]:.4f}")

# ============================================================================
# EXERCÍCIO 6: Letras A-F em fila
# ============================================================================

def exercicio6():
    """
    Resolve o problema das letras A-F em fila
    """
    print("=== EXERCÍCIO 6: LETRAS A-F EM FILA ===")
    
    print("Letras A, B, C, D, E, F em fila")
    print("Pode saltar para vizinhas com probabilidades iguais:")
    print("- Uma vizinha: 100%")
    print("- Duas vizinhas: 50% para cada uma")
    
    # Estados: A, B, C, D, E, F
    # Probabilidades de transição
    P = np.array([
        [0, 1, 0, 0, 0, 0],    # A → B
        [0.5, 0, 0.5, 0, 0, 0], # B → A ou C
        [0, 0.5, 0, 0.5, 0, 0], # C → B ou D
        [0, 0, 0.5, 0, 0.5, 0], # D → C ou E
        [0, 0, 0, 0.5, 0, 0.5], # E → D ou F
        [0, 0, 0, 0, 1, 0]      # F → E
    ])
    
    print(f"\nMatriz de transição P:")
    print(P)
    
    # Verificar se é uma matriz de transição válida
    print(f"\nVerificação (soma das linhas deve ser 1):")
    for i, letra in enumerate(['A', 'B', 'C', 'D', 'E', 'F']):
        soma = sum(P[i, :])
        print(f"{letra}: {soma:.2f}")

# ============================================================================
# EXERCÍCIO 7: Distribuição de probabilidades
# ============================================================================

def exercicio7():
    """
    Calcula a distribuição de probabilidades para as letras A-F
    """
    print("=== EXERCÍCIO 7: DISTRIBUIÇÃO DE PROBABILIDADES ===")
    
    # Matriz de transição do exercício anterior
    P = np.array([
        [0, 1, 0, 0, 0, 0],    # A → B
        [0.5, 0, 0.5, 0, 0, 0], # B → A ou C
        [0, 0.5, 0, 0.5, 0, 0], # C → B ou D
        [0, 0, 0.5, 0, 0.5, 0], # D → C ou E
        [0, 0, 0, 0.5, 0, 0.5], # E → D ou F
        [0, 0, 0, 0, 1, 0]      # F → E
    ])
    
    # Estado inicial: começar em A
    estado_inicial = np.array([1, 0, 0, 0, 0, 0])
    
    print("Evolução da distribuição de probabilidades:")
    print("Começando em A")
    print("\nSaltos\tA\t\tB\t\tC\t\tD\t\tE\t\tF")
    print("-" * 80)
    
    estado_atual = estado_inicial.copy()
    for i in range(11):
        letras = ['A', 'B', 'C', 'D', 'E', 'F']
        probs = [f"{p:.4f}" for p in estado_atual]
        print(f"{i}\t" + "\t".join(probs))
        estado_atual = estado_atual @ P
    
    # Calcular estado estacionário
    print(f"\nEstado estacionário:")
    
    # Resolver sistema linear π = πP
    A = np.array([
        [P[0,0] - 1, P[1,0], P[2,0], P[3,0], P[4,0], P[5,0]],
        [P[0,1], P[1,1] - 1, P[2,1], P[3,1], P[4,1], P[5,1]],
        [P[0,2], P[1,2], P[2,2] - 1, P[3,2], P[4,2], P[5,2]],
        [P[0,3], P[1,3], P[2,3], P[3,3] - 1, P[4,3], P[5,3]],
        [P[0,4], P[1,4], P[2,4], P[3,4], P[4,4] - 1, P[5,4]],
        [1, 1, 1, 1, 1, 1]
    ])
    
    b = np.array([0, 0, 0, 0, 0, 1])
    
    try:
        pi = np.linalg.solve(A, b)
        
        letras = ['A', 'B', 'C', 'D', 'E', 'F']
        print("Letra\tProbabilidade")
        print("-" * 25)
        
        for i, letra in enumerate(letras):
            print(f"{letra}\t{pi[i]:.4f} = {pi[i]*100:.2f}%")
        
        # Encontrar a letra mais visitada
        max_idx = np.argmax(pi)
        print(f"\nLetra mais visitada: {letras[max_idx]} ({pi[max_idx]*100:.2f}%)")
        
    except np.linalg.LinAlgError:
        print("Erro ao calcular estado estacionário")

# ============================================================================
# EXERCÍCIO 8: Modificação com vogais
# ============================================================================

def exercicio8():
    """
    Modifica a matriz para incluir probabilidade extra para vogais
    """
    print("=== EXERCÍCIO 8: MODIFICAÇÃO COM VOGAIS ===")
    
    print("Nova regra: se estiver em uma vogal (A, E), também tem 2% de")
    print("probabilidade de pular para uma letra duas posições adiante")
    print("(descontado das probabilidades já existentes)")
    
    # Vogais: A, E
    # Nova matriz de transição
    P_nova = np.array([
        [0, 0.98, 0, 0.02, 0, 0],    # A → B (98%), A → C (2%)
        [0.5, 0, 0.5, 0, 0, 0],      # B → A ou C (inalterado)
        [0, 0.5, 0, 0.5, 0, 0],      # C → B ou D (inalterado)
        [0, 0, 0.5, 0, 0.5, 0],      # D → C ou E (inalterado)
        [0, 0, 0, 0.5, 0, 0.5],      # E → D ou F (inalterado)
        [0, 0, 0, 0, 1, 0]           # F → E (inalterado)
    ])
    
    print(f"\nNova matriz de transição P:")
    print(P_nova)
    
    # Verificar se é uma matriz de transição válida
    print(f"\nVerificação (soma das linhas deve ser 1):")
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    for i, letra in enumerate(letras):
        soma = sum(P_nova[i, :])
        print(f"{letra}: {soma:.2f}")

# ============================================================================
# EXERCÍCIO 9: Nova distribuição de probabilidades
# ============================================================================

def exercicio9():
    """
    Calcula a nova distribuição de probabilidades com a modificação
    """
    print("=== EXERCÍCIO 9: NOVA DISTRIBUIÇÃO DE PROBABILIDADES ===")
    
    # Nova matriz de transição do exercício anterior
    P_nova = np.array([
        [0, 0.98, 0, 0.02, 0, 0],    # A → B (98%), A → C (2%)
        [0.5, 0, 0.5, 0, 0, 0],      # B → A ou C
        [0, 0.5, 0, 0.5, 0, 0],      # C → B ou D
        [0, 0, 0.5, 0, 0.5, 0],      # D → C ou E
        [0, 0, 0, 0.5, 0, 0.5],      # E → D ou F
        [0, 0, 0, 0, 1, 0]           # F → E
    ])
    
    # Estado inicial: começar em A
    estado_inicial = np.array([1, 0, 0, 0, 0, 0])
    
    print("Evolução da distribuição de probabilidades (nova regra):")
    print("Começando em A")
    print("\nSaltos\tA\t\tB\t\tC\t\tD\t\tE\t\tF")
    print("-" * 80)
    
    estado_atual = estado_inicial.copy()
    for i in range(11):
        letras = ['A', 'B', 'C', 'D', 'E', 'F']
        probs = [f"{p:.4f}" for p in estado_atual]
        print(f"{i}\t" + "\t".join(probs))
        estado_atual = estado_atual @ P_nova
    
    # Calcular novo estado estacionário
    print(f"\nNovo estado estacionário:")
    
    # Resolver sistema linear π = πP
    A = np.array([
        [P_nova[0,0] - 1, P_nova[1,0], P_nova[2,0], P_nova[3,0], P_nova[4,0], P_nova[5,0]],
        [P_nova[0,1], P_nova[1,1] - 1, P_nova[2,1], P_nova[3,1], P_nova[4,1], P_nova[5,1]],
        [P_nova[0,2], P_nova[1,2], P_nova[2,2] - 1, P_nova[3,2], P_nova[4,2], P_nova[5,2]],
        [P_nova[0,3], P_nova[1,3], P_nova[2,3], P_nova[3,3] - 1, P_nova[4,3], P_nova[5,3]],
        [P_nova[0,4], P_nova[1,4], P_nova[2,4], P_nova[3,4], P_nova[4,4] - 1, P_nova[5,4]],
        [1, 1, 1, 1, 1, 1]
    ])
    
    b = np.array([0, 0, 0, 0, 0, 1])
    
    try:
        pi_nova = np.linalg.solve(A, b)
        
        letras = ['A', 'B', 'C', 'D', 'E', 'F']
        print("Letra\tProbabilidade")
        print("-" * 25)
        
        for i, letra in enumerate(letras):
            print(f"{letra}\t{pi_nova[i]:.4f} = {pi_nova[i]*100:.2f}%")
        
        # Encontrar a nova letra mais visitada
        max_idx = np.argmax(pi_nova)
        print(f"\nNova letra mais visitada: {letras[max_idx]} ({pi_nova[max_idx]*100:.2f}%)")
        
        # Comparar com a situação anterior
        print(f"\nComparação com a situação anterior:")
        print("A modificação das vogais alterou a distribuição de probabilidades")
        print("e pode ter mudado qual letra é mais visitada no longo prazo.")
        
    except np.linalg.LinAlgError:
        print("Erro ao calcular novo estado estacionário")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Cadeias de Markov
    """
    print("MÉTODOS NUMÉRICOS - CADEIAS DE MARKOV")
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
    exercicio7()
    
    print("\n" + "="*60)
    exercicio8()
    
    print("\n" + "="*60)
    exercicio9()
    
    print("\n" + "="*60)
    print("EXECUÇÃO CONCLUÍDA!")
    print("Todos os exercícios de Cadeias de Markov foram resolvidos.")

if __name__ == "__main__":
    main()
