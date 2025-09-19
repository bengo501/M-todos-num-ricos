#!/usr/bin/env python3
"""
Simulador de Jogo Coreano - Trabalho de Métodos Numéricos

Este programa calcula a população estacionária de atores em um jogo
onde eles se movem entre n salas conectadas, com probabilidades específicas
de movimento e possibilidade de morte nas extremidades.

Autor: Implementação baseada no enunciado do Trabalho II
"""

import numpy as np
import sys


def criar_matriz_transicao(n):
    """
    Cria a matriz de transição P para n salas.
    
    Args:
        n (int): Número de salas (deve ser ímpar)
    
    Returns:
        numpy.ndarray: Matriz de transição P de tamanho n×n
    """
    print(f"\n=== CRIANDO MATRIZ DE TRANSIÇÃO PARA {n} SALAS ===")
    
    # Probabilidade de ficar na mesma sala
    prob_ficar = 1.0 / n
    print(f"Probabilidade de ficar na mesma sala: {prob_ficar:.4f}")
    
    # Probabilidade total de se mover
    prob_mover = 1.0 - prob_ficar
    print(f"Probabilidade total de movimento: {prob_mover:.4f}")
    
    # Inicializar matriz com zeros
    P = np.zeros((n, n))
    
    # Preencher a matriz sala por sala
    for i in range(n):
        sala_atual = i + 1  # Salas numeradas de 1 a n
        print(f"\nSala {sala_atual}:")
        
        # Probabilidade de ficar na mesma sala
        P[i, i] = prob_ficar
        print(f"  Ficar na sala {sala_atual}: {prob_ficar:.4f}")
        
        # Identificar salas vizinhas
        vizinhas = []
        if i > 0:  # Tem vizinha à esquerda
            vizinhas.append(i - 1)
        if i < n - 1:  # Tem vizinha à direita
            vizinhas.append(i + 1)
        
        print(f"  Salas vizinhas: {[v+1 for v in vizinhas]}")
        
        # Distribuir probabilidade de movimento entre vizinhas
        if len(vizinhas) > 0:
            # Para salas das pontas: metade da prob_mover vai para vizinha, metade é morte
            # Para salas internas: prob_mover é dividida igualmente entre as 2 vizinhas
            if len(vizinhas) == 1:  # Sala da ponta
                prob_por_vizinha = prob_mover / 2.0  # Metade para vizinha
                prob_morte = prob_mover / 2.0        # Metade para morte
                print(f"  Probabilidade para vizinha: {prob_por_vizinha:.4f}")
                print(f"  Probabilidade de morte: {prob_morte:.4f}")
            else:  # Sala interna
                prob_por_vizinha = prob_mover / 2.0  # Dividir igualmente entre 2 vizinhas
                prob_morte = 0.0
                print(f"  Probabilidade por vizinha: {prob_por_vizinha:.4f}")
            
            for j in vizinhas:
                P[i, j] = prob_por_vizinha
                print(f"  Ir para sala {j+1}: {prob_por_vizinha:.4f}")
        
        # Mostrar probabilidade de morte para referência
        if len(vizinhas) == 1:
            print(f"  💀 Morte (sair do jogo): {prob_morte:.4f}")
    
    print(f"\nMatriz de transição P ({n}×{n}):")
    print(P)
    
    # Verificar se as linhas somam corretamente
    print(f"\nVerificação - soma das linhas (deve ser ≤ 1.0):")
    for i in range(n):
        soma = np.sum(P[i, :])
        prob_morte = 1.0 - soma
        print(f"  Sala {i+1}: soma = {soma:.4f}, morte = {prob_morte:.4f}")
    
    return P


def calcular_populacao_estacionaria(n, taxa_chegada=1.0):
    """
    Calcula a distribuição estacionária de população nas salas.
    
    Args:
        n (int): Número de salas
        taxa_chegada (float): Taxa de chegada de novos atores por episódio
    
    Returns:
        numpy.ndarray: Vetor com população esperada em cada sala
    """
    print(f"\n=== CALCULANDO POPULAÇÃO ESTACIONÁRIA ===")
    print(f"Número de salas: {n}")
    print(f"Taxa de chegada: {taxa_chegada} atores/episódio")
    
    # Criar matriz de transição
    P = criar_matriz_transicao(n)
    
    # Criar matriz identidade
    I = np.eye(n)
    print(f"\nMatriz identidade I ({n}×{n}) criada")
    
    # Calcular (I - P^T)
    A = I - P.T
    print(f"\nMatriz A = I - P^T:")
    print(A)
    
    # Criar vetor de chegadas (b)
    b = np.zeros(n)
    sala_central = (n + 1) // 2 - 1  # Índice da sala central (base 0)
    b[sala_central] = taxa_chegada
    
    print(f"\nSala central: {sala_central + 1} (índice {sala_central})")
    print(f"Vetor de chegadas b: {b}")
    
    # Resolver sistema linear A × x = b
    print(f"\nResolvendo sistema linear A × x = b...")
    try:
        x = np.linalg.solve(A, b)
        print("Sistema resolvido com sucesso!")
    except np.linalg.LinAlgError as e:
        print(f"Erro ao resolver sistema: {e}")
        return None
    
    print(f"\nSolução x (população por sala):")
    for i in range(n):
        print(f"  Sala {i+1}: {x[i]:.6f} atores")
    
    return x


def main():
    """
    Função principal do programa.
    """
    print("=" * 60)
    print("SIMULADOR DE JOGO COREANO")
    print("Trabalho de Métodos Numéricos")
    print("=" * 60)
    
    # Verificar argumentos da linha de comando
    if len(sys.argv) != 2:
        print("\nUso: python simulador_jogo.py <número_de_salas>")
        print("Exemplo: python simulador_jogo.py 23")
        
        # Executar exemplos padrão
        print("\nExecutando exemplos padrão...")
        numeros_salas = [3, 5, 7, 23]
    else:
        try:
            n = int(sys.argv[1])
            if n <= 0 or n % 2 == 0:
                print("Erro: O número de salas deve ser um inteiro positivo ímpar!")
                sys.exit(1)
            numeros_salas = [n]
        except ValueError:
            print("Erro: Por favor, forneça um número inteiro válido!")
            sys.exit(1)
    
    # Executar simulação para cada número de salas
    for n in numeros_salas:
        print(f"\n{'='*60}")
        print(f"SIMULAÇÃO PARA {n} SALAS")
        print(f"{'='*60}")
        
        # Calcular população estacionária
        x = calcular_populacao_estacionaria(n, taxa_chegada=1.0)
        
        if x is not None:
            populacao_total = np.sum(x)
            print(f"\n🎯 RESULTADO FINAL:")
            print(f"População para {n} salas: {populacao_total:.0f} atores")
            print(f"População total exata: {populacao_total:.6f}")
            
            # Mostrar distribuição detalhada
            print(f"\nDistribuição por sala:")
            for i in range(n):
                percentual = (x[i] / populacao_total) * 100
                print(f"  Sala {i+1}: {x[i]:8.4f} atores ({percentual:5.1f}%)")
            
            # Análise adicional
            print(f"\nAnálise:")
            sala_central = (n + 1) // 2
            print(f"  - Sala central ({sala_central}): {x[sala_central-1]:.4f} atores")
            print(f"  - Sala com mais atores: Sala {np.argmax(x)+1} ({np.max(x):.4f})")
            print(f"  - Sala com menos atores: Sala {np.argmin(x)+1} ({np.min(x):.4f})")


if __name__ == "__main__":
    main()
