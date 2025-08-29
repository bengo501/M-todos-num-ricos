# Métodos Numéricos - Lista de Exercícios: Cadeias de Markov

## 📋 Visão Geral

Esta lista de exercícios aborda conceitos fundamentais de **Cadeias de Markov** em Métodos Numéricos, focando na modelagem de sistemas estocásticos, análise de transições de estado e comportamento de longo prazo. Os exercícios foram projetados para desenvolver habilidades em probabilidade aplicada, álgebra linear estocástica e análise de sistemas dinâmicos.

## 🎯 Objetivos de Aprendizagem

### 1. **Modelagem de Sistemas Estocásticos**
- Identificar estados e transições em sistemas reais
- Construir matrizes de transição
- Formular cadeias de Markov para problemas práticos

### 2. **Análise de Comportamento Temporal**
- Calcular distribuições de probabilidade em diferentes tempos
- Analisar evolução temporal de sistemas
- Determinar estados estacionários

### 3. **Cálculo de Probabilidades de Absorção**
- Identificar estados absorventes
- Calcular probabilidades de absorção
- Usar matriz fundamental para análise

### 4. **Aplicações Práticas**
- Modelagem de opinião pública
- Análise de mobilidade social
- Simulação de jogos e processos aleatórios

## 📚 Conteúdo Programático

### **Módulo 1: Cadeias de Markov Básicas**
- **Exercício 1**: Pesquisa de opinião - Sorveteria
  - Modelagem de mudança de opinião
  - Cálculo de distribuições temporais
  - Análise de estado estacionário

- **Exercício 2**: Migração de torcedores
  - Sistema de três estados
  - Cálculo de evolução temporal
  - Estabilização de populações

### **Módulo 2: Cadeias com Estados Especiais**
- **Exercício 3**: Lobo guará - Regiões de caça
  - Matriz de transição assimétrica
  - Cálculo de probabilidades em múltiplos passos
  - Distribuição de longo prazo

- **Exercício 4**: Mobilidade social
  - Sistema de três classes sociais
  - Cálculo de probabilidades multi-geracionais
  - Análise de impacto de políticas

### **Módulo 3: Cadeias com Estados Absorventes**
- **Exercício 5**: Jogo de dados
  - Estados absorventes e transientes
  - Cálculo de probabilidades de vitória
  - Uso de matriz fundamental

### **Módulo 4: Cadeias com Estados Finitos**
- **Exercícios 6-9**: Letras A-F em fila
  - Modelagem de movimento entre posições
  - Análise de distribuições estacionárias
  - Modificação de regras de transição

## 🔧 Ferramentas e Conceitos Utilizados

### **Conceitos Matemáticos**
- **Probabilidade**: Distribuições, transições condicionais
- **Álgebra Linear**: Matrizes estocásticas, autovalores
- **Cadeias de Markov**: Estados, transições, ergodicidade
- **Análise Assintótica**: Comportamento de longo prazo

### **Algoritmos Implementados**
- **Potência de Matrizes**: Pⁿ para evolução temporal
- **Solução de Sistemas Lineares**: Para estados estacionários
- **Decomposição de Matrizes**: Para análise de absorção
- **Iteração de Potência**: Para convergência

### **Técnicas de Programação**
- **Manipulação de Matrizes**: NumPy para álgebra linear
- **Simulação Monte Carlo**: Para validação de resultados
- **Visualização**: Gráficos de evolução temporal
- **Análise Numérica**: Convergência e precisão

## 📈 Níveis de Dificuldade

### **Básico (Exercícios 1-2)**
- Cadeias simples com 2-3 estados
- Cálculos diretos de potências de matrizes
- Análise de convergência básica

### **Intermediário (Exercícios 3-4)**
- Cadeias com regras assimétricas
- Cálculos multi-período
- Análise de impacto de mudanças

### **Avançado (Exercícios 5-9)**
- Estados absorventes e transientes
- Cadeias com modificações dinâmicas
- Análise comparativa de cenários

## 🎓 Competências Desenvolvidas

### **Técnicas**
- Implementação de algoritmos de cadeias de Markov
- Cálculo de probabilidades complexas
- Análise de convergência numérica
- Simulação de sistemas estocásticos

### **Teóricas**
- Compreensão de processos estocásticos
- Análise de ergodicidade e periodicidade
- Teoria de estados absorventes
- Propriedades de matrizes estocásticas

### **Práticas**
- Modelagem de sistemas reais
- Interpretação de resultados probabilísticos
- Análise de sensibilidade a parâmetros
- Comunicação de descobertas estatísticas

