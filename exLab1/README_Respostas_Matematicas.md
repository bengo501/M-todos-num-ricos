# Respostas Matemáticas Detalhadas - Métodos Numéricos

## 📐 Análise Matemática dos Exercícios

Este documento apresenta as soluções matemáticas detalhadas para cada exercício da lista, incluindo demonstrações, fórmulas e análises teóricas.

---

## **Exercício 1: Algoritmo de Precisão da Máquina**

### **Enunciado**
```c
double aux = 1.0;
while (1 + aux > 1) {
    print aux;
    aux = aux / 2;
}
```

### **Resposta Matemática**

#### **(a) O algoritmo termina? Por quê?**

**Sim, o algoritmo termina.** 

**Demonstração:**
- Seja ε a precisão da máquina (epsilon)
- O algoritmo termina quando `1 + aux ≤ 1` em aritmética de ponto flutuante
- Isso ocorre quando `aux ≤ ε/2`
- Como `aux` é dividido por 2 a cada iteração, após k iterações: `aux = 1/2^k`
- O algoritmo para quando `1/2^k ≤ ε/2`, ou seja, `k ≥ log₂(2/ε)`
- Como ε é finito, k é finito, garantindo a terminação

#### **(b) Significado do valor impresso na última linha**

O valor impresso é **aproximadamente ε/2**, onde ε é a precisão da máquina.

**Justificativa Matemática:**
- Seja `aux_final` o último valor impresso
- Temos: `1 + aux_final > 1` (última iteração que imprime)
- E: `1 + aux_final/2 ≤ 1` (próxima iteração não imprime)
- Portanto: `ε/2 < aux_final ≤ ε`
- Em prática: `aux_final ≈ ε/2`

**Fórmula:**
```
ε ≈ 2 × aux_final
```

---

## **Exercício 2: Cotas de Cauchy, Lagrange e Fujiwara**

### **Polinômio**
```
p(x) = 6x⁵ + 18x³ - 34x² - 493x + 1431
```

### **Respostas Matemáticas**

#### **Cota de Cauchy**
**Fórmula:** `|r| ≤ 1 + max{|a₀|, |a₁|, ..., |a_{n-1}|}/|a_n|`

**Cálculo:**
- `a₅ = 6`, `a₄ = 0`, `a₃ = 18`, `a₂ = -34`, `a₁ = -493`, `a₀ = 1431`
- `max{|a₀|, |a₁|, |a₂|, |a₃|, |a₄|} = max{1431, 493, 34, 18, 0} = 1431`
- **Cota de Cauchy:** `|r| ≤ 1 + 1431/6 = 239.5`

#### **Cota de Lagrange**
**Fórmula:** `|r| ≤ max{1, (|a₀| + |a₁| + ... + |a_{n-1}|)/|a_n|}`

**Cálculo:**
- `|a₀| + |a₁| + |a₂| + |a₃| + |a₄| = 1431 + 493 + 34 + 18 + 0 = 1976`
- **Cota de Lagrange:** `|r| ≤ max{1, 1976/6} = 329.33`

#### **Cota de Fujiwara**
**Fórmula:** `|r| ≤ 2 × max{|a_{n-1}/a_n|, √|a_{n-2}/a_n|, ∛|a_{n-3}/a_n|, ..., ⁿ√|a₀/a_n|}`

**Cálculo:**
- `|a₄/a₅| = 0/6 = 0`
- `√|a₃/a₅| = √(18/6) = √3 ≈ 1.732`
- `∛|a₂/a₅| = ∛(34/6) ≈ 1.78`
- `⁴√|a₁/a₅| = ⁴√(493/6) ≈ 2.84`
- `⁵√|a₀/a₅| = ⁵√(1431/6) ≈ 3.12`
- **Cota de Fujiwara:** `|r| ≤ 2 × 3.12 = 6.24`

**Comparação:** Fujiwara é mais precisa (6.24) que Lagrange (329.33) e Cauchy (239.5).

---

## **Exercício 3: Polinômio com Raízes 2, 3, 4**

### **Construção do Polinômio**
**Fórmula:** `p(x) = (x - r₁)(x - r₂)(x - r₃)`

**Desenvolvimento:**
```
p(x) = (x - 2)(x - 3)(x - 4)
     = (x² - 5x + 6)(x - 4)
     = x³ - 4x² - 5x² + 20x + 6x - 24
     = x³ - 9x² + 26x - 24
```

### **Aplicação do Método da Bissecção**

**Teorema da Bissecção:** Se f é contínua em [a,b] e f(a) × f(b) < 0, então existe r ∈ (a,b) tal que f(r) = 0.

