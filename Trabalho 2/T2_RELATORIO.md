# Métodos Numéricos - Trabalho 2

Aluno: Bernardo Klein Heitz

## 1. Resultado

    Aplicando interpolação polinomial aos dados fornecidos, conseguimos o resultado, que para um peru de 6.22 kg precisamaos de t (6.22) = 178.09 minutos, o que da aproximadamente 2h e 58 min para assar ele a 230 °C.

## 2. Interpolação Numérica

### 2.1 Dados de referência

| Peso em kg | Tempo de cozimento | Tempo em minutos |
| ---------- | ------------------ | ---------------- |
| 3.0        | 1 h 23 min         | 83               |
| 5.0        | 2 h 26 min         | 146              |
| 7.0        | 3 h 17 min         | 197              |
| 9.0        | 4 h 03 min         | 243              |

O valor de tempo que é procurado dentro deste intervalo, é o correpondente ao tempo de 6.22 kg.

### 2.2 Interpolação de lagrange

    O polinômio interpolador foi construído com a forma padrão.

    Utilizando laços duplos em python para calcular os termos de cada$L_i(x)$. A avaliação de $L(6.22)$ forneceu 178.09 minutos.

### 2.3 Interpolação de newton

    Também implementamos as diferenças divididas de newton. A primeira linha da tabela gera o polinômio

$$
N(x) = F[0,0] + F[0,1](x - x_0) + F[0,2](x - x_0)(x - x_1) + F[0,3](x - x_0)(x - x_1)(x - x_2)
$$

    Avaliar$N(6.22)$ resultou no mesmo valor, confirmando que ambos os métodos produzem o polinômio cúbico único que passa pelos quatro pontos.

### 2.4 Verificações

    O polinômio reproduziu exatamente os valores conhecidos em 3.0 kg, 5.0 kg, 7.0 kg e 9.0 kg

    Uma interpolação linear simples entre 5.0 kg e 7.0 kg geraria 177.1 minutos, próximo mas ligeiramente inferior ao valor polinomial

    Como 6.22 kg está dentro do intervalo da tabela, tratamos de fato de uma interpolação, com menor risco de erro do que uma extrapolação

## 3. Avaliação do uso de ia

### 3.1 Experiência com chatgpt

Ao enviar o prompt com a tabela original, o chatgpt:

interpretou o problema rapidamente

montou o polinômio interpolador completo

apresentou $P(6.22) = 178.09$ minutos

Ponto positivo: a resposta foi direta e correta, facilitando a validação. Limitação: o modelo não detalhou o passo a passo das diferenças divididas nem exibiu os cálculos intermediários da base de lagrange.

### 3.2 Como obtivemos o resultado

implementamos a fórmula de lagrange em python com dois laços aninhados

construímos a tabela de diferenças divididas e o polinômio de newton como checagem independente

avaliamos ambos os polinômios no ponto 6.22 kg

validamos os polinômios nos pontos conhecidos para garantir erro numérico desprezível

### 3.3 Comparação

| Método                     | Resultado      | Diferença |
| --------------------------- | -------------- | ---------- |
| Interpolação implementada | 178.09 minutos | -          |
| chatgpt                     | 178.09 minutos | 0.00 min   |

    A coincidência total mostra que o uso da ia foi adequado para conferência e reforça a correção da implementação própria.

## 4. Conclusão

    O estudo cumpriu as três etapas solicitadas: determinamos t(6.22) com interpolação (lagrange e newton), comparamos com uma ferramenta de ia e documentamos o processo. A estimativa de 178.09 minutos é consistente com os dados originais e reforça a utilidade da interpolação polinomial em situações onde poucos pontos de referência estão disponíveis, sem dispensar a necessidade de compreender e implementar os métodos manualmente.
