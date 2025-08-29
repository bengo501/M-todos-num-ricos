# Respostas Matemáticas Detalhadas - Cadeias de Markov

## 📐 Análise Matemática dos Exercícios

Este documento apresenta as soluções matemáticas detalhadas para cada exercício da lista de Cadeias de Markov, incluindo modelagem, cálculo de probabilidades e análise de comportamento assintótico.

---

## **Exercício 1: Pesquisa de Opinião - Sorveteria**

### **Enunciado**
Análise de mudança de opinião sobre sorvete de chocolate em duas pesquisas consecutivas.

### **Modelagem Matemática**

#### **Estados**
- **Estado 0**: Opinião "Sim" (sorvete é melhor)
- **Estado 1**: Opinião "Não" (sorvete não é melhor)

#### **Matriz de Transição**
```
P = [0.70  0.30]
    [0.60  0.40]
```

**Interpretação:**
- P₀₀ = 0.70: Probabilidade de manter opinião "Sim"
- P₀₁ = 0.30: Probabilidade de mudar de "Sim" para "Não"
- P₁₀ = 0.60: Probabilidade de mudar de "Não" para "Sim"
- P₁₁ = 0.40: Probabilidade de manter opinião "Não"

#### **Cálculo da Distribuição Inicial**
```
π₀ = [1000, 0]  # Todos começam com opinião "Sim"
```

#### **Distribuição Após 4 Visitas**
```
π₄ = π₀ × P⁴
```

**Cálculo de P⁴:**
```
P² = [0.70  0.30] × [0.70  0.30] = [0.67  0.33]
     [0.60  0.40]   [0.60  0.40]   [0.66  0.34]

P⁴ = P² × P² = [0.667  0.333]
                [0.666  0.334]
```

**Resultado:**
```
π₄ = [1000, 0] × [0.667  0.333] = [667, 333]
                    [0.666  0.334]
```

**Resposta:** Após 4 visitas, 667 clientes acharão que o sorvete é melhor.

#### **Estado Estacionário**
**Cálculo via autovetores:**
```
P × π = π
[0.70  0.30] [π₀] = [π₀]
[0.60  0.40] [π₁]   [π₁]
```

**Sistema de equações:**
```
0.70π₀ + 0.60π₁ = π₀
0.30π₀ + 0.40π₁ = π₁
π₀ + π₁ = 1
```

**Solução:**
```
π₀ = 2/3 ≈ 0.667
π₁ = 1/3 ≈ 0.333
```

**Resposta:** A longo prazo, 2/3 dos clientes acharão que o sorvete é melhor.

---

## **Exercício 2: Migração de Torcedores**

### **Enunciado**
Análise de migração entre três times de futebol com probabilidades de transição específicas.

### **Modelagem Matemática**

#### **Estados**
- **Estado 0**: Trêmio
- **Estado 1**: Internacional
- **Estado 2**: Cassis

#### **Matriz de Transição**
```
P = [0.78  0.12  0.10]  # Trêmio
    [0.07  0.85  0.08]  # Internacional
    [0.11  0.09  0.80]  # Cassis
```

**Cálculo das probabilidades diagonais:**
- P₀₀ = 1 - 0.12 - 0.10 = 0.78
- P₁₁ = 1 - 0.07 - 0.08 = 0.85
- P₂₂ = 1 - 0.11 - 0.09 = 0.80

#### **Distribuição Inicial**
```
π₀ = [10000, 11000, 6000]
```

#### **Evolução Temporal**
```
πₜ₊₁ = πₜ × P
```

**Cálculo ano a ano:**
```
π₁ = [10000, 11000, 6000] × [0.78  0.12  0.10]
                            [0.07  0.85  0.08]
                            [0.11  0.09  0.80]
   = [10000×0.78 + 11000×0.07 + 6000×0.11,
      10000×0.12 + 11000×0.85 + 6000×0.09,
      10000×0.10 + 11000×0.08 + 6000×0.80]
   = [7800 + 770 + 660, 1200 + 9350 + 540, 1000 + 880 + 4800]
   = [9230, 11090, 6680]
```

#### **Estado Estacionário**
**Solução do sistema:**
```
π₀ = 0.78π₀ + 0.07π₁ + 0.11π₂
π₁ = 0.12π₀ + 0.85π₁ + 0.09π₂
π₂ = 0.10π₀ + 0.08π₁ + 0.80π₂
π₀ + π₁ + π₂ = 1
```

**Solução numérica:**
```
π ≈ [0.333, 0.444, 0.223]
```

**Resposta:** A longo prazo, as torcidas se estabilizarão em aproximadamente 33.3%, 44.4% e 22.3% para Trêmio, Internacional e Cassis, respectivamente.

