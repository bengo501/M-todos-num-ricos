
import numpy as np
from scipy.linalg import lu

def exemplo_lu_parquinho():
    print("=== DEMONSTRAÇÃO: DECOMPOSIÇÃO LU (EXERCÍCIO 1: PARQUINHO) ===")
    
    # Matriz A do problema do parquinho
    # x1 = 20 + (1/3)x2 + (1/3)x4
    # x2 = (1/2)x1 + (1/2)x3
    # x3 = 10 + (1/3)x2 + (1/3)x4
    # x4 = (1/3)x2 + (1/3)x4
    
    # Reorganizando:
    # x1 - 1/3x2 - 1/3x4 = 20
    # -1/2x1 + x2 - 1/2x3 = 0
    # -1/3x2 + x3 - 1/3x4 = 10
    # -1/3x2 + 2/3x4 = 0  (Note: x4 - 1/3x4 = 2/3x4)
    
    A = np.array([
        [1, -1/3, 0, -1/3],
        [-1/2, 1, -1/2, 0],
        [0, -1/3, 1, -1/3],
        [0, -1/3, 0, 2/3]
    ])
    
    b = np.array([20, 0, 10, 0])
    
    print("Matriz A:")
    print(A)
    print("\nVetor b:")
    print(b)
    
    # Decomposição LU
    # A = P @ L @ U
    # P: Matriz de permutação
    # L: Matriz triangular inferior (Lower)
    # U: Matriz triangular superior (Upper)
    P, L, U = lu(A)
    
    print("\n--- Decomposição LU ---")
    print("Matriz P (Permutação):")
    print(P)
    print("\nMatriz L (Triangular Inferior):")
    print(L)
    print("\nMatriz U (Triangular Superior):")
    print(U)
    
    # Verificação: P @ L @ U deve ser igual a A
    A_reconstruida = P @ L @ U
    print("\nVerificação (P @ L @ U):")
    print(A_reconstruida)
    
    # Resolução do sistema usando LU
    # Ax = b  =>  P(LU)x = b  =>  LUx = P_inv @ b
    # 1. Resolver Ly = P_inv @ b (substituição para frente)
    # 2. Resolver Ux = y (substituição para trás)
    
    print("\n--- Resolução ---")
    
    # Ajustar b pela permutação
    # Como P é ortogonal/permutação, P_inv = P.T
    pb = P.T @ b
    print(f"Vetor b permutado (Pb): {pb}")
    
    # 1. Resolver Ly = Pb
    y = np.linalg.solve(L, pb)
    print(f"Solução intermediária y (Ly = Pb): {y}")
    
    # 2. Resolver Ux = y
    x = np.linalg.solve(U, y)
    print(f"Solução final x (Ux = y): {x}")
    
    print("\nInterpretação:")
    print(f"x1 (Brinquedo A): {x[0]:.2f}")
    print(f"x2 (Brinquedo B): {x[1]:.2f}")
    print(f"x3 (Brinquedo C): {x[2]:.2f}")
    print(f"x4 (Brinquedo D): {x[3]:.2f}")

if __name__ == "__main__":
    exemplo_lu_parquinho()
