
import numpy as np
import matplotlib.pyplot as plt

def exemplo_gradiente_descendente():
    print("=== DEMONSTRAÇÃO: OTIMIZAÇÃO 1D E GRADIENTE DESCENDENTE ===")
    
    # Função objetivo: f(x) = x^2 - 4x + 4  (Mínimo em x=2)
    # Derivada: f'(x) = 2x - 4
    
    def f(x):
        return x**2 - 4*x + 4
    
    def df(x):
        return 2*x - 4
    
    print("Função: f(x) = x² - 4x + 4")
    print("Derivada: f'(x) = 2x - 4")
    print("Objetivo: Encontrar x que minimiza f(x)")
    
    # Parâmetros do Gradiente Descendente
    learning_rate = 0.1  # Taxa de aprendizado (alpha)
    max_iter = 20
    x_inicial = 0.0  # Começar em x=0
    
    print(f"\nParâmetros:")
    print(f"Taxa de aprendizado: {learning_rate}")
    print(f"Chute inicial: {x_inicial}")
    
    # Algoritmo
    x = x_inicial
    historico = [(0, x, f(x))]
    
    print(f"\nIterações:")
    print("i\tx\t\tf(x)\t\tf'(x)\t\tNovo x")
    print("-" * 70)
    
    for i in range(max_iter):
        grad = df(x)
        x_novo = x - learning_rate * grad
        
        print(f"{i+1}\t{x:.6f}\t{f(x):.6f}\t{grad:.6f}\t{x_novo:.6f}")
        
        x = x_novo
        historico.append((i+1, x, f(x)))
        
        # Critério de parada (gradiente próximo de zero)
        if abs(grad) < 1e-6:
            print(f"\nConvergência alcançada na iteração {i+1}!")
            break
            
    print(f"\nMínimo encontrado: x = {x:.6f}")
    print(f"Valor mínimo: f(x) = {f(x):.6f}")
    print(f"Valor exato: x = 2.0, f(x) = 0.0")

if __name__ == "__main__":
    exemplo_gradiente_descendente()