---

## **Exercício 3: Lobo Guará - Regiões de Caça**

### **Enunciado**
Análise do movimento de um lobo guará entre três regiões de caça com regras específicas.

### **Modelagem Matemática**

#### **Estados**
- **Estado 0**: Região A
- **Estado 1**: Região B
- **Estado 2**: Região C

#### **Matriz de Transição**
```
P = [0.50  0.00  0.50]  # Região A
    [0.25  0.50  0.25]  # Região B
    [0.25  0.25  0.50]  # Região C
```

**Justificativa:**
- **A → A**: 50% (probabilidade de repetir)
- **A → B**: 0% (não caça em B se caçou em A)
- **A → C**: 50% (probabilidade restante)
- **B → A**: 25% (50% de escolher entre A e C)
- **B → B**: 50% (probabilidade de repetir)
- **B → C**: 25% (50% de escolher entre A e C)
- **C → A**: 25% (50% de escolher entre A e B)
- **C → B**: 25% (50% de escolher entre A e B)
- **C → C**: 50% (probabilidade de repetir)

#### **Probabilidade de Caçar em C na Quarta-feira**
**Condição inicial:** Segunda-feira em A
**Tempo:** 2 dias (terça e quarta)

```
π₀ = [1, 0, 0]  # Começa em A
π₂ = π₀ × P²
```

**Cálculo de P²:**
```
P² = [0.50  0.00  0.50] × [0.50  0.00  0.50]
     [0.25  0.50  0.25]   [0.25  0.50  0.25]
     [0.25  0.25  0.50]   [0.25  0.25  0.50]

   = [0.375  0.125  0.500]
     [0.250  0.375  0.375]
     [0.250  0.250  0.500]
```

**Resultado:**
```
π₂ = [1, 0, 0] × [0.375  0.125  0.500]
                  [0.250  0.375  0.375]
                  [0.250  0.250  0.500]
   = [0.375, 0.125, 0.500]
```

**Resposta:** Probabilidade de caçar em C na quarta-feira = 0.500 (50%).

#### **Distribuição de Longo Prazo**
**Estado estacionário:**
```
π₀ = 0.50π₀ + 0.25π₁ + 0.25π₂
π₁ = 0.00π₀ + 0.50π₁ + 0.25π₂
π₂ = 0.50π₀ + 0.25π₁ + 0.50π₂
π₀ + π₁ + π₂ = 1
```

**Solução:**
```
π ≈ [0.400, 0.200, 0.400]
```

**Resposta:** A longo prazo, o lobo caçará 40% das vezes em A, 20% em B e 40% em C.

---

## **Exercício 4: Mobilidade Social**

### **Enunciado**
Análise de mobilidade social entre classes Ricas, Médias e Pobres com transições geracionais.

### **Modelagem Matemática**

#### **Estados**
- **Estado 0**: Ricos
- **Estado 1**: Médios
- **Estado 2**: Pobres

#### **Matriz de Transição Original**
```
P = [0.70  0.20  0.10]  # Ricos
    [0.15  0.70  0.15]  # Médios
    [0.10  0.30  0.60]  # Pobres
```

#### **Probabilidade de Netos Ricos (2 gerações)**
**Condição inicial:** Pobre
```
π₀ = [0, 0, 1]  # Começa pobre
π₂ = π₀ × P²
```

**Cálculo de P²:**
```
P² = [0.70  0.20  0.10] × [0.70  0.20  0.10]
     [0.15  0.70  0.15]   [0.15  0.70  0.15]
     [0.10  0.30  0.60]   [0.10  0.30  0.60]

   = [0.515  0.320  0.165]
     [0.175  0.545  0.280]
     [0.145  0.380  0.475]
```

**Resultado:**
```
π₂ = [0, 0, 1] × [0.515  0.320  0.165]
                  [0.175  0.545  0.280]
                  [0.145  0.380  0.475]
   = [0.145, 0.380, 0.475]
```

**Resposta:** Probabilidade de netos ricos = 0.145 (14.5%).

#### **Probabilidade de Bisnetos Ricos (3 gerações)**
```
π₃ = π₀ × P³ = π₂ × P
π₃ = [0.145, 0.380, 0.475] × [0.70  0.20  0.10]
                              [0.15  0.70  0.15]
                              [0.10  0.30  0.60]
   = [0.145×0.70 + 0.380×0.15 + 0.475×0.10,
      0.145×0.20 + 0.380×0.70 + 0.475×0.30,
      0.145×0.10 + 0.380×0.15 + 0.475×0.60]
   = [0.1015 + 0.0570 + 0.0475,
      0.0290 + 0.2660 + 0.1425,
      0.0145 + 0.0570 + 0.2850]
   = [0.206, 0.438, 0.356]
```

