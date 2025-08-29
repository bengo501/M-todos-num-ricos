# Métodos Numéricos - Lista de Exercícios: Sistemas Lineares

## 📋 Visão Geral

Esta lista de exercícios aborda conceitos fundamentais de **Sistemas Lineares** em Métodos Numéricos, focando na modelagem matemática de problemas reais e suas soluções computacionais. Os exercícios foram projetados para desenvolver habilidades em álgebra linear aplicada, modelagem de sistemas e análise de dados.

## 🎯 Objetivos de Aprendizagem

### 1. **Modelagem Matemática de Sistemas Reais**
- Traduzir problemas práticos em sistemas de equações lineares
- Identificar variáveis e relações entre elas
- Formular matrizes de coeficientes e vetores de termos independentes

### 2. **Solução de Sistemas Lineares**
- Implementar métodos diretos (Eliminação de Gauss, LU)
- Aplicar métodos iterativos (Jacobi, Gauss-Seidel)
- Analisar convergência e estabilidade numérica

### 3. **Interpolação e Ajuste de Dados**
- Construir polinômios interpoladores via sistemas lineares
- Implementar ajuste por mínimos quadrados
- Avaliar qualidade de ajustes e interpolações

### 4. **Análise de Dados e Inversão de Problemas**
- Resolver problemas de composição química
- Lidar com dados incompletos e incertezas
- Interpretar resultados em contexto aplicado

## 📚 Conteúdo Programático

### **Módulo 1: Modelagem de Sistemas Dinâmicos**
- **Exercício 1**: Problema do parquinho
  - Modelagem de fluxo de pessoas entre brinquedos
  - Sistema de equações de balanço
  - Análise de distribuição estacionária

### **Módulo 2: Interpolação Polinomial**
- **Exercício 2**: Polinômio de terceiro grau
  - Construção de sistema linear para interpolação
  - Resolução via métodos diretos
  - Verificação da precisão da solução

### **Módulo 3: Análise Química - Composição de Substâncias**
- **Exercício 3**: Composição exata
  - Sistema linear para determinação de proporções
  - Análise de dados cromatográficos
  - Verificação de consistência

- **Exercício 4**: Composição com incertezas
  - Sistema sobredeterminado
  - Método dos mínimos quadrados
  - Interpretação de resultados com dados incompletos

## 🔧 Ferramentas e Conceitos Utilizados

### **Conceitos Matemáticos**
- **Álgebra Linear**: Matrizes, vetores, sistemas lineares
- **Análise Numérica**: Condicionamento, estabilidade
- **Interpolação**: Polinômios de Lagrange, Newton
- **Mínimos Quadrados**: Ajuste de dados, resíduos

### **Algoritmos Implementados**
- **Eliminação de Gauss**: O(n³) para sistemas n×n
- **Decomposição LU**: Fatorização de matrizes
- **Métodos Iterativos**: Jacobi, Gauss-Seidel
- **Mínimos Quadrados**: `np.linalg.lstsq`

### **Técnicas de Programação**
- **Manipulação de Matrizes**: NumPy, SciPy
- **Análise de Dados**: Pandas, Matplotlib
- **Validação Numérica**: Verificação de resultados
- **Visualização**: Gráficos de dados e soluções

## 📈 Níveis de Dificuldade

### **Básico (Exercício 1)**
- Modelagem de sistema simples
- Sistema linear bem condicionado
- Solução direta via métodos clássicos

### **Intermediário (Exercícios 2-3)**
- Interpolação polinomial
- Sistemas com dados experimentais
- Análise de precisão e validação

### **Avançado (Exercício 4)**
- Sistema sobredeterminado
- Dados com incertezas
- Interpretação de resultados em contexto real

## 🎓 Competências Desenvolvidas

### **Técnicas**
- Implementação de algoritmos de álgebra linear
- Modelagem matemática de problemas reais
- Análise de dados experimentais
- Validação de soluções numéricas

