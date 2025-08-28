"""
Métodos Numéricos - Interpolação
Versão de demonstração (sem gráficos)
"""

import numpy as np
from typing import List, Tuple
from scipy.interpolate import lagrange
from scipy.optimize import fsolve
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# EXERCÍCIO 1: Parábola que passa por três pontos
# ============================================================================

def exercicio1():
    """
    Encontra a parábola que passa pelos pontos (2,3), (3,5) e (5,7)
    e depois encontra os pontos onde p(x) = 0
    """
    print("=== EXERCÍCIO 1: PARÁBOLA POR TRÊS PONTOS ===")
    
    # Pontos dados
    x = np.array([2, 3, 5])
    y = np.array([3, 5, 7])
    
    print(f"Pontos dados: {list(zip(x, y))}")
    
    # Método 1: Usando Lagrange
    print("\n--- Método 1: Interpolação de Lagrange ---")
    poly_lagrange = lagrange(x, y)
    print(f"Polinômio de Lagrange: {poly_lagrange}")
    
    # Método 2: Resolvendo sistema linear
    print("\n--- Método 2: Sistema Linear ---")
    # p(x) = ax² + bx + c
    # Sistema: 4a + 2b + c = 3
    #          9a + 3b + c = 5  
    #          25a + 5b + c = 7
    
    A = np.array([
        [4, 2, 1],
        [9, 3, 1],
        [25, 5, 1]
    ])
    b = np.array([3, 5, 7])
    
    coeffs = np.linalg.solve(A, b)
    a, b_coeff, c = coeffs
    
    print(f"Coeficientes: a = {a:.4f}, b = {b_coeff:.4f}, c = {c:.4f}")
    print(f"Parábola: p(x) = {a:.4f}x² + {b_coeff:.4f}x + {c:.4f}")
    
    # Verificação
    print("\n--- Verificação ---")
    for i, (xi, yi) in enumerate(zip(x, y)):
        p_xi = a * xi**2 + b_coeff * xi + c
        print(f"p({xi}) = {p_xi:.4f} (esperado: {yi})")
    
    # Encontrar raízes (p(x) = 0)
    print("\n--- Encontrando raízes (p(x) = 0) ---")
    
    def parabola(x):
        return a * x**2 + b_coeff * x + c
    
    # Usando fsolve para encontrar raízes
    x0_guess = [0, 10]  # Chutes iniciais
    raizes = []
    
    for x0 in x0_guess:
        raiz = fsolve(parabola, x0)[0]
        if abs(parabola(raiz)) < 1e-10:  # Verificar se é realmente uma raiz
            raizes.append(raiz)
    
    # Remover duplicatas
    raizes = list(set([round(r, 6) for r in raizes]))
    
    print(f"Raízes encontradas: x* = {raizes}")
    
    # Verificar as raízes
    for raiz in raizes:
        valor = parabola(raiz)
        print(f"p({raiz:.6f}) = {valor:.10f}")
    
    return coeffs, raizes

# ============================================================================
# EXERCÍCIO 2: Interpolação de Newton - Três cientistas
# ============================================================================

def exercicio2():
    """
    Compara os polinômios encontrados pelos três cientistas usando diferentes
    ordens dos pontos na interpolação de Newton
    """
    print("=== EXERCÍCIO 2: INTERPOLAÇÃO DE NEWTON - TRÊS CIENTISTAS ===")
    
    # Dados originais
    dados_originais = [(1, 2), (3, 5), (5, 4), (7, 8)]
    
    # Organização dos cientistas
    ana = [(1, 2), (3, 5), (5, 4), (7, 8)]      # Ordem original
    beto = [(7, 8), (5, 4), (3, 5), (1, 2)]     # Ordem inversa
    carol = [(5, 4), (1, 2), (7, 8), (3, 5)]    # Ordem bagunçada
    
    cientistas = {
        "Ana": ana,
        "Beto": beto,
        "Carol": carol
    }
    
    polinomios = {}
    
    for nome, pontos in cientistas.items():
        print(f"\n--- {nome} ---")
        print(f"Pontos na ordem: {pontos}")
        
        x = np.array([p[0] for p in pontos])
        y = np.array([p[1] for p in pontos])
        
        # Interpolação de Lagrange (equivalente a Newton para os mesmos pontos)
        poly = lagrange(x, y)
        polinomios[nome] = poly
        
        print(f"Polinômio: {poly}")
        
        # Verificação
        print("Verificação:")
        for xi, yi in pontos:
            p_xi = poly(xi)
            print(f"  p({xi}) = {p_xi:.4f} (esperado: {yi})")
    
    # Comparação dos polinômios
    print("\n=== COMPARAÇÃO DOS POLINÔMIOS ===")
    
    # Verificar se são iguais
    ana_poly = polinomios["Ana"]
    beto_poly = polinomios["Beto"]
    carol_poly = polinomios["Carol"]
    
    # Comparar coeficientes
    print("Coeficientes dos polinômios:")
    print(f"Ana:   {ana_poly.coef}")
    print(f"Beto:  {beto_poly.coef}")
    print(f"Carol: {carol_poly.coef}")
    
    # Verificar se são idênticos
    sao_iguais = np.allclose(ana_poly.coef, beto_poly.coef) and np.allclose(ana_poly.coef, carol_poly.coef)
    
    print(f"\nOs polinômios são iguais? {sao_iguais}")
    
    if sao_iguais:
        print("EXPLICAÇÃO: Todos os polinômios são iguais porque:")
        print("- A interpolação polinomial é única para um conjunto de pontos")
        print("- A ordem dos pontos não afeta o resultado final")
        print("- O polinômio de menor grau que passa pelos pontos é sempre o mesmo")
    else:
        print("EXPLICAÇÃO: Os polinômios são diferentes porque...")
    
    return polinomios, sao_iguais

