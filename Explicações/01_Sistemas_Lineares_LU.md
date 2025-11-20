# Sistemas Lineares: Decomposição LU

## Conceito
A Decomposição LU é um método para resolver sistemas de equações lineares da forma $Ax = b$. A ideia principal é fatorar a matriz $A$ em duas matrizes triangulares:
- **L (Lower)**: Matriz triangular inferior (elementos acima da diagonal principal são zero).
- **U (Upper)**: Matriz triangular superior (elementos abaixo da diagonal principal são zero).

Assim, $A = LU$. O sistema original $Ax = b$ torna-se $LUx = b$.
Para resolver, fazemos em duas etapas:
1.  Resolvemos $Ly = b$ para encontrar $y$ (substituição para frente).
2.  Resolvemos $Ux = y$ para encontrar $x$ (substituição para trás).

Frequentemente, usa-se uma matriz de permutação $P$ para garantir estabilidade numérica (pivoteamento), resultando em $PA = LU$.

## Exercício: O Problema do Parquinho
(Baseado no Exercício 1 da Lista 1)

Um parquinho tem 4 brinquedos (A, B, C, D). O fluxo de pessoas entre eles é descrito por um sistema linear.
Após modelar o problema, chegamos ao seguinte sistema:

$$
\begin{cases}
x_1 - \frac{1}{3}x_2 - \frac{1}{3}x_4 = 20 \\
-\frac{1}{2}x_1 + x_2 - \frac{1}{2}x_3 = 0 \\
-\frac{1}{3}x_2 + x_3 - \frac{1}{3}x_4 = 10 \\
-\frac{1}{3}x_2 + \frac{2}{3}x_4 = 0
\end{cases}
$$

Onde $x_1, x_2, x_3, x_4$ representam o número de pessoas nos brinquedos A, B, C e D.

## Resolução com Python (Scipy)

Utilizamos a função `lu` do pacote `scipy.linalg` para obter as matrizes $P, L, U$.

```python
import numpy as np
from scipy.linalg import lu

# Matriz dos coeficientes
A = np.array([
    [1, -1/3, 0, -1/3],
    [-1/2, 1, -1/2, 0],
    [0, -1/3, 1, -1/3],
    [0, -1/3, 0, 2/3]
])

# Vetor dos termos independentes
b = np.array([20, 0, 10, 0])

# Decomposição LU
P, L, U = lu(A)

print("Matriz L:\n", L)
print("Matriz U:\n", U)

# Resolução
# 1. Ajustar b pela permutação P
pb = P.T @ b
# 2. Resolver Ly = Pb
y = np.linalg.solve(L, pb)
# 3. Resolver Ux = y
x = np.linalg.solve(U, y)

print("\nSolução x:", x)
```

## Resultados Obtidos

Ao executar o código, obtemos:

**Matriz L (Triangular Inferior):**
```
[[ 1.    0.    0.    0.  ]
 [-0.5   1.    0.    0.  ]
 [ 0.   -0.4   1.    0.  ]
 [ 0.   -0.4  -0.25  1.  ]]
```

**Matriz U (Triangular Superior):**
```
[[ 1.         -0.33333333  0.         -0.33333333]
 [ 0.          0.83333333 -0.5        -0.16666667]
 [ 0.          0.          0.8        -0.4       ]
 [ 0.          0.          0.          0.5       ]]
```

**Solução Final:**
- $x_1$ (Brinquedo A): **35 pessoas**
- $x_2$ (Brinquedo B): **30 pessoas**
- $x_3$ (Brinquedo C): **25 pessoas**
- $x_4$ (Brinquedo D): **15 pessoas**

Isso confirma que o fluxo total de entrada (20 + 10 = 30 pessoas/hora) é consistente com a distribuição estacionária no parque.
