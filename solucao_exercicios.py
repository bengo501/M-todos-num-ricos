

"""
Métodos Numéricos - Solução de Equações
Implementação completa dos exercícios
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Complex
import cmath

# ============================================================================
# EXERCÍCIO 1: Algoritmo de precisão da máquina
# ============================================================================

def exercicio1():
    """
    Implementa o algoritmo para encontrar a precisão da máquina
    """
    print("=== EXERCÍCIO 1 ===")
    
    aux = 1.0
    iteracoes = 0
    
    print("Valores de aux durante a execução:")
    while 1 + aux > 1:
        print(f"Iteração {iteracoes}: aux = {aux}")
        aux = aux / 2
        iteracoes += 1
    
    print(f"\n(a) O algoritmo termina? Sim, após {iteracoes} iterações.")
    print("    Por quê? Porque existe um limite finito para a precisão da máquina.")
    print(f"    O valor final de aux é: {aux}")
    
    print(f"\n(b) O valor impresso na última linha ({aux}) representa")
    print("    a menor diferença que pode ser representada pela máquina")
    print("    (precisão da máquina ou epsilon da máquina).")
    print("    Este é o menor número tal que 1 + epsilon > 1.")

# ============================================================================
# EXERCÍCIO 2: Cotas de Cauchy, Lagrange e Fujiwara
# ============================================================================

def cota_cauchy(coeficientes: List[float]) -> float:
    """
    Calcula a cota de Cauchy para as raízes de um polinômio
    """
    n = len(coeficientes) - 1  # grau do polinômio
    a_n = abs(coeficientes[0])  # coeficiente do termo de maior grau
    
    # Soma dos valores absolutos dos outros coeficientes
    soma = sum(abs(coeficientes[i]) for i in range(1, n + 1))
    
    return 1 + soma / a_n

def cota_lagrange(coeficientes: List[float]) -> float:
    """
    Calcula a cota de Lagrange para as raízes de um polinômio
    """
    n = len(coeficientes) - 1  # grau do polinômio
    a_n = abs(coeficientes[0])  # coeficiente do termo de maior grau
    
    # Encontra o maior valor absoluto dos coeficientes negativos
    max_negativo = 0
    for i in range(1, n + 1):
        if coeficientes[i] < 0:
            max_negativo = max(max_negativo, abs(coeficientes[i]))
    
    return 1 + (max_negativo / a_n) ** (1 / n)

def cota_fujiwara(coeficientes: List[float]) -> float:
    """
    Calcula a cota de Fujiwara para as raízes de um polinômio
    """
    n = len(coeficientes) - 1  # grau do polinômio
    a_n = abs(coeficientes[0])  # coeficiente do termo de maior grau
    
    # Calcula os valores de A_k
    A = []
    for k in range(1, n + 1):
        if coeficientes[k] != 0:
            A.append(abs(coeficientes[k] / a_n) ** (1 / k))
        else:
            A.append(0)
    
    # Encontra os dois maiores valores de A_k
    A.sort(reverse=True)
    if len(A) >= 2:
        return 2 * max(A[0], A[1])
    elif len(A) == 1:
        return 2 * A[0]
    else:
        return 0

def exercicio2():
    """
    Calcula as cotas de Cauchy, Lagrange e Fujiwara para o polinômio dado
    """
    print("\n=== EXERCÍCIO 2 ===")
    
    # Polinômio: p(x) = 6*x^5 + 18*x^3 - 34*x^2 - 493*x + 1431
    # Coeficientes: [6, 0, 18, -34, -493, 1431]
    coeficientes = [6, 0, 18, -34, -493, 1431]
    
    print(f"Polinômio: p(x) = 6*x^5 + 18*x^3 - 34*x^2 - 493*x + 1431")
    print(f"Coeficientes: {coeficientes}")
    
    cota_c = cota_cauchy(coeficientes)
    cota_l = cota_lagrange(coeficientes)
    cota_f = cota_fujiwara(coeficientes)
    
    print(f"\nCota de Cauchy: {cota_c:.6f}")
    print(f"Cota de Lagrange: {cota_l:.6f}")
    print(f"Cota de Fujiwara: {cota_f:.6f}")
    
    print(f"\nTodas as raízes reais e complexas do polinômio")
    print(f"estão dentro do círculo de raio {min(cota_c, cota_l, cota_f):.6f}")

# ============================================================================
# EXERCÍCIO 3: Polinômio com raízes 2, 3, 4 e método da bissecção
# ============================================================================

def criar_polinomio_raizes(raizes: List[float]) -> List[float]:
    """
    Cria um polinômio com as raízes especificadas
    """
    # Começa com (x - r1)
    polinomio = [1, -raizes[0]]
    
    # Multiplica por (x - ri) para cada raiz
    for raiz in raizes[1:]:
        novo_polinomio = [0] * (len(polinomio) + 1)
        for i in range(len(polinomio)):
            novo_polinomio[i] += polinomio[i]
            novo_polinomio[i + 1] += polinomio[i] * (-raiz)
        polinomio = novo_polinomio
    
    return polinomio

def avaliar_polinomio(coeficientes: List[float], x: float) -> float:
    """
    Avalia um polinômio no ponto x usando o método de Horner
    """
    resultado = 0
    for coef in coeficientes:
        resultado = resultado * x + coef
    return resultado

def bisseccao(f, a: float, b: float, tol: float = 1e-10, max_iter: int = 100) -> Tuple[float, int, bool]:
    """
    Implementa o método da bissecção para encontrar raízes
    """
    if f(a) * f(b) > 0:
        return None, 0, False
    
    iteracoes = 0
    while iteracoes < max_iter:
        c = (a + b) / 2
        fc = f(c)
        
        if abs(fc) < tol:
            return c, iteracoes, True
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        iteracoes += 1
    
    return (a + b) / 2, iteracoes, False

def exercicio3():
    """
    Cria polinômio com raízes 2, 3, 4 e usa bissecção
    """
    print("\n=== EXERCÍCIO 3 ===")
    
    # Cria polinômio com raízes 2, 3, 4
    raizes = [2, 3, 4]
    coeficientes = criar_polinomio_raizes(raizes)
    
    print(f"Polinômio criado: p(x) = (x-2)(x-3)(x-4)")
    print(f"Coeficientes: {coeficientes}")
    
    # Função para avaliar o polinômio
    def f(x):
        return avaliar_polinomio(coeficientes, x)
    
    # Testa o método da bissecção no intervalo [1, 5]
    print(f"\nAplicando bissecção no intervalo [1, 5]:")
    raiz, iteracoes, convergiu = bisseccao(f, 1, 5)
    
    if convergiu:
        print(f"Raiz encontrada: {raiz:.10f}")
        print(f"Número de iterações: {iteracoes}")
        print(f"Valor do polinômio na raiz: {f(raiz):.2e}")
    else:
        print("Método não convergiu")
    
    print(f"\nResposta: O método da bissecção encontra apenas UMA raiz")
    print(f"no intervalo [1, 5], que é a raiz {raiz:.2f}.")
    print(f"Não encontra todas as raízes porque o método converge")
    print(f"para a primeira raiz que encontra no intervalo.")

# ============================================================================
# EXERCÍCIO 4: Polinômio com raízes 2, 3, 4, 5 e adaptação do algoritmo
# ============================================================================

def exercicio4():
    """
    Cria polinômio com raízes 2, 3, 4, 5 e adapta o algoritmo
    """
    print("\n=== EXERCÍCIO 4 ===")
    
    # Cria polinômio com raízes 2, 3, 4, 5
    raizes = [2, 3, 4, 5]
    coeficientes = criar_polinomio_raizes(raizes)
    
    print(f"Polinômio criado: p(x) = (x-2)(x-3)(x-4)(x-5)")
    print(f"Coeficientes: {coeficientes}")
    
    # Função para avaliar o polinômio
    def f(x):
        return avaliar_polinomio(coeficientes, x)
    
    # Testa o método da bissecção no intervalo [1, 6]
    print(f"\nAplicando bissecção no intervalo [1, 6]:")
    raiz, iteracoes, convergiu = bisseccao(f, 1, 6)
    
    if convergiu:
        print(f"Raiz encontrada: {raiz:.10f}")
        print(f"Número de iterações: {iteracoes}")
        print(f"Valor do polinômio na raiz: {f(raiz):.2e}")
    else:
        print("Método não convergiu")
    
    # Algoritmo adaptado para encontrar múltiplas raízes
    def encontrar_multiplas_raizes(f, a, b, num_raizes, tol=1e-10):
        """
        Algoritmo adaptado para encontrar múltiplas raízes
        """
        raizes_encontradas = []
        intervalo = (b - a) / num_raizes
        
        for i in range(num_raizes):
            inicio = a + i * intervalo
            fim = a + (i + 1) * intervalo
            
            raiz, _, convergiu = bisseccao(f, inicio, fim, tol)
            if convergiu and raiz not in raizes_encontradas:
                raizes_encontradas.append(raiz)
        
        return raizes_encontradas
    
    print(f"\nAlgoritmo adaptado para encontrar múltiplas raízes:")
    raizes_encontradas = encontrar_multiplas_raizes(f, 1, 6, 4)
    print(f"Raízes encontradas: {[round(r, 6) for r in raizes_encontradas]}")
    
    print(f"\nResposta: O método original encontra apenas uma raiz.")
    print(f"O algoritmo adaptado divide o intervalo em subintervalos")
    print(f"e aplica bissecção em cada um, encontrando múltiplas raízes.")

# ============================================================================
# EXERCÍCIO 5: Método de Newton para raiz quadrada
# ============================================================================

def newton_raiz_quadrada(p: float, tol: float = 1e-10, max_iter: int = 100) -> Tuple[float, int]:
    """
    Implementa o método de Newton para encontrar a raiz quadrada de p
    """
    if p < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo")
    
    if p == 0:
        return 0, 0
    
    # Chute inicial: x0 = p/2
    x = p / 2
    iteracoes = 0
    
    while iteracoes < max_iter:
        x_anterior = x
        # Fórmula de Newton: x_{n+1} = x_n - f(x_n)/f'(x_n)
        # Para f(x) = x^2 - p, temos f'(x) = 2x
        # Então: x_{n+1} = x_n - (x_n^2 - p)/(2x_n) = (x_n + p/x_n)/2
        x = (x + p / x) / 2
        
        if abs(x - x_anterior) < tol:
            break
        
        iteracoes += 1
    
    return x, iteracoes

def exercicio5():
    """
    Implementa método de Newton para raiz quadrada
    """
    print("\n=== EXERCÍCIO 5 ===")
    
    # Testa com diferentes valores
    valores_teste = [2, 9, 16, 25, 100]
    
    for p in valores_teste:
        raiz, iteracoes = newton_raiz_quadrada(p)
        raiz_exata = math.sqrt(p)
        erro = abs(raiz - raiz_exata)
        
        print(f"√{p} = {raiz:.10f} (exato: {raiz_exata:.10f})")
        print(f"  Iterações: {iteracoes}, Erro: {erro:.2e}")

# ============================================================================
# EXERCÍCIO 6: Método para raiz cúbica
# ============================================================================

def newton_raiz_cubica(p: float, tol: float = 1e-10, max_iter: int = 100) -> Tuple[float, int]:
    """
    Implementa o método de Newton para encontrar a raiz cúbica de p
    """
    if p == 0:
        return 0, 0
    
    # Chute inicial: x0 = p/3
    x = p / 3
    iteracoes = 0
    
    while iteracoes < max_iter:
        x_anterior = x
        # Fórmula de Newton: x_{n+1} = x_n - f(x_n)/f'(x_n)
        # Para f(x) = x^3 - p, temos f'(x) = 3x^2
        # Então: x_{n+1} = x_n - (x_n^3 - p)/(3x_n^2) = (2x_n^3 + p)/(3x_n^2)
        x = (2 * x**3 + p) / (3 * x**2)
        
        if abs(x - x_anterior) < tol:
            break
        
        iteracoes += 1
    
    return x, iteracoes

def exercicio6():
    """
    Implementa método para raiz cúbica
    """
    print("\n=== EXERCÍCIO 6 ===")
    
    # Testa com diferentes valores
    valores_teste = [8, 27, 64, 125, 1000]
    
    for p in valores_teste:
        raiz, iteracoes = newton_raiz_cubica(p)
        raiz_exata = p**(1/3)
        erro = abs(raiz - raiz_exata)
        
        print(f"∛{p} = {raiz:.10f} (exato: {raiz_exata:.10f})")
        print(f"  Iterações: {iteracoes}, Erro: {erro:.2e}")

# ============================================================================
# EXERCÍCIO 7: Transformação f(1/x) para plotagem restrita
# ============================================================================

def exercicio7():
    """
    Resolve o problema de plotagem restrita usando f(1/x)
    """
    print("\n=== EXERCÍCIO 7 ===")
    
    # Função original: f(x) = 8*x^4 - 238*x^3 + 1047*x^2 - 953*x + 154
    def f(x):
        return 8*x**4 - 238*x**3 + 1047*x**2 - 953*x + 154
    
    # Função transformada: g(x) = f(1/x)
    def g(x):
        if x == 0:
            return float('inf')
        return f(1/x)
    
    print("Função original: f(x) = 8*x^4 - 238*x^3 + 1047*x^2 - 953*x + 154")
    print("Função transformada: g(x) = f(1/x)")
    
    # Encontra raízes da função transformada no intervalo [-1, 1]
    def encontrar_raizes_transformadas():
        raizes = []
        x_vals = np.linspace(-1, 1, 1000)
        y_vals = [g(x) for x in x_vals]
        
        # Encontra mudanças de sinal
        for i in range(len(y_vals) - 1):
            if y_vals[i] * y_vals[i + 1] < 0:
                # Aplica bissecção para refinar a raiz
                raiz, _, convergiu = bisseccao(g, x_vals[i], x_vals[i + 1])
                if convergiu:
                    raizes.append(raiz)
        
        return raizes
    
    raizes_g = encontrar_raizes_transformadas()
    print(f"\nRaízes de g(x) no intervalo [-1, 1]: {[round(r, 6) for r in raizes_g]}")
    
    # Converte de volta para as raízes de f(x)
    raizes_f = [1/r for r in raizes_g if r != 0]
    print(f"Raízes de f(x) (convertidas): {[round(r, 6) for r in raizes_f]}")
    
    print(f"\nExplicação: A transformação f(1/x) mapeia valores grandes de x")
    print(f"para valores pequenos, permitindo visualizar o comportamento")
    print(f"da função fora do intervalo [-1, 1].")

# ============================================================================
# EXERCÍCIO 8: Algoritmo de Horner
# ============================================================================

def metodo_horner(x: float) -> float:
    """
    Implementa o algoritmo de Horner para avaliar o polinômio
    p(x) = x^5 + 18*x^3 + 34*x^2 - 493*x + 1431
    """
    a = [1, 0, 18, 34, -493, 1431]
    p = 0
    
    for i in range(len(a)):
        p = x * p + a[i]
    
    return p

def exercicio8():
    """
    Analisa e implementa o algoritmo de Horner
    """
    print("\n=== EXERCÍCIO 8 ===")
    
    print("Algoritmo implementado:")
    print("void metodo(double x) {")
    print("    double a[] = {1, 0, 18, 34, -493, 1431};")
    print("    double p = 0;")
    print("    for (int i = 0; i < tamanho(a); i++) {")
    print("        p = x * p + a[i];")
    print("    }")
    print("    imprime(x, p);")
    print("}")
    
    print(f"\nEste é o algoritmo de Horner para avaliar o polinômio")
    print(f"p(x) = x^5 + 18*x^3 + 34*x^2 - 493*x + 1431")
    
    # Testa com diferentes valores
    valores_teste = [-2, -1, 0, 1, 2, 5, 10]
    
    print(f"\nTestando o algoritmo:")
    for x in valores_teste:
        resultado = metodo_horner(x)
        print(f"p({x}) = {resultado}")

# ============================================================================
# EXERCÍCIO 9: Método da secante
# ============================================================================

def secante(f, x0: float, x1: float, tol: float = 1e-10, max_iter: int = 100) -> Tuple[float, int, bool]:
    """
    Implementa o método da secante para encontrar raízes
    """
    iteracoes = 0
    
    while iteracoes < max_iter:
        f0 = f(x0)
        f1 = f(x1)
        
        if abs(f1) < tol:
            return x1, iteracoes, True
        
        if abs(f1 - f0) < tol:
            return x1, iteracoes, False
        
        # Fórmula da secante
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        
        x0, x1 = x1, x2
        iteracoes += 1
    
    return x1, iteracoes, False

def exercicio9():
    """
    Implementa método da secante para encontrar raízes reais
    """
    print("\n=== EXERCÍCIO 9 ===")
    
    # Polinômio: p(x) = x^5 + 18*x^3 + 34*x^2 - 493*x + 1431
    def f(x):
        return metodo_horner(x)
    
    print("Polinômio: p(x) = x^5 + 18*x^3 + 34*x^2 - 493*x + 1431")
    print("Método da secante para encontrar raízes reais")
    
    # Análise do número de raízes reais
    print(f"\nAnálise do número de raízes reais:")
    print(f"Pelo teorema de Descartes, o número de raízes reais positivas")
    print(f"é no máximo igual ao número de mudanças de sinal nos coeficientes.")
    print(f"Coeficientes: [1, 0, 18, 34, -493, 1431]")
    print(f"Mudanças de sinal: 1 -> 0 (não conta), 34 -> -493 (1), -493 -> 1431 (1)")
    print(f"Total: no máximo 2 raízes reais positivas")
    
    # Testa o método da secante com diferentes pontos iniciais
    pontos_iniciais = [(-2, -1), (0, 1), (5, 6), (10, 11)]
    
    print(f"\nAplicando método da secante:")
    for x0, x1 in pontos_iniciais:
        raiz, iteracoes, convergiu = secante(f, x0, x1)
        if convergiu:
            print(f"Pontos iniciais ({x0}, {x1}): raiz = {raiz:.6f}, iterações = {iteracoes}")
        else:
            print(f"Pontos iniciais ({x0}, {x1}): não convergiu")

# ============================================================================
# EXERCÍCIO 10: Algoritmo modificado (derivada)
# ============================================================================

def metodo_horner_derivada(x: float) -> Tuple[float, float]:
    """
    Implementa o algoritmo de Horner modificado que calcula
    tanto o valor do polinômio quanto sua derivada
    """
    a = [1, 0, 18, 34, -493, 1431]
    p = 0
    q = 0
    
    for i in range(len(a)):
        q = x * q + p
        p = x * p + a[i]
    
    return p, q

def exercicio10():
    """
    Analisa o algoritmo modificado
    """
    print("\n=== EXERCÍCIO 10 ===")
    
    print("Algoritmo modificado:")
    print("void metodo(double x) {")
    print("    double a[] = {1, 0, 18, 34, -493, 1431};")
    print("    double p = 0;")
    print("    double q = 0;")
    print("    for (int i = 0; i < tamanho(a); i++) {")
    print("        q = x * q + p;")
    print("        p = x * p + a[i];")
    print("    }")
    print("    imprime(x, p, q);")
    print("}")
    
    print(f"\nEste algoritmo calcula:")
    print(f"p = valor do polinômio p(x)")
    print(f"q = valor da derivada p'(x)")
    
    # Testa com diferentes valores
    valores_teste = [-2, -1, 0, 1, 2]
    
    print(f"\nTestando o algoritmo:")
    for x in valores_teste:
        p, q = metodo_horner_derivada(x)
        print(f"x = {x}: p(x) = {p}, p'(x) = {q}")

# ============================================================================
# EXERCÍCIO 11: Método de Newton com números complexos
# ============================================================================

def newton_complexo(x0: complex, tol: float = 1e-10, max_iter: int = 100) -> Tuple[complex, int, bool]:
    """
    Implementa o método de Newton usando números complexos
    """
    x = x0
    iteracoes = 0
    
    while iteracoes < max_iter:
        # Calcula p(x) e p'(x) usando o algoritmo de Horner
        p, q = metodo_horner_derivada_complexo(x)
        
        if abs(p) < tol:
            return x, iteracoes, True
        
        if abs(q) < tol:
            return x, iteracoes, False
        
        # Fórmula de Newton: x_{n+1} = x_n - p(x_n)/p'(x_n)
        x_novo = x - p / q
        
        if abs(x_novo - x) < tol:
            return x_novo, iteracoes, True
        
        x = x_novo
        iteracoes += 1
    
    return x, iteracoes, False

def metodo_horner_derivada_complexo(x: complex) -> Tuple[complex, complex]:
    """
    Versão complexa do algoritmo de Horner com derivada
    """
    a = [1, 0, 18, 34, -493, 1431]
    p = 0 + 0j
    q = 0 + 0j
    
    for i in range(len(a)):
        q = x * q + p
        p = x * p + a[i]
    
    return p, q

def exercicio11():
    """
    Implementa método de Newton com números complexos
    """
    print("\n=== EXERCÍCIO 11 ===")
    
    print("Método de Newton com números complexos")
    print("para encontrar todas as raízes do polinômio")
    
    # Pontos iniciais complexos
    pontos_iniciais = [
        1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j,
        2 + 2j, -2 + 2j, -2 - 2j, 2 - 2j
    ]
    
    raizes_encontradas = []
    
    print(f"\nAplicando método de Newton:")
    for x0 in pontos_iniciais:
        raiz, iteracoes, convergiu = newton_complexo(x0)
        if convergiu:
            # Verifica se a raiz já foi encontrada (com tolerância)
            raiz_encontrada = False
            for r in raizes_encontradas:
                if abs(raiz - r) < 1e-6:
                    raiz_encontrada = True
                    break
            
            if not raiz_encontrada:
                raizes_encontradas.append(raiz)
                print(f"Ponto inicial {x0}: raiz = {raiz:.6f}, iterações = {iteracoes}")
    
    print(f"\nRaízes encontradas:")
    for i, raiz in enumerate(raizes_encontradas):
        print(f"Raiz {i+1}: {raiz:.6f}")

# ============================================================================
# EXERCÍCIO 12: Fractais de Newton
# ============================================================================

def criar_polinomio_raizes_complexas(raizes: List[complex]) -> List[complex]:
    """
    Cria um polinômio com raízes complexas especificadas
    """
    # Começa com (x - r1)
    polinomio = [1, -raizes[0]]
    
    # Multiplica por (x - ri) para cada raiz
    for raiz in raizes[1:]:
        novo_polinomio = [0] * (len(polinomio) + 1)
        for i in range(len(polinomio)):
            novo_polinomio[i] += polinomio[i]
            novo_polinomio[i + 1] += polinomio[i] * (-raiz)
        polinomio = novo_polinomio
    
    return polinomio

def newton_fractal(raizes: List[complex], x_min: float, x_max: float, 
                   y_min: float, y_max: float, resolucao: int = 100) -> np.ndarray:
    """
    Gera fractal de Newton para um polinômio com raízes conhecidas
    """
    # Cria o polinômio
    coeficientes = criar_polinomio_raizes_complexas(raizes)
    
    # Função para avaliar polinômio e derivada
    def avaliar_polinomio_derivada(x):
        p = 0 + 0j
        q = 0 + 0j
        for i in range(len(coeficientes)):
            q = x * q + p
            p = x * p + coeficientes[i]
        return p, q
    
    # Gera grade de pontos
    x_vals = np.linspace(x_min, x_max, resolucao)
    y_vals = np.linspace(y_min, y_max, resolucao)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    # Matriz para armazenar cores
    cores = np.zeros((resolucao, resolucao), dtype=int)
    
    # Para cada ponto inicial
    for i in range(resolucao):
        for j in range(resolucao):
            x0 = X[i, j] + 1j * Y[i, j]
            
            # Aplica método de Newton
            x = x0
            for _ in range(50):  # Máximo 50 iterações
                p, q = avaliar_polinomio_derivada(x)
                
                if abs(q) < 1e-10:
                    break
                
                x = x - p / q
            
            # Encontra qual raiz foi convergida
            raiz_mais_proxima = 0
            distancia_min = float('inf')
            
            for k, raiz in enumerate(raizes):
                distancia = abs(x - raiz)
                if distancia < distancia_min:
                    distancia_min = distancia
                    raiz_mais_proxima = k
            
            cores[i, j] = raiz_mais_proxima
    
    return cores

def exercicio12():
    """
    Implementa fractais de Newton
    """
    print("\n=== EXERCÍCIO 12 ===")
    
    print("Fractais de Newton")
    print("Criando polinômio com raízes conhecidas e gerando fractal")
    
    # Define raízes para o polinômio
    raizes = [1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j]
    
    print(f"Raízes do polinômio: {raizes}")
    
    # Gera fractal
    cores = newton_fractal(raizes, -2, 2, -2, 2, 200)
    
    # Plota o fractal
    plt.figure(figsize=(10, 8))
    plt.imshow(cores, extent=[-2, 2, -2, 2], cmap='viridis')
    plt.colorbar(label='Raiz convergida')
    plt.title('Fractal de Newton')
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    
    # Marca as raízes
    for i, raiz in enumerate(raizes):
        plt.plot(raiz.real, raiz.imag, 'ro', markersize=10, label=f'Raiz {i+1}')
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('fractal_newton.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"Fractal salvo como 'fractal_newton.png'")
    print(f"Cada cor representa uma raiz diferente")
    print(f"Os pontos vermelhos marcam as posições das raízes")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios
    """
    print("MÉTODOS NUMÉRICOS - SOLUÇÃO DE EQUAÇÕES")
    print("=" * 50)
    
    # Executa todos os exercícios
    exercicio1()
    exercicio2()
    exercicio3()
    exercicio4()
    exercicio5()
    exercicio6()
    exercicio7()
    exercicio8()
    exercicio9()
    exercicio10()
    exercicio11()
    exercicio12()
    
    print("\n" + "=" * 50)
    print("TODOS OS EXERCÍCIOS CONCLUÍDOS!")

if __name__ == "__main__":
    main()