**Resposta:** Probabilidade de bisnetos ricos = 0.206 (20.6%).

#### **Distribuição de Longo Prazo Original**
**Estado estacionário:**
```
π₀ = 0.70π₀ + 0.15π₁ + 0.10π₂
π₁ = 0.20π₀ + 0.70π₁ + 0.30π₂
π₂ = 0.10π₀ + 0.15π₁ + 0.60π₂
π₀ + π₁ + π₂ = 1
```

**Solução:**
```
π ≈ [0.250, 0.500, 0.250]
```

#### **Matriz de Transição Modificada**
```
P' = [0.70  0.20  0.10]  # Ricos
     [0.15  0.70  0.15]  # Médios
     [0.10  0.40  0.50]  # Pobres (modificado)
```

#### **Distribuição de Longo Prazo Modificada**
**Estado estacionário:**
```
π₀ = 0.70π₀ + 0.15π₁ + 0.10π₂
π₁ = 0.20π₀ + 0.70π₁ + 0.40π₂
π₂ = 0.10π₀ + 0.15π₁ + 0.50π₂
π₀ + π₁ + π₂ = 1
```

**Solução:**
```
π ≈ [0.200, 0.600, 0.200]
```

**Resposta:** Com a política de redistribuição, a longo prazo teremos 20% ricos, 60% médios e 20% pobres.

---

## **Exercício 5: Jogo de Dados**

### **Enunciado**
Análise de um jogo entre Guilherme e Christian com regras específicas de vitória.

### **Modelagem Matemática**

#### **Estados**
- **Estado 0**: N5 (não é 5)
- **Estado 1**: Primeiro 5
- **Estado 2**: Vitória de Guilherme (5→5)
- **Estado 3**: Vitória de Christian (5→6)

#### **Matriz de Transição**
```
P = [5/6  1/6    0    0]  # N5
    [0    5/6   1/6  0]   # Primeiro 5
    [0     0     1    0]  # Vitória Guilherme
    [0     0     0    1]  # Vitória Christian
```

**Justificativa:**
- **N5 → N5**: 5/6 (probabilidade de não tirar 5)
- **N5 → Primeiro 5**: 1/6 (probabilidade de tirar 5)
- **Primeiro 5 → Primeiro 5**: 5/6 (probabilidade de não tirar 5 novamente)
- **Primeiro 5 → Vitória Guilherme**: 1/6 (probabilidade de tirar 5)
- **Primeiro 5 → Vitória Christian**: 0 (não pode tirar 6 diretamente)

#### **Cálculo de Probabilidades de Absorção**
**Matriz fundamental:**
```
N = (I - Q)⁻¹
```

Onde Q é a submatriz dos estados transientes:
```
Q = [5/6  1/6]
    [0    5/6]
```

**Cálculo:**
```
I - Q = [1/6  -1/6]
        [0    1/6]

N = (I - Q)⁻¹ = [6  6]
                [0  6]
```

**Matriz de absorção:**
```
B = N × R
```

Onde R é a matriz de transição dos estados transientes para absorventes:
```
R = [0    0]
    [1/6  0]
```

**Cálculo:**
```
B = [6  6] × [0    0] = [1  0]
    [0  6]   [1/6  0]   [1  0]
```

**Resposta:** 
- Probabilidade de Guilherme vencer = 1 (100%)
- Probabilidade de Christian vencer = 0 (0%)

**Nota:** Esta análise está incompleta. O jogo real tem regras mais complexas que requerem análise adicional.

---

## **Exercícios 6-9: Letras A-F em Fila**

### **Enunciado**
Análise de movimento entre letras A-F com diferentes regras de transição.

### **Modelagem Matemática**

#### **Estados**
- **Estados 0-5**: Letras A, B, C, D, E, F

#### **Matriz de Transição Original**
```
P = [0.5  0.5  0    0    0    0]  # A
    [0.5  0    0.5  0    0    0]  # B
    [0    0.5  0    0.5  0    0]  # C
    [0    0    0.5  0    0.5  0]  # D
    [0    0    0    0.5  0    0.5] # E
    [0    0    0    0    0.5  0.5] # F
```

**Justificativa:**
- Cada letra pode saltar para suas vizinhas com probabilidade 50%
- Letras nas extremidades (A, F) só têm uma vizinha

