# Otimização: 1D e Gradiente Descendente

## Conceito
A otimização visa encontrar o valor de $x$ que minimiza (ou maximiza) uma função objetiva $f(x)$.
Para funções diferenciáveis, o mínimo ocorre onde a derivada é zero: $f'(x) = 0$.

### Gradiente Descendente
É um método iterativo para encontrar o mínimo local de uma função. A ideia é dar passos na direção oposta ao gradiente (derivada).
A regra de atualização é:
$$ x_{novo} = x_{atual} - \alpha \cdot f'(x_{atual}) $$
Onde $\alpha$ é a **taxa de aprendizado** (learning rate), que controla o tamanho do passo.

## Exemplo Prático

**Função:** $f(x) = x^2 - 4x + 4$
**Derivada:** $f'(x) = 2x - 4$
**Mínimo Teórico:** $x = 2$ (onde $2x - 4 = 0$)

**Implementação em Python:**

```python
def f(x):
    return x**2 - 4*x + 4

def df(x):
    return 2*x - 4

learning_rate = 0.1
x = 0.0  # Chute inicial

print("Iteração\tx\t\tf(x)\t\tf'(x)")
for i in range(20):
    grad = df(x)
    x = x - learning_rate * grad
    print(f"{i+1}\t\t{x:.4f}\t{f(x):.4f}\t{grad:.4f}")
```

**Resultados (Primeiras Iterações):**
1. $x = 0.4000$, $f(x) = 2.5600$
2. $x = 0.7200$, $f(x) = 1.6384$
3. $x = 0.9760$, $f(x) = 1.0486$
...
20. $x \approx 1.9769$, $f(x) \approx 0.0005$

O algoritmo converge para $x=2$. Se a taxa de aprendizado for muito grande, o algoritmo pode oscilar ou divergir. Se for muito pequena, a convergência será lenta.
