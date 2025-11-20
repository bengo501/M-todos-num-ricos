# Interpolação Polinomial

## Conceito
A interpolação polinomial consiste em encontrar um polinômio de grau $n$ (ou menor) que passe exatamente por $n+1$ pontos dados $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$.

### Polinômio de Lagrange
É construído como uma combinação linear de polinômios de base $L_k(x)$:
$$ P(x) = \sum_{k=0}^{n} y_k L_k(x) $$
Onde $L_k(x)$ vale 1 em $x_k$ e 0 nos outros pontos.

### Polinômio de Newton
Utiliza diferenças divididas para construir o polinômio de forma incremental:
$$ P(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \dots $$
Onde os coeficientes $a_i$ são calculados pela tabela de diferenças divididas.

## Exercício 2: Interpolação de Newton (Três Cientistas)

**Problema:** Três cientistas (Ana, Beto, Carol) interpolam os mesmos dados, mas em ordens diferentes. O polinômio resultante é o mesmo?

**Dados:**
$x = [1, 3, 5, 7]$
$y = [2, 5, 4, 8]$

**Resolução (Python):**
Implementamos o método de Newton com diferenças divididas.

```python
def interpolacao_newton(x, y):
    n = len(x)
    dd = np.zeros((n, n))
    dd[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            dd[i, j] = (dd[i+1, j-1] - dd[i, j-1]) / (x[i+j] - x[i])
            
    # Função do polinômio
    def p(x_val):
        result = dd[0, 0]
        for i in range(1, n):
            term = dd[0, i]
            for j in range(i):
                term *= (x_val - x[j])
            result += term
        return result
    
    return p
```

**Resultado:**
Ao testar com diferentes ordens de pontos (Crescente, Decrescente, Aleatória), verificamos que **todos os polinômios são idênticos**.
A interpolação polinomial é única para um conjunto de pontos, independentemente da ordem ou do método (Newton ou Lagrange) utilizado.

## Exercício 3: Produção Chinesa de Aço (Lagrange)

**Problema:** Prever a produção de aço em 1996 usando dados de 1990 a 1995.

**Dados (Treino):**
Anos: 1990-1995
Produção: [62.4, 67.7, 75.9, 87.4, 97.4, 105.3]

**Resolução (Python):**
Usamos `scipy.interpolate.lagrange`.

```python
from scipy.interpolate import lagrange

anos = [1990, 1991, 1992, 1993, 1994, 1995]
producao = [62.4, 67.7, 75.9, 87.4, 97.4, 105.3]

p = lagrange(anos, producao)
previsao_1996 = p(1996)

print(f"Previsão 1996: {previsao_1996:.2f}")
```

**Resultado:**
A previsão por interpolação polinomial (extrapolação, neste caso) pode divergir significativamente da realidade se o grau do polinômio for alto (Fenômeno de Runge nas bordas).
No exercício, comparamos com o valor real para avaliar o erro.
