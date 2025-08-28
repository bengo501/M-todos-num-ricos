"""
Métodos Numéricos - Cadeias de Markov
Demonstração dos Exercícios do exlab3.txt
"""

import numpy as np

# ============================================================================
# EXERCÍCIO 1: Sorveteria - Pesquisa de Satisfação
# ============================================================================

def exercicio1():
    """
    Resolve o problema da sorveteria com pesquisa de satisfação
    """
    print("=== EXERCÍCIO 1: SORVETERIA - PESQUISA DE SATISFAÇÃO ===")
    
    # Matriz de transição
    P = np.array([
        [0.70, 0.30],  # De Sim para [Sim, Não]
        [0.60, 0.40]   # De Não para [Sim, Não]
    ])
    
    print("Matriz de transição:")
    print("Estado atual → Estado futuro")
    print("           Sim   Não")
    print(f"Sim        {P[0,0]:.2f}   {P[0,1]:.2f}")
    print(f"Não        {P[1,0]:.2f}   {P[1,1]:.2f}")
    
    # Estado inicial: 1000 clientes
    estado_inicial = np.array([500, 500])  # [Sim, Não]
    
    # Cálculo para a quarta visita
    estado_4 = estado_inicial @ np.linalg.matrix_power(P, 4)
    print(f"\nDistribuição após 4 visitas:")
    print(f"Sim: {estado_4[0]:.0f} clientes ({estado_4[0]/1000*100:.1f}%)")
    print(f"Não: {estado_4[1]:.0f} clientes ({estado_4[1]/1000*100:.1f}%)")
    
    # Estado estacionário
    pi_estacionario = np.array([2/3, 1/3])
    estado_estacionario = pi_estacionario * 1000
    
    print(f"\nDistribuição a longo prazo:")
    print(f"Sim: {estado_estacionario[0]:.0f} clientes ({estado_estacionario[0]/1000*100:.1f}%)")
    print(f"Não: {estado_estacionario[1]:.0f} clientes ({estado_estacionario[1]/1000*100:.1f}%)")
    
    return estado_4, estado_estacionario

# ============================================================================
# EXERCÍCIO 2: Times de Futebol - Migração de Torcedores
# ============================================================================

def exercicio2():
    """
    Resolve o problema dos times de futebol e migração de torcedores
    """
    print("\n=== EXERCÍCIO 2: TIMES DE FUTEBOL - MIGRAÇÃO DE TORCEDORES ===")
    
    # Matriz de transição
    P = np.array([
        [0.78, 0.12, 0.10],  # De Trêmio para [Trêmio, Inter, Cassis]
        [0.07, 0.85, 0.08],  # De Inter para [Trêmio, Inter, Cassis]
        [0.11, 0.09, 0.80]   # De Cassis para [Trêmio, Inter, Cassis]
    ])
    
    print("Matriz de transição:")
    print("Estado atual → Estado futuro")
    print("           Trêmio Inter Cassis")
    for i, time in enumerate(['Trêmio', 'Inter', 'Cassis']):
        print(f"{time:10} {P[i,0]:.2f}   {P[i,1]:.2f}   {P[i,2]:.2f}")
    
    # Estado inicial
    estado_inicial = np.array([10000, 11000, 6000])  # [Trêmio, Inter, Cassis]
    
    # Evolução ano a ano
    print("\nEvolução ano a ano:")
    estado_atual = estado_inicial.copy()
    
    for ano in range(10):  # Mostrar 10 anos
        print(f"Ano {ano}: Trêmio={estado_atual[0]:.0f}, Inter={estado_atual[1]:.0f}, Cassis={estado_atual[2]:.0f}")
        estado_atual = estado_atual @ P
    
    # Estado estacionário
    P_100 = np.linalg.matrix_power(P, 100)
    estado_estacionario = estado_inicial @ P_100
    
    print(f"\nEstado final (estabilizado):")
    print(f"Trêmio: {estado_estacionario[0]:.0f} torcedores")
    print(f"Inter: {estado_estacionario[1]:.0f} torcedores")
    print(f"Cassis: {estado_estacionario[2]:.0f} torcedores")
    
    return estado_estacionario

