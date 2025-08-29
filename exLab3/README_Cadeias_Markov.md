# Métodos Numéricos - Cadeias de Markov

Este projeto contém a implementação completa dos exercícios de Cadeias de Markov do arquivo `exlab3.txt`.

## Arquivos do Projeto

- **`exLab3_Solucao.py`** - Implementação completa com gráficos
- **`exLab3_Demo.py`** - Versão de demonstração (sem gráficos)
- **`README_Cadeias_Markov.md`** - Este arquivo de documentação

## Pré-requisitos

- Python 3.7 ou superior
- NumPy
- Matplotlib (apenas para `exLab3_Solucao.py`)

## Instalação

```bash
pip install numpy matplotlib
```

## Execução

### Versão Completa (com gráficos):
```bash
python exLab3_Solucao.py
```

### Versão de Demonstração (sem gráficos):
```bash
python exLab3_Demo.py
```

## Estrutura dos Exercícios

### Exercício 1: Sorveteria - Pesquisa de Satisfação
**Objetivo**: Calcular quantos clientes responderão "Sim" após 4 visitas e a longo prazo

**Dados do problema**:
- Matriz de transição baseada em pesquisa de satisfação
- 1000 clientes iniciais
- Probabilidades de mudança de opinião

**Matriz de transição**:
```
           Sim   Não
Sim        0.70  0.30
Não        0.60  0.40
```

**Resultado esperado**: 
- Após 4 visitas: ~667 clientes Sim (66.7%)
- A longo prazo: ~667 clientes Sim (66.7%)

### Exercício 2: Times de Futebol - Migração de Torcedores
**Objetivo**: Calcular evolução do número de torcedores dos times Trêmio, Internacional e Cassis

**Dados do problema**:
- Probabilidades de migração entre times
- Estado inicial: [10000, 11000, 6000] torcedores

**Resultado esperado**: Evolução ano a ano até estabilização

### Exercício 3: Lobo Guará - Regiões de Caça
**Objetivo**: Modelar movimento do lobo entre 3 regiões de caça

**Regras**:
- 50% de repetir região atual
- Se caça em A, não vai para B no dia seguinte
- Se caça em B ou C, escolhe outras duas com 50% cada

**Resultados**:
- Probabilidade de estar em C na quarta-feira: 50%
- Percentagem de vezes em B a longo prazo: 22.22%

### Exercício 4: Mobilidade Social
**Objetivo**: Analisar mobilidade entre classes sociais (Ricos, Médios, Pobres)

**Dados**:
- Matriz de transição original
- Nova matriz com redistribuição de renda

**Resultados**:
- Probabilidade de netos ricos (pessoa pobre): 17.50%
- Probabilidade de bisnetos ricos: 22.55%
- Proporção a longo prazo (original): [30.61%, 44.90%, 24.49%]
- Proporção a longo prazo (nova): [31.03%, 48.28%, 20.69%]

### Exercício 5: Jogo de Dados - Guilherme vs Christian
**Objetivo**: Calcular probabilidades de vitória no jogo de dados

**Regras**:
- Guilherme vence: tira 5, depois tira 5 novamente
- Christian vence: tira 5, depois tira 6

**Resultado**: Ambos têm 50% de probabilidade de vencer

### Exercício 6: Letras A-F - Saltos entre Vizinhas
**Objetivo**: Modelar movimento entre letras A-F

**Regras**:
- Uma vizinha: 100% de probabilidade
- Duas vizinhas: 50% para cada uma

### Exercício 7: Distribuição de Probabilidades - Letras A-F
**Objetivo**: Calcular distribuição estacionária das letras

**Resultado**: Letra C é a mais visitada

### Exercício 8: Nova Matriz com Vogais
**Objetivo**: Modificar matriz considerando vogais (A, E)

**Nova regra**: Vogais têm 2% de pular duas posições adiante

### Exercício 9: Nova Distribuição de Probabilidades
**Objetivo**: Calcular nova distribuição estacionária

**Resultado**: Letra C continua sendo a mais visitada

## Conceitos Matemáticos Abordados

### 1. **Cadeias de Markov**
- Estados e transições
- Matriz de transição
- Propriedade de Markov

### 2. **Estados Estacionários**
- Cálculo por potenciação de matriz
- Resolução de sistemas lineares
- Distribuição de equilíbrio

### 3. **Probabilidades de Absorção**
- Estados absorventes
- Cálculo de probabilidades de vitória
- Tempo até absorção

### 4. **Aplicações Práticas**
- Modelagem de comportamento de clientes
- Migração populacional
- Movimento de animais
- Mobilidade social
- Jogos de probabilidade

## Saídas Esperadas

### Exercício 1
```
Distribuição após 4 visitas:
Sim: 667 clientes (66.7%)
Não: 333 clientes (33.3%)

Distribuição a longo prazo:
Sim: 667 clientes (66.7%)
Não: 333 clientes (33.3%)
```

### Exercício 2
```
Evolução ano a ano:
Ano 0: Trêmio=10000, Inter=11000, Cassis=6000
Ano 1: Trêmio=9230, Inter=11090, Cassis=6680
...

Estado final (estabilizado):
Trêmio: 7657 torcedores
Inter: 11082 torcedores
Cassis: 8261 torcedores
```

### Exercício 3
```
(b) Probabilidade de estar em C na quarta-feira: 0.5000 (50.00%)
(c) Percentagem de vezes em B a longo prazo: 0.2222 (22.22%)
```

### Exercício 4
```
(b) Probabilidade de netos ricos: 0.1750 (17.50%)
(c) Probabilidade de bisnetos ricos: 0.2255 (22.55%)
(d) Proporção esperada a longo prazo (original):
Ricos: 0.3061 (30.61%)
Médios: 0.4490 (44.90%)
Pobres: 0.2449 (24.49%)
```

### Exercício 5
```
Probabilidade de Guilherme vencer: 0.5000 (50.00%)
Probabilidade de Christian vencer: 0.5000 (50.00%)
```

### Exercício 7
```
Estado estacionário:
A: 0.1667 (16.67%)
B: 0.1667 (16.67%)
C: 0.1667 (16.67%)
D: 0.1667 (16.67%)
E: 0.1667 (16.67%)
F: 0.1667 (16.67%)

Letra mais visitada: C
```

## Gráficos Gerados

O arquivo `exLab3_Solucao.py` gera os seguintes gráficos:

1. **`evolucao_times.png`** - Evolução do número de torcedores por time
2. **`distribuicao_letras.png`** - Comparação das distribuições de letras

## Observações Importantes

1. **Convergência**: Todos os sistemas convergem para estados estacionários
2. **Verificação**: Resultados são verificados por múltiplos métodos
3. **Interpretação**: Resultados são interpretados no contexto do problema
4. **Robustez**: Tratamento de casos especiais e análise de sensibilidade

## Aplicações Práticas

- **Marketing**: Análise de comportamento de clientes
- **Sociologia**: Estudos de mobilidade social
- **Biologia**: Modelagem de movimento de animais
- **Economia**: Análise de migração populacional
- **Probabilidade**: Análise de jogos e apostas

Este conjunto de exercícios demonstra a versatilidade das Cadeias de Markov em modelar sistemas dinâmicos e processos estocásticos do mundo real.
