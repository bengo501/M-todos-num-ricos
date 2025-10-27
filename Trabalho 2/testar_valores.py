"""
Script de teste para validar a interpolação com vários valores
"""

import numpy as np

# Importar a função do script principal
import sys
sys.path.insert(0, '.')

# Recriar a função aqui para teste independente
def lagrange_interpolation(x_dados, y_dados, x):
    """
    Implementação manual da interpolação de Lagrange
    """
    n = len(x_dados)
    resultado = 0.0
    
    for i in range(n):
        # Calcular L_i(x)
        L_i = 1.0
        for j in range(n):
            if i != j:
                L_i *= (x - x_dados[j]) / (x_dados[i] - x_dados[j])
        
        # Adicionar termo y_i * L_i(x)
        resultado += y_dados[i] * L_i
    
    return resultado


# Dados do problema
pesos = np.array([3.0, 5.0, 7.0, 9.0])
tempos = np.array([83, 146, 197, 243])

print("=" * 70)
print("TESTE DE VALIDACAO DA INTERPOLACAO")
print("=" * 70)

# Teste 1: Pontos conhecidos (devem ter erro zero)
print("\n1. TESTE COM PONTOS CONHECIDOS:")
print("-" * 70)
print(f"{'Peso (kg)':<15} {'Tempo esperado':<20} {'Tempo calculado':<20} {'Erro':<15} {'Status'}")
print("-" * 70)

todos_ok = True
for peso, tempo_esperado in zip(pesos, tempos):
    resultado = lagrange_interpolation(pesos, tempos, peso)
    erro = abs(resultado - tempo_esperado)
    status = "OK" if erro < 1e-10 else "ERRO"
    if erro >= 1e-10:
        todos_ok = False
    print(f"{peso:<15.1f} {tempo_esperado:<20} {resultado:<20.6f} {erro:<15.10f} {status}")

if todos_ok:
    print("\n[OK] Todos os pontos conhecidos foram reproduzidos corretamente!")
else:
    print("\n[ERRO] Alguns pontos conhecidos nao foram reproduzidos!")

# Teste 2: Ponto principal (6.22 kg)
print("\n2. TESTE COM PONTO PRINCIPAL (6.22 kg):")
print("-" * 70)
peso_teste = 6.22
resultado = lagrange_interpolation(pesos, tempos, peso_teste)
horas = int(resultado // 60)
minutos = int(resultado % 60)
print(f"Peso: {peso_teste} kg")
print(f"Tempo calculado: {resultado:.2f} minutos")
print(f"Tempo calculado: {horas}h {minutos:02d}min")
print(f"Esperado: ~178 minutos (2h 58min)")

if abs(resultado - 178.09) < 0.1:
    print("[OK] Resultado esta correto!")
else:
    print("[ERRO] Resultado diferente do esperado!")

# Teste 3: Pontos intermediários
print("\n3. TESTE COM PONTOS INTERMEDIARIOS:")
print("-" * 70)
testes = [4.0, 6.0, 8.0]
print(f"{'Peso (kg)':<15} {'Tempo (min)':<20} {'Tempo (h:min)':<20}")
print("-" * 70)
for peso_teste in testes:
    resultado = lagrange_interpolation(pesos, tempos, peso_teste)
    horas = int(resultado // 60)
    minutos = int(resultado % 60)
    print(f"{peso_teste:<15.1f} {resultado:<20.2f} {horas}h {minutos:02d}min")

# Teste 4: Verificar monotonicidade (peru maior = mais tempo)
print("\n4. TESTE DE MONOTONICIDADE:")
print("-" * 70)
print("Verificando se o tempo aumenta com o peso...")
tempos_testados = []
pesos_testados = [3.0, 4.0, 5.0, 6.0, 6.22, 7.0, 8.0, 9.0]
for peso in pesos_testados:
    tempo = lagrange_interpolation(pesos, tempos, peso)
    tempos_testados.append(tempo)

monotono = True
for i in range(len(tempos_testados) - 1):
    if tempos_testados[i] >= tempos_testados[i+1]:
        monotono = False
        break

if monotono:
    print("[OK] Funcao e monotona crescente (peru maior = mais tempo)")
else:
    print("[ATENCAO] Funcao nao e monotona!")

print("\n" + "=" * 70)
print("TESTES CONCLUIDOS")
print("=" * 70)