# ============================================================================
# EXERCÍCIO 3: Produção chinesa de aço - Extrapolação
# ============================================================================

def exercicio3():
    """
    Usa interpolação polinomial para prever a produção chinesa de aço
    """
    print("=== EXERCÍCIO 3: PRODUÇÃO CHINESA DE AÇO ===")
    
    # Dados da produção chinesa de aço (1990-1996)
    anos = np.array([1990, 1991, 1992, 1993, 1994, 1995, 1996])
    producao = np.array([62.4, 67.7, 75.9, 87.4, 97.4, 105.3, 107.2])
    
    print("Dados originais:")
    for ano, prod in zip(anos, producao):
        print(f"  {ano}: {prod} Mton")
    
    # Teste: usar dados até 1995 para prever 1996
    print("\n=== TESTE DE EXTRAPOLAÇÃO ===")
    print("Usando dados de 1990-1995 para prever 1996:")
    
    anos_treino = anos[:-1]  # 1990-1995
    producao_treino = producao[:-1]  # Dados até 1995
    ano_teste = anos[-1]  # 1996
    valor_real = producao[-1]  # 107.2
    
    # Interpolação polinomial
    poly = lagrange(anos_treino, producao_treino)
    previsao_1996 = poly(ano_teste)
    
    print(f"Previsão para 1996: {previsao_1996:.2f} Mton")
    print(f"Valor real: {valor_real} Mton")
    print(f"Erro absoluto: {abs(previsao_1996 - valor_real):.2f} Mton")
    print(f"Erro relativo: {abs(previsao_1996 - valor_real)/valor_real*100:.2f}%")
    
    # Previsão para 1997
    print("\n=== PREVISÃO PARA 1997 ===")
    previsao_1997 = poly(1997)
    print(f"Previsão para 1997: {previsao_1997:.2f} Mton")
    
    # Análise do polinômio
    print(f"\nPolinômio interpolador (grau {len(anos_treino)-1}):")
    print(f"{poly}")
    
    # Verificar se a extrapolação faz sentido
    print("\n=== ANÁLISE DA EXTRAPOLAÇÃO ===")
    if previsao_1997 > previsao_1996:
        print("A previsão para 1997 é maior que 1996 (crescimento)")
    else:
        print("A previsão para 1997 é menor que 1996 (queda)")
    
    print("AVISO: Extrapolação polinomial pode ser instável e imprecisa!")
    
    return poly, previsao_1996, previsao_1997

# ============================================================================
# EXERCÍCIO 4: Produção brasileira de ovos
# ============================================================================

