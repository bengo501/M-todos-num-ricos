# Métodos Numéricos - Lista de Exercícios: Interpolação

## 📋 Visão Geral

Esta lista de exercícios aborda conceitos fundamentais de **Interpolação** em Métodos Numéricos, focando na construção de polinômios que passam por pontos dados, extrapolação de dados e ajuste por mínimos quadrados. Os exercícios foram projetados para desenvolver habilidades em aproximação polinomial, análise de dados e previsão numérica.

## 🎯 Objetivos de Aprendizagem

### 1. **Interpolação Polinomial**
- Construir polinômios que passam exatamente por pontos dados
- Implementar métodos de interpolação (Lagrange, Newton)
- Analisar unicidade e existência de soluções

### 2. **Extrapolação e Previsão**
- Estender polinômios interpoladores além dos dados
- Avaliar riscos e limitações da extrapolação
- Comparar previsões com valores reais

### 3. **Ajuste por Mínimos Quadrados**
- Implementar ajuste linear e polinomial
- Avaliar qualidade de ajustes via R² e RMSE
- Escolher grau apropriado de polinômio

### 4. **Análise de Dados Reais**
- Trabalhar com dados econômicos e industriais
- Interpretar resultados em contexto aplicado
- Validar previsões com dados históricos

## 📚 Conteúdo Programático

### **Módulo 1: Interpolação Polinomial Básica**
- **Exercício 1**: Parábola por três pontos
  - Construção de polinômio de grau 2
  - Cálculo de raízes do polinômio
  - Verificação de unicidade

### **Módulo 2: Método de Newton**
- **Exercício 2**: Interpolação de Newton
  - Comparação de diferentes ordenações de pontos
  - Análise de unicidade do polinômio
  - Verificação de independência da ordem

### **Módulo 3: Extrapolação e Previsão**
- **Exercício 3**: Produção chinesa de aço
  - Extrapolação de dados temporais
  - Comparação com valores reais
  - Análise de riscos da extrapolação

- **Exercício 4**: Produção brasileira de ovos
  - Ajuste de dados recentes
  - Previsão para anos futuros
  - Validação com dados do IBGE

### **Módulo 4: Interpolação e Ajuste**
- **Exercício 5**: Produção de camarão
  - Estimação de valores faltantes
  - Interpolação para dados incompletos
  - Previsão de valores futuros

- **Exercício 6**: Mínimos Quadrados
  - Ajuste linear vs polinomial
  - Comparação de qualidade de ajustes
  - Escolha de grau ótimo

## 🔧 Ferramentas e Conceitos Utilizados

### **Conceitos Matemáticos**
- **Interpolação**: Polinômios de Lagrange, Newton
- **Extrapolação**: Extensão além dos dados
- **Mínimos Quadrados**: Ajuste de curvas
- **Análise de Erro**: RMSE, R², resíduos

### **Algoritmos Implementados**
- **Interpolação de Lagrange**: O(n²) para n pontos
- **Diferenças Divididas**: Método de Newton
- **Mínimos Quadrados**: Solução de sistemas normais
- **Avaliação de Polinômios**: Método de Horner

### **Técnicas de Programação**
- **Manipulação de Polinômios**: NumPy, SciPy
- **Visualização de Dados**: Matplotlib
- **Análise Estatística**: Pandas, Scikit-learn
- **Validação de Resultados**: Comparação com dados reais

## 📈 Níveis de Dificuldade

### **Básico (Exercícios 1-2)**
- Interpolação polinomial direta
- Construção de polinômios simples
- Verificação de propriedades básicas

### **Intermediário (Exercícios 3-4)**
- Extrapolação de dados temporais
- Análise de riscos de previsão
- Validação com dados reais

### **Avançado (Exercícios 5-6)**
- Dados incompletos e estimação
- Comparação de métodos de ajuste
- Otimização de grau polinomial

## 🎓 Competências Desenvolvidas

### **Técnicas**
- Implementação de algoritmos de interpolação
- Cálculo de polinômios interpoladores
- Análise de qualidade de ajustes
- Validação de previsões numéricas

### **Teóricas**
- Compreensão de unicidade de interpolação
- Análise de erros de aproximação
- Teoria de mínimos quadrados
- Propriedades de polinômios

### **Práticas**
- Trabalho com dados reais
- Interpretação de resultados em contexto
- Escolha adequada de métodos
- Comunicação de descobertas científicas

## 🔗 Conexões com Outras Disciplinas