### **Teóricas**
- Compreensão de sistemas lineares
- Análise de condicionamento
- Teoria de interpolação
- Métodos de mínimos quadrados

### **Práticas**
- Tradução de problemas em equações
- Escolha adequada de métodos numéricos
- Interpretação de resultados
- Comunicação de descobertas científicas

## 🔗 Conexões com Outras Disciplinas

### **Matemática**
- **Álgebra Linear**: Base teórica dos sistemas
- **Análise Numérica**: Estabilidade e convergência
- **Teoria de Aproximação**: Interpolação e ajuste
- **Otimização**: Mínimos quadrados

### **Computação**
- **Estruturas de Dados**: Representação de matrizes
- **Análise de Algoritmos**: Complexidade computacional
- **Programação Científica**: Bibliotecas especializadas
- **Visualização**: Gráficos e análise de dados

### **Ciências Aplicadas**
- **Engenharia**: Modelagem de sistemas físicos
- **Química**: Análise de composição
- **Física**: Sistemas de equações diferenciais
- **Economia**: Modelos de equilíbrio

## 📊 Tipos de Problemas Abordados

### **1. Problemas de Fluxo e Balanço**
- **Características**: Sistemas de conservação
- **Aplicações**: Tráfego, fluidos, redes
- **Métodos**: Sistemas lineares homogêneos

### **2. Problemas de Interpolação**
- **Características**: Ajuste de curvas a pontos
- **Aplicações**: Análise de dados, previsão
- **Métodos**: Sistemas de Vandermonde

### **3. Problemas de Inversão**
- **Características**: Determinação de parâmetros
- **Aplicações**: Análise química, geofísica
- **Métodos**: Mínimos quadrados, regularização

## 🛠️ Ferramentas Computacionais

### **Bibliotecas Python**
- **NumPy**: Operações com matrizes e vetores
- **SciPy**: Algoritmos de álgebra linear
- **Matplotlib**: Visualização de dados
- **Pandas**: Manipulação de dados tabulares

### **Algoritmos Específicos**
```python
# Solução direta
x = np.linalg.solve(A, b)

# Decomposição LU
lu, piv = scipy.linalg.lu_factor(A)
x = scipy.linalg.lu_solve((lu, piv), b)

# Mínimos quadrados
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
```

## 📖 Bibliografia Sugerida

### **Livros Fundamentais**
- "Numerical Linear Algebra" - Trefethen & Bau
- "Matrix Computations" - Golub & Van Loan
- "Applied Linear Algebra" - Strang

### **Recursos Online**
- [NumPy Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [SciPy Linear Algebra](https://docs.scipy.org/doc/scipy/reference/linalg.html)
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)

### **Ferramentas Computacionais**
- **Python**: NumPy, SciPy, Matplotlib
- **MATLAB**: Toolbox de Álgebra Linear
- **Julia**: LinearAlgebra.jl
- **R**: Matrix package

## 🎯 Aplicações Práticas

### **Engenharia**
- Análise de estruturas
- Circuitos elétricos
- Sistemas de controle

### **Ciências Naturais**
- Análise química
- Modelagem física
- Processamento de sinais

### **Ciências Sociais**
- Economia matemática
- Análise de redes sociais
- Pesquisa operacional

## 🔬 Metodologia de Resolução

### **1. Análise do Problema**
- Identificar variáveis e parâmetros
- Estabelecer relações matemáticas
- Formular sistema de equações

### **2. Implementação Numérica**
- Escolher método apropriado
- Implementar algoritmo
- Validar implementação

### **3. Análise de Resultados**
- Verificar consistência
- Interpretar soluções
- Avaliar qualidade numérica

### **4. Documentação**
- Explicar metodologia
- Apresentar resultados
- Discutir limitações

---

**Nota**: Esta lista de exercícios fornece uma base sólida em sistemas lineares aplicados, preparando o estudante para problemas complexos em modelagem matemática, análise de dados e computação científica.
