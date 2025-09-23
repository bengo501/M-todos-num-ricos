#!/usr/bin/env python3
"""
Script de validação automática para o simulador de jogo.
Testa múltiplos casos e verifica se os resultados estão corretos.
"""

import subprocess
import sys
import re

def executar_simulador(n):
    """Executa o simulador e retorna a população total."""
    try:
        result = subprocess.run([sys.executable, 'simulador_jogo.py', str(n)], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            return None, f"Erro na execução: {result.stderr}"
        
        # Extrair população total do output
        output = result.stdout
        match = re.search(r'População total exata: ([\d.]+)', output)
        if match:
            return float(match.group(1)), None
        else:
            return None, "Não foi possível extrair população total"
            
    except subprocess.TimeoutExpired:
        return None, "Timeout na execução"
    except Exception as e:
        return None, f"Erro: {e}"

def testar_casos_validos():
    """Testa casos válidos e verifica resultados esperados."""
    casos_teste = [
        (3, 6.0, 0.01),      # n=3, esperado=6.0, tolerância=0.01
        (5, 11.25, 0.01),    # n=5, esperado=11.25
        (7, 18.67, 0.02),    # n=7, esperado=18.67, tolerância maior
        (23, 150.55, 0.1),   # n=23, esperado=150.55
    ]
    
    print("=== TESTE DE CASOS VÁLIDOS ===")
    todos_passaram = True
    
    for n, esperado, tolerancia in casos_teste:
        print(f"\nTestando n={n}...")
        resultado, erro = executar_simulador(n)
        
        if erro:
            print(f"❌ FALHOU: {erro}")
            todos_passaram = False
        elif abs(resultado - esperado) <= tolerancia:
            print(f"✅ PASSOU: {resultado:.6f} (esperado: {esperado})")
        else:
            print(f"❌ FALHOU: {resultado:.6f} (esperado: {esperado}, diferença: {abs(resultado - esperado):.6f})")
            todos_passaram = False
    
    return todos_passaram

def testar_casos_invalidos():
    """Testa casos inválidos que devem dar erro."""
    casos_invalidos = [
        ('4', 'Número par'),
        ('-3', 'Número negativo'),  
        ('0', 'Zero'),
        ('abc', 'Não é número'),
        ('2.5', 'Não é inteiro'),
    ]
    
    print("\n=== TESTE DE CASOS INVÁLIDOS ===")
    todos_passaram = True
    
    for entrada, descricao in casos_invalidos:
        print(f"\nTestando {descricao} ({entrada})...")
        try:
            result = subprocess.run([sys.executable, 'simulador_jogo.py', entrada], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode != 0:
                print(f"✅ PASSOU: Erro detectado corretamente")
            else:
                print(f"❌ FALHOU: Deveria ter dado erro mas executou normalmente")
                todos_passaram = False
                
        except Exception as e:
            print(f"✅ PASSOU: Exceção capturada ({e})")
    
    return todos_passaram

def testar_propriedades_matematicas():
    """Testa propriedades matemáticas dos resultados."""
    print("\n=== TESTE DE PROPRIEDADES MATEMÁTICAS ===")
    
    # Para n=5, vamos verificar se os resultados são simétricos
    n = 5
    print(f"\nTestando simetria para n={n}...")
    
    try:
        result = subprocess.run([sys.executable, 'simulador_jogo.py', str(n)], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            print("❌ FALHOU: Erro na execução")
            return False
        
        # Extrair populações por sala
        output = result.stdout
        populacoes = []
        
        for i in range(1, n+1):
            pattern = rf'Sala {i}: +(\d+\.\d+) atores'
            match = re.search(pattern, output)
            if match:
                populacoes.append(float(match.group(1)))
        
        if len(populacoes) != n:
            print("❌ FALHOU: Não foi possível extrair todas as populações")
            return False
        
        # Verificar simetria
        simetrico = True
        for i in range(n//2):
            if abs(populacoes[i] - populacoes[n-1-i]) > 0.001:
                simetrico = False
                break
        
        if simetrico:
            print("✅ PASSOU: Distribuição é simétrica")
        else:
            print("❌ FALHOU: Distribuição não é simétrica")
            print(f"Populações: {populacoes}")
            return False
        
        # Verificar se o centro tem a maior população
        centro_idx = n // 2
        centro_pop = populacoes[centro_idx]
        
        if all(centro_pop >= pop for pop in populacoes):
            print("✅ PASSOU: Sala central tem a maior população")
        else:
            print("❌ FALHOU: Sala central não tem a maior população")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ FALHOU: Erro durante teste ({e})")
        return False

def main():
    """Executa todos os testes."""
    print("🧪 INICIANDO TESTES DO SIMULADOR DE JOGO COREANO")
    print("=" * 60)
    
    # Verificar se o arquivo existe
    try:
        with open('simulador_jogo.py', 'r'):
            pass
    except FileNotFoundError:
        print("❌ ERRO: Arquivo 'simulador_jogo.py' não encontrado!")
        return
    
    # Executar testes
    teste1 = testar_casos_validos()
    teste2 = testar_casos_invalidos()  
    teste3 = testar_propriedades_matematicas()
    
    # Resultado final
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES:")
    
    if teste1:
        print("✅ Casos válidos: PASSOU")
    else:
        print("❌ Casos válidos: FALHOU")
    
    if teste2:
        print("✅ Casos inválidos: PASSOU")
    else:
        print("❌ Casos inválidos: FALHOU")
    
    if teste3:
        print("✅ Propriedades matemáticas: PASSOU")
    else:
        print("❌ Propriedades matemáticas: FALHOU")
    
    if teste1 and teste2 and teste3:
        print("\n🎉 TODOS OS TESTES PASSARAM! O trabalho está funcionando corretamente.")
    else:
        print("\n⚠️  ALGUNS TESTES FALHARAM. Verifique os erros acima.")

if __name__ == "__main__":
    main()

