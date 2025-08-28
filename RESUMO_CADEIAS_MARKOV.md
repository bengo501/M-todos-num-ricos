# Resumo dos Resultados - Cadeias de Markov

## Exercício 1: Sorveteria - Pesquisa de Satisfação

### Problema
Uma sorveteria faz pesquisa de satisfação com clientes sobre a qualidade do sorvete de chocolate. A matriz de transição mostra as probabilidades de mudança de opinião.

### Matriz de Transição
```
           Sim   Não
Sim        0.70  0.30
Não        0.60  0.40
```

### Resultados
- **Após 4 visitas**: 667 clientes Sim (66.7%), 333 clientes Não (33.3%)
- **A longo prazo**: 667 clientes Sim (66.7%), 333 clientes Não (33.3%)

### Interpretação
O sistema converge rapidamente para o estado estacionário, onde aproximadamente 2/3 dos clientes respondem "Sim" e 1/3 responde "Não".

---

## Exercício 2: Times de Futebol - Migração de Torcedores

### Problema
Três times de futebol (Trêmio, Internacional, Cassis) com migração de torcedores baseada em probabilidades específicas.

### Matriz de Transição
```
           Trêmio Inter Cassis
Trêmio     0.78   0.12   0.10
Inter      0.07   0.85   0.08
Cassis     0.11   0.09   0.80
```

### Evolução Ano a Ano
```
Ano 0: Trêmio=10000, Inter=11000, Cassis=6000
Ano 1: Trêmio=9230, Inter=11090, Cassis=6680
Ano 2: Trêmio=8710, Inter=11135, Cassis=7154
...
Ano 9: Trêmio=7714, Inter=11119, Cassis=8167
```

### Estado Estacionário
- **Trêmio**: 7,657 torcedores
- **Internacional**: 11,082 torcedores  
- **Cassis**: 8,261 torcedores

### Interpretação
O Internacional mantém a maior torcida, seguido pelo Cassis e depois pelo Trêmio. O sistema estabiliza após aproximadamente 10 anos.

---

## Exercício 3: Lobo Guará - Regiões de Caça

### Problema
Um lobo guará caça em 3 regiões (A, B, C) com regras específicas de movimento.

### Matriz de Transição
```
           A     B     C
A          0.50   0.00   0.50
B          0.25   0.50   0.25
C          0.25   0.25   0.50
```

### Resultados
- **Probabilidade de estar em C na quarta-feira**: 50.00%
- **Percentagem de vezes em B a longo prazo**: 22.22%

### Interpretação
A região B é a menos visitada pelo lobo devido às restrições de movimento (não pode ir de A para B).

---

## Exercício 4: Mobilidade Social

### Problema
Análise de mobilidade entre classes sociais (Ricos, Médios, Pobres) com duas versões: original e com redistribuição de renda.

### Matriz Original
```
           Ricos Médios Pobres
Ricos      0.70   0.20   0.10
Médios     0.15   0.70   0.15
Pobres     0.10   0.30   0.60
```

### Resultados Originais
- **Probabilidade de netos ricos (pessoa pobre)**: 17.50%
- **Probabilidade de bisnetos ricos**: 22.55%
- **Proporção a longo prazo**: Ricos 30.61%, Médios 44.90%, Pobres 24.49%

### Nova Matriz (com redistribuição)
```
           Ricos Médios Pobres
Ricos      0.70   0.20   0.10
Médios     0.15   0.70   0.15
Pobres     0.10   0.40   0.50
```

### Resultados com Redistribuição
- **Proporção a longo prazo**: Ricos 31.03%, Médios 48.28%, Pobres 20.69%

### Interpretação
A redistribuição de renda aumenta a mobilidade social, reduzindo a proporção de pobres e aumentando a classe média.

---

## Exercício 5: Jogo de Dados - Guilherme vs Christian

### Problema
Dois jogadores disputam um jogo de dados com regras específicas:
- Guilherme vence: tira 5, depois tira 5 novamente
- Christian vence: tira 5, depois tira 6

### Estados da Cadeia
- Início
- Guilherme tirou primeiro 5
- Christian tirou primeiro 5
- Guilherme venceu (absorvente)
- Christian venceu (absorvente)

### Resultado
- **Probabilidade de Guilherme vencer**: 50.00%
- **Probabilidade de Christian vencer**: 50.00%

### Interpretação
O jogo é perfeitamente equilibrado, com ambos os jogadores tendo a mesma chance de vitória.

---

## Exercício 6-9: Letras A-F - Saltos entre Vizinhas

### Problema
Modelagem de movimento entre letras A-F com diferentes regras de transição.

### Matriz Original
```
           A     B     C     D     E     F
A          0.00   0.50   0.25   0.00   0.00   0.00
B          0.50   0.00   0.50   0.25   0.00   0.00
C          0.25   0.50   0.00   0.50   0.25   0.00
D          0.00   0.25   0.50   0.00   0.50   0.25
E          0.00   0.00   0.25   0.50   0.00   0.50
F          0.00   0.00   0.00   0.25   0.50   0.00
```

### Nova Matriz (com vogais)
Regra adicional: vogais (A, E) têm 2% de pular duas posições adiante.

### Resultados
- **Letra mais visitada (original)**: C
- **Letra mais visitada (com vogais)**: C

### Interpretação
A letra C permanece como a mais visitada mesmo com a modificação das regras para vogais.

---

## Conceitos Demonstrados

### 1. **Modelagem de Cadeias de Markov**
- Identificação de estados e transições
- Construção de matrizes de transição
- Verificação da propriedade de Markov

### 2. **Cálculo de Estados Estacionários**
- **Método 1**: Potenciação de matriz (P^n)
- **Método 2**: Resolução de sistemas lineares (π = πP)
- **Método 3**: Análise de autovalores e autovetores

### 3. **Probabilidades de Absorção**
- Estados absorventes
- Cálculo de probabilidades de vitória
- Tempo médio até absorção

### 4. **Aplicações Práticas**
- **Marketing**: Comportamento de clientes
- **Sociologia**: Mobilidade social
- **Biologia**: Movimento de animais
- **Economia**: Migração populacional
- **Probabilidade**: Análise de jogos

## Observações Importantes

### 1. **Convergência**
Todos os sistemas estudados convergem para estados estacionários, demonstrando a propriedade ergódica das cadeias de Markov.

### 2. **Sensibilidade**
Pequenas mudanças nas probabilidades de transição podem ter efeitos significativos nos estados estacionários (exemplo: redistribuição de renda).

### 3. **Interpretação Física**
Os resultados são interpretados no contexto de cada problema, fornecendo insights práticos sobre os sistemas modelados.

### 4. **Verificação Numérica**
Todos os resultados são verificados por múltiplos métodos, garantindo a acurácia dos cálculos.

## Conclusões

Este conjunto de exercícios demonstra:

1. **Versatilidade** das Cadeias de Markov em modelar sistemas dinâmicos
2. **Importância** da modelagem correta de estados e transições
3. **Eficácia** dos métodos numéricos para cálculo de estados estacionários
4. **Aplicabilidade** em problemas reais de diversas áreas

As Cadeias de Markov são uma ferramenta poderosa para modelar processos estocásticos e sistemas dinâmicos, fornecendo insights valiosos sobre o comportamento de sistemas complexos ao longo do tempo.
