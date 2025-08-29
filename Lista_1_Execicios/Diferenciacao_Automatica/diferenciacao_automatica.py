"""
Métodos Numéricos - Diferenciação Automática
Solução dos exercícios da Lista 1
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# ============================================================================
# EXERCÍCIO 1: Diferenciação automática de função multivariável
# ============================================================================

class DualNumber:
    """
    Implementa números duais para diferenciação automática
    Um número dual tem a forma: a + b*ε, onde ε² = 0
    """
    def __init__(self, real, dual=0):
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real + other.real, self.dual + other.dual)
        else:
            return DualNumber(self.real + other, self.dual)
    
    def __sub__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real - other.real, self.dual - other.dual)
        else:
            return DualNumber(self.real - other, self.dual)
    
    def __mul__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real * other.real, 
                            self.real * other.dual + self.dual * other.real)
        else:
            return DualNumber(self.real * other, self.dual * other)
    
    def __truediv__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real / other.real,
                            (self.dual * other.real - self.real * other.dual) / (other.real ** 2))
        else:
            return DualNumber(self.real / other, self.dual / other)
    
    def __pow__(self, power):
        if isinstance(power, DualNumber):
            raise ValueError("Expoente não pode ser um número dual")
        return DualNumber(self.real ** power, 
                         power * (self.real ** (power - 1)) * self.dual)
    
    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        return DualNumber(other, 0) - self
    
    def __rmul__(self, other):
        return self * other
    
    def __rtruediv__(self, other):
        return DualNumber(other, 0) / self

def exercicio1():
    """
    Implementa diferenciação automática para função multivariável
    """
    print("=== EXERCÍCIO 1: DIFERENCIAÇÃO AUTOMÁTICA ===")
    
    # Função: f(x, y, z) = 3x²y/z + x(y - z)
    print("Função: f(x, y, z) = 3x²y/z + x(y - z)")
    print("Ponto de avaliação: (2, 3, 5)")
    
    # PARTE A: Decomposição em passos elementares
    print(f"\n--- PARTE A: DECOMPOSIÇÃO EM PASSOS ELEMENTARES ---")
    
    def f_decomposicao(x, y, z):
        """
        Decomposição da função em passos elementares
        """
        # Passo 1: t1 = x²
        t1 = x * x
        
        # Passo 2: t2 = 3 * t1
        t2 = 3 * t1
        
        # Passo 3: t3 = t2 * y
        t3 = t2 * y
        
        # Passo 4: t4 = t3 / z
        t4 = t3 / z
        
        # Passo 5: t5 = y - z
        t5 = y - z
        
        # Passo 6: t6 = x * t5
        t6 = x * t5
        
        # Passo 7: resultado = t4 + t6
        resultado = t4 + t6
        
        return resultado, {
            't1': t1, 't2': t2, 't3': t3, 't4': t4,
            't5': t5, 't6': t6, 'resultado': resultado
        }
    
    # Avaliar com valores reais
    x, y, z = 2, 3, 5
    resultado, passos = f_decomposicao(x, y, z)
    
    print("Decomposição da função:")
    print("t1 = x² = 2² = 4")
    print("t2 = 3 * t1 = 3 * 4 = 12")
    print("t3 = t2 * y = 12 * 3 = 36")
    print("t4 = t3 / z = 36 / 5 = 7.2")
    print("t5 = y - z = 3 - 5 = -2")
    print("t6 = x * t5 = 2 * (-2) = -4")
    print("resultado = t4 + t6 = 7.2 + (-4) = 3.2")
    
    print(f"\nResultado calculado: {resultado}")
    
    # PARTE B: Cálculo usando decomposição
    print(f"\n--- PARTE B: CÁLCULO f(2, 3, 5) ---")
    
    # Verificar cálculo direto
    f_direto = 3 * x**2 * y / z + x * (y - z)
    print(f"Cálculo direto: f(2, 3, 5) = 3*2²*3/5 + 2*(3-5) = 3*4*3/5 + 2*(-2) = 36/5 - 4 = 7.2 - 4 = 3.2")
    print(f"Resultado direto: {f_direto}")
    print(f"Resultado por decomposição: {resultado}")
    print(f"Verificação: {abs(f_direto - resultado) < 1e-10}")
    
    # PARTE C: Cálculo das derivadas parciais
    print(f"\n--- PARTE C: DERIVADAS PARCIAIS ---")
    
    def calcular_derivada_parcial(variavel, x, y, z):
        """
        Calcula derivada parcial usando diferenciação automática
        """
        if variavel == 'x':
            x_dual = DualNumber(x, 1)  # dx/dx = 1
            y_dual = DualNumber(y, 0)  # dy/dx = 0
            z_dual = DualNumber(z, 0)  # dz/dx = 0
        elif variavel == 'y':
            x_dual = DualNumber(x, 0)  # dx/dy = 0
            y_dual = DualNumber(y, 1)  # dy/dy = 1
            z_dual = DualNumber(z, 0)  # dz/dy = 0
        elif variavel == 'z':
            x_dual = DualNumber(x, 0)  # dx/dz = 0
            y_dual = DualNumber(y, 0)  # dy/dz = 0
            z_dual = DualNumber(z, 1)  # dz/dz = 1
        
        # Aplicar função com números duais
        t1 = x_dual * x_dual
        t2 = DualNumber(3, 0) * t1
        t3 = t2 * y_dual
        t4 = t3 / z_dual
        t5 = y_dual - z_dual
        t6 = x_dual * t5
        resultado = t4 + t6
        
        return resultado.dual
    
    # Calcular derivadas parciais
    df_dx = calcular_derivada_parcial('x', x, y, z)
    df_dy = calcular_derivada_parcial('y', x, y, z)
    df_dz = calcular_derivada_parcial('z', x, y, z)
    
    print(f"∂f/∂x = {df_dx}")
    print(f"∂f/∂y = {df_dy}")
    print(f"∂f/∂z = {df_dz}")
    
    # Verificar com cálculo manual
    print(f"\nVerificação manual:")
    print(f"f(x,y,z) = 3x²y/z + x(y-z)")
    print(f"∂f/∂x = 6xy/z + (y-z) = 6*2*3/5 + (3-5) = 36/5 - 2 = 7.2 - 2 = 5.2")
    print(f"∂f/∂y = 3x²/z + x = 3*4/5 + 2 = 12/5 + 2 = 2.4 + 2 = 4.4")
    print(f"∂f/∂z = -3x²y/z² - x = -3*4*3/25 - 2 = -36/25 - 2 = -1.44 - 2 = -3.44")
    
    print(f"\nComparação:")
    print(f"∂f/∂x: Automática = {df_dx}, Manual = 5.2, Diferença = {abs(df_dx - 5.2):.2e}")
    print(f"∂f/∂y: Automática = {df_dy}, Manual = 4.4, Diferença = {abs(df_dy - 4.4):.2e}")
    print(f"∂f/∂z: Automática = {df_dz}, Manual = -3.44, Diferença = {abs(df_dz - (-3.44)):.2e}")

def exercicio2():
    """
    Implementa aproximação de função usando derivada
    """
    print("=== EXERCÍCIO 2: APROXIMAÇÃO DE FUNÇÃO USANDO DERIVADA ===")
    
    # Função exemplo: f(x) = cos(x)
    # Derivada: f'(x) = -sin(x)
    
    def f(x):
        """Função original"""
        return math.cos(x)
    
    def df_dx(x):
        """Derivada da função"""
        return -math.sin(x)
    
    def aproximacao_linear(x, x0, f_x0, df_dx_x0):
        """
        Aproximação linear: f(x) ≈ f(x0) + f'(x0)(x - x0)
        """
        return f_x0 + df_dx_x0 * (x - x0)
    
    # Parâmetros
    x0 = 0  # Ponto inicial
    delta_x = 0.1  # Passo
    x_max = 5  # Valor máximo
    
    print(f"Função: f(x) = cos(x)")
    print(f"Derivada: f'(x) = -sin(x)")
    print(f"Ponto inicial: x0 = {x0}")
    print(f"Passo: Δx = {delta_x}")
    print(f"Intervalo: [0, {x_max}]")
    
    # Calcular valores
    print(f"\n--- CÁLCULO DOS VALORES ---")
    print("x\tf(x) real\tf(x) aproximado\tErro")
    print("-" * 50)
    
    valores_reais = []
    valores_aproximados = []
    pontos_x = []
    
    for i in range(int(x_max / delta_x) + 1):
        x = i * delta_x
        f_real = f(x)
        f_aprox = aproximacao_linear(x, x0, f(x0), df_dx(x0))
        erro = abs(f_real - f_aprox)
        
        valores_reais.append(f_real)
        valores_aproximados.append(f_aprox)
        pontos_x.append(x)
        
        print(f"{x:.1f}\t{f_real:.6f}\t{f_aprox:.6f}\t\t{erro:.6f}")
    
    # Análise dos resultados
    print(f"\n--- ANÁLISE DOS RESULTADOS ---")
    
    erro_max = max(abs(f_real - f_aprox) for f_real, f_aprox in zip(valores_reais, valores_aproximados))
    erro_medio = np.mean([abs(f_real - f_aprox) for f_real, f_aprox in zip(valores_reais, valores_aproximados)])
    
    print(f"Erro máximo: {erro_max:.6f}")
    print(f"Erro médio: {erro_medio:.6f}")
    
    # Observações
    print(f"\nOBSERVAÇÕES:")
    print("- A aproximação linear é boa próximo ao ponto x0 = 0")
    print("- O erro aumenta conforme nos afastamos do ponto de referência")
    print("- Esta é a base do método de Euler para EDOs")
    print("- A aproximação é uma reta tangente à função no ponto x0")

def main():
    """
    Executa todos os exercícios de Diferenciação Automática
    """
    print("MÉTODOS NUMÉRICOS - DIFERENCIAÇÃO AUTOMÁTICA")
    print("=" * 60)
    
    # Executar exercícios
    print("\n" + "="*60)
    exercicio1()
    
    print("\n" + "="*60)
    exercicio2()
    
    print("\n" + "="*60)
    print("EXECUÇÃO CONCLUÍDA!")
    print("Exercícios de Diferenciação Automática resolvidos.")

if __name__ == "__main__":
    main()
