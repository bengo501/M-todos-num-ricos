# Métodos Numéricos - Lista de Exercícios: Solução de Equações

## 📋 Visão Geral

Esta lista de exercícios aborda conceitos fundamentais de **Métodos Numéricos** com foco especial na **Solução de Equações**. Os exercícios foram projetados para desenvolver habilidades práticas em algoritmos numéricos, análise de precisão computacional e métodos iterativos para encontrar raízes de funções.

## 🎯 Objetivos de Aprendizagem

### 1. **Precisão Computacional e Sistemas de Ponto Flutuante**
- Compreender os limites da representação numérica em computadores
- Analisar algoritmos que exploram a precisão da máquina
- Identificar problemas de cancelamento catastrófico

### 2. **Análise de Polinômios**
- Calcular cotas para localização de raízes (Cauchy, Lagrange, Fujiwara)
- Construir polinômios a partir de raízes conhecidas
- Implementar métodos eficientes de avaliação polinomial

### 3. **Métodos Iterativos para Solução de Equações**
- **Método da Bissecção**: Localização de raízes em intervalos
- **Método de Newton-Raphson**: Convergência quadrática
- **Método da Secante**: Aproximação de derivadas
- **Método de Newton com Números Complexos**: Solução de equações complexas

### 4. **Técnicas Avançadas**
- Manipulação de funções para contornar limitações computacionais
- Visualização de convergência em espaços complexos
- Análise de estabilidade numérica

## 📚 Conteúdo Programático

### **Módulo 1: Fundamentos de Precisão Numérica**
- **Exercício 1**: Algoritmo de precisão da máquina
  - Explora os limites da representação em ponto flutuante
  - Demonstra por que algoritmos terminam ou não
  - Introduz conceitos de epsilon da máquina

### **Módulo 2: Análise de Polinômios**
- **Exercício 2**: Cotas de Cauchy, Lagrange e Fujiwara
  - Teoria de localização de raízes
  - Implementação de algoritmos de cota
  - Comparação de precisão entre diferentes métodos

- **Exercícios 3-4**: Construção e análise de polinômios
  - Construção de polinômios a partir de raízes
  - Aplicação do método da bissecção
  - Análise de múltiplas raízes e suas implicações

### **Módulo 3: Métodos Iterativos Clássicos**
- **Exercícios 5-6**: Método de Newton para raízes n-ésimas
  - Implementação para raiz quadrada e cúbica
  - Análise de convergência
  - Comparação com métodos alternativos

- **Exercício 7**: Técnicas de manipulação de funções
  - Transformação de domínios para contornar limitações
  - Análise de comportamento em diferentes intervalos

### **Módulo 4: Avaliação Eficiente de Polinômios**
- **Exercício 8**: Método de Horner
  - Algoritmo eficiente para avaliação polinomial
  - Análise de complexidade computacional
  - Implementação e testes

### **Módulo 5: Métodos Avançados**
- **Exercício 9**: Método da Secante
  - Aproximação de derivadas
  - Análise de convergência
  - Comparação com Newton-Raphson

- **Exercício 10**: Método de Horner Modificado
  - Cálculo simultâneo de polinômio e derivada
  - Aplicação no método de Newton
  - Otimização computacional

### **Módulo 6: Números Complexos e Visualização**
- **Exercício 11**: Newton-Raphson Complexo
  - Extensão para domínio complexo
  - Análise de convergência em ℂ
  - Implementação com números complexos

- **Exercício 12**: Conjuntos de Julia e Fractais de Newton
  - Visualização de convergência
  - Análise de bacias de atração
  - Criação de fractais matemáticos

## 🔧 Ferramentas e Conceitos Utilizados

### **Conceitos Matemáticos**
- **Análise Numérica**: Precisão, estabilidade, convergência
- **Álgebra Linear**: Avaliação de polinômios, sistemas lineares
- **Análise Complexa**: Raízes complexas, convergência em ℂ
- **Teoria de Polinômios**: Cotas de raízes, fatoração

### **Algoritmos Implementados**
- **Método da Bissecção**: O(log₂(1/ε)) iterações
- **Método de Newton**: Convergência quadrática
- **Método da Secante**: Ordem de convergência ≈ 1.618
- **Método de Horner**: O(n) para avaliação polinomial

### **Técnicas de Programação**
- **Análise de Precisão**: Identificação de erros numéricos
- **Otimização**: Algoritmos eficientes para problemas específicos
- **Visualização**: Gráficos de convergência e fractais
- **Debugging Numérico**: Identificação de instabilidades

## 📈 Níveis de Dificuldade

### **Básico (Exercícios 1-4)**
- Conceitos fundamentais de precisão numérica
- Implementação de métodos básicos
- Análise de polinômios simples

### **Intermediário (Exercícios 5-9)**
- Métodos iterativos clássicos
- Otimização de algoritmos
- Análise de convergência

### **Avançado (Exercícios 10-12)**
- Técnicas avançadas de avaliação polinomial
- Números complexos e análise em ℂ
- Visualização matemática e fractais

## 🎓 Competências Desenvolvidas

### **Técnicas**
- Implementação de algoritmos numéricos
- Análise de precisão e estabilidade
- Otimização de código para problemas específicos
- Visualização de resultados matemáticos

### **Teóricas**
- Compreensão de limites computacionais
- Análise de convergência de métodos iterativos
- Teoria de localização de raízes
- Propriedades de polinômios

### **Práticas**
- Debugging de problemas numéricos
- Escolha adequada de métodos para problemas específicos
- Interpretação de resultados computacionais
- Documentação de algoritmos numéricos

## 🔗 Conexões com Outras Disciplinas

### **Matemática**
- **Análise Numérica**: Base teórica dos métodos
- **Álgebra Linear**: Sistemas de equações
- **Análise Complexa**: Raízes complexas
- **Teoria de Polinômios**: Propriedades algébricas

### **Computação**
- **Estruturas de Dados**: Representação de polinômios
- **Análise de Algoritmos**: Complexidade computacional
- **Programação Científica**: Implementação eficiente
- **Visualização**: Gráficos e fractais

### **Física e Engenharia**
- **Modelagem Matemática**: Equações diferenciais
- **Simulação Numérica**: Solução de problemas físicos
- **Otimização**: Encontrar valores ótimos
- **Análise de Sistemas**: Estabilidade e convergência

## 📖 Bibliografia Sugerida

### **Livros Fundamentais**
- "Numerical Analysis" - Burden & Faires
- "Numerical Recipes" - Press et al.
- "Introduction to Numerical Analysis" - Stoer & Bulirsch

### **Recursos Online**
- [Wikipedia - Geometrical Properties of Polynomial Roots](https://en.wikipedia.org/wiki/Geometrical_properties_of_polynomial_roots)
- [Paul Bourke - Newton-Raphson Fractals](https://paulbourke.net/fractals/newtonraphson/)
- [Mitch Ritchling - Newton Fractals](https://www.mitchr.me/SS/newton/)

### **Ferramentas Computacionais**
- **Python**: NumPy, SciPy, Matplotlib
- **MATLAB**: Toolbox de Análise Numérica
- **Julia**: Pacotes de Computação Científica
- **C/C++**: Bibliotecas de Matemática

---

**Nota**: Esta lista de exercícios fornece uma base sólida em métodos numéricos, preparando o estudante para problemas mais complexos em computação científica, engenharia e pesquisa aplicada.
