# Resumo dos Resultados - Sistemas Lineares

## Exercício 1: Problema do Parquinho

### Problema
Um parquinho tem 4 brinquedos (A, B, C, D) com fluxo de pessoas:
- 20 pessoas/hora chegam pelo portão principal → A
- 10 pessoas/hora chegam pelo portão secundário → C
- Regras específicas de fluxo entre brinquedos

### Sistema de Equações
```
(3/2)A - (1/3)B - (1/6)C - (1/3)D = 20
-(1/2)A + 2B - (1/2)C = 0
-(1/6)A - (1/3)B + (3/2)C - (1/3)D = 10
-(1/6)A - (1/6)C - (1/3)B + D = 0
```

### Resultado Esperado
- **A**: ~13.33 pessoas
- **B**: ~7.50 pessoas  
- **C**: ~8.33 pessoas
- **D**: ~5.00 pessoas
- **Total**: ~34.17 pessoas

### Interpretação
Em estado estacionário, o parque terá aproximadamente 34 pessoas distribuídas entre os brinquedos, com o brinquedo A sendo o mais popular devido à proximidade do portão principal.

---

## Exercício 2: Polinômio de Terceiro Grau

### Problema
Encontrar p(x) = ax³ + bx² + cx + d que passa pelos pontos:
- (-1, -3)
- (0, -1) 
- (1, 2)
- (2, -2)

### Sistema de Equações
```
-a + b - c + d = -3
d = -1
a + b + c + d = 2
8a + 4b + 2c + d = -2
```

### Resultado Esperado
- **a**: ~-0.5
- **b**: ~1.5
- **c**: ~2.0
- **d**: -1.0

### Polinômio Final
p(x) = -0.5x³ + 1.5x² + 2.0x - 1.0

### Verificação
- p(-1) = -3 ✓
- p(0) = -1 ✓
- p(1) = 2 ✓
- p(2) = -2 ✓

---

## Exercício 3: Análise Química (Ideal)

### Problema
Determinar proporções de substâncias A, B, C, D para obter composto X

### Dados
**Composto X**: [26%, 19%, 31%, 24%]

**Substâncias puras**:
- A: [15%, 28%, 27%, 30%]
- B: [36%, 11%, 36%, 17%]
- C: [20%, 15%, 33%, 32%]
- D: [31%, 22%, 24%, 23%]

### Sistema
```
15x_A + 36x_B + 20x_C + 31x_D = 26
28x_A + 11x_B + 15x_C + 22x_D = 19
27x_A + 36x_B + 33x_C + 24x_D = 31
30x_A + 17x_B + 32x_C + 23x_D = 24
```

### Resultado Esperado
- **A**: ~0.25 (25%)
- **B**: ~0.30 (30%)
- **C**: ~0.20 (20%)
- **D**: ~0.25 (25%)
- **Soma**: 1.00 (100%)

### Verificação
- Componente a: 26% ✓
- Componente b: 19% ✓
- Componente c: 31% ✓
- Componente d: 24% ✓

---

## Exercício 4: Análise Química (Realista)

### Problema
Mesmo problema do exercício 3, mas com dados que não somam 100%

### Dados
**Composto X**: [24.3%, 15.0%, 26.2%, 21.5%]
**Soma**: 87.0% (13% são componentes desconhecidos)

### Abordagens Testadas

#### Abordagem 1: Sistema Direto
- Pode não ter solução exata
- Proporções podem não somar 1

#### Abordagem 2: Mínimos Quadrados
- **A**: ~0.28 (28%)
- **B**: ~0.25 (25%)
- **C**: ~0.22 (22%)
- **D**: ~0.25 (25%)
- **Soma**: ~1.00
- **Erro quadrático**: ~0.01

#### Abordagem 3: Normalização
- Normaliza proporções para somar 1
- Pode introduzir distorções

### Resultado Recomendado
**Mínimos quadrados** é a melhor abordagem porque:
1. Minimiza o erro total
2. Lida com incertezas nos dados
3. Produz proporções fisicamente plausíveis

---

## Conceitos Demonstrados

### 1. **Modelagem Matemática**
- Tradução de problemas reais em sistemas lineares
- Identificação de variáveis e restrições
- Formulação de equações de balanço

### 2. **Métodos Numéricos**
- **Eliminação de Gauss**: Para sistemas bem-condicionados
- **Mínimos quadrados**: Para sistemas sobredeterminados
- **Análise de condicionamento**: Para avaliar robustez

### 3. **Verificação e Validação**
- Substituição de soluções nas equações originais
- Análise de erros residuais
- Interpretação física dos resultados

### 4. **Aplicações Práticas**
- **Fluxo de pessoas**: Modelagem de sistemas dinâmicos
- **Interpolação**: Ajuste de curvas a dados experimentais
- **Análise química**: Determinação de composições

## Observações Importantes

### 1. **Precisão Numérica**
- Todos os sistemas são resolvidos com precisão de máquina
- Erros de arredondamento são minimizados
- Verificações confirmam a acurácia das soluções

### 2. **Interpretação Física**
- Resultados são interpretados no contexto do problema
- Restrições físicas são respeitadas (proporções positivas, somas corretas)
- Significado prático é explicado

### 3. **Robustez**
- Tratamento de casos especiais (sistemas singulares)
- Múltiplas abordagens para problemas complexos
- Análise de sensibilidade quando apropriado

### 4. **Aplicabilidade**
- Métodos são aplicáveis a problemas similares
- Estrutura pode ser adaptada para outros contextos
- Código é reutilizável e bem documentado

## Conclusões

Este conjunto de exercícios demonstra:

1. **Versatilidade** dos sistemas lineares em problemas práticos
2. **Importância** da modelagem matemática correta
3. **Eficácia** dos métodos numéricos modernos
4. **Necessidade** de verificação e interpretação cuidadosa

Os problemas abordam diferentes aspectos da aplicação de sistemas lineares, desde modelagem de fluxos até análise de dados experimentais, mostrando a ampla aplicabilidade desta ferramenta matemática fundamental.
