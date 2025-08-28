"""
Métodos Numéricos - Resolução de Equações
Solução dos exercícios da Lista 1
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

# ============================================================================
# EXERCÍCIO 1: Comparação de funções próximas a zero
# ============================================================================

def exercicio1():
    """
    Compara funções f(x) e g(x) próximas a zero
    """
    print("=== EXERCÍCIO 1: COMPARAÇÃO DE FUNÇÕES PRÓXIMAS A ZERO ===")
    
    def f(x):
        """f(x) = √(x² + 1) - 1"""
        return math.sqrt(x**2 + 1) - 1
    
    def g(x):
        """g(x) = x² / (√(x² + 1) + 1)"""
        return x**2 / (math.sqrt(x**2 + 1) + 1)
    
    print("f(x) = √(x² + 1) - 1")
    print("g(x) = x² / (√(x² + 1) + 1)")
    print("\nVerificação matemática: f(x)/g(x) = 1")
    
    # Testar com valores próximos a zero
    valores_x = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
    
    print("\nx\t\tf(x)\t\tg(x)\t\tf(x)/g(x)")
    print("-" * 60)
    
    for x in valores_x:
        fx = f(x)
        gx = g(x)
        if gx != 0:
            razao = fx / gx
        else:
            razao = float('inf')
        print(f"{x:.1e}\t{fx:.6e}\t{gx:.6e}\t{razao:.6f}")
    
    print("\nANÁLISE:")
    print("Para valores muito pequenos de x, a função f(x) perde precisão")
    print("devido ao cancelamento catastrófico na subtração √(x² + 1) - 1.")
    print("A função g(x) é mais estável numericamente.")

# ============================================================================
# EXERCÍCIO 2: Plotagem de f(1/x) para contornar restrição
# ============================================================================

def exercicio2():
    """
    Usa f(1/x) para plotar função fora do intervalo [-1, 1]
    """
    print("=== EXERCÍCIO 2: PLOTAGEM DE F(1/X) ===")
    
    def f(x):
        """f(x) = 8x⁴ - 238x³ + 1047x² - 953x + 154"""
        return 8*x**4 - 238*x**3 + 1047*x**2 - 953*x + 154
    
    def f_inv(x):
        """f(1/x) para plotar fora do intervalo [-1, 1]"""
        if x == 0:
            return float('inf')
        return f(1/x)
    
    print("f(x) = 8x⁴ - 238x³ + 1047x² - 953x + 154")
    print("Restrição: só pode plotar para x ∈ [-1, 1]")
    print("Solução: plotar f(1/x) para x ∈ [-1, 1]")
    
    # Encontrar raízes usando f(1/x)
    print("\nPara encontrar raízes fora de [-1, 1]:")
    print("Se f(a) = 0, então f(1/x) = 0 quando x = 1/a")
    
    # Testar alguns valores
    x_test = np.linspace(-1, 1, 21)
    x_test = x_test[x_test != 0]  # Remover x = 0
    
    print("\nx\t\t1/x\t\tf(1/x)")
    print("-" * 40)
    
    for x in x_test[:10]:  # Mostrar apenas os primeiros 10
        if x != 0:
            fx = f_inv(x)
            print(f"{x:.3f}\t\t{1/x:.3f}\t\t{fx:.6e}")
    
    print("\nMÉTODO:")
    print("1. Plotar f(1/x) para x ∈ [-1, 1]")
    print("2. Encontrar onde f(1/x) = 0")
    print("3. As raízes de f(x) são 1/x onde f(1/x) = 0")

# ============================================================================
# EXERCÍCIO 3: Método de Heron para raiz quadrada
# ============================================================================

def metodo_heron(p, tol=1e-10, max_iter=100):
    """
    Implementa o método de Heron para encontrar √p
    """
    if p < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo")
    
    if p == 0:
        return 0
    
    # Estimativa inicial
    x = p / 2
    
    iteracoes = []
    
    for i in range(max_iter):
        x_anterior = x
        x = (x + p / x) / 2
        
        iteracoes.append((i+1, x, abs(x - x_anterior)))
        
        if abs(x - x_anterior) < tol:
            break
    
    return x, iteracoes

def exercicio3():
    """
    Implementa e testa o método de Heron
    """
    print("=== EXERCÍCIO 3: MÉTODO DE HERON PARA RAIZ QUADRADA ===")
    
    # Testar com diferentes valores
    valores = [2, 3, 5, 10, 100]
    
    for p in valores:
        print(f"\nCalculando √{p}:")
        raiz, iteracoes = metodo_heron(p)
        
        print(f"Iteração\tx\t\tErro")
        print("-" * 40)
        
        for i, x, erro in iteracoes:
            print(f"{i}\t\t{x:.10f}\t{erro:.2e}")
        
        print(f"\nResultado: √{p} ≈ {raiz:.10f}")
        print(f"Valor real: √{p} = {math.sqrt(p):.10f}")
        print(f"Erro absoluto: {abs(raiz - math.sqrt(p)):.2e}")

# ============================================================================
# EXERCÍCIO 4: Polinômio com raízes 2, 3, 4 e método da bissecção
# ============================================================================

def criar_polinomio(raizes):
    """
    Cria um polinômio com as raízes especificadas
    """
    # Começar com 1 (coeficiente do termo de maior grau)
    polinomio = [1]
    
    # Multiplicar por (x - raiz) para cada raiz
    for raiz in raizes:
        # Multiplicar polinomio atual por (x - raiz)
        novo_polinomio = [0] * (len(polinomio) + 1)
        
        for i, coef in enumerate(polinomio):
            novo_polinomio[i] += coef  # x * coef
            novo_polinomio[i+1] += coef  # -raiz * coef
        
        polinomio = novo_polinomio
    
    return polinomio

def avaliar_polinomio(polinomio, x):
    """
    Avalia o polinômio no ponto x usando o método de Horner
    """
    resultado = 0
    for coef in reversed(polinomio):
        resultado = resultado * x + coef
    return resultado

def bisseccao(f, a, b, tol=1e-10, max_iter=100):
    """
    Implementa o método da bissecção
    """
    if f(a) * f(b) > 0:
        return None, "Não há mudança de sinal no intervalo"
    
    iteracoes = []
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        iteracoes.append((i+1, a, b, c, fc))
        
        if abs(fc) < tol:
            return c, iteracoes
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return c, iteracoes

def exercicio4():
    """
    Cria polinômio com raízes 2, 3, 4 e testa bissecção
    """
    print("=== EXERCÍCIO 4: POLINÔMIO COM RAÍZES 2, 3, 4 ===")
    
    raizes = [2, 3, 4]
    polinomio = criar_polinomio(raizes)
    
    print(f"Polinômio criado: {polinomio}")
    print("Forma expandida:")
    
    # Mostrar forma expandida
    termos = []
    for i, coef in enumerate(reversed(polinomio)):
        if coef != 0:
            if i == 0:
                termos.append(f"{coef}")
            elif i == 1:
                termos.append(f"{coef}x")
            else:
                termos.append(f"{coef}x^{i}")
    
    print(" + ".join(termos))
    
    # Testar se as raízes são realmente raízes
    print(f"\nVerificação das raízes:")
    for raiz in raizes:
        valor = avaliar_polinomio(polinomio, raiz)
        print(f"p({raiz}) = {valor:.2e}")
    
    # Definir função para bissecção
    def p(x):
        return avaliar_polinomio(polinomio, x)
    
    # Testar bissecção no intervalo [1, 5]
    print(f"\nMétodo da bissecção no intervalo [1, 5]:")
    raiz_encontrada, iteracoes = bisseccao(p, 1, 5)
    
    if raiz_encontrada is not None:
        print(f"Raiz encontrada: {raiz_encontrada:.10f}")
        print(f"p(raiz) = {p(raiz_encontrada):.2e}")
        
        print(f"\nIterações:")
        print("i\ta\t\tb\t\tc\t\tf(c)")
        print("-" * 60)
        
        for i, a, b, c, fc in iteracoes:
            print(f"{i}\t{a:.6f}\t{b:.6f}\t{c:.6f}\t{fc:.2e}")
    else:
        print(iteracoes)  # iteracoes contém a mensagem de erro

# ============================================================================
# EXERCÍCIO 5: Polinômio com raízes 2, 3, 4, 5
# ============================================================================

def exercicio5():
    """
    Cria polinômio com raízes 2, 3, 4, 5 e testa bissecção
    """
    print("=== EXERCÍCIO 5: POLINÔMIO COM RAÍZES 2, 3, 4, 5 ===")
    
    raizes = [2, 3, 4, 5]
    polinomio = criar_polinomio(raizes)
    
    print(f"Polinômio criado: {polinomio}")
    
    # Definir função para bissecção
    def p(x):
        return avaliar_polinomio(polinomio, x)
    
    # Testar bissecção no intervalo [1, 6]
    print(f"\nMétodo da bissecção no intervalo [1, 6]:")
    raiz_encontrada, iteracoes = bisseccao(p, 1, 6)
    
    if raiz_encontrada is not None:
        print(f"Raiz encontrada: {raiz_encontrada:.10f}")
        print(f"p(raiz) = {p(raiz_encontrada):.2e}")
        
        # Verificar qual raiz foi encontrada
        for raiz_esperada in raizes:
            if abs(raiz_encontrada - raiz_esperada) < 1e-6:
                print(f"Esta é a raiz x = {raiz_esperada}")
                break
    else:
        print(iteracoes)
    
    print(f"\nPROBLEMA IDENTIFICADO:")
    print("O método da bissecção pode não funcionar quando há múltiplas raízes")
    print("no intervalo, pois pode não haver mudança de sinal.")
    print("Solução: dividir o intervalo em subintervalos menores.")

# ============================================================================
# EXERCÍCIO 6: Avaliação de polinômio usando método de Horner
# ============================================================================

def exercicio6():
    """
    Analisa e implementa o algoritmo de avaliação de polinômio
    """
    print("=== EXERCÍCIO 6: AVALIAÇÃO DE POLINÔMIO (MÉTODO DE HORNER) ===")
    
    # Polinômio: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431
    coeficientes = [1, 0, 18, 34, -493, 1431]
    
    print(f"Polinômio: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431")
    print(f"Coeficientes: {coeficientes}")
    
    def avaliar_horner(x):
        """
        Avalia o polinômio usando o método de Horner
        """
        p = 0
        for i in range(len(coeficientes)):
            p = x * p + coeficientes[i]
        return p
    
    # Testar com diferentes valores de x
    valores_x = [-5, -2, 0, 2, 5, 10]
    
    print(f"\nAvaliação do polinômio:")
    print("x\t\tp(x)")
    print("-" * 30)
    
    for x in valores_x:
        resultado = avaliar_horner(x)
        print(f"{x}\t\t{resultado}")
    
    print(f"\nANÁLISE DO ALGORITMO:")
    print("O algoritmo implementa o método de Horner para avaliar polinômios.")
    print("É mais eficiente que calcular cada termo separadamente.")
    print("Para um polinômio de grau n, são necessárias n multiplicações e n adições.")

# ============================================================================
# EXERCÍCIO 7: Método da secante
# ============================================================================

def secante(f, x0, x1, tol=1e-10, max_iter=100):
    """
    Implementa o método da secante
    """
    iteracoes = []
    
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        
        if abs(f1 - f0) < tol:
            return x1, iteracoes
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        
        iteracoes.append((i+1, x0, x1, x2, f0, f1))
        
        if abs(x2 - x1) < tol:
            return x2, iteracoes
        
        x0, x1 = x1, x2
    
    return x1, iteracoes

def exercicio7():
    """
    Implementa o método da secante para encontrar raízes
    """
    print("=== EXERCÍCIO 7: MÉTODO DA SECANTE ===")
    
    # Polinômio: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431
    coeficientes = [1, 0, 18, 34, -493, 1431]
    
    def p(x):
        resultado = 0
        for coef in reversed(coeficientes):
            resultado = resultado * x + coef
        return resultado
    
    print(f"Polinômio: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431")
    
    # Análise do número de raízes reais
    print(f"\nANÁLISE DO NÚMERO DE RAÍZES REAIS:")
    print("Um polinômio de grau 5 pode ter no máximo 5 raízes reais.")
    print("Para determinar quantas são reais, podemos usar o critério de Descartes:")
    
    # Contar mudanças de sinal
    sinais = [1 if coef > 0 else -1 if coef < 0 else 0 for coef in coeficientes]
    mudancas = sum(1 for i in range(len(sinais)-1) if sinais[i] != sinais[i+1] and sinais[i] != 0 and sinais[i+1] != 0)
    
    print(f"Mudanças de sinal: {mudancas}")
    print(f"Pelo critério de Descartes, há no máximo {mudancas} raízes reais positivas.")
    
    # Testar método da secante
    print(f"\nMétodo da secante:")
    print("Chutes iniciais: x0 = 0, x1 = 1")
    
    raiz, iteracoes = secante(p, 0, 1)
    
    if raiz is not None:
        print(f"Raiz encontrada: {raiz:.10f}")
        print(f"p(raiz) = {p(raiz):.2e}")
        
        print(f"\nIterações:")
        print("i\tx0\t\tx1\t\tx2\t\tf(x0)\t\tf(x1)")
        print("-" * 70)
        
        for i, x0, x1, x2, f0, f1 in iteracoes:
            print(f"{i}\t{x0:.6f}\t{x1:.6f}\t{x2:.6f}\t{f0:.2e}\t{f1:.2e}")

# ============================================================================
# EXERCÍCIO 8: Algoritmo modificado (derivada)
# ============================================================================

def exercicio8():
    """
    Analisa o algoritmo modificado que calcula também a derivada
    """
    print("=== EXERCÍCIO 8: ALGORITMO MODIFICADO (DERIVADA) ===")
    
    # Polinômio: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431
    coeficientes = [1, 0, 18, 34, -493, 1431]
    
    def avaliar_polinomio_e_derivada(x):
        """
        Avalia o polinômio e sua derivada usando método de Horner
        """
        p = 0
        q = 0
        
        for i in range(len(coeficientes)):
            q = x * q + p
            p = x * p + coeficientes[i]
        
        return p, q
    
    # Testar com diferentes valores
    valores_x = [-2, 0, 2, 5]
    
    print(f"Polinômio: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431")
    print(f"Derivada: p'(x) = 5x⁴ + 54x² + 68x - 493")
    
    print(f"\nAvaliação do polinômio e derivada:")
    print("x\t\tp(x)\t\tp'(x)")
    print("-" * 50)
    
    for x in valores_x:
        p_val, p_deriv = avaliar_polinomio_e_derivada(x)
        print(f"{x}\t\t{p_val}\t\t{p_deriv}")
    
    print(f"\nANÁLISE DO ALGORITMO:")
    print("O algoritmo modificado calcula simultaneamente:")
    print("- p(x): valor do polinômio")
    print("- p'(x): valor da derivada do polinômio")
    print("Isso é útil para o método de Newton, que precisa de ambos os valores.")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Resolução de Equações
    """
    print("MÉTODOS NUMÉRICOS - RESOLUÇÃO DE EQUAÇÕES")
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
    print("EXECUÇÃO CONCLUÍDA!")
    print("Todos os exercícios de Resolução de Equações foram resolvidos.")

if __name__ == "__main__":
    main()
