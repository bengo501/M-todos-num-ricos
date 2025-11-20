# Diferenciação Automática Progressiva

## Conceito
A Diferenciação Automática (AD) é uma técnica para calcular derivadas de funções computacionais com precisão de máquina, sem usar diferenças finitas (que têm erros de arredondamento) nem cálculo simbólico (que pode ser lento e complexo).

### Modo Progressivo (Forward Mode)
No modo progressivo, calculamos o valor da função e sua derivada simultaneamente, percorrendo o grafo computacional da entrada para a saída.
Isso é frequentemente implementado usando **Números Duais**.

### Números Duais
Um número dual tem a forma $z = a + b\epsilon$, onde $\epsilon^2 = 0$.
- A parte real $a$ armazena o valor da função.
- A parte dual $b$ armazena o valor da derivada.

Propriedades:
- Soma: $(a + b\epsilon) + (c + d\epsilon) = (a+c) + (b+d)\epsilon$
- Produto: $(a + b\epsilon)(c + d\epsilon) = ac + (ad + bc)\epsilon$ (pois $\epsilon^2=0$)
- Regra da Cadeia: $f(a + b\epsilon) = f(a) + f'(a)b\epsilon$

## Exercício: Derivadas Parciais

**Função:** $f(x, y, z) = \frac{3x^2y}{z} + x(y - z)$
**Ponto:** $(2, 3, 5)$

**Implementação em Python (Números Duais):**

```python
class DualNumber:
    def __init__(self, real, dual=0):
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real + other.real, self.dual + other.dual)
        return DualNumber(self.real + other, self.dual)
    
    def __mul__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real * other.real, 
                            self.real * other.dual + self.dual * other.real)
        return DualNumber(self.real * other, self.dual * other)
    
    # ... (outras operações como sub, div, pow)

def f(x, y, z):
    return 3 * x**2 * y / z + x * (y - z)

# Para calcular df/dx:
# x é dual com parte dual 1 (dx/dx = 1)
# y, z são duais com parte dual 0 (dy/dx = 0, dz/dx = 0)
x = DualNumber(2, 1)
y = DualNumber(3, 0)
z = DualNumber(5, 0)

resultado = f(x, y, z)
print(f"Valor: {resultado.real}")
print(f"Derivada (df/dx): {resultado.dual}")
```

**Resultados:**
- Valor da função: **3.2**
- $\partial f/\partial x$: **5.2**
- $\partial f/\partial y$: **4.4**
- $\partial f/\partial z$: **-3.44**

Os resultados coincidem exatamente com o cálculo analítico manual, demonstrando a precisão do método.
