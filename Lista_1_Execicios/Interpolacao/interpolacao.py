"""
Métodos Numéricos - Interpolação
Solução dos exercícios da Lista 1
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, interp1d
from scipy.optimize import curve_fit
import math

# ============================================================================
# EXERCÍCIO 1: Parábola que passa por três pontos
# ============================================================================

def exercicio1():
    """
    Encontra a parábola que passa pelos pontos dados e suas raízes
    """
    print("=== EXERCÍCIO 1: PARÁBOLA QUE PASSA POR TRÊS PONTOS ===")
    
    # Pontos dados: (2, 3), (3, 5), (5, 7)
    pontos = [(2, 3), (3, 5), (5, 7)]
    
    print("Pontos: (2, 3), (3, 5), (5, 7)")
    print("Parábola: p(x) = ax² + bx + c")
    
    # Construir sistema linear
    A = np.zeros((3, 3))
    b = np.zeros(3)
    
    for i, (x, y) in enumerate(pontos):
        A[i, 0] = x**2  # coeficiente de a
        A[i, 1] = x     # coeficiente de b
        A[i, 2] = 1     # coeficiente de c
        b[i] = y
    
    print(f"\nSistema linear:")
    print("4a + 2b + c = 3")
    print("9a + 3b + c = 5")
    print("25a + 5b + c = 7")
    
    print(f"\nMatriz A:")
    print(A)
    print(f"\nVetor b:")
    print(b)
    
    # Resolver o sistema
    try:
        coeficientes = np.linalg.solve(A, b)
        a, b_coef, c = coeficientes
        
        print(f"\nCoeficientes encontrados:")
        print(f"a = {a:.6f}")
        print(f"b = {b_coef:.6f}")
        print(f"c = {c:.6f}")
        
        print(f"\nParábola: p(x) = {a:.6f}x² + {b_coef:.6f}x + {c:.6f}")
        
        # Verificar se a parábola passa pelos pontos
        print(f"\nVerificação:")
        for x, y_esperado in pontos:
            y_calculado = a*x**2 + b_coef*x + c
            erro = abs(y_calculado - y_esperado)
            print(f"p({x}) = {y_calculado:.6f} (esperado: {y_esperado}), erro: {erro:.2e}")
        
        # Encontrar raízes (p(x) = 0)
        print(f"\nRaízes da parábola (p(x) = 0):")
        print(f"ax² + bx + c = 0")
        print(f"{a:.6f}x² + {b_coef:.6f}x + {c:.6f} = 0")
        
        # Usar fórmula de Bhaskara
        delta = b_coef**2 - 4*a*c
        print(f"Δ = b² - 4ac = {b_coef:.6f}² - 4({a:.6f})({c:.6f}) = {delta:.6f}")
        
        if delta >= 0:
            x1 = (-b_coef + math.sqrt(delta)) / (2*a)
            x2 = (-b_coef - math.sqrt(delta)) / (2*a)
            print(f"x₁ = {x1:.6f}")
            print(f"x₂ = {x2:.6f}")
            
            # Verificar se as raízes são corretas
            print(f"\nVerificação das raízes:")
            print(f"p({x1:.6f}) = {a*x1**2 + b_coef*x1 + c:.2e}")
            print(f"p({x2:.6f}) = {a*x2**2 + b_coef*x2 + c:.2e}")
        else:
            print("A parábola não tem raízes reais (Δ < 0)")
        
    except np.linalg.LinAlgError:
        print("Erro: Sistema singular ou mal condicionado")

# ============================================================================
# EXERCÍCIO 2: Interpolação de Newton - Três cientistas
# ============================================================================

def interpolacao_newton(x, y):
    """
    Implementa interpolação de Newton
    """
    n = len(x)
    # Tabela de diferenças divididas
    dd = np.zeros((n, n))
    dd[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            dd[i, j] = (dd[i+1, j-1] - dd[i, j-1]) / (x[i+j] - x[i])
    
    # Construir polinômio
    def p(x_val):
        result = dd[0, 0]
        for i in range(1, n):
            term = dd[0, i]
            for j in range(i):
                term *= (x_val - x[j])
            result += term
        return result
    
    return p, dd

def exercicio2():
    """
    Compara polinômios encontrados por três cientistas usando diferentes ordens
    """
    print("=== EXERCÍCIO 2: INTERPOLAÇÃO DE NEWTON - TRÊS CIENTISTAS ===")
    
    # Dados originais
    x_original = [1, 3, 5, 7]
    y_original = [2, 5, 4, 8]
    
    print("Dados originais:")
    print("x: [1, 3, 5, 7]")
    print("y: [2, 5, 4, 8]")
    
    # Ana: ordem original
    print(f"\n--- ANA (ordem original) ---")
    x_ana = [1, 3, 5, 7]
    y_ana = [2, 5, 4, 8]
    p_ana, dd_ana = interpolacao_newton(x_ana, y_ana)
    
    print("Ordem: (1,2), (3,5), (5,4), (7,8)")
    print("Tabela de diferenças divididas:")
    print(dd_ana)
    
    # Beto: ordem inversa
    print(f"\n--- BETO (ordem inversa) ---")
    x_beto = [7, 5, 3, 1]
    y_beto = [8, 4, 5, 2]
    p_beto, dd_beto = interpolacao_newton(x_beto, y_beto)
    
    print("Ordem: (7,8), (5,4), (3,5), (1,2)")
    print("Tabela de diferenças divididas:")
    print(dd_beto)
    
    # Carol: ordem bagunçada
    print(f"\n--- CAROL (ordem bagunçada) ---")
    x_carol = [5, 1, 7, 3]
    y_carol = [4, 2, 8, 5]
    p_carol, dd_carol = interpolacao_newton(x_carol, y_carol)
    
    print("Ordem: (5,4), (1,2), (7,8), (3,5)")
    print("Tabela de diferenças divididas:")
    print(dd_carol)
    
    # Comparar os polinômios
    print(f"\n--- COMPARAÇÃO DOS POLINÔMIOS ---")
    
    # Testar em alguns pontos
    pontos_teste = [0, 2, 4, 6, 8]
    print("Comparação dos valores dos polinômios:")
    print("x\tAna\t\tBeto\t\tCarol\t\tDiferença")
    print("-" * 60)
    
    for x in pontos_teste:
        val_ana = p_ana(x)
        val_beto = p_beto(x)
        val_carol = p_carol(x)
        
        # Verificar se são iguais
        dif_ana_beto = abs(val_ana - val_beto)
        dif_ana_carol = abs(val_ana - val_carol)
        dif_beto_carol = abs(val_beto - val_carol)
        
        max_dif = max(dif_ana_beto, dif_ana_carol, dif_beto_carol)
        
        print(f"{x}\t{val_ana:.6f}\t{val_beto:.6f}\t{val_carol:.6f}\t{max_dif:.2e}")
    
    # Verificar se passam pelos pontos originais
    print(f"\nVerificação nos pontos originais:")
    print("x\ty_original\tAna\t\tBeto\t\tCarol")
    print("-" * 50)
    
    for i, x in enumerate(x_original):
        y_orig = y_original[i]
        val_ana = p_ana(x)
        val_beto = p_beto(x)
        val_carol = p_carol(x)
        print(f"{x}\t{y_orig}\t\t{val_ana:.6f}\t{val_beto:.6f}\t{val_carol:.6f}")
    
    print(f"\nCONCLUSÃO:")
    print("✓ Todos os polinômios são idênticos!")
    print("✓ A ordem dos pontos não afeta o resultado final")
    print("✓ A interpolação polinomial é única para um conjunto de pontos")

# ============================================================================
# EXERCÍCIO 3: Produção chinesa de aço - Extrapolação
# ============================================================================

def exercicio3():
    """
    Usa interpolação polinomial para prever produção futura de aço
    """
    print("=== EXERCÍCIO 3: PRODUÇÃO CHINESA DE AÇO - EXTRAPOLAÇÃO ===")
    
    # Dados da produção chinesa de aço (ferro gusa) - década de 1990
    anos = [1990, 1991, 1992, 1993, 1994, 1995, 1996]
    producao = [62.4, 67.7, 75.9, 87.4, 97.4, 105.3, 107.2]  # Mton
    
    print("Produção chinesa de aço (ferro gusa) - década de 1990:")
    print("Ano\tProdução (Mton)")
    print("-" * 25)
    for ano, prod in zip(anos, producao):
        print(f"{ano}\t{prod}")
    
    # Teste: usar todos os pontos exceto o último para prever o último
    print(f"\n--- TESTE: PREVER 1996 USANDO DADOS ATÉ 1995 ---")
    
    anos_treino = anos[:-1]  # 1990-1995
    producao_treino = producao[:-1]  # até 1995
    ano_teste = anos[-1]  # 1996
    producao_real_1996 = producao[-1]  # valor real de 1996
    
    print(f"Anos de treino: {anos_treino}")
    print(f"Produção de treino: {producao_treino}")
    print(f"Ano a prever: {ano_teste}")
    print(f"Produção real de 1996: {producao_real_1996} Mton")
    
    # Interpolação polinomial
    p_interp = lagrange(anos_treino, producao_treino)
    previsao_1996 = p_interp(ano_teste)
    
    print(f"\nPrevisão para 1996 (interpolação polinomial): {previsao_1996:.2f} Mton")
    print(f"Valor real: {producao_real_1996} Mton")
    print(f"Erro: {abs(previsao_1996 - producao_real_1996):.2f} Mton")
    print(f"Erro relativo: {abs(previsao_1996 - producao_real_1996)/producao_real_1996*100:.2f}%")
    
    # Extrapolação para 1997
    print(f"\n--- EXTRAPOLAÇÃO: PREVER 1997 ---")
    
    ano_1997 = 1997
    previsao_1997 = p_interp(ano_1997)
    
    print(f"Previsão para 1997: {previsao_1997:.2f} Mton")
    
    # Análise da qualidade da extrapolação
    print(f"\n--- ANÁLISE DA QUALIDADE ---")
    
    # Calcular valores interpolados nos pontos de treino
    valores_interpolados = [p_interp(ano) for ano in anos_treino]
    
    print("Comparação nos pontos de treino:")
    print("Ano\tReal\t\tInterpolado\tErro")
    print("-" * 40)
    
    for i, ano in enumerate(anos_treino):
        real = producao_treino[i]
        interp = valores_interpolados[i]
        erro = abs(real - interp)
        print(f"{ano}\t{real}\t\t{interp:.2f}\t\t{erro:.2e}")
    
    print(f"\nOBSERVAÇÕES:")
    print("- A interpolação polinomial passa exatamente pelos pontos de treino")
    print("- A extrapolação pode ser instável devido ao polinômio de alto grau")
    print("- Para dados reais, seria recomendável usar métodos mais robustos")

# ============================================================================
# EXERCÍCIO 4: Produção brasileira de ovos - Previsão 2022
# ============================================================================

def exercicio4():
    """
    Ajusta dados de produção de ovos e prevê 2022
    """
    print("=== EXERCÍCIO 4: PRODUÇÃO BRASILEIRA DE OVOS - PREVISÃO 2022 ===")
    
    # Dados da produção brasileira de ovos
    anos = [2016, 2017, 2018, 2019, 2020, 2021]
    producao = [3097841, 3313061, 3606747, 3842136, 3967138, 4012512]  # mil dúzias
    
    print("Produção brasileira de ovos (mil dúzias):")
    print("Ano\tProdução")
    print("-" * 20)
    for ano, prod in zip(anos, producao):
        print(f"{ano}\t{prod:,}")
    
    # Ajuste linear por mínimos quadrados
    print(f"\n--- AJUSTE LINEAR POR MÍNIMOS QUADRADOS ---")
    
    # Converter para numpy arrays
    x = np.array(anos)
    y = np.array(producao)
    
    # Ajuste linear: y = ax + b
    coeffs = np.polyfit(x, y, 1)
    a, b = coeffs
    
    print(f"Reta ajustada: y = {a:.2f}x + {b:.2f}")
    
    # Função de previsão
    def previsao_linear(ano):
        return a * ano + b
    
    # Previsão para 2022
    ano_2022 = 2022
    previsao_2022_linear = previsao_linear(ano_2022)
    
    print(f"Previsão para 2022 (linear): {previsao_2022_linear:,.0f} mil dúzias")
    
    # Ajuste polinomial de grau 2
    print(f"\n--- AJUSTE POLINOMIAL DE GRAU 2 ---")
    
    coeffs_poly2 = np.polyfit(x, y, 2)
    p_poly2 = np.poly1d(coeffs_poly2)
    
    print(f"Polinômio ajustado: {p_poly2}")
    
    previsao_2022_poly2 = p_poly2(ano_2022)
    print(f"Previsão para 2022 (polinomial grau 2): {previsao_2022_poly2:,.0f} mil dúzias")
    
    # Ajuste polinomial de grau 3
    print(f"\n--- AJUSTE POLINOMIAL DE GRAU 3 ---")
    
    coeffs_poly3 = np.polyfit(x, y, 3)
    p_poly3 = np.poly1d(coeffs_poly3)
    
    print(f"Polinômio ajustado: {p_poly3}")
    
    previsao_2022_poly3 = p_poly3(ano_2022)
    print(f"Previsão para 2022 (polinomial grau 3): {previsao_2022_poly3:,.0f} mil dúzias")
    
    # Comparação dos ajustes
    print(f"\n--- COMPARAÇÃO DOS AJUSTES ---")
    
    # Calcular R² para cada ajuste
    def r_squared(y_real, y_pred):
        ss_res = np.sum((y_real - y_pred) ** 2)
        ss_tot = np.sum((y_real - np.mean(y_real)) ** 2)
        return 1 - (ss_res / ss_tot)
    
    # Valores preditos nos pontos conhecidos
    y_pred_linear = [previsao_linear(ano) for ano in anos]
    y_pred_poly2 = [p_poly2(ano) for ano in anos]
    y_pred_poly3 = [p_poly3(ano) for ano in anos]
    
    r2_linear = r_squared(y, y_pred_linear)
    r2_poly2 = r_squared(y, y_pred_poly2)
    r2_poly3 = r_squared(y, y_pred_poly3)
    
    print("Qualidade dos ajustes (R²):")
    print(f"Linear: {r2_linear:.6f}")
    print(f"Polinomial grau 2: {r2_poly2:.6f}")
    print(f"Polinomial grau 3: {r2_poly3:.6f}")
    
    print(f"\nPrevisões para 2022:")
    print(f"Linear: {previsao_2022_linear:,.0f} mil dúzias")
    print(f"Polinomial grau 2: {previsao_2022_poly2:,.0f} mil dúzias")
    print(f"Polinomial grau 3: {previsao_2022_poly3:,.0f} mil dúzias")
    
    print(f"\nOBSERVAÇÕES:")
    print("- O ajuste linear é mais simples e pode ser mais confiável para extrapolação")
    print("- Polinômios de grau alto podem ser instáveis na extrapolação")
    print("- Para dados reais, verificar no IBGE o valor real de 2022")

# ============================================================================
# EXERCÍCIO 5: Produção brasileira de camarão - Estimativa e previsão
# ============================================================================

def exercicio5():
    """
    Estima valor de 2017 e prevê 2021 para produção de camarão
    """
    print("=== EXERCÍCIO 5: PRODUÇÃO BRASILEIRA DE CAMARÃO ===")
    
    # Dados da produção brasileira de camarão cultivado
    anos_completos = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    producao_completa = [64678, 65028, 70521, 52127, 41078, 47316, 56667, 66561, 0]  # ton
    
    print("Produção brasileira de camarão cultivado (ton):")
    print("Ano\tProdução")
    print("-" * 20)
    for ano, prod in zip(anos_completos, producao_completa):
        if prod == 0:
            print(f"{ano}\t(desconhecido)")
        else:
            print(f"{ano}\t{prod:,}")
    
    # Dados conhecidos (excluindo 2017 e 2021)
    anos_conhecidos = [2013, 2014, 2015, 2016, 2018, 2019, 2020]
    producao_conhecida = [64678, 65028, 70521, 52127, 47316, 56667, 66561]
    
    print(f"\nDados conhecidos (excluindo 2017 e 2021):")
    print("Ano\tProdução")
    print("-" * 20)
    for ano, prod in zip(anos_conhecidos, producao_conhecida):
        print(f"{ano}\t{prod:,}")
    
    # PARTE A: Estimar 2017
    print(f"\n--- PARTE A: ESTIMAR 2017 ---")
    
    # Interpolação polinomial para estimar 2017
    p_interp = lagrange(anos_conhecidos, producao_conhecida)
    estimativa_2017 = p_interp(2017)
    
    print(f"Estimativa para 2017 (interpolação polinomial): {estimativa_2017:,.0f} ton")
    print(f"Valor real de 2017: 41,078 ton")
    print(f"Erro: {abs(estimativa_2017 - 41078):,.0f} ton")
    print(f"Erro relativo: {abs(estimativa_2017 - 41078)/41078*100:.2f}%")
    
    # Ajuste linear por mínimos quadrados
    coeffs_linear = np.polyfit(anos_conhecidos, producao_conhecida, 1)
    a_linear, b_linear = coeffs_linear
    
    def previsao_linear(ano):
        return a_linear * ano + b_linear
    
    estimativa_2017_linear = previsao_linear(2017)
    print(f"Estimativa para 2017 (linear): {estimativa_2017_linear:,.0f} ton")
    print(f"Erro: {abs(estimativa_2017_linear - 41078):,.0f} ton")
    print(f"Erro relativo: {abs(estimativa_2017_linear - 41078)/41078*100:.2f}%")
    
    # PARTE B: Prever 2021
    print(f"\n--- PARTE B: PREVER 2021 ---")
    
    # Usar todos os dados conhecidos (incluindo 2017 real)
    anos_todos = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    producao_todos = [64678, 65028, 70521, 52127, 41078, 47316, 56667, 66561]
    
    # Interpolação polinomial
    p_interp_todos = lagrange(anos_todos, producao_todos)
    previsao_2021_interp = p_interp_todos(2021)
    
    print(f"Previsão para 2021 (interpolação polinomial): {previsao_2021_interp:,.0f} ton")
    
    # Ajuste linear
    coeffs_linear_todos = np.polyfit(anos_todos, producao_todos, 1)
    a_linear_todos, b_linear_todos = coeffs_linear_todos
    
    def previsao_linear_todos(ano):
        return a_linear_todos * ano + b_linear_todos
    
    previsao_2021_linear = previsao_linear_todos(2021)
    print(f"Previsão para 2021 (linear): {previsao_2021_linear:,.0f} ton")
    
    # Ajuste polinomial de grau 2
    coeffs_poly2 = np.polyfit(anos_todos, producao_todos, 2)
    p_poly2 = np.poly1d(coeffs_poly2)
    
    previsao_2021_poly2 = p_poly2(2021)
    print(f"Previsão para 2021 (polinomial grau 2): {previsao_2021_poly2:,.0f} ton")
    
    print(f"\nOBSERVAÇÕES:")
    print("- A interpolação polinomial de alto grau pode ser instável")
    print("- O ajuste linear é mais robusto para extrapolação")
    print("- Para dados reais, verificar no IBGE o valor real de 2021")

# ============================================================================
# EXERCÍCIO 6: Ajuste por mínimos quadrados - Reta e polinômio grau 3
# ============================================================================

def exercicio6():
    """
    Ajusta dados de camarão usando mínimos quadrados
    """
    print("=== EXERCÍCIO 6: AJUSTE POR MÍNIMOS QUADRADOS ===")
    
    # Dados completos de produção de camarão (incluindo 2017)
    anos = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    producao = [64678, 65028, 70521, 52127, 41078, 47316, 56667, 66561]  # ton
    
    print("Dados completos de produção de camarão:")
    print("Ano\tProdução (ton)")
    print("-" * 25)
    for ano, prod in zip(anos, producao):
        print(f"{ano}\t{prod:,}")
    
    # Converter para numpy arrays
    x = np.array(anos)
    y = np.array(producao)
    
    # AJUSTE 1: Melhor reta (grau 1)
    print(f"\n--- AJUSTE 1: MELHOR RETA (GRAU 1) ---")
    
    coeffs_reta = np.polyfit(x, y, 1)
    a_reta, b_reta = coeffs_reta
    p_reta = np.poly1d(coeffs_reta)
    
    print(f"Reta ajustada: y = {a_reta:.2f}x + {b_reta:.2f}")
    
    # Calcular R² para a reta
    y_pred_reta = [p_reta(ano) for ano in anos]
    ss_res_reta = np.sum((y - y_pred_reta) ** 2)
    ss_tot_reta = np.sum((y - np.mean(y)) ** 2)
    r2_reta = 1 - (ss_res_reta / ss_tot_reta)
    
    print(f"R² (reta): {r2_reta:.6f}")
    
    # AJUSTE 2: Melhor polinômio de grau 3
    print(f"\n--- AJUSTE 2: MELHOR POLINÔMIO DE GRAU 3 ---")
    
    coeffs_poly3 = np.polyfit(x, y, 3)
    p_poly3 = np.poly1d(coeffs_poly3)
    
    print(f"Polinômio ajustado: {p_poly3}")
    
    # Calcular R² para o polinômio
    y_pred_poly3 = [p_poly3(ano) for ano in anos]
    ss_res_poly3 = np.sum((y - y_pred_poly3) ** 2)
    ss_tot_poly3 = np.sum((y - np.mean(y)) ** 2)
    r2_poly3 = 1 - (ss_res_poly3 / ss_tot_poly3)
    
    print(f"R² (polinômio grau 3): {r2_poly3:.6f}")
    
    # Comparação dos ajustes
    print(f"\n--- COMPARAÇÃO DOS AJUSTES ---")
    
    print("Valores ajustados:")
    print("Ano\tReal\t\tReta\t\tPolinômio G3\tErro Reta\tErro Pol3")
    print("-" * 80)
    
    for i, ano in enumerate(anos):
        real = producao[i]
        val_reta = p_reta(ano)
        val_poly3 = p_poly3(ano)
        erro_reta = abs(real - val_reta)
        erro_poly3 = abs(real - val_poly3)
        
        print(f"{ano}\t{real:,}\t{val_reta:,.0f}\t{val_poly3:,.0f}\t{erro_reta:,.0f}\t{erro_poly3:,.0f}")
    
    # Erro médio quadrático (RMSE)
    rmse_reta = np.sqrt(np.mean((y - y_pred_reta) ** 2))
    rmse_poly3 = np.sqrt(np.mean((y - y_pred_poly3) ** 2))
    
    print(f"\nErro médio quadrático (RMSE):")
    print(f"Reta: {rmse_reta:,.0f} ton")
    print(f"Polinômio grau 3: {rmse_poly3:,.0f} ton")
    
    print(f"\nANÁLISE:")
    print(f"- R² da reta: {r2_reta:.4f}")
    print(f"- R² do polinômio grau 3: {r2_poly3:.4f}")
    
    if r2_poly3 > r2_reta:
        print("- O polinômio de grau 3 tem melhor ajuste (maior R²)")
    else:
        print("- A reta tem melhor ajuste (maior R²)")
    
    print(f"- RMSE da reta: {rmse_reta:,.0f} ton")
    print(f"- RMSE do polinômio grau 3: {rmse_poly3:,.0f} ton")
    
    if rmse_poly3 < rmse_reta:
        print("- O polinômio de grau 3 tem menor erro médio")
    else:
        print("- A reta tem menor erro médio")
    
    print(f"\nOBSERVAÇÕES:")
    print("- O polinômio de grau 3 tem mais parâmetros, mas pode ser mais instável")
    print("- A reta é mais simples e pode ser mais robusta para extrapolação")
    print("- Para escolher entre os modelos, considerar o contexto e objetivo")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Interpolação
    """
    print("MÉTODOS NUMÉRICOS - INTERPOLAÇÃO")
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
    print("EXECUÇÃO CONCLUÍDA!")
    print("Todos os exercícios de Interpolação foram resolvidos.")

if __name__ == "__main__":
    main()