# ============================================================================
# EXERCÍCIO 3: Lobo Guará - Regiões de Caça
# ============================================================================

def exercicio3():
    """
    Resolve o problema do lobo guará e suas regiões de caça
    """
    print("\n=== EXERCÍCIO 3: LOBO GUARÁ - REGIÕES DE CAÇA ===")
    
    # Matriz de transições
    P = np.array([
        [0.50, 0.00, 0.50],  # De A para [A, B, C] (não vai para B)
        [0.25, 0.50, 0.25],  # De B para [A, B, C] (escolhe outras duas)
        [0.25, 0.25, 0.50]   # De C para [A, B, C] (escolhe outras duas)
    ])
    
    print("(a) Matriz de transições:")
    print("Estado atual → Estado futuro")
    print("           A     B     C")
    for i, regiao in enumerate(['A', 'B', 'C']):
        print(f"{regiao:10} {P[i,0]:.2f}   {P[i,1]:.2f}   {P[i,2]:.2f}")
    
    # Probabilidade de estar em C na quarta-feira
    estado_inicial = np.array([1, 0, 0])  # Começa em A
    P_2 = np.linalg.matrix_power(P, 2)
    estado_quarta = estado_inicial @ P_2
    prob_C_quarta = estado_quarta[2]
    print(f"\n(b) Probabilidade de estar em C na quarta-feira: {prob_C_quarta:.4f} ({prob_C_quarta*100:.2f}%)")
    
    # Percentagem de vezes em B a longo prazo
    P_100 = np.linalg.matrix_power(P, 100)
    estado_estacionario = np.array([1/3, 1/3, 1/3]) @ P_100
    prob_B_longo_prazo = estado_estacionario[1]
    print(f"\n(c) Percentagem de vezes em B a longo prazo: {prob_B_longo_prazo:.4f} ({prob_B_longo_prazo*100:.2f}%)")
    
    return prob_C_quarta, prob_B_longo_prazo

# ============================================================================
# EXERCÍCIO 4: Mobilidade Social
# ============================================================================

def exercicio4():
    """
    Resolve o problema de mobilidade social
    """
    print("\n=== EXERCÍCIO 4: MOBILIDADE SOCIAL ===")
    
    # Matriz de transições original
    P_original = np.array([
        [0.70, 0.20, 0.10],  # De Ricos para [Ricos, Médios, Pobres]
        [0.15, 0.70, 0.15],  # De Médios para [Ricos, Médios, Pobres]
        [0.10, 0.30, 0.60]   # De Pobres para [Ricos, Médios, Pobres]
    ])
    
    print("(a) Matriz de transições original:")
    print("Estado atual → Estado futuro")
    print("           Ricos Médios Pobres")
    for i, classe in enumerate(['Ricos', 'Médios', 'Pobres']):
        print(f"{classe:10} {P_original[i,0]:.2f}   {P_original[i,1]:.2f}   {P_original[i,2]:.2f}")
    
    # Probabilidade de pessoa pobre ter netos ricos
    estado_pobre = np.array([0, 0, 1])  # Começa pobre
    P_2 = np.linalg.matrix_power(P_original, 2)
    estado_netos = estado_pobre @ P_2
    prob_netos_ricos = estado_netos[0]
    print(f"\n(b) Probabilidade de netos ricos: {prob_netos_ricos:.4f} ({prob_netos_ricos*100:.2f}%)")
    
    # Probabilidade de bisnetos ricos
    P_3 = np.linalg.matrix_power(P_original, 3)
    estado_bisnetos = estado_pobre @ P_3
    prob_bisnetos_ricos = estado_bisnetos[0]
    print(f"\n(c) Probabilidade de bisnetos ricos: {prob_bisnetos_ricos:.4f} ({prob_bisnetos_ricos*100:.2f}%)")
    
    # Proporção esperada a longo prazo (original)
    P_100 = np.linalg.matrix_power(P_original, 100)
    estado_estacionario_original = np.array([1/3, 1/3, 1/3]) @ P_100
    print(f"\n(d) Proporção esperada a longo prazo (original):")
    print(f"Ricos: {estado_estacionario_original[0]:.4f} ({estado_estacionario_original[0]*100:.2f}%)")
    print(f"Médios: {estado_estacionario_original[1]:.4f} ({estado_estacionario_original[1]*100:.2f}%)")
    print(f"Pobres: {estado_estacionario_original[2]:.4f} ({estado_estacionario_original[2]*100:.2f}%)")
    
    # Nova matriz com redistribuição de renda
    P_nova = np.array([
        [0.70, 0.20, 0.10],  # Ricos (inalterado)
        [0.15, 0.70, 0.15],  # Médios (inalterado)
        [0.10, 0.40, 0.50]   # Pobres (alterado)
    ])
    
    P_100_nova = np.linalg.matrix_power(P_nova, 100)
    estado_estacionario_nova = np.array([1/3, 1/3, 1/3]) @ P_100_nova
    print(f"\n(e) Nova proporção a longo prazo:")
    print(f"Ricos: {estado_estacionario_nova[0]:.4f} ({estado_estacionario_nova[0]*100:.2f}%)")
    print(f"Médios: {estado_estacionario_nova[1]:.4f} ({estado_estacionario_nova[1]*100:.2f}%)")
    print(f"Pobres: {estado_estacionario_nova[2]:.4f} ({estado_estacionario_nova[2]*100:.2f}%)")
    
    return prob_netos_ricos, prob_bisnetos_ricos, estado_estacionario_original, estado_estacionario_nova