## 🔗 Conexões com Outras Disciplinas

### **Matemática**
- **Probabilidade**: Base teórica dos processos
- **Álgebra Linear**: Manipulação de matrizes estocásticas
- **Análise**: Convergência e limites
- **Teoria de Grafos**: Representação de transições

### **Computação**
- **Simulação**: Métodos Monte Carlo
- **Algoritmos**: Potenciação de matrizes
- **Estruturas de Dados**: Representação de grafos
- **Visualização**: Gráficos de evolução

### **Ciências Aplicadas**
- **Economia**: Modelos de mercado
- **Sociologia**: Mobilidade social
- **Biologia**: Processos evolutivos
- **Engenharia**: Sistemas de filas

## 📊 Tipos de Problemas Abordados

### **1. Problemas de Opinião e Preferência**
- **Características**: Mudança de opinião ao longo do tempo
- **Aplicações**: Pesquisas, marketing, comportamento social
- **Métodos**: Matrizes de transição simétricas

### **2. Problemas de Migração e Movimento**
- **Características**: Movimento entre estados/regiões
- **Aplicações**: Demografia, ecologia, tráfego
- **Métodos**: Cadeias ergódicas

### **3. Problemas de Absorção**
- **Características**: Estados finais que não podem ser deixados
- **Aplicações**: Jogos, processos de decisão
- **Métodos**: Matriz fundamental

### **4. Problemas de Estado Estacionário**
- **Características**: Comportamento de longo prazo
- **Aplicações**: Planejamento, políticas públicas
- **Métodos**: Autovetores de matrizes estocásticas

## 🛠️ Ferramentas Computacionais

### **Bibliotecas Python**
- **NumPy**: Operações com matrizes e álgebra linear
- **SciPy**: Algoritmos de álgebra linear avançados
- **Matplotlib**: Visualização de evolução temporal
- **Pandas**: Manipulação de dados probabilísticos

### **Algoritmos Específicos**
```python
# Potenciação de matriz
P_n = np.linalg.matrix_power(P, n)

# Estado estacionário
eigenvals, eigenvecs = np.linalg.eig(P.T)
stationary = eigenvecs[:, 0] / eigenvecs[:, 0].sum()

# Simulação Monte Carlo
def simulate_markov(P, initial_state, n_steps):
    states = [initial_state]
    for _ in range(n_steps):
        current = states[-1]
        next_state = np.random.choice(len(P), p=P[current])
        states.append(next_state)
    return states
```

## 📖 Bibliografia Sugerida

### **Livros Fundamentais**
- "Introduction to Probability Models" - Ross
- "Markov Chains" - Norris
- "Stochastic Processes" - Karlin & Taylor

### **Recursos Online**
- [Wikipedia - Markov Chains](https://en.wikipedia.org/wiki/Markov_chain)
- [Khan Academy - Markov Chains](https://www.khanacademy.org/computing/computer-science/informationtheory)
- [MIT OpenCourseWare - Probability](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/)

### **Ferramentas Computacionais**
- **Python**: NumPy, SciPy, Matplotlib
- **R**: markovchain package
- **MATLAB**: Statistics and Machine Learning Toolbox
- **Julia**: MarkovChains.jl

## 🎯 Aplicações Práticas

### **Ciências Sociais**
- Análise de mobilidade social
- Modelagem de opinião pública
- Estudos demográficos

### **Economia e Finanças**
- Modelos de mercado
- Análise de risco
- Previsão de tendências

### **Biologia e Medicina**
- Processos evolutivos
- Modelagem de doenças
- Análise de populações

### **Engenharia**
- Sistemas de filas
- Controle de qualidade
- Análise de confiabilidade

## 🔬 Metodologia de Resolução

### **1. Identificação do Sistema**
- Definir estados possíveis
- Identificar regras de transição
- Formular matriz de transição

### **2. Análise Matemática**
- Calcular potências da matriz
- Determinar estados estacionários
- Analisar propriedades ergódicas

### **3. Implementação Computacional**
- Implementar algoritmos numéricos
- Validar com simulações
- Analisar convergência

### **4. Interpretação de Resultados**
- Interpretar probabilidades
- Analisar comportamento temporal
- Extrair insights práticos

---

**Nota**: Esta lista de exercícios fornece uma base sólida em cadeias de Markov aplicadas, preparando o estudante para modelagem de sistemas estocásticos complexos em diversas áreas do conhecimento.