#### **Distribuição Estacionária**
**Solução do sistema:**
```
π₀ = 0.5π₀ + 0.5π₁
π₁ = 0.5π₀ + 0.5π₂
π₂ = 0.5π₁ + 0.5π₃
π₃ = 0.5π₂ + 0.5π₄
π₄ = 0.5π₃ + 0.5π₅
π₅ = 0.5π₄ + 0.5π₅
π₀ + π₁ + π₂ + π₃ + π₄ + π₅ = 1
```

**Solução:**
```
π = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
```

**Resposta:** Todas as letras são visitadas igualmente (1/6 cada).

#### **Matriz Modificada (com vogais)**
**Vogais:** A, E
**Regra adicional:** 2% de probabilidade de pular 2 posições a partir de vogais.

```
P' = [0.48  0.5   0.02  0    0    0]  # A (vogal)
     [0.5   0     0.5   0    0    0]  # B
     [0     0.5   0     0.5  0    0]  # C
     [0     0     0.5   0    0.5  0]  # D
     [0     0     0.02  0.5  0    0.48] # E (vogal)
     [0     0     0     0    0.5  0.5] # F
```

#### **Distribuição Estacionária Modificada**
**Solução numérica:**
```
π ≈ [0.167, 0.167, 0.167, 0.167, 0.167, 0.167]
```

**Resposta:** A distribuição permanece aproximadamente uniforme, com pequenas variações devido às regras especiais das vogais.

---

## **📊 Resumo das Fórmulas Principais**

### **Cadeias de Markov**
| Conceito | Fórmula | Aplicação |
|----------|---------|-----------|
| Evolução temporal | πₜ₊₁ = πₜ × P | Cálculo de distribuições |
| Potência de matriz | πₙ = π₀ × Pⁿ | Distribuição após n passos |
| Estado estacionário | π = π × P | Comportamento de longo prazo |
| Probabilidade de absorção | B = N × R | Estados absorventes |

### **Métodos Numéricos**
| Método | Complexidade | Aplicação |
|--------|--------------|-----------|
| Potenciação de matriz | O(n³ log k) | Evolução temporal |
| Autovetores | O(n³) | Estado estacionário |
| Matriz fundamental | O(n³) | Estados absorventes |
| Simulação Monte Carlo | O(k) | Validação de resultados |

### **Análise de Qualidade**
| Métrica | Fórmula | Interpretação |
|---------|---------|---------------|
| Ergodidade | Pⁿ > 0 para algum n | Convergência garantida |
| Período | gcd{n : Pᵢᵢⁿ > 0} | Periodicidade |
| Tempo de absorção | τ = N × 1 | Tempo médio até absorção |
| Probabilidade de absorção | B = N × R | Probabilidades finais |

---

## **🔬 Considerações Teóricas Avançadas**

### **Propriedades de Cadeias de Markov**
- **Irredutibilidade:** Todos os estados se comunicam
- **Aperiodicidade:** Período = 1 para todos os estados
- **Ergodicidade:** Irredutível + aperiódico + finito
- **Reversibilidade:** πᵢPᵢⱼ = πⱼPⱼᵢ

### **Convergência**
- **Teorema de Perron-Frobenius:** Matriz estocástica tem autovalor 1
- **Convergência assintótica:** Pⁿ → π para n → ∞
- **Taxa de convergência:** Segundo maior autovalor
- **Mistura:** Tempo para aproximar distribuição estacionária

### **Estados Absorventes**
- **Classificação:** Estados absorventes vs transientes
- **Matriz fundamental:** N = (I - Q)⁻¹
- **Tempo de absorção:** τ = N × 1
- **Probabilidades de absorção:** B = N × R

### **Interpretação de Resultados**
- **Distribuição estacionária:** Comportamento de longo prazo
- **Tempo de mistura:** Velocidade de convergência
- **Sensibilidade:** Efeito de mudanças nos parâmetros
- **Robustez:** Estabilidade das conclusões

---

## **📈 Aplicações Práticas**

### **Ciências Sociais**
- **Mobilidade social:** Transições entre classes
- **Opinião pública:** Mudança de preferências
- **Demografia:** Migração populacional

### **Economia e Finanças**
- **Modelos de mercado:** Transições de preços
- **Análise de risco:** Estados de default
- **Previsão:** Tendências de mercado

### **Biologia e Medicina**
- **Processos evolutivos:** Mutação de genes
- **Modelagem de doenças:** Progressão de estados
- **Ecologia:** Movimento de espécies

### **Engenharia**
- **Sistemas de filas:** Estados de ocupação
- **Controle de qualidade:** Estados de defeito
- **Confiabilidade:** Estados de funcionamento

---

**Nota:** Estas soluções matemáticas fornecem a base teórica para implementações computacionais robustas e interpretação correta de resultados em problemas de cadeias de Markov aplicadas.