### **Matemática**
- **Álgebra Linear**: Sistemas de equações
- **Análise Numérica**: Aproximação de funções
- **Estatística**: Ajuste de dados
- **Teoria de Polinômios**: Propriedades algébricas

### **Computação**
- **Algoritmos**: Complexidade computacional
- **Estruturas de Dados**: Representação de polinômios
- **Visualização**: Gráficos de dados
- **Análise de Dados**: Pandas, NumPy

### **Ciências Aplicadas**
- **Economia**: Previsão de produção
- **Engenharia**: Análise de dados experimentais
- **Estatística**: Modelagem de tendências
- **Pesquisa Operacional**: Otimização

## 📊 Tipos de Problemas Abordados

### **1. Problemas de Interpolação Exata**
- **Características**: Polinômios que passam exatamente pelos pontos
- **Aplicações**: Análise matemática, computação gráfica
- **Métodos**: Lagrange, Newton, sistemas lineares

### **2. Problemas de Extrapolação**
- **Características**: Extensão de polinômios além dos dados
- **Aplicações**: Previsão, análise de tendências
- **Métodos**: Polinômios interpoladores, análise de risco

### **3. Problemas de Ajuste**
- **Características**: Aproximação de dados com erro
- **Aplicações**: Modelagem estatística, análise de dados
- **Métodos**: Mínimos quadrados, regressão

### **4. Problemas de Estimação**
- **Características**: Dados incompletos ou faltantes
- **Aplicações**: Análise de séries temporais
- **Métodos**: Interpolação, extrapolação

## 🛠️ Ferramentas Computacionais

### **Bibliotecas Python**
- **NumPy**: Operações com polinômios e álgebra linear
- **SciPy**: Algoritmos de interpolação e ajuste
- **Matplotlib**: Visualização de dados e curvas
- **Pandas**: Manipulação e análise de dados

### **Algoritmos Específicos**
```python
# Interpolação de Lagrange
from scipy.interpolate import lagrange
poly = lagrange(x, y)

# Interpolação de Newton
from scipy.interpolate import interp1d
f = interp1d(x, y, kind='linear')

# Mínimos quadrados
from numpy.polynomial import Polynomial
coeffs = Polynomial.fit(x, y, deg=3).convert().coef

# Avaliação de polinômios
y_pred = np.polyval(coeffs, x_new)
```

## 📖 Bibliografia Sugerida

### **Livros Fundamentais**
- "Numerical Analysis" - Burden & Faires
- "Numerical Recipes" - Press et al.
- "Introduction to Numerical Analysis" - Stoer & Bulirsch

### **Recursos Online**
- [SciPy Interpolation](https://docs.scipy.org/doc/scipy/reference/interpolate.html)
- [NumPy Polynomials](https://numpy.org/doc/stable/reference/routines.polynomials.html)
- [Khan Academy - Polynomial Interpolation](https://www.khanacademy.org/math/algebra2)

### **Ferramentas Computacionais**
- **Python**: NumPy, SciPy, Matplotlib, Pandas
- **MATLAB**: Interpolation Toolbox
- **R**: stats package, splines
- **Julia**: Interpolations.jl

## 🎯 Aplicações Práticas

### **Engenharia**
- Análise de dados experimentais
- Modelagem de sistemas físicos
- Controle de qualidade

### **Economia e Finanças**
- Previsão de tendências
- Análise de séries temporais
- Modelagem de mercados

### **Ciências Naturais**
- Análise de dados experimentais
- Modelagem de fenômenos físicos
- Previsão climática

### **Computação**
- Computação gráfica
- Processamento de sinais
- Machine Learning

## 🔬 Metodologia de Resolução

### **1. Análise dos Dados**
- Identificar tipo de problema (interpolação/extrapolação/ajuste)
- Verificar qualidade e completude dos dados
- Escolher método apropriado

### **2. Implementação Numérica**
- Implementar algoritmo escolhido
- Validar implementação com casos simples
- Analisar convergência e precisão

### **3. Análise de Resultados**
- Avaliar qualidade do ajuste
- Interpretar resultados em contexto
- Validar com dados externos

### **4. Documentação**
- Explicar metodologia escolhida
- Apresentar resultados e limitações
- Discutir aplicabilidade prática

---

**Nota**: Esta lista de exercícios fornece uma base sólida em interpolação e aproximação polinomial, preparando o estudante para análise de dados complexos e modelagem matemática em diversas áreas aplicadas.
