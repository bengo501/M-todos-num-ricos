"""
Métodos Numéricos - Lista 1 Geral
Solução completa de todos os exercícios

Prof. João B. Oliveira

Este script organiza e executa todos os exercícios da Lista 1 de Métodos Numéricos,
divididos nas seguintes seções:

1. Sistemas de Ponto Flutuante
2. Resolução de Equações  
3. Sistemas Lineares
4. Cadeias de Markov
5. Interpolação
6. Diferenciação Automática
7. Sistemas Dinâmicos
"""

import sys
import os

# Adicionar os diretórios dos módulos ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Sistemas_Ponto_Flutuante'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Resolucao_Equacoes'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Sistemas_Lineares'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Cadeias_Markov'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Interpolacao'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Diferenciacao_Automatica'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Sistemas_Dinamicos'))

def executar_sistemas_ponto_flutuante():
    """
    Executa os exercícios de Sistemas de Ponto Flutuante
    """
    print("\n" + "="*80)
    print("SEÇÃO 1: SISTEMAS DE PONTO FLUTUANTE")
    print("="*80)
    
    try:
        from sistemas_ponto_flutuante import main as main_spf
        main_spf()
    except ImportError:
        print("Erro: Não foi possível importar o módulo de Sistemas de Ponto Flutuante")
        print("Verifique se o arquivo sistemas_ponto_flutuante.py existe")

def executar_resolucao_equacoes():
    """
    Executa os exercícios de Resolução de Equações
    """
    print("\n" + "="*80)
    print("SEÇÃO 2: RESOLUÇÃO DE EQUAÇÕES")
    print("="*80)
    
    try:
        from resolucao_equacoes import main as main_re
        main_re()
    except ImportError:
        print("Erro: Não foi possível importar o módulo de Resolução de Equações")
        print("Verifique se o arquivo resolucao_equacoes.py existe")

def executar_sistemas_lineares():
    """
    Executa os exercícios de Sistemas Lineares
    """
    print("\n" + "="*80)
    print("SEÇÃO 3: SISTEMAS LINEARES")
    print("="*80)
    
    try:
        from sistemas_lineares import main as main_sl
        main_sl()
    except ImportError:
        print("Erro: Não foi possível importar o módulo de Sistemas Lineares")
        print("Verifique se o arquivo sistemas_lineares.py existe")

def executar_cadeias_markov():
    """
    Executa os exercícios de Cadeias de Markov
    """
    print("\n" + "="*80)
    print("SEÇÃO 4: CADEIAS DE MARKOV")
    print("="*80)
    
    try:
        from cadeias_markov import main as main_cm
        main_cm()
    except ImportError:
        print("Erro: Não foi possível importar o módulo de Cadeias de Markov")
        print("Verifique se o arquivo cadeias_markov.py existe")

def executar_interpolacao():
    """
    Executa os exercícios de Interpolação
    """
    print("\n" + "="*80)
    print("SEÇÃO 5: INTERPOLAÇÃO")
    print("="*80)
    
    try:
        from interpolacao import main as main_int
        main_int()
    except ImportError:
        print("Erro: Não foi possível importar o módulo de Interpolação")
        print("Verifique se o arquivo interpolacao.py existe")

def executar_diferenciacao_automatica():
    """
    Executa os exercícios de Diferenciação Automática
    """
    print("\n" + "="*80)
    print("SEÇÃO 6: DIFERENCIAÇÃO AUTOMÁTICA")
    print("="*80)
    
    try:
        from diferenciacao_automatica import main as main_da
        main_da()
    except ImportError:
        print("Erro: Não foi possível importar o módulo de Diferenciação Automática")
        print("Verifique se o arquivo diferenciacao_automatica.py existe")

def executar_sistemas_dinamicos():
    """
    Executa os exercícios de Sistemas Dinâmicos
    """
    print("\n" + "="*80)
    print("SEÇÃO 7: SISTEMAS DINÂMICOS")
    print("="*80)
    
    try:
        from sistemas_dinamicos import main as main_sd
        main_sd()
    except ImportError:
        print("Erro: Não foi possível importar o módulo de Sistemas Dinâmicos")
        print("Verifique se o arquivo sistemas_dinamicos.py existe")

def mostrar_menu():
    """
    Mostra o menu de opções
    """
    print("\n" + "="*80)
    print("MÉTODOS NUMÉRICOS - LISTA 1 GERAL")
    print("="*80)
    print("Escolha uma opção:")
    print("1. Sistemas de Ponto Flutuante")
    print("2. Resolução de Equações")
    print("3. Sistemas Lineares")
    print("4. Cadeias de Markov")
    print("5. Interpolação")
    print("6. Diferenciação Automática")
    print("7. Sistemas Dinâmicos")
    print("8. Executar todos os exercícios")
    print("0. Sair")
    print("="*80)

def main():
    """
    Função principal que executa todos os exercícios
    """
    print("MÉTODOS NUMÉRICOS - LISTA 1 GERAL")
    print("Prof. João B. Oliveira")
    print("="*80)
    
    while True:
        mostrar_menu()
        
        try:
            opcao = input("\nDigite sua opção: ").strip()
            
            if opcao == "0":
                print("\nSaindo...")
                break
            elif opcao == "1":
                executar_sistemas_ponto_flutuante()
            elif opcao == "2":
                executar_resolucao_equacoes()
            elif opcao == "3":
                executar_sistemas_lineares()
            elif opcao == "4":
                executar_cadeias_markov()
            elif opcao == "5":
                executar_interpolacao()
            elif opcao == "6":
                executar_diferenciacao_automatica()
            elif opcao == "7":
                executar_sistemas_dinamicos()
            elif opcao == "8":
                print("\nExecutando todos os exercícios...")
                executar_sistemas_ponto_flutuante()
                executar_resolucao_equacoes()
                executar_sistemas_lineares()
                executar_cadeias_markov()
                executar_interpolacao()
                executar_diferenciacao_automatica()
                executar_sistemas_dinamicos()
                
                print("\n" + "="*80)
                print("TODOS OS EXERCÍCIOS FORAM EXECUTADOS COM SUCESSO!")
                print("="*80)
                break
            else:
                print("Opção inválida! Digite um número de 0 a 8.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            print("Tente novamente.")

if __name__ == "__main__":
    main()
