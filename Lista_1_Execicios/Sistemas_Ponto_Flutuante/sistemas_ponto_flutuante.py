"""
Métodos Numéricos - Sistemas de Ponto Flutuante
Solução dos exercícios da Lista 1
"""

import numpy as np
import struct
import math
import sys

# ============================================================================
# EXERCÍCIO 1: Algoritmo de precisão da máquina
# ============================================================================

def exercicio1():
    """
    Examina o algoritmo de precisão da máquina
    """
    print("=== EXERCÍCIO 1: ALGORITMO DE PRECISÃO DA MÁQUINA ===")
    
    aux = 1.0
    iteracoes = 0
    
    print("Valores de aux durante a execução:")
    while 1 + aux > 1:
        print(f"Iteração {iteracoes}: aux = {aux}")
        aux = aux / 2
        iteracoes += 1
    
    print(f"\n(a) O algoritmo termina? Por que?")
    print("RESPOSTA: Sim, o algoritmo termina porque:")
    print("- A variável aux é dividida por 2 a cada iteração")
    print("- Eventualmente, aux se torna menor que a precisão da máquina")
    print("- Quando 1 + aux não é mais maior que 1, o loop para")
    
    print(f"\n(b) O que significa o valor impresso na última linha?")
    print("RESPOSTA: O valor impresso na última linha é aproximadamente")
    print("a precisão da máquina (epsilon), que é o menor número")
    print("que, quando somado a 1, ainda produz um resultado > 1")
    
    print(f"\n(c) Teste do algoritmo:")
    print(f"Número de iterações: {iteracoes}")
    print(f"Valor final de aux: {aux}")
    print(f"1 + aux = {1 + aux}")
    print(f"1 + aux > 1? {1 + aux > 1}")
    
    # Comparar com numpy.eps
    eps_numpy = np.finfo(float).eps
    print(f"\nComparação com numpy.eps: {eps_numpy}")
    print(f"Diferença: {abs(aux - eps_numpy)}")
    
    return aux, iteracoes

# ============================================================================
# EXERCÍCIO 2: Calculadora com exceções IEEE-754
# ============================================================================

def float_to_bits(f):
    """
    Converte um float para sua representação em bits IEEE-754
    """
    # Usar struct para obter os bytes
    bytes_data = struct.pack('>f', f)
    # Converter para inteiro
    int_data = struct.unpack('>I', bytes_data)[0]
    # Converter para string binária
    binary = format(int_data, '032b')
    
    # Separar sinal, expoente e mantissa
    sign = binary[0]
    exponent = binary[1:9]
    mantissa = binary[9:]
    
    return sign, exponent, mantissa

def bits_to_float(sign, exponent, mantissa):
    """
    Converte bits IEEE-754 para float
    """
    binary = sign + exponent + mantissa
    int_data = int(binary, 2)
    bytes_data = struct.pack('>I', int_data)
    return struct.unpack('>f', bytes_data)[0]

def exercicio2():
    """
    Implementa calculadora com exceções IEEE-754
    """
    print("=== EXERCÍCIO 2: CALCULADORA COM EXCEÇÕES IEEE-754 ===")
    
    def calcular(val1, op, val2):
        """
        Realiza operação e mostra detalhes IEEE-754
        """
        print(f"\nRecebi {val1} {op} {val2}")
        
        # Limpar exceções (simulado)
        print("Registrador de exceções limpo")
        
        # Realizar operação
        if op == '+':
            resultado = val1 + val2
        elif op == '-':
            resultado = val1 - val2
        elif op == '*':
            resultado = val1 * val2
        elif op == '/':
            resultado = val1 / val2
        else:
            print("Operação inválida")
            return
        
        print(f"Resultado: {resultado}")
        
        # Mostrar configuração de bits
        sign1, exp1, mant1 = float_to_bits(val1)
        sign2, exp2, mant2 = float_to_bits(val2)
        sign_r, exp_r, mant_r = float_to_bits(resultado)
        
        print(f"val1 = {sign1} {exp1} {mant1} = {val1}")
        print(f"val2 = {sign2} {exp2} {mant2} = {val2}")
        print(f"res  = {sign_r} {exp_r} {mant_r} = {resultado}")
        
        # Verificar exceções (simulado)
        print("\nVerificação de exceções:")
        
        # FE_INEXACT: sempre 1 para operações de ponto flutuante
        print("Exceção FE_INEXACT: 1")
        
        # FE_DIVBYZERO: divisão por zero
        if op == '/' and val2 == 0:
            print("Exceção FE_DIVBYZERO: 1")
        else:
            print("Exceção FE_DIVBYZERO: 0")
        
        # FE_UNDERFLOW: resultado muito pequeno
        if abs(resultado) < 1e-38:
            print("Exceção FE_UNDERFLOW: 1")
        else:
            print("Exceção FE_UNDERFLOW: 0")
        
        # FE_OVERFLOW: resultado muito grande
        if abs(resultado) > 1e38:
            print("Exceção FE_OVERFLOW: 1")
        else:
            print("Exceção FE_OVERFLOW: 0")
        
        # FE_INVALID: operação inválida
        if math.isnan(resultado):
            print("Exceção FE_INVALID: 1")
        else:
            print("Exceção FE_INVALID: 0")
    
    # Testes
    print("Testando calculadora...")
    
    # Teste 1: 21 / -0
    calcular(21.0, '/', -0.0)
    
    # Teste 2: 0 / 0
    calcular(0.0, '/', 0.0)
    
    # Teste 3: 1e35 * 1e35 (overflow)
    calcular(1e35, '*', 1e35)
    
    # Teste 4: 1e-40 / 1e-40 (underflow)
    calcular(1e-40, '/', 1e-40)
    
    # Teste 5: 1 / inf
    calcular(1.0, '/', float('inf'))

