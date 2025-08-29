"""
Métodos Numéricos - Cadeias de Markov
Solução completa dos exercícios do exlab3.txt
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

# ============================================================================
# EXERCÍCIO 1: Sorveteria - Pesquisa de Satisfação
# ============================================================================

def exercicio1():
    """
    Resolve o problema da sorveteria com pesquisa de satisfação
    """
    print("=== EXERCÍCIO 1: SORVETERIA - PESQUISA DE SATISFAÇÃO ===")
    print("Uma sorveteria faz pesquisa com clientes sobre qualidade do sorvete de chocolate")
    
    # Matriz de transição
    # Estados: 0 = Sim, 1 = Não
    # P[i][j] = probabilidade de ir do estado i para o estado j
    P = np.array([
        [0.70, 0.30],  # De Sim para [Sim, Não]
        [0.60, 0.40]   # De Não para [Sim, Não]
    ])
    
    print("\nMatriz de transição:")
    print("Estado atual → Estado futuro")
    print("           Sim   Não")
    print(f"Sim        {P[0,0]:.2f}   {P[0,1]:.2f}")
    print(f"Não        {P[1,0]:.2f}   {P[1,1]:.2f}")
    
    # Estado inicial: 1000 clientes
    # Assumindo que inicialmente 50% responderam Sim e 50% Não
    estado_inicial = np.array([500, 500])  # [Sim, Não]
    print(f"\nEstado inicial: {estado_inicial}")
    
    # Cálculo para a quarta visita
    print("\n=== CÁLCULO PARA A QUARTA VISITA ===")
    estado_4 = estado_inicial @ np.linalg.matrix_power(P, 4)
    print(f"Distribuição após 4 visitas:")
    print(f"Sim: {estado_4[0]:.0f} clientes ({estado_4[0]/1000*100:.1f}%)")
    print(f"Não: {estado_4[1]:.0f} clientes ({estado_4[1]/1000*100:.1f}%)")
    
    # Cálculo do estado estacionário (longo prazo)
    print("\n=== CÁLCULO DO ESTADO ESTACIONÁRIO ===")
    
    # Método 1: Potenciação da matriz
    P_100 = np.linalg.matrix_power(P, 100)
    estado_estacionario_1 = estado_inicial @ P_100
    print(f"Distribuição a longo prazo (método 1):")
    print(f"Sim: {estado_estacionario_1[0]:.0f} clientes ({estado_estacionario_1[0]/1000*100:.1f}%)")
    print(f"Não: {estado_estacionario_1[1]:.0f} clientes ({estado_estacionario_1[1]/1000*100:.1f}%)")
    
    # Método 2: Resolver sistema linear
    # π = πP, onde π é o vetor estacionário
    # π[0] + π[1] = 1 (normalização)
    # π[0] = 0.70π[0] + 0.60π[1]
    # π[1] = 0.30π[0] + 0.40π[1]
    
    # Sistema: π[0] = 0.70π[0] + 0.60π[1] e π[0] + π[1] = 1
    # Simplificando: 0.30π[0] = 0.60π[1] e π[0] + π[1] = 1
    # π[0] = 2π[1] e π[0] + π[1] = 1
    # 2π[1] + π[1] = 1 → 3π[1] = 1 → π[1] = 1/3
    # π[0] = 2/3
    
    pi_estacionario = np.array([2/3, 1/3])
    estado_estacionario_2 = pi_estacionario * 1000
    
    print(f"Distribuição a longo prazo (método 2):")
    print(f"Sim: {estado_estacionario_2[0]:.0f} clientes ({estado_estacionario_2[0]/1000*100:.1f}%)")
    print(f"Não: {estado_estacionario_2[1]:.0f} clientes ({estado_estacionario_2[1]/1000*100:.1f}%)")
    
    return estado_4, estado_estacionario_2

# ============================================================================
# EXERCÍCIO 2: Times de Futebol - Migração de Torcedores
# ============================================================================

def exercicio2():
    """
    Resolve o problema dos times de futebol e migração de torcedores
    """
    print("\n=== EXERCÍCIO 2: TIMES DE FUTEBOL - MIGRAÇÃO DE TORCEDORES ===")
    print("Três times: Trêmio, Internacional e Cassis")
    
    # Matriz de transição
    # Estados: 0 = Trêmio, 1 = Internacional, 2 = Cassis
    P = np.array([
        [0.78, 0.12, 0.10],  # De Trêmio para [Trêmio, Inter, Cassis]
        [0.07, 0.85, 0.08],  # De Inter para [Trêmio, Inter, Cassis]
        [0.11, 0.09, 0.80]   # De Cassis para [Trêmio, Inter, Cassis]
    ])
    
    print("\nMatriz de transição:")
    print("Estado atual → Estado futuro")
    print("           Trêmio Inter Cassis")
    for i, time in enumerate(['Trêmio', 'Inter', 'Cassis']):
        print(f"{time:10} {P[i,0]:.2f}   {P[i,1]:.2f}   {P[i,2]:.2f}")
    
    # Estado inicial
    estado_inicial = np.array([10000, 11000, 6000])  # [Trêmio, Inter, Cassis]
    print(f"\nEstado inicial: {estado_inicial}")
    
    # Evolução ano a ano até estabilização
    print("\n=== EVOLUÇÃO ANO A ANO ===")
    estado_atual = estado_inicial.copy()
    anos = []
    trêmio_evolucao = []
    inter_evolucao = []
    cassis_evolucao = []
    
    for ano in range(20):  # Vamos simular 20 anos
        anos.append(ano)
        trêmio_evolucao.append(estado_atual[0])
        inter_evolucao.append(estado_atual[1])
        cassis_evolucao.append(estado_atual[2])
        
        if ano <= 5:  # Mostrar apenas os primeiros 6 anos
            print(f"Ano {ano}: Trêmio={estado_atual[0]:.0f}, Inter={estado_atual[1]:.0f}, Cassis={estado_atual[2]:.0f}")
        
        estado_atual = estado_atual @ P
        
        # Verificar se estabilizou (diferença < 1 torcedor)
        if ano > 0:
            diff = np.abs(estado_atual - (estado_atual @ P))
            if np.all(diff < 1):
                print(f"Estabilizou no ano {ano}")
                break
    
    # Estado estacionário
    print(f"\nEstado final (estabilizado):")
    print(f"Trêmio: {estado_atual[0]:.0f} torcedores")
    print(f"Inter: {estado_atual[1]:.0f} torcedores")
    print(f"Cassis: {estado_atual[2]:.0f} torcedores")
    
    return anos, trêmio_evolucao, inter_evolucao, cassis_evolucao, estado_atual

# ============================================================================
# EXERCÍCIO 3: Lobo Guará - Regiões de Caça
# ============================================================================

def exercicio3():
    """
    Resolve o problema do lobo guará e suas regiões de caça
    """
    print("\n=== EXERCÍCIO 3: LOBO GUARÁ - REGIÕES DE CAÇA ===")
    print("Lobo guará caça em 3 regiões: A, B, C")
    
    # (a) Matriz de transições
    # Estados: 0 = A, 1 = B, 2 = C
    # Regras:
    # - Se caça em uma região, 50% de repetir
    # - Se caça em A, não caça em B no dia seguinte
    # - Se caça em B ou C, escolhe uma das outras duas com 50% cada
    
    P = np.array([
        [0.50, 0.00, 0.50],  # De A para [A, B, C] (não vai para B)
        [0.25, 0.50, 0.25],  # De B para [A, B, C] (escolhe outras duas)
        [0.25, 0.25, 0.50]   # De C para [A, B, C] (escolhe outras duas)
    ])
    
    print("\n(a) Matriz de transições:")
    print("Estado atual → Estado futuro")
    print("           A     B     C")
    for i, regiao in enumerate(['A', 'B', 'C']):
        print(f"{regiao:10} {P[i,0]:.2f}   {P[i,1]:.2f}   {P[i,2]:.2f}")
    
    # (b) Probabilidade de estar em C na quarta-feira, começando em A na segunda
    print("\n(b) Probabilidade de estar em C na quarta-feira (2 dias depois)")
    estado_inicial = np.array([1, 0, 0])  # Começa em A
    P_2 = np.linalg.matrix_power(P, 2)
    estado_quarta = estado_inicial @ P_2
    prob_C_quarta = estado_quarta[2]
    print(f"Probabilidade de estar em C na quarta-feira: {prob_C_quarta:.4f} ({prob_C_quarta*100:.2f}%)")
    
    # (c) Percentagem de vezes em B a longo prazo
    print("\n(c) Percentagem de vezes em B a longo prazo")
    P_100 = np.linalg.matrix_power(P, 100)
    estado_estacionario = np.array([1/3, 1/3, 1/3]) @ P_100  # Estado inicial não importa
    prob_B_longo_prazo = estado_estacionario[1]
    print(f"Percentagem de vezes em B a longo prazo: {prob_B_longo_prazo:.4f} ({prob_B_longo_prazo*100:.2f}%)")
    
    return P, prob_C_quarta, prob_B_longo_prazo

# ============================================================================
# EXERCÍCIO 4: Mobilidade Social
# ============================================================================

def exercicio4():
    """
    Resolve o problema de mobilidade social
    """
    print("\n=== EXERCÍCIO 4: MOBILIDADE SOCIAL ===")
    print("Classes sociais: Ricos, Médios, Pobres")
    
    # (a) Matriz de transições original
    # Estados: 0 = Ricos, 1 = Médios, 2 = Pobres
    P_original = np.array([
        [0.70, 0.20, 0.10],  # De Ricos para [Ricos, Médios, Pobres]
        [0.15, 0.70, 0.15],  # De Médios para [Ricos, Médios, Pobres]
        [0.10, 0.30, 0.60]   # De Pobres para [Ricos, Médios, Pobres]
    ])
    
    print("\n(a) Matriz de transições original:")
    print("Estado atual → Estado futuro")
    print("           Ricos Médios Pobres")
    for i, classe in enumerate(['Ricos', 'Médios', 'Pobres']):
        print(f"{classe:10} {P_original[i,0]:.2f}   {P_original[i,1]:.2f}   {P_original[i,2]:.2f}")
    
    # (b) Probabilidade de pessoa pobre ter netos ricos
    print("\n(b) Probabilidade de pessoa pobre ter netos ricos")
    estado_pobre = np.array([0, 0, 1])  # Começa pobre
    P_2 = np.linalg.matrix_power(P_original, 2)
    estado_netos = estado_pobre @ P_2
    prob_netos_ricos = estado_netos[0]
    print(f"Probabilidade de netos ricos: {prob_netos_ricos:.4f} ({prob_netos_ricos*100:.2f}%)")
    
    # (c) Probabilidade de bisnetos ricos
    print("\n(c) Probabilidade de bisnetos ricos")
    P_3 = np.linalg.matrix_power(P_original, 3)
    estado_bisnetos = estado_pobre @ P_3
    prob_bisnetos_ricos = estado_bisnetos[0]
    print(f"Probabilidade de bisnetos ricos: {prob_bisnetos_ricos:.4f} ({prob_bisnetos_ricos*100:.2f}%)")
    
    # (d) Proporção esperada a longo prazo (original)
    print("\n(d) Proporção esperada a longo prazo (original)")
    P_100 = np.linalg.matrix_power(P_original, 100)
    estado_estacionario_original = np.array([1/3, 1/3, 1/3]) @ P_100
    print(f"Ricos: {estado_estacionario_original[0]:.4f} ({estado_estacionario_original[0]*100:.2f}%)")
    print(f"Médios: {estado_estacionario_original[1]:.4f} ({estado_estacionario_original[1]*100:.2f}%)")
    print(f"Pobres: {estado_estacionario_original[2]:.4f} ({estado_estacionario_original[2]*100:.2f}%)")
    
    # (e) Nova matriz com redistribuição de renda
    print("\n(e) Nova proporção com redistribuição de renda")
    P_nova = np.array([
        [0.70, 0.20, 0.10],  # Ricos (inalterado)
        [0.15, 0.70, 0.15],  # Médios (inalterado)
        [0.10, 0.40, 0.50]   # Pobres (alterado: 50% permanecem, 40% viram médios, 10% viram ricos)
    ])
    
    print("Nova matriz de transições:")
    print("Estado atual → Estado futuro")
    print("           Ricos Médios Pobres")
    for i, classe in enumerate(['Ricos', 'Médios', 'Pobres']):
        print(f"{classe:10} {P_nova[i,0]:.2f}   {P_nova[i,1]:.2f}   {P_nova[i,2]:.2f}")
    
    P_100_nova = np.linalg.matrix_power(P_nova, 100)
    estado_estacionario_nova = np.array([1/3, 1/3, 1/3]) @ P_100_nova
    print(f"\nNova proporção a longo prazo:")
    print(f"Ricos: {estado_estacionario_nova[0]:.4f} ({estado_estacionario_nova[0]*100:.2f}%)")
    print(f"Médios: {estado_estacionario_nova[1]:.4f} ({estado_estacionario_nova[1]*100:.2f}%)")
    print(f"Pobres: {estado_estacionario_nova[2]:.4f} ({estado_estacionario_nova[2]*100:.2f}%)")
    
    return P_original, prob_netos_ricos, prob_bisnetos_ricos, estado_estacionario_original, estado_estacionario_nova

# ============================================================================
# EXERCÍCIO 5: Jogo de Dados - Guilherme vs Christian
# ============================================================================

def exercicio5():
    """
    Resolve o problema do jogo de dados entre Guilherme e Christian
    """
    print("\n=== EXERCÍCIO 5: JOGO DE DADOS - GUILHERME VS CHRISTIAN ===")
    print("Regras:")
    print("- Guilherme vence: tira 5, depois tira 5 novamente")
    print("- Christian vence: tira 5, depois tira 6")
    
    # Estados da cadeia de Markov:
    # 0 = Início
    # 1 = Guilherme tirou primeiro 5
    # 2 = Christian tirou primeiro 5
    # 3 = Guilherme venceu
    # 4 = Christian venceu
    
    # Probabilidades do dado:
    prob_5 = 1/6
    prob_6 = 1/6
    prob_outro = 4/6
    
    # Matriz de transição
    P = np.array([
        [prob_outro, prob_5, prob_5, 0, 0],           # Início
        [prob_outro, prob_5, 0, prob_5, 0],           # Guilherme tirou primeiro 5
        [prob_outro, 0, prob_5, 0, prob_6],           # Christian tirou primeiro 5
        [0, 0, 0, 1, 0],                              # Guilherme venceu (absorvente)
        [0, 0, 0, 0, 1]                               # Christian venceu (absorvente)
    ])
    
    print("\nMatriz de transição:")
    print("Estado atual → Estado futuro")
    print("           Início G1_5  C1_5  G_vence C_vence")
    estados = ['Início', 'G1_5', 'C1_5', 'G_vence', 'C_vence']
    for i, estado in enumerate(estados):
        print(f"{estado:10} {P[i,0]:.3f}  {P[i,1]:.3f}  {P[i,2]:.3f}  {P[i,3]:.3f}  {P[i,4]:.3f}")
    
    # Cálculo das probabilidades de vitória
    print("\n=== CÁLCULO DAS PROBABILIDADES DE VITÓRIA ===")
    
    # Método: Resolver sistema linear para probabilidades de absorção
    # π[i] = probabilidade de Guilherme vencer começando do estado i
    
    # Sistema de equações:
    # π[0] = prob_outro*π[0] + prob_5*π[1] + prob_5*π[2]
    # π[1] = prob_outro*π[0] + prob_5*π[1] + prob_5*1
    # π[2] = prob_outro*π[0] + prob_5*π[2] + 0
    # π[3] = 1 (Guilherme já venceu)
    # π[4] = 0 (Christian já venceu)
    
    # Simplificando:
    # π[0] = (4/6)π[0] + (1/6)π[1] + (1/6)π[2]
    # π[1] = (4/6)π[0] + (1/6)π[1] + (1/6)
    # π[2] = (4/6)π[0] + (1/6)π[2]
    
    # Resolvendo:
    # π[0] = (4/6)π[0] + (1/6)π[1] + (1/6)π[2]
    # (2/6)π[0] = (1/6)π[1] + (1/6)π[2]
    # 2π[0] = π[1] + π[2]
    
    # π[1] = (4/6)π[0] + (1/6)π[1] + (1/6)
    # (5/6)π[1] = (4/6)π[0] + (1/6)
    # 5π[1] = 4π[0] + 1
    
    # π[2] = (4/6)π[0] + (1/6)π[2]
    # (5/6)π[2] = (4/6)π[0]
    # 5π[2] = 4π[0]
    # π[2] = (4/5)π[0]
    
    # Substituindo:
    # 2π[0] = π[1] + (4/5)π[0]
    # 2π[0] - (4/5)π[0] = π[1]
    # (6/5)π[0] = π[1]
    
    # 5π[1] = 4π[0] + 1
    # 5*(6/5)π[0] = 4π[0] + 1
    # 6π[0] = 4π[0] + 1
    # 2π[0] = 1
    # π[0] = 1/2
    
    # π[1] = (6/5)*(1/2) = 3/5
    # π[2] = (4/5)*(1/2) = 2/5
    
    prob_guilherme = 1/2
    prob_christian = 1 - prob_guilherme
    
    print(f"Probabilidade de Guilherme vencer: {prob_guilherme:.4f} ({prob_guilherme*100:.2f}%)")
    print(f"Probabilidade de Christian vencer: {prob_christian:.4f} ({prob_christian*100:.2f}%)")
    
    return prob_guilherme, prob_christian

# ============================================================================
# EXERCÍCIO 6: Letras A-F - Saltos entre Vizinhas
# ============================================================================

def exercicio6():
    """
    Resolve o problema das letras A-F com saltos entre vizinhas
    """
    print("\n=== EXERCÍCIO 6: LETRAS A-F - SALTOS ENTRE VIZINHAS ===")
    print("Letras: A, B, C, D, E, F")
    print("Regras:")
    print("- Uma vizinha: 100% de probabilidade")
    print("- Duas vizinhas: 50% para cada uma")
    
    # Estados: 0=A, 1=B, 2=C, 3=D, 4=E, 5=F
    P = np.zeros((6, 6))
    
    # Preenchendo a matriz de transição
    for i in range(6):
        # Uma vizinha (100%)
        if i > 0:  # Pode ir para a esquerda
            P[i, i-1] += 0.5
        if i < 5:  # Pode ir para a direita
            P[i, i+1] += 0.5
        
        # Duas vizinhas (50% cada)
        if i > 1:  # Pode ir duas posições para a esquerda
            P[i, i-2] += 0.25
        if i < 4:  # Pode ir duas posições para a direita
            P[i, i+2] += 0.25
    
    print("\nMatriz de transição:")
    print("Estado atual → Estado futuro")
    print("           A     B     C     D     E     F")
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    for i, letra in enumerate(letras):
        print(f"{letra:10}", end="")
        for j in range(6):
            print(f" {P[i,j]:.2f}  ", end="")
        print()
    
    return P

# ============================================================================
# EXERCÍCIO 7: Distribuição de Probabilidades - Letras A-F
# ============================================================================

def exercicio7(P):
    """
    Calcula a distribuição de probabilidades para as letras A-F
    """
    print("\n=== EXERCÍCIO 7: DISTRIBUIÇÃO DE PROBABILIDADES ===")
    
    # Estado inicial: começa em A
    estado_inicial = np.array([1, 0, 0, 0, 0, 0])
    
    # Evolução ao longo do tempo
    print("Evolução da distribuição de probabilidades:")
    print("Passos  A     B     C     D     E     F")
    
    estado_atual = estado_inicial.copy()
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    
    for passo in range(10):
        print(f"{passo:2}     ", end="")
        for j in range(6):
            print(f"{estado_atual[j]:.3f} ", end="")
        print()
        
        estado_atual = estado_atual @ P
    
    # Estado estacionário
    print("\nEstado estacionário (após muitos passos):")
    P_100 = np.linalg.matrix_power(P, 100)
    estado_estacionario = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) @ P_100
    
    for i, letra in enumerate(letras):
        print(f"{letra}: {estado_estacionario[i]:.4f} ({estado_estacionario[i]*100:.2f}%)")
    
    # Letra mais visitada
    letra_mais_visitada = letras[np.argmax(estado_estacionario)]
    print(f"\nLetra mais visitada: {letra_mais_visitada}")
    
    return estado_estacionario, letra_mais_visitada

# ============================================================================
# EXERCÍCIO 8: Nova Matriz com Vogais
# ============================================================================

def exercicio8():
    """
    Cria nova matriz considerando vogais (A, E) com probabilidade extra
    """
    print("\n=== EXERCÍCIO 8: NOVA MATRIZ COM VOGAIS ===")
    print("Nova regra: Se estiver em vogal (A, E), 2% de pular duas posições adiante")
    
    # Estados: 0=A, 1=B, 2=C, 3=D, 4=E, 5=F
    P_nova = np.zeros((6, 6))
    
    # Preenchendo a matriz de transição
    for i in range(6):
        # Uma vizinha (100% - ajustado para vogais)
        if i > 0:  # Pode ir para a esquerda
            if i in [0, 4]:  # Vogal (A ou E)
                P_nova[i, i-1] += 0.49  # 50% - 1% = 49%
            else:
                P_nova[i, i-1] += 0.5
        
        if i < 5:  # Pode ir para a direita
            if i in [0, 4]:  # Vogal (A ou E)
                P_nova[i, i+1] += 0.49  # 50% - 1% = 49%
            else:
                P_nova[i, i+1] += 0.5
        
        # Duas vizinhas (50% cada - ajustado para vogais)
        if i > 1:  # Pode ir duas posições para a esquerda
            if i in [0, 4]:  # Vogal (A ou E)
                P_nova[i, i-2] += 0.24  # 25% - 1% = 24%
            else:
                P_nova[i, i-2] += 0.25
        
        if i < 4:  # Pode ir duas posições para a direita
            if i in [0, 4]:  # Vogal (A ou E)
                P_nova[i, i+2] += 0.24  # 25% - 1% = 24%
            else:
                P_nova[i, i+2] += 0.25
        
        # Nova regra: vogais podem pular duas posições adiante com 2%
        if i in [0, 4]:  # Vogal (A ou E)
            if i < 4:  # Pode pular duas posições adiante
                P_nova[i, i+2] += 0.02
    
    print("\nNova matriz de transição:")
    print("Estado atual → Estado futuro")
    print("           A     B     C     D     E     F")
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    for i, letra in enumerate(letras):
        print(f"{letra:10}", end="")
        for j in range(6):
            print(f" {P_nova[i,j]:.2f}  ", end="")
        print()
    
    return P_nova

# ============================================================================
# EXERCÍCIO 9: Nova Distribuição de Probabilidades
# ============================================================================

def exercicio9(P_nova):
    """
    Calcula a nova distribuição de probabilidades
    """
    print("\n=== EXERCÍCIO 9: NOVA DISTRIBUIÇÃO DE PROBABILIDADES ===")
    
    # Estado inicial: começa em A
    estado_inicial = np.array([1, 0, 0, 0, 0, 0])
    
    # Estado estacionário
    P_100 = np.linalg.matrix_power(P_nova, 100)
    estado_estacionario_nova = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) @ P_100
    
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    
    print("Nova distribuição estacionária:")
    for i, letra in enumerate(letras):
        print(f"{letra}: {estado_estacionario_nova[i]:.4f} ({estado_estacionario_nova[i]*100:.2f}%)")
    
    # Nova letra mais visitada
    letra_mais_visitada_nova = letras[np.argmax(estado_estacionario_nova)]
    print(f"\nNova letra mais visitada: {letra_mais_visitada_nova}")
    
    return estado_estacionario_nova, letra_mais_visitada_nova

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def plotar_evolucao_times(anos, trêmio, inter, cassis):
    """
    Plota a evolução dos torcedores dos times
    """
    plt.figure(figsize=(12, 8))
    plt.plot(anos, trêmio, 'r-', label='Trêmio', linewidth=2)
    plt.plot(anos, inter, 'b-', label='Internacional', linewidth=2)
    plt.plot(anos, cassis, 'g-', label='Cassis', linewidth=2)
    plt.xlabel('Ano')
    plt.ylabel('Número de Torcedores')
    plt.title('Evolução do Número de Torcedores por Time')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('evolucao_times.png', dpi=300, bbox_inches='tight')
    plt.show()

def plotar_distribuicao_letras(estado_original, estado_nova):
    """
    Plota a distribuição de probabilidades das letras
    """
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Distribuição original
    ax1.bar(letras, estado_original, color='skyblue', alpha=0.7)
    ax1.set_title('Distribuição Original')
    ax1.set_ylabel('Probabilidade')
    ax1.grid(True, alpha=0.3)
    
    # Distribuição nova
    ax2.bar(letras, estado_nova, color='lightcoral', alpha=0.7)
    ax2.set_title('Distribuição com Vogais')
    ax2.set_ylabel('Probabilidade')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('distribuicao_letras.png', dpi=300, bbox_inches='tight')
    plt.show()

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Cadeias de Markov
    """
    print("MÉTODOS NUMÉRICOS - CADEIAS DE MARKOV")
    print("Solução dos Exercícios do exlab3.txt")
    print("=" * 60)
    
    # Executa todos os exercícios
    resultado1 = exercicio1()
    resultado2 = exercicio2()
    resultado3 = exercicio3()
    resultado4 = exercicio4()
    resultado5 = exercicio5()
    P_letras = exercicio6()
    resultado7 = exercicio7(P_letras)
    P_nova_letras = exercicio8()
    resultado9 = exercicio9(P_nova_letras)
    
    # Cria gráficos
    print("\n=== CRIANDO GRÁFICOS ===")
    try:
        plotar_evolucao_times(*resultado2[:4])
        plotar_distribuicao_letras(resultado7[0], resultado9[0])
    except Exception as e:
        print(f"Erro ao criar gráficos: {e}")
    
    print("\n" + "=" * 60)
    print("TODOS OS EXERCÍCIOS CONCLUÍDOS!")
    print("Gráficos salvos como:")
    print("- evolucao_times.png")
    print("- distribuicao_letras.png")

if __name__ == "__main__":
    main()
