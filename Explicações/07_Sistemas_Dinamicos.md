# Sistemas Dinâmicos

## Conceito
Sistemas dinâmicos descrevem como o estado de um sistema evolui ao longo do tempo. Frequentemente, são modelados por sistemas de Equações Diferenciais Ordinárias (EDOs).
Para resolver essas equações numericamente, utilizamos métodos como o de **Euler** ou **Runge-Kutta**.

O Método de Euler aproxima a derivada por uma diferença finita:
$$ \frac{dy}{dt} \approx \frac{y(t+\Delta t) - y(t)}{\Delta t} \implies y(t+\Delta t) \approx y(t) + f(t, y) \cdot \Delta t $$

## Exercício: Os Dois Tanques

**Problema:** Dois tanques interconectados trocam líquido contendo sal.
- Tanque A: volume $V_A$, quantidade de sal $x(t)$.
- Tanque B: volume $V_B$, quantidade de sal $y(t)$.
- Taxa de transferência A $\to$ B: $k_1$.
- Taxa de transferência B $\to$ A: $k_2$.

**Equações:**
$$
\begin{cases}
\frac{dx}{dt} = -k_1 x + k_2 y \\
\frac{dy}{dt} = k_1 x - k_2 y
\end{cases}
$$

**Simulação (Python):**
Com $x_0 = 100$, $y_0 = 0$, $k_1 = 0.1$, $k_2 = 0.05$.

```python
# Método de Euler
for i in range(steps - 1):
    dxdt = -k1 * x[i] + k2 * y[i]
    dydt = k1 * x[i] - k2 * y[i]
    
    x[i+1] = x[i] + dxdt * dt
    y[i+1] = y[i] + dydt * dt
```

**Resultados:**
Após 50 unidades de tempo:
- Tanque A: **33.37 kg**
- Tanque B: **66.63 kg**
O sistema tende ao equilíbrio onde as taxas de troca se igualam ($k_1 x = k_2 y \implies 0.1x = 0.05y \implies y = 2x$). Como $x+y=100$, temos $x \approx 33.3, y \approx 66.6$.

## Exercício: Epidemias (Modelo SIR)

**Problema:** Modelar a propagação de uma doença em uma população.
- **S**: Suscetíveis
- **I**: Infectados
- **R**: Recuperados

**Equações:**
$$
\begin{cases}
\frac{dS}{dt} = -\beta S I \\
\frac{dI}{dt} = \beta S I - \gamma I \\
\frac{dR}{dt} = \gamma I
\end{cases}
$$

**Simulação (Python):**
Com $\beta = 0.001$, $\gamma = 0.1$, População = 1000.

```python
# Método de Euler
for i in range(steps - 1):
    dSdt = -beta * S[i] * I[i]
    dIdt = beta * S[i] * I[i] - gamma * I[i]
    dRdt = gamma * I[i]
    
    S[i+1] = S[i] + dSdt * dt
    I[i+1] = I[i] + dIdt * dt
    R[i+1] = R[i] + dRdt * dt
```

**Resultados:**
- **Pico de infecção:** 677 pessoas infectadas simultaneamente em $t=7.9$.
- **Final:** Toda a população eventualmente foi infectada e se recuperou (S=0, I=0, R=1000), pois não houve intervenção ou imunidade inicial.