**Análise no intervalo [1,5]:**
- `f(1) = 1 - 9 + 26 - 24 = -6`
- `f(5) = 125 - 225 + 130 - 24 = 6`
- Como `f(1) × f(5) < 0`, existe pelo menos uma raiz em [1,5]

**Convergência:** O método encontra uma raiz (não necessariamente todas) com precisão ε em aproximadamente `log₂((b-a)/ε)` iterações.

---

## **Exercício 4: Polinômio com Raízes 2, 3, 4, 5**

### **Construção do Polinômio**
```
p(x) = (x - 2)(x - 3)(x - 4)(x - 5)
     = x⁴ - 14x³ + 71x² - 154x + 120
```

### **Problema com Múltiplas Raízes**

**Análise no intervalo [1,6]:**
- `f(1) = 1 - 14 + 71 - 154 + 120 = 24`
- `f(6) = 1296 - 3024 + 2556 - 924 + 120 = 24`
- Como `f(1) = f(6)`, o método da bissecção pode não funcionar

**Solução Adaptativa:**
1. **Método de Sturm:** Contar raízes em intervalos
2. **Método de Newton:** Para raízes simples
3. **Deflação:** Remover raízes encontradas e continuar

---

## **Exercício 5: Método de Newton para Raiz Quadrada**

### **Formulação Matemática**
Para encontrar √p, resolver: `f(x) = x² - p = 0`

**Iteração de Newton:**
```
x_{n+1} = x_n - f(x_n)/f'(x_n)
        = x_n - (x_n² - p)/(2x_n)
        = x_n - x_n/2 + p/(2x_n)
        = (x_n + p/x_n)/2
```

### **Análise de Convergência**
- **Ordem de convergência:** Quadrática
- **Condição de convergência:** x₀ > 0
- **Erro:** `|x_{n+1} - √p| ≤ C|x_n - √p|²`

---

## **Exercício 6: Método de Newton para Raiz Cúbica**

### **Formulação Matemática**
Para encontrar ³√p, resolver: `f(x) = x³ - p = 0`

**Iteração de Newton:**
```
x_{n+1} = x_n - f(x_n)/f'(x_n)
        = x_n - (x_n³ - p)/(3x_n²)
        = x_n - x_n/3 + p/(3x_n²)
        = (2x_n + p/x_n²)/3
```

### **Análise de Convergência**
- **Ordem de convergência:** Quadrática
- **Condição de convergência:** x₀ ≠ 0
- **Estabilidade:** Melhor que métodos de potência

---

## **Exercício 7: Manipulação de Função**

### **Problema**
Encontrar raízes de `f(x) = 8x⁴ - 238x³ + 1047x² - 953x + 154` no intervalo [-1,1].

### **Solução Matemática**
**Transformação:** `g(x) = f(1/x)`

**Desenvolvimento:**
```
g(x) = 8(1/x)⁴ - 238(1/x)³ + 1047(1/x)² - 953(1/x) + 154
     = 8/x⁴ - 238/x³ + 1047/x² - 953/x + 154
     = (8 - 238x + 1047x² - 953x³ + 154x⁴)/x⁴
     = (154x⁴ - 953x³ + 1047x² - 238x + 8)/x⁴
```

**Relação:** Se r é raiz de g(x), então 1/r é raiz de f(x).

---

## **Exercício 8: Método de Horner**

### **Algoritmo**
```c
void metodo(double x) {
    double a[] = {1, 0, 18, 34, -493, 1431};
    double p = 0;
    for (int i = 0; i < tamanho(a); i++) {
        p = x * p + a[i];
    }
    imprime(x, p);
}
```

### **Análise Matemática**
**Polinômio:** `p(x) = x⁵ + 18x³ + 34x² - 493x + 1431`

**Método de Horner:**
```
p(x) = ((((x + 0)x + 18)x + 34)x - 493)x + 1431
```

**Complexidade:** O(n) multiplicações e adições
**Vantagem:** Minimiza erros de arredondamento

---

## **Exercício 9: Método da Secante**

### **Formulação Matemática**
**Iteração:**
```
x_{n+1} = x_n - f(x_n) × (x_n - x_{n-1})/(f(x_n) - f(x_{n-1}))
```

### **Análise de Convergência**
- **Ordem de convergência:** ≈ 1.618 (número áureo)
- **Vantagem:** Não requer cálculo de derivada
- **Desvantagem:** Mais lento que Newton

### **Número de Raízes Reais**
**Regra de Descartes:** Número de mudanças de sinal em f(x) e f(-x) fornece limite superior para raízes reais positivas e negativas.

---

## **Exercício 10: Método de Horner Modificado**

