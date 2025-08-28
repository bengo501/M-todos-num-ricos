# Resumo dos Resultados - Métodos Numéricos

## Exercício 1: Precisão da Máquina
**Resultado**: O algoritmo termina após **53 iterações**
- **Epsilon da máquina**: 1.1102230246251565e-16
- **Significado**: Este é o menor número tal que 1 + ε > 1
- **Conclusão**: Demonstra os limites da precisão numérica em ponto flutuante

## Exercício 2: Cotas para Raízes de Polinômios
**Polinômio**: p(x) = 6x⁵ + 18x³ - 34x² - 493x + 1431

| Cota | Valor | Observação |
|------|-------|------------|
| Cauchy | 330.333333 | Mais conservadora |
| Lagrange | 3.415122 | **Mais precisa** |
| Fujiwara | 6.021489 | Intermediária |

**Conclusão**: Todas as raízes estão dentro do círculo de raio **3.415122**

## Exercício 3: Polinômio com Raízes 2, 3, 4
**Polinômio criado**: p(x) = (x-2)(x-3)(x-4) = x³ - 9x² + 26x - 24
- **Raiz encontrada**: 3.0000000000
- **Iterações**: 0 (convergência imediata)
- **Conclusão**: Método da bissecção encontra apenas UMA raiz no intervalo [1, 5]

## Exercício 4: Polinômio com Raízes 2, 3, 4, 5
**Polinômio criado**: p(x) = (x-2)(x-3)(x-4)(x-5) = x⁴ - 14x³ + 71x² - 154x + 120
- **Método original**: Não convergiu no intervalo [1, 6]
- **Algoritmo adaptado**: Encontrou todas as 4 raízes: [2.0, 3.0, 4.0, 5.0]
- **Conclusão**: Divisão em subintervalos permite encontrar múltiplas raízes

## Exercício 5: Método de Newton para Raiz Quadrada
**Fórmula**: x_{n+1} = (x_n + p/x_n)/2

| Valor | Resultado | Iterações | Erro |
|-------|-----------|-----------|------|
| √2 | 1.4142135624 | 4 | 2.22e-16 |
| √9 | 3.0000000000 | 4 | 0.00e+00 |
| √16 | 4.0000000000 | 5 | 0.00e+00 |
| √25 | 5.0000000000 | 5 | 0.00e+00 |
| √100 | 10.0000000000 | 7 | 0.00e+00 |

**Conclusão**: Convergência quadrática rápida e precisa

## Exercício 6: Método de Newton para Raiz Cúbica
**Fórmula**: x_{n+1} = (2x_n³ + p)/(3x_n²)

| Valor | Resultado | Iterações | Erro |
|-------|-----------|-----------|------|
| ∛8 | 2.0000000000 | 5 | 0.00e+00 |
| ∛27 | 3.0000000000 | 7 | 0.00e+00 |
| ∛64 | 4.0000000000 | 8 | 4.44e-16 |
| ∛125 | 5.0000000000 | 10 | 8.88e-16 |
| ∛1000 | 10.0000000000 | 13 | 1.78e-15 |

**Conclusão**: Método eficiente para raízes cúbicas

## Exercício 7: Transformação f(1/x)
**Função original**: f(x) = 8x⁴ - 238x³ + 1047x² - 953x + 154
**Função transformada**: g(x) = f(1/x)
- **Raiz de g(x)**: 0.25299
- **Raiz de f(x)**: 3.952732
- **Conclusão**: Transformação permite visualizar comportamento fora do intervalo [-1, 1]

## Exercício 8: Algoritmo de Horner
**Polinômio**: p(x) = x⁵ + 18x³ + 34x² - 493x + 1431

| x | p(x) |
|---|------|
| -2 | 2377 |
| -1 | 1939 |
| 0 | 1431 |
| 1 | 991 |
| 2 | 757 |
| 5 | 5191 |
| 10 | 117901 |

**Conclusão**: Algoritmo de Horner é eficiente para avaliação de polinômios

## Exercício 9: Método da Secante
**Análise teórica**: Máximo 2 raízes reais positivas (teorema de Descartes)
**Resultados**:
- Pontos iniciais (0, 1): raiz = -4.813582 (44 iterações)
- Pontos iniciais (5, 6): raiz = -4.813582 (36 iterações)
- Pontos iniciais (10, 11): raiz = -4.813582 (60 iterações)

**Conclusão**: Método converge para a mesma raiz real, independente dos pontos iniciais

## Exercício 10: Algoritmo de Horner com Derivada
**Algoritmo modificado calcula simultaneamente**:
- p(x): valor do polinômio
- p'(x): valor da derivada

| x | p(x) | p'(x) |
|---|------|-------|
| -2 | 2377 | -333 |
| -1 | 1939 | -502 |
| 0 | 1431 | -493 |
| 1 | 991 | -366 |
| 2 | 757 | -61 |

**Conclusão**: Preparação ideal para método de Newton

## Exercício 11: Método de Newton com Números Complexos
**Raízes encontradas**:
1. 2.501703 + 1.645720j
2. 2.501703 - 1.645720j

**Conclusão**: Método de Newton funciona no plano complexo, encontrando raízes complexas

## Conceitos Matemáticos Demonstrados

### 1. **Precisão Numérica**
- Epsilon da máquina e limites da aritmética de ponto flutuante
- Importância da tolerância em métodos iterativos

### 2. **Teoremas de Cotas**
- Cauchy, Lagrange e Fujiwara para localização de raízes
- Comparação de diferentes métodos de estimativa

### 3. **Métodos Iterativos**
- **Bissecção**: Convergência linear, robusto
- **Newton**: Convergência quadrática, rápido
- **Secante**: Sem necessidade de derivada

### 4. **Polinômios**
- Construção a partir de raízes conhecidas
- Avaliação eficiente com algoritmo de Horner
- Cálculo simultâneo de função e derivada

### 5. **Números Complexos**
- Extensão de métodos para plano complexo
- Busca de raízes complexas

### 6. **Transformações**
- Mapeamento de domínios para visualização
- Técnica f(1/x) para plotagem restrita

## Observações Importantes

1. **Convergência**: Todos os métodos implementados convergem adequadamente
2. **Precisão**: Erros na ordem de 10⁻¹⁶ para métodos de Newton
3. **Robustez**: Tratamento de casos especiais (divisão por zero, etc.)
4. **Eficiência**: Algoritmo de Horner é computacionalmente eficiente
5. **Flexibilidade**: Métodos adaptáveis para diferentes cenários

## Aplicações Práticas

- **Engenharia**: Cálculo de raízes em problemas físicos
- **Computação**: Algoritmos de precisão numérica
- **Matemática**: Análise de polinômios e funções
- **Visualização**: Fractais e comportamento de métodos iterativos

Este conjunto de exercícios demonstra uma compreensão completa dos fundamentos de métodos numéricos para solução de equações, desde conceitos básicos de precisão até técnicas avançadas com números complexos.
