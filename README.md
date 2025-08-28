# Métodos Numéricos - Solução de Equações

Este projeto contém a implementação completa dos exercícios de Métodos Numéricos sobre solução de equações.

## Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas Python listadas em `requirements.txt`

## Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução

Para executar todos os exercícios:
```bash
python solucao_exercicios.py
```

## Estrutura dos Exercícios

### Exercício 1: Precisão da Máquina
- **Objetivo**: Implementa algoritmo para encontrar a precisão da máquina
- **Conceitos**: Epsilon da máquina, aritmética de ponto flutuante
- **Resposta**: O algoritmo termina após um número finito de iterações, encontrando o menor número tal que 1 + ε > 1

### Exercício 2: Cotas de Cauchy, Lagrange e Fujiwara
- **Objetivo**: Calcula cotas para as raízes do polinômio p(x) = 6x⁵ + 18x³ - 34x² - 493x + 1431
- **Conceitos**: Teoremas de cotas para raízes de polinômios
- **Implementação**: Três métodos diferentes de cálculo de cotas

### Exercício 3: Polinômio com Raízes Conhecidas e Bissecção
- **Objetivo**: Cria polinômio com raízes 2, 3, 4 e aplica método da bissecção
- **Conceitos**: Construção de polinômios, método da bissecção
- **Resultado**: Encontra apenas uma raiz no intervalo [1, 5]

### Exercício 4: Múltiplas Raízes e Adaptação do Algoritmo
- **Objetivo**: Cria polinômio com raízes 2, 3, 4, 5 e adapta algoritmo para múltiplas raízes
- **Conceitos**: Divisão de intervalos, busca sistemática de raízes
- **Implementação**: Algoritmo adaptado que divide o intervalo em subintervalos

### Exercício 5: Método de Newton para Raiz Quadrada
- **Objetivo**: Implementa método de Newton para calcular raiz quadrada
- **Conceitos**: Método de Newton, convergência quadrática
- **Fórmula**: x_{n+1} = (x_n + p/x_n)/2

### Exercício 6: Método para Raiz Cúbica
- **Objetivo**: Implementa método de Newton para calcular raiz cúbica
- **Conceitos**: Extensão do método de Newton para raízes cúbicas
- **Fórmula**: x_{n+1} = (2x_n³ + p)/(3x_n²)

### Exercício 7: Transformação f(1/x) para Plotagem Restrita
- **Objetivo**: Resolve problema de plotagem restrita usando transformação
- **Conceitos**: Transformação de coordenadas, mapeamento de domínios
- **Aplicação**: Encontra raízes de f(x) = 8x⁴ - 238x³ + 1047x² - 953x + 154

### Exercício 8: Algoritmo de Horner
- **Objetivo**: Analisa e implementa algoritmo de Horner
- **Conceitos**: Avaliação eficiente de polinômios
- **Polinômio**: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431

### Exercício 9: Método da Secante
- **Objetivo**: Implementa método da secante para encontrar raízes reais
- **Conceitos**: Método da secante, análise de raízes reais
- **Vantagem**: Não requer cálculo de derivada

### Exercício 10: Algoritmo de Horner com Derivada
- **Objetivo**: Analisa algoritmo modificado que calcula polinômio e derivada
- **Conceitos**: Cálculo simultâneo de função e derivada
- **Aplicação**: Preparação para método de Newton

### Exercício 11: Método de Newton com Números Complexos
- **Objetivo**: Implementa método de Newton para números complexos
- **Conceitos**: Extensão para plano complexo, raízes complexas
- **Resultado**: Encontra todas as raízes (reais e complexas)

### Exercício 12: Fractais de Newton
- **Objetivo**: Gera fractais de Newton para polinômio com raízes conhecidas
- **Conceitos**: Fractais, convergência de métodos iterativos
- **Visualização**: Mapa de cores mostrando convergência para diferentes raízes

## Saídas Esperadas

O programa gera:
1. **Saída textual**: Resultados detalhados de cada exercício
2. **Gráfico**: Fractal de Newton salvo como `fractal_newton.png`

## Conceitos Matemáticos Abordados

- **Precisão numérica**: Epsilon da máquina
- **Teoremas de cotas**: Cauchy, Lagrange, Fujiwara
- **Métodos iterativos**: Bissecção, Newton, Secante
- **Polinômios**: Construção, avaliação, raízes
- **Números complexos**: Extensão de métodos para plano complexo
- **Fractais**: Comportamento de métodos iterativos

## Observações Importantes

1. **Convergência**: Todos os métodos implementados incluem critérios de parada
2. **Precisão**: Tolerâncias configuráveis para cada método
3. **Robustez**: Tratamento de casos especiais (divisão por zero, etc.)
4. **Visualização**: Gráficos para melhor compreensão dos conceitos

## Autor

Implementação completa dos exercícios de Métodos Numéricos sobre solução de equações.
