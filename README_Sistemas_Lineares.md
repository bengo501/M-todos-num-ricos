# Métodos Numéricos - Sistemas Lineares

Este projeto contém a implementação completa dos exercícios de Sistemas Lineares do arquivo `exlab2.txt`.

## Arquivos do Projeto

- **`exLab2_Solucao.py`** - Implementação completa com gráficos
- **`exLab2_Demo.py`** - Versão de demonstração (sem gráficos)
- **`README_Sistemas_Lineares.md`** - Este arquivo de documentação

## Pré-requisitos

- Python 3.7 ou superior
- NumPy
- Matplotlib (apenas para `exLab2_Solucao.py`)

## Instalação

```bash
pip install numpy matplotlib
```

## Execução

### Versão Completa (com gráficos):
```bash
python exLab2_Solucao.py
```

### Versão de Demonstração (sem gráficos):
```bash
python exLab2_Demo.py
```

## Estrutura dos Exercícios

### Exercício 1: Problema do Parquinho
**Objetivo**: Calcular quantas pessoas vão brincar em cada um dos 4 brinquedos (A, B, C, D)

**Dados do problema**:
- 20 pessoas/hora chegam pelo portão principal → brinquedo A
- 10 pessoas/hora chegam pelo portão secundário → brinquedo C
- Fluxo de pessoas entre brinquedos segue regras específicas

**Sistema de equações**:
```
(3/2)A - (1/3)B - (1/6)C - (1/3)D = 20
-(1/2)A + 2B - (1/2)C = 0
-(1/6)A - (1/3)B + (3/2)C - (1/3)D = 10
-(1/6)A - (1/6)C - (1/3)B + D = 0
```

**Resultado esperado**: Número de pessoas em cada brinquedo em estado estacionário

### Exercício 2: Polinômio de Terceiro Grau
**Objetivo**: Encontrar o polinômio p(x) = ax³ + bx² + cx + d que passa pelos pontos:
- (-1, -3)
- (0, -1)
- (1, 2)
- (2, -2)

**Sistema de equações**:
```
(-1)³a + (-1)²b + (-1)c + d = -3
(0)³a + (0)²b + (0)c + d = -1
(1)³a + (1)²b + (1)c + d = 2
(2)³a + (2)²b + (2)c + d = -2
```

**Resultado**: Coeficientes a, b, c, d do polinômio

### Exercício 3: Análise Química (Versão Ideal)
**Objetivo**: Determinar como as substâncias A, B, C e D foram misturadas para obter o composto X

**Dados**:
- Composição do composto X: [26%, 19%, 31%, 24%]
- Composição das substâncias puras:
  - A: [15%, 28%, 27%, 30%]
  - B: [36%, 11%, 36%, 17%]
  - C: [20%, 15%, 33%, 32%]
  - D: [31%, 22%, 24%, 23%]

**Sistema**: 4 equações lineares para as proporções x_A, x_B, x_C, x_D

**Resultado**: Proporções de cada substância na mistura

### Exercício 4: Análise Química (Versão Realista)
**Objetivo**: Mesmo problema do exercício 3, mas com dados reais que não somam 100%

**Dados**:
- Composição do composto X: [24.3%, 15.0%, 26.2%, 21.5%]
- Soma: 86.9% (13.1% são componentes desconhecidos)

**Abordagens**:
1. Resolver sistema como está
2. Mínimos quadrados
3. Normalização

**Resultado**: Proporções aproximadas com análise de erro

## Conceitos Matemáticos Abordados

### 1. **Sistemas de Equações Lineares**
- Forma matricial Ax = b
- Solução única vs. múltiplas soluções
- Sistemas sobredeterminados e subdeterminados

### 2. **Métodos de Resolução**
- Eliminação de Gauss (np.linalg.solve)
- Mínimos quadrados (np.linalg.lstsq)
- Análise de condicionamento

### 3. **Aplicações Práticas**
- Modelagem de fluxo de pessoas
- Interpolação polinomial
- Análise de composição química

### 4. **Análise de Erro**
- Verificação de soluções
- Erro quadrático médio
- Interpretação de resultados

## Saídas Esperadas

### Exercício 1
```
Solução do sistema:
A = XX.XX pessoas
B = XX.XX pessoas
C = XX.XX pessoas
D = XX.XX pessoas
Total: XX.XX pessoas
```

### Exercício 2
```
Polinômio: p(x) = X.XXXXXXx³ + X.XXXXXXx² + X.XXXXXXx + X.XXXXXX
Verificação:
p(-1) = -3.000000 (esperado: -3)
p(0) = -1.000000 (esperado: -1)
p(1) = 2.000000 (esperado: 2)
p(2) = -2.000000 (esperado: -2)
```

### Exercício 3
```
Solução:
Proporção de A: X.XXXX (XX.XX%)
Proporção de B: X.XXXX (XX.XX%)
Proporção de C: X.XXXX (XX.XX%)
Proporção de D: X.XXXX (XX.XX%)
Soma das proporções: 1.0000
```

### Exercício 4
```
Solução por mínimos quadrados:
Proporção de A: X.XXXX (XX.XX%)
Proporção de B: X.XXXX (XX.XX%)
Proporção de C: X.XXXX (XX.XX%)
Proporção de D: X.XXXX (XX.XX%)
Erro quadrático total: X.XXXX
```

## Gráficos Gerados

O arquivo `exLab2_Solucao.py` gera os seguintes gráficos:

1. **`polinomio_terceiro_grau.png`** - Gráfico do polinômio interpolador
2. **`resultados_sistemas_lineares.png`** - Resumo visual de todos os exercícios

## Observações Importantes

1. **Precisão**: Todos os sistemas são resolvidos com precisão numérica
2. **Verificação**: Cada solução é verificada substituindo na equação original
3. **Interpretação**: Resultados são interpretados no contexto do problema
4. **Robustez**: Tratamento de casos especiais (sistemas singulares, etc.)

## Aplicações Práticas

- **Engenharia**: Análise de fluxos, interpolação de dados
- **Química**: Análise de composição de misturas
- **Economia**: Modelagem de fluxos de pessoas/recursos
- **Computação**: Interpolação e ajuste de curvas

Este conjunto de exercícios demonstra a versatilidade dos sistemas lineares em problemas práticos do mundo real.