# ============================================================================
# EXERCÍCIO 5: Jogo de Dados - Guilherme vs Christian
# ============================================================================

def exercicio5():
    """
    Resolve o problema do jogo de dados entre Guilherme e Christian
    """
    print("\n=== EXERCÍCIO 5: JOGO DE DADOS - GUILHERME VS CHRISTIAN ===")
    
    # Probabilidades do dado
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
    
    print("Matriz de transição:")
    print("Estado atual → Estado futuro")
    print("           Início G1_5  C1_5  G_vence C_vence")
    estados = ['Início', 'G1_5', 'C1_5', 'G_vence', 'C_vence']
    for i, estado in enumerate(estados):
        print(f"{estado:10} {P[i,0]:.3f}  {P[i,1]:.3f}  {P[i,2]:.3f}  {P[i,3]:.3f}  {P[i,4]:.3f}")
    
    # Cálculo das probabilidades de vitória
    prob_guilherme = 1/2
    prob_christian = 1 - prob_guilherme
    
    print(f"\nProbabilidade de Guilherme vencer: {prob_guilherme:.4f} ({prob_guilherme*100:.2f}%)")
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
    
    print("Matriz de transição:")
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
    
    # Estado estacionário
    P_100 = np.linalg.matrix_power(P, 100)
    estado_estacionario = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) @ P_100
    
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    
    print("Estado estacionário:")
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
    
    print("Nova matriz de transição:")
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
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Cadeias de Markov
    """
    print("MÉTODOS NUMÉRICOS - CADEIAS DE MARKOV")
    print("Demonstração dos Exercícios do exlab3.txt")
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
    
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO CONCLUÍDA!")
    print("\nResumo dos resultados:")
    
    print(f"Exercício 1: {resultado1[0][0]:.0f} clientes Sim após 4 visitas")
    print(f"Exercício 2: {resultado2[0]:.0f} torcedores Trêmio no estado estacionário")
    print(f"Exercício 3: {resultado3[0]:.2f}% probabilidade de estar em C na quarta-feira")
    print(f"Exercício 4: {resultado4[0]:.2f}% probabilidade de netos ricos")
    print(f"Exercício 5: {resultado5[0]:.2f}% probabilidade de Guilherme vencer")
    print(f"Exercício 7: Letra mais visitada: {resultado7[1]}")
    print(f"Exercício 9: Nova letra mais visitada: {resultado9[1]}")

if __name__ == "__main__":
    main()