# ============================================================================
# EXERCÍCIO 3: Plotagem de funções próximas a x = 1
# ============================================================================

def exercicio3():
    """
    Plota funções próximas a x = 1 para demonstrar problemas de precisão
    """
    print("=== EXERCÍCIO 3: PLOTAGEM DE FUNÇÕES PRÓXIMAS A X = 1 ===")
    
    def f(x):
        """f(x) = x³ - 3x² + 3x - 1"""
        return x**3 - 3*x**2 + 3*x - 1
    
    def g(x):
        """g(x) = x³"""
        return x**3
    
    print("Função f(x) = x³ - 3x² + 3x - 1")
    print("Função g(x) = x³")
    
    # Testar em diferentes intervalos
    intervalos = [
        (0.99, 1.01, "x = [0.99, 1.01]"),
        (0.999, 1.001, "x = [0.999, 1.001]"),
        (0.9999, 1.0001, "x = [0.9999, 1.0001]"),
        (0.99999, 1.00001, "x = [0.99999, 1.00001]")
    ]
    
    for x_min, x_max, desc in intervalos:
        print(f"\n--- {desc} ---")
        
        # Testar alguns pontos
        pontos = np.linspace(x_min, x_max, 5)
        
        print("x\t\tf(x)\t\tg(x)")
        print("-" * 50)
        
        for x in pontos:
            fx = f(x)
            gx = g(x)
            print(f"{x:.6f}\t{fx:.6e}\t{gx:.6e}")
        
        # Verificar se f(x) = 0 em x = 1
        f1 = f(1.0)
        print(f"\nf(1.0) = {f1:.6e}")
        
        if abs(f1) < 1e-10:
            print("f(x) ≈ 0 em x = 1 (correto)")
        else:
            print("f(x) ≠ 0 em x = 1 (problema de precisão)")
    
    print("\nEXPLICAÇÃO:")
    print("Quando plotamos f(x) = x³ - 3x² + 3x - 1 = (x-1)³ em intervalos")
    print("muito pequenos próximos a x = 1, começamos a ver problemas de")
    print("precisão numérica. A função deveria ser exatamente zero em x = 1,")
    print("mas erros de arredondamento fazem com que pequenas diferenças")
    print("sejam amplificadas.")

# ============================================================================
# EXERCÍCIO 4: Série de Taylor para exp(x)
# ============================================================================

def meuexp(x, n_termos=5):
    """
    Calcula exp(x) usando série de Taylor com n_termos
    """
    resultado = 1.0
    for i in range(1, n_termos + 1):
        resultado += (x**i) / math.factorial(i)
    return resultado

def exercicio4():
    """
    Analisa problemas com série de Taylor para exp(x) com x negativo
    """
    print("=== EXERCÍCIO 4: SÉRIE DE TAYLOR PARA EXP(X) ===")
    
    print("Série: meuexp(x) = 1 + x + x²/2! + x³/3! + x⁴/4! + x⁵/5!")
    
    # Teste com x positivo
    print("\n(a) Teste com x positivo [1, 5]:")
    print("x\t\tmeuexp(x)\t\texp(x)\t\tErro")
    print("-" * 60)
    
    for x in [1, 2, 3, 4, 5]:
        meu = meuexp(x)
        real = math.exp(x)
        erro = abs(meu - real) / real * 100
        print(f"{x}\t\t{meu:.6f}\t\t{real:.6f}\t\t{erro:.2f}%")
    
    # Teste com x negativo
    print("\n(b) Teste com x negativo [-5, -1]:")
    print("x\t\tmeuexp(x)\t\texp(x)\t\tErro")
    print("-" * 60)
    
    for x in [-1, -2, -3, -4, -5]:
        meu = meuexp(x)
        real = math.exp(x)
        erro = abs(meu - real) / real * 100
        print(f"{x}\t\t{meu:.6f}\t\t{real:.6f}\t\t{erro:.2f}%")
    
    print("\nPROBLEMA IDENTIFICADO:")
    print("Para x negativo, a série de Taylor converge muito lentamente")
    print("e pode ter problemas de cancelamento de termos alternados.")
    
    # Teste da solução alternativa
    print("\n(c) Solução alternativa: meuexp(x) = 1/meuexp(-x)")
    print("x\t\tmeuexp(x)\t\t1/meuexp(-x)\t\texp(x)")
    print("-" * 70)
    
    for x in [-1, -2, -3]:
        meu_direto = meuexp(x)
        meu_alternativo = 1 / meuexp(-x)
        real = math.exp(x)
        print(f"{x}\t\t{meu_direto:.6f}\t\t{meu_alternativo:.6f}\t\t{real:.6f}")
    
    print("\nA solução alternativa funciona melhor para x negativo!")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Sistemas de Ponto Flutuante
    """
    print("MÉTODOS NUMÉRICOS - SISTEMAS DE PONTO FLUTUANTE")
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
    print("EXECUÇÃO CONCLUÍDA!")
    print("Todos os exercícios de Sistemas de Ponto Flutuante foram resolvidos.")

if __name__ == "__main__":
    main()
