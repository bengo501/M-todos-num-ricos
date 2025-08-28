"""
Métodos Numéricos - Lista 1 Geral
Versão de Demonstração (Execução Automática)

Prof. João B. Oliveira

Este script executa automaticamente todos os exercícios da Lista 1 de Métodos Numéricos
sem interação do usuário, ideal para demonstrações e testes.
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
        return True
    except ImportError as e:
        print(f"Erro: Não foi possível importar o módulo de Sistemas de Ponto Flutuante: {e}")
        return False
    except Exception as e:
        print(f"Erro durante execução: {e}")
        return False

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
        return True
    except ImportError as e:
        print(f"Erro: Não foi possível importar o módulo de Resolução de Equações: {e}")
        return False
    except Exception as e:
        print(f"Erro durante execução: {e}")
        return False

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
        return True
    except ImportError as e:
        print(f"Erro: Não foi possível importar o módulo de Sistemas Lineares: {e}")
        return False
    except Exception as e:
        print(f"Erro durante execução: {e}")
        return False

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
        return True
    except ImportError as e:
        print(f"Erro: Não foi possível importar o módulo de Cadeias de Markov: {e}")
        return False
    except Exception as e:
        print(f"Erro durante execução: {e}")
        return False

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
        return True
    except ImportError as e:
        print(f"Erro: Não foi possível importar o módulo de Interpolação: {e}")
        return False
    except Exception as e:
        print(f"Erro durante execução: {e}")
        return False

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
        return True
    except ImportError as e:
        print(f"Erro: Não foi possível importar o módulo de Diferenciação Automática: {e}")
        return False
    except Exception as e:
        print(f"Erro durante execução: {e}")
        return False

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
        return True
    except ImportError as e:
        print(f"Erro: Não foi possível importar o módulo de Sistemas Dinâmicos: {e}")
        return False
    except Exception as e:
        print(f"Erro durante execução: {e}")
        return False

def main():
    """
    Função principal que executa todos os exercícios automaticamente
    """
    print("MÉTODOS NUMÉRICOS - LISTA 1 GERAL")
    print("Prof. João B. Oliveira")
    print("VERSÃO DE DEMONSTRAÇÃO - EXECUÇÃO AUTOMÁTICA")
    print("="*80)
    
    # Lista de funções para executar
    funcoes = [
        ("Sistemas de Ponto Flutuante", executar_sistemas_ponto_flutuante),
        ("Resolução de Equações", executar_resolucao_equacoes),
        ("Sistemas Lineares", executar_sistemas_lineares),
        ("Cadeias de Markov", executar_cadeias_markov),
        ("Interpolação", executar_interpolacao),
        ("Diferenciação Automática", executar_diferenciacao_automatica),
        ("Sistemas Dinâmicos", executar_sistemas_dinamicos)
    ]
    
    # Contadores para estatísticas
    sucessos = 0
    falhas = 0
    
    print("\nIniciando execução automática de todos os exercícios...")
    print("="*80)
    
    # Executar cada seção
    for nome, funcao in funcoes:
        print(f"\nExecutando: {nome}")
        print("-" * 50)
        
        try:
            resultado = funcao()
            if resultado:
                sucessos += 1
                print(f"✓ {nome} executado com sucesso")
            else:
                falhas += 1
                print(f"✗ {nome} falhou na execução")
        except Exception as e:
            falhas += 1
            print(f"✗ {nome} falhou com erro: {e}")
    
    # Resumo final
    print("\n" + "="*80)
    print("RESUMO DA EXECUÇÃO")
    print("="*80)
    print(f"Seções executadas com sucesso: {sucessos}")
    print(f"Seções com falhas: {falhas}")
    print(f"Total de seções: {len(funcoes)}")
    
    if falhas == 0:
        print("\n🎉 TODOS OS EXERCÍCIOS FORAM EXECUTADOS COM SUCESSO!")
    else:
        print(f"\n⚠️  {falhas} seção(ões) falharam na execução.")
        print("Verifique os arquivos dos módulos correspondentes.")
    
    print("\n" + "="*80)
    print("EXECUÇÃO CONCLUÍDA!")
    print("="*80)

if __name__ == "__main__":
    main()