### **Algoritmo**
```c
void metodo(double x) {
    double a[] = {1, 0, 18, 34, -493, 1431};
    double p = 0, q = 0;
    for (int i = 0; i < tamanho(a); i++) {
        q = x * q + p;
        p = x * p + a[i];
    }
    imprime(x, p, q);
}
```

### **Análise Matemática**
**Saída:**
- `p = p(x)` (valor do polinômio)
- `q = p'(x)` (valor da derivada)

**Demonstração:**
Se `p(x) = a₀ + a₁x + a₂x² + ... + aₙxⁿ`, então:
- `p'(x) = a₁ + 2a₂x + 3a₃x² + ... + naₙx^{n-1}`

**Aplicação:** Método de Newton com uma única passagem pelo polinômio.

---

## **Exercício 11: Newton-Raphson Complexo**

### **Extensão para ℂ**
**Iteração:** `z_{n+1} = z_n - f(z_n)/f'(z_n)`

### **Análise de Convergência**
- **Condição de convergência:** |f'(z₀)| ≠ 0
- **Bacias de atração:** Regiões que convergem para cada raiz
- **Fronteiras fractais:** Entre bacias de atração

### **Implementação**
```python
def newton_complexo(z, f, f_prime, tol=1e-10, max_iter=100):
    for i in range(max_iter):
        z_new = z - f(z)/f_prime(z)
        if abs(z_new - z) < tol:
            return z_new
        z = z_new
    return z
```

---

## **Exercício 12: Fractais de Newton**

### **Conceito Matemático**
**Conjunto de Julia:** Para cada ponto inicial z₀, determinar para qual raiz o método de Newton converge.

### **Algoritmo de Colorização**
1. **Discretização:** Grade no plano complexo
2. **Iteração:** Aplicar Newton-Raphson
3. **Classificação:** Identificar raiz de convergência
4. **Colorização:** Cor baseada na raiz encontrada

### **Análise Matemática**
**Bacias de Atração:**
- Para cada raiz rᵢ, existe uma região Bᵢ tal que z₀ ∈ Bᵢ ⇒ lim zₙ = rᵢ
- As fronteiras entre Bᵢ são fractais
- **Dimensão fractal:** ≈ 1.5 para polinômios genéricos

### **Implementação**
```python
def newton_fractal(poly, roots, x_range, y_range, resolution):
    colors = []
    for x in np.linspace(x_range[0], x_range[1], resolution):
        for y in np.linspace(y_range[0], y_range[1], resolution):
            z = complex(x, y)
            root = newton_complexo(z, poly, poly.deriv())
            color = find_closest_root(root, roots)
            colors.append(color)
    return colors
```

---

## **📊 Resumo das Fórmulas Principais**

### **Métodos Iterativos**
| Método | Iteração | Ordem de Convergência |
|--------|----------|----------------------|
| Bissecção | `c = (a+b)/2` | Linear (1) |
| Newton | `x_{n+1} = x_n - f(x_n)/f'(x_n)` | Quadrática (2) |
| Secante | `x_{n+1} = x_n - f(x_n)(x_n-x_{n-1})/(f(x_n)-f(x_{n-1}))` | ≈1.618 |

### **Cotas de Raízes**
| Cota | Fórmula | Precisão |
|------|---------|----------|
| Cauchy | `|r| ≤ 1 + max{|aᵢ|}/|aₙ|` | Moderada |
| Lagrange | `|r| ≤ max{1, Σ|aᵢ|/|aₙ|}` | Moderada |
| Fujiwara | `|r| ≤ 2×max{ⁱ√|a_{n-i}/aₙ|}` | Alta |

### **Complexidade Computacional**
| Algoritmo | Complexidade | Observações |
|-----------|--------------|-------------|
| Horner | O(n) | Ótimo para avaliação |
| Newton | O(n) por iteração | Convergência rápida |
| Bissecção | O(log(1/ε)) | Robusto mas lento |

---

## **🔬 Considerações Teóricas Avançadas**

### **Estabilidade Numérica**
- **Cancelamento catastrófico:** Evitar subtrações de números próximos
- **Overflow/Underflow:** Monitorar crescimento de valores
- **Condicionamento:** Sensibilidade a perturbações nos dados

### **Convergência Global vs Local**
- **Newton:** Convergência local (próximo à raiz)
- **Bissecção:** Convergência global (qualquer intervalo)
- **Híbridos:** Combinar robustez com velocidade

### **Análise de Erro**
- **Erro de truncamento:** Devido à discretização
- **Erro de arredondamento:** Devido à precisão finita
- **Propagação de erro:** Como erros se acumulam

---

**Nota:** Estas soluções matemáticas fornecem a base teórica para implementações computacionais eficientes e robustas dos métodos numéricos apresentados.