def exercicio4():
    """
    Ajusta dados da produção brasileira de ovos e prevê para 2022
    """
    print("=== EXERCÍCIO 4: PRODUÇÃO BRASILEIRA DE OVOS ===")
    
    # Dados da produção brasileira de ovos (2016-2021)
    anos = np.array([2016, 2017, 2018, 2019, 2020, 2021])
    producao = np.array([3097841, 3313061, 3606747, 3842136, 3967138, 4012512])
    
    print("Dados originais (em mil dúzias):")
    for ano, prod in zip(anos, producao):
        print(f"  {ano}: {prod:,}")
    
    # Interpolação polinomial
    print("\n=== INTERPOLAÇÃO POLINOMIAL ===")
    poly = lagrange(anos, producao)
    previsao_2022 = poly(2022)
    
    print(f"Polinômio interpolador (grau {len(anos)-1}):")
    print(f"{poly}")
    print(f"Previsão para 2022: {previsao_2022:,.0f} mil dúzias")
    
    # Ajuste por mínimos quadrados (reta)
    print("\n=== AJUSTE POR MÍNIMOS QUADRADOS (RETA) ===")
    coeffs = np.polyfit(anos, producao, 1)
    a, b = coeffs
    
    print(f"Reta: y = {a:.2f}x + {b:.2f}")
    previsao_reta_2022 = a * 2022 + b
    print(f"Previsão para 2022 (reta): {previsao_reta_2022:,.0f} mil dúzias")
    
    # Ajuste por mínimos quadrados (polinômio de grau 2)
    print("\n=== AJUSTE POR MÍNIMOS QUADRADOS (GRAU 2) ===")
    coeffs_2 = np.polyfit(anos, producao, 2)
    a2, b2, c2 = coeffs_2
    
    print(f"Polinômio grau 2: y = {a2:.2f}x² + {b2:.2f}x + {c2:.2f}")
    previsao_grau2_2022 = a2 * 2022**2 + b2 * 2022 + c2
    print(f"Previsão para 2022 (grau 2): {previsao_grau2_2022:,.0f} mil dúzias")
    
    # Comparação das previsões
    print("\n=== COMPARAÇÃO DAS PREVISÕES PARA 2022 ===")
    print(f"Interpolação polinomial: {previsao_2022:,.0f} mil dúzias")
    print(f"Ajuste linear:           {previsao_reta_2022:,.0f} mil dúzias")
    print(f"Ajuste grau 2:           {previsao_grau2_2022:,.0f} mil dúzias")
    
    return {
        'interpolacao': previsao_2022,
        'reta': previsao_reta_2022,
        'grau2': previsao_grau2_2022
    }

# ============================================================================
# EXERCÍCIO 5: Produção brasileira de camarão - Interpolação
# ============================================================================

def exercicio5():
    """
    Estima o valor de 2017 usando interpolação e prevê 2021
    """
    print("=== EXERCÍCIO 5: PRODUÇÃO BRASILEIRA DE CAMARÃO ===")
    
    # Dados da produção brasileira de camarão (2013-2020)
    anos = np.array([2013, 2014, 2015, 2016, 2018, 2019, 2020])
    producao = np.array([64678, 65028, 70521, 52127, 47316, 56667, 66561])
    
    print("Dados disponíveis (em ton):")
    for ano, prod in zip(anos, producao):
        print(f"  {ano}: {prod:,}")
    
    print("\nValor faltante: 2017")
    
    # Interpolação para estimar 2017
    print("\n=== ESTIMATIVA PARA 2017 ===")
    poly = lagrange(anos, producao)
    estimativa_2017 = poly(2017)
    
    print(f"Polinômio interpolador:")
    print(f"{poly}")
    print(f"Estimativa para 2017: {estimativa_2017:,.0f} ton")
    
    # Valor real de 2017 (dado no enunciado)
    valor_real_2017 = 41078
    print(f"Valor real de 2017: {valor_real_2017:,} ton")
    print(f"Erro absoluto: {abs(estimativa_2017 - valor_real_2017):,.0f} ton")
    print(f"Erro relativo: {abs(estimativa_2017 - valor_real_2017)/valor_real_2017*100:.2f}%")
    
    # Previsão para 2021
    print("\n=== PREVISÃO PARA 2021 ===")
    previsao_2021 = poly(2021)
    print(f"Previsão para 2021: {previsao_2021:,.0f} ton")
    
    # Análise da qualidade da interpolação
    print("\n=== ANÁLISE DA QUALIDADE ===")
    print("Verificação dos pontos interpolados:")
    for ano, prod in zip(anos, producao):
        p_ano = poly(ano)
        print(f"  p({ano}) = {p_ano:,.0f} (real: {prod:,})")
    
    return estimativa_2017, previsao_2021

# ============================================================================
# EXERCÍCIO 6: Mínimos quadrados - Ajuste de dados
# ============================================================================

