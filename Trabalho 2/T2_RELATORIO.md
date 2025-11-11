# Métodos Numéricos - Trabalho 2

Aluno: Bernardo Klein Heitz

## 1. Resultado

aplicando interpolação polinomial aos dados fornecidos, obtivemos t(6.22) = 178.09 minutos para um peru de 6.22 kg, equivalente a cerca de 2 h 58 min a 230 °c.

## 2. Interpolação Numérica

### 2.1 Dados de referência

| peso em kg | tempo de cozimento | tempo em minutos |
| ---------- | ------------------ | ---------------- |
| 3.0        | 1 h 23 min         | 83               |
| 5.0        | 2 h 26 min         | 146              |
| 7.0        | 3 h 17 min         | 197              |
| 9.0        | 4 h 03 min         | 243              |

procuramos o tempo correspondente a 6.22 kg, valor que está no interior do intervalo amostrado.

### 2.2 Interpolação de lagrange

o polinômio interpolador foi construído na forma

$$
L(x) = \sum_{i=0}^{3} y_i \cdot L_i(x), \quad L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{3} \frac{x - x_j}{x_i - x_j}
$$

utilizando laços duplos em python para calcular cada termo $L_i(x)$. a avaliação de $L(6.22)$ forneceu 178.09 minutos.

### 2.3 Interpolação de newton

também implementamos as diferenças divididas de newton. a primeira linha da tabela gera

$$
N(x) = F[0,0] + F[0,1](x - x_0) + F[0,2](x - x_0)(x - x_1) + F[0,3](x - x_0)(x - x_1)(x - x_2)
$$

avaliar $N(6.22)$ resultou no mesmo valor, confirmando que os dois métodos produzem o polinômio cúbico único que passa pelos quatro pontos conhecidos.

### 2.4 Verificações

- o polinômio reproduziu exatamente os valores de 3.0 kg, 5.0 kg, 7.0 kg e 9.0 kg
- uma interpolação linear entre 5.0 kg e 7.0 kg gera 177.1 minutos, valor próximo porém ligeiramente menor que o polinomial
- como 6.22 kg está dentro do intervalo da tabela, tratamos de uma interpolação, reduzindo o risco de erro frente a uma extrapolação

## 3. Avaliação do uso de ia

### 3.1 Experiência com chatgpt

ao enviar o prompt com a tabela original, o chatgpt:

- interpretou o problema rapidamente
- montou o polinômio interpolador completo
- apresentou $P(6.22) = 178.09$ minutos

ponto positivo: a resposta foi direta e correta, facilitando a validação. limitação: a ia não detalhou o passo a passo das diferenças divididas nem exibiu os cálculos intermediários da base de lagrange.

### 3.2 Como obtivemos o resultado

- implementamos a fórmula de lagrange em python com dois laços aninhados
- construímos a tabela de diferenças divididas e o polinômio de newton como checagem independente
- avaliamos ambos os polinômios no ponto 6.22 kg
- validamos os polinômios nos pontos conhecidos para garantir erro numérico desprezível

### 3.3 Comparação

| método                     | resultado      | diferença |
| --------------------------- | -------------- | ---------- |
| interpolação implementada | 178.09 minutos | -          |
| chatgpt                     | 178.09 minutos | 0.00 min   |

a igualdade dos resultados confirma que o uso da ia foi adequado para conferir o cálculo e reforça a correção da implementação própria.

## 4. Conclusão

o estudo cumpriu as três etapas solicitadas: determinamos t(6.22) com interpolação (lagrange e newton), comparamos com uma ferramenta de ia e registramos o processo. a estimativa de 178.09 minutos é consistente com os dados originais e reforça a utilidade da interpolação polinomial em cenários com poucos pontos de referência, sem dispensar o entendimento e a implementação manual dos métodos.
