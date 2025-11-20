# Cadeias de Markov

## Conceito
Uma Cadeia de Markov é um processo estocástico onde a probabilidade de transição para um estado futuro depende apenas do estado atual, e não da sequência de eventos que precederam (propriedade de Markov).

É definida por:
- Um conjunto de estados.
- Uma matriz de transição $P$, onde $P_{ij}$ é a probabilidade de ir do estado $i$ para o estado $j$.

### Estado Estacionário
Muitas cadeias de Markov atingem um equilíbrio a longo prazo, onde a distribuição de probabilidades não muda mais. Esse vetor $\pi$ satisfaz $\pi P = \pi$ e $\sum \pi_i = 1$.

### Estados Absorventes
São estados que, uma vez atingidos, não podem ser abandonados ($P_{ii} = 1$).

## Exercício 1: Pesquisa de Satisfação (Sorveteria)

**Problema:** Clientes respondem "Sim" ou "Não" sobre se gostam do sorvete.
- Se respondeu Sim: 70% chance de responder Sim na próxima, 30% Não.
- Se respondeu Não: 60% chance de responder Sim na próxima, 40% Não.

**Matriz de Transição:**
$$
P = \begin{bmatrix} 0.7 & 0.3 \\ 0.6 & 0.4 \end{bmatrix}
$$

**Resolução (Python):**
Para achar o estado estacionário, resolvemos o sistema linear derivado de $\pi P = \pi$.

```python
import numpy as np

P = np.array([[0.7, 0.3], [0.6, 0.4]])

# Sistema linear para estado estacionário: pi * P = pi  =>  pi * (P - I) = 0
# Com a restrição sum(pi) = 1
A = np.array([
    [P[0,0] - 1, P[1,0]],
    [1, 1]
])
b = np.array([0, 1])

pi = np.linalg.solve(A, b)
print(f"Sim: {pi[0]:.2%}, Não: {pi[1]:.2%}")
```

**Resultado:**
- Sim: **66.67%**
- Não: **33.33%**
A longo prazo, 2/3 dos clientes preferem o sorvete.

## Exercício 5: Jogo de Dados (Estados Absorventes)

**Problema:** Guilherme vence se tirar (5, 5). Christian vence se tirar (5, 6).
Estados:
1. **N5**: Último dado não foi 5.
2. **5**: Último dado foi 5.
3. **G**: Guilherme venceu (Absorvente).
4. **C**: Christian venceu (Absorvente).

**Matriz de Transição:**
$$
P = \begin{bmatrix} 
2/3 & 1/6 & 0 & 0 \\
2/3 & 0 & 1/6 & 1/6 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

**Resolução (Python):**
Usamos a matriz fundamental $N = (I - Q)^{-1}$ para calcular as probabilidades de absorção.

```python
# Matriz Q (transientes para transientes)
Q = np.array([[2/3, 1/6], [2/3, 0]])
# Matriz R (transientes para absorventes)
R = np.array([[0, 0], [1/6, 1/6]])

# Matriz Fundamental
I = np.eye(2)
N = np.linalg.inv(I - Q)

# Probabilidades de Absorção B = N * R
B = N @ R

print("Probabilidades de vitória começando de N5:")
print(f"Guilherme: {B[0,0]:.2%}, Christian: {B[0,1]:.2%}")
```

**Resultado:**
- Guilherme: **50.00%**
- Christian: **50.00%**
Apesar das regras parecerem diferentes, as probabilidades de vitória são iguais.