def exercicio6():
    """
    Usa mínimos quadrados para ajustar os dados de produção de camarão
    """
    print("=== EXERCÍCIO 6: MÍNIMOS QUADRADOS - AJUSTE DE DADOS ===")
    
    # Dados completos incluindo 2017
    anos_completos = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    producao_completa = np.array([64678, 65028, 70521, 52127, 41078, 47316, 56667, 66561])
    
    print("Dados completos (em ton):")
    for ano, prod in zip(anos_completos, producao_completa):
        print(f"  {ano}: {prod:,}")
    
    # Ajuste linear (reta)
    print("\n=== AJUSTE LINEAR (RETA) ===")
    coeffs_linear = np.polyfit(anos_completos, producao_completa, 1)
    a_linear, b_linear = coeffs_linear
    
    print(f"Reta: y = {a_linear:.2f}x + {b_linear:.2f}")
    
    # Calcular R² para o ajuste linear
    y_pred_linear = a_linear * anos_completos + b_linear
    ss_res_linear = np.sum((producao_completa - y_pred_linear)**2)
    ss_tot_linear = np.sum((producao_completa - np.mean(producao_completa))**2)
    r2_linear = 1 - (ss_res_linear / ss_tot_linear)
    
    print(f"R² (ajuste linear): {r2_linear:.4f}")
    
    # Ajuste polinomial de grau 3
    print("\n=== AJUSTE POLINOMIAL (GRAU 3) ===")
    coeffs_cubico = np.polyfit(anos_completos, producao_completa, 3)
    a_cub, b_cub, c_cub, d_cub = coeffs_cubico
    
    print(f"Polinômio grau 3: y = {a_cub:.2e}x³ + {b_cub:.2f}x² + {c_cub:.2f}x + {d_cub:.2f}")
    
    # Calcular R² para o ajuste cúbico
    y_pred_cubico = np.polyval(coeffs_cubico, anos_completos)
    ss_res_cubico = np.sum((producao_completa - y_pred_cubico)**2)
    ss_tot_cubico = np.sum((producao_completa - np.mean(producao_completa))**2)
    r2_cubico = 1 - (ss_res_cubico / ss_tot_cubico)
    
    print(f"R² (ajuste cúbico): {r2_cubico:.4f}")
    
    # Comparação dos ajustes
    print("\n=== COMPARAÇÃO DOS AJUSTES ===")
    print("Valores ajustados:")
    print("Ano    Real    Linear  Cúbico")
    print("-" * 40)
    for i, ano in enumerate(anos_completos):
        real = producao_completa[i]
        linear = y_pred_linear[i]
        cubico = y_pred_cubico[i]
        print(f"{ano}  {real:6.0f}  {linear:6.0f}  {cubico:6.0f}")
    
    print(f"\nR² Linear:  {r2_linear:.4f}")
    print(f"R² Cúbico:  {r2_cubico:.4f}")
    
    if r2_cubico > r2_linear:
        print("O ajuste cúbico tem melhor R² (melhor ajuste)")
    else:
        print("O ajuste linear tem melhor R² (melhor ajuste)")
    
    # Previsões para 2021
    previsao_linear_2021 = a_linear * 2021 + b_linear
    previsao_cubico_2021 = np.polyval(coeffs_cubico, 2021)
    
    print(f"\nPrevisões para 2021:")
    print(f"Linear:  {previsao_linear_2021:,.0f} ton")
    print(f"Cúbico:  {previsao_cubico_2021:,.0f} ton")
    
    return {
        'linear': {'coeffs': coeffs_linear, 'r2': r2_linear, 'previsao_2021': previsao_linear_2021},
        'cubico': {'coeffs': coeffs_cubico, 'r2': r2_cubico, 'previsao_2021': previsao_cubico_2021}
    }

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de interpolação
    """
    print("MÉTODOS NUMÉRICOS - INTERPOLAÇÃO")
    print("=" * 50)
    
    # Executar todos os exercícios
    print("\n" + "="*50)
    resultado1 = exercicio1()
    
    print("\n" + "="*50)
    resultado2 = exercicio2()
    
    print("\n" + "="*50)
    resultado3 = exercicio3()
    
    print("\n" + "="*50)
    resultado4 = exercicio4()
    
    print("\n" + "="*50)
    resultado5 = exercicio5()
    
    print("\n" + "="*50)
    resultado6 = exercicio6()
    
    print("\n" + "="*50)
    print("EXECUÇÃO CONCLUÍDA!")
    print("Todos os exercícios de interpolação foram resolvidos.")

if __name__ == "__main__":
    main()
