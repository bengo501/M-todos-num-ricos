# Mínimos Quadrados

## Conceito
O método dos Mínimos Quadrados é utilizado para resolver sistemas sobredeterminados, ou seja, sistemas que possuem mais equações do que incógnitas ($m > n$). Nesses casos, geralmente não existe uma solução exata que satisfaça todas as equações simultaneamente.

O objetivo é encontrar um vetor $x$ que minimize a norma do resíduo $r = Ax - b$:
$$ \min_x ||Ax - b||^2 $$

A solução analítica é dada pelas Equações Normais:
$$ A^T Ax = A^T b $$

No Python (NumPy), utilizamos `np.linalg.lstsq`, que é numericamente mais estável do que calcular a inversa de $A^T A$.

## Exercício: Análise Química (Lista 1, Exercício 5)

**Problema:** Determinar a composição de um composto X a partir de 4 substâncias (A, B, C, D), sabendo as proporções de componentes (a, b, c, d) em cada uma.
Como há incertezas e substâncias desconhecidas, as proporções não somam 100% e o sistema é sobredeterminado (ou inconsistente para uma solução exata).

**Dados:**
- Matriz $A$ (Proporções dos componentes nas substâncias A, B, C, D).
- Vetor $b$ (Proporções dos componentes no composto X).

$$
A = \begin{bmatrix} 
15 & 36 & 20 & 31 \\ 
28 & 11 & 15 & 22 \\ 
27 & 36 & 33 & 24 \\ 
30 & 17 & 32 & 23 
\end{bmatrix}, \quad
b = \begin{bmatrix} 24.3 \\ 15.0 \\ 26.2 \\ 21.5 \end{bmatrix}
$$

**Resolução com Python:**

```python
import numpy as np

# Matriz dos coeficientes (Componentes x Substâncias)
A = np.array([
    [15, 36, 20, 31],
    [28, 11, 15, 22],
    [27, 36, 33, 24],
    [30, 17, 32, 23]
])

# Vetor dos resultados observados em X
b = np.array([24.3, 15.0, 26.2, 21.5])

# Resolver usando Mínimos Quadrados
# rcond=None deixa o numpy decidir o cutoff para valores singulares pequenos
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print("Proporções estimadas (A, B, C, D):")
print(x)

print(f"\nResíduo total (erro quadrático): {residuals[0]:.4f}")
```

**Interpretação:**
O vetor $x$ nos dá a "melhor" combinação possível de A, B, C e D que explica a composição de X, minimizando o erro quadrático total entre o esperado e o observado.

Se o resíduo for alto, significa que o modelo (mistura apenas de A, B, C, D) não explica bem a composição de X, sugerindo a presença de outras substâncias ou erros de medição significativos.
