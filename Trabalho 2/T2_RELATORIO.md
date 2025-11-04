# Métodos Numéricos - Trabalho 2

Aluno: Bernardo Klein Heitz
Professor: João B. Oliveira
Data: 04/11/2025

## 1. Resultado

Para assar um peru de 6.22 kg a 230°C, utilizando métodos de interpolação polinomial,o resultado obtido foi t(6.22) = 178.09 minutos (2h 58min).

## 2. Obtenção do Resultado usando Interpolação

### 2.1 Dados do Problema

Tabela de referência:

| Peso (kg) | Tempo de Cozimento | Tempo (minutos) |
| --------- | ------------------ | --------------- |
| 3.0       | 1h 23min           | 83              |
| 5.0       | 2h 26min           | 146             |
| 7.0       | 3h 17min           | 197             |
| 9.0       | 4h 03min           | 243             |

Devesse determinar o tempo para assar um peru de 6.22 kg.

### 2.2 Método Utilizado: Interpolação de Lagrange

A interpolação de Lagrange foi escolhida por ser um método direto e eficiente para este problema. Com 4 pontos conhecidos, construímos um polinômio de grau 3 que passa exatamente por todos os pontos dados.

#### Implementação:

Para o caso:

Ponto a interpolar: x = 6.22 kg

Pesos (x): [3.0, 5.0, 7.0, 9.0]

Tempos (y): [83, 146, 197, 243]

### 2.3 Resultado Obtido

Utilizando interpolação de Lagrange:

t(6.22) = 178.09 minutos = 2h 58min

#### Verificação:

Os cálculos foram verificados testando o polinômio interpolador nos pontos conhecidos:

P(3.0) = 83.00 min

P(5.0) = 146.00 min

P(7.0) = 197.00 min

P(9.0) = 243.00 min

Todos os valores foram reproduzidos com mínimo erro numérico, o que validou a implementação.

### 2.4 Interpolação de Newton

    Para validar o resultado, também foi implementado a interpolação de Newton usando diferenças divididas. O resultado foi idêntico:

Newton: t(6.22) = 178.09 minutos

    Dessa forma, é possível confirmar que o resultado está correto, pois os dois métodos devem produzir o mesmo polinômio interpolador para um conjunto dado de pontos.

### 2.5 Análise do Resultado

    O ponto 6.22 kg está localizado entre 5.0 kg e 7.0 kg. Uma interpolação linear simples entre esses dois pontos daria:

tlinear≈177,1 minutos

    Essa interpolação polinomial considera todos os 4 pontos, resultando em 178.09 minutos. Desse jeito, considera a curvatura da função em todos os pontos o que o torna teoricamente mais preciso.

## 3. Avaliação da Adequação do Resultado

#### (a) Experiência com ChatGPT

Para verificar o resultado com o ChatGPT, forneci os seguintes dados:

Prompt utilizado:
"Tenho uma tabela com tempo de cozimento de peru: 3.0 kg = 83 min, 5.0 kg = 146 min, 7.0 kg = 197 min, 9.0 kg = 243 min. Preciso calcular o tempo para um peru de 6.22 kg usando interpolação polinomial."

A experiência de usar o ChatGPT como ferramenta de verificação foi muito positiva. O ChatGPT conseguiu:

Entender o problema rapidamente.

Aplicar corretamente o método de interpolação polinomial.

Fornecer o polinômio interpolador completo.

Encontrar um resultado igual ao encontrado com a implementação: 178.09 minutos

**Obervações positivas:**

    O ChatGPT foi muito eficiente e preciso. Ele forneceu o resultado e mostrou o polinômio interpolador completo:

P(x)=0.14583333x3−3.68750000x2+53.85416667x−49.31250000.

    E avaliou P(6.22) = 178.09 isso permitiu verificar que ele realmente calculou o polinômio de grau 3 que passa pelos 4 pontos dados.

**Limitações observadas:**

    Embora o gpt tenha sido muito bom, ele não forneceu os cálculos passo a passo detalhados, como as diferenças divididas no método de Newton ou a construção dos polinômios base de Lagrange. Ele apenas focou no resultado.

#### (b) Como Obtivemos Nosso Resultado

O resultado da implementação foi obtido:

**1. Implementação manual da interpolação de Lagrange em Python:**

    Utilizamos a fórmula de Lagrange para construir um polinômio de grau 3 que passa pelos 4 pontos conhecidos (3.0, 83), (5.0, 146), (7.0, 197), (9.0, 243).

    A implementação funciona da seguinte forma: para cada ponto$i$ (onde $i = 0, 1, 2, 3$), calculamos o polinômio base de Lagrange $L_i(x)$ usando a fórmula:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{3} \frac{x - x_j}{x_i - x_j}
$$

Por exemplo, para $i = 0$ (ponto $x_0 = 3.0$), calculamos:

$$
L_0(x) = \frac{(x - 5.0)(x - 7.0)(x - 9.0)}{(3.0 - 5.0)(3.0 - 7.0)(3.0 - 9.0)}
$$

O polinômio interpolador completo é então construído como:

$$
L(x) = \sum_{i=0}^{3} y_i \cdot L_i(x) = 83 \cdot L_0(x) + 146 \cdot L_1(x) + 197 \cdot L_2(x) + 243 \cdot L_3(x)
$$

    A implementação em Python utiliza dois loops aninhados: o loop externo percorre todos os pontos$i$, e o loop interno calcula o produto dos termos $(x - x_j)/(x_i - x_j)$ para todos os $j \neq i$. Em seguida, multiplicamos cada $L_i(x)$ pelo valor correspondente $y_i$ e somamos todos os termos para obter o valor final do polinômio no ponto desejado $x = 6.22$ kg.

**2. Implementação da interpolação de Newton para validação:**

    Para confirmar o resultado, implementamos também o método de Newton usando diferenças divididas. Este método é baseado na construção de uma tabela de diferenças divididas, que é mais eficiente computacionalmente que Lagrange para adicionar novos pontos.

**O processo funciona da seguinte forma:**

Primeiro, construímos a tabela de diferenças divididas $F[i, j]$:

A primeira coluna ($j = 0$) contém os valores conhecidos: $F[i, 0] = y_i$ para $i = 0, 1, 2, 3$

As colunas subsequentes são calculadas usando a fórmula recursiva:

$$
F[i, j] = \frac{F[i+1, j-1] - F[i, j-1]}{x_{i+j} - x_i}
$$

Por exemplo:

Primeira diferença dividida: $F[0, 1] = \frac{F[1, 0] - F[0, 0]}{x_1 - x_0} = \frac{146 - 83}{5.0 - 3.0} = 31.5$

Segunda diferença dividida: $F[0, 2] = \frac{F[1, 1] - F[0, 1]}{x_2 - x_0}$

Até completar a tabela...

O polinômio interpolador de Newton é construído usando os coeficientes da primeira linha da tabela:

$$
N(x) = F[0, 0] + F[0, 1](x - x_0) + F[0, 2](x - x_0)(x - x_1) + F[0, 3](x - x_0)(x - x_1)(x - x_2)
$$

    Avaliando este polinômio no ponto$x = 6.22$ kg, obtivemos o resultado: 178.09 minutos. O fato de que ambos os métodos (Lagrange e Newton) produziram exatamente o mesmo resultado confirma que a implementação está correta, pois ambos devem gerar o mesmo polinômio interpolador único de grau 3 que passa pelos 4 pontos dados.

**3. Verificação do polinômio interpolador nos pontos conhecidos:**

Testamos o polinômio interpolador calculado em todos os pontos conhecidos da tabela:

P(3.0) = 83.00 min  	P(5.0) = 146.00 min	 P(7.0) = 197.00 min 	P(9.0) = 243.00 min

    Todos os valores foram reproduzidos com erro numérico mínimo (praticamente zero), validando que a implementação está correta.

**4. Análise da localização do ponto:**

    Verificamos que o ponto 6.22 kg está localizado entre 5.0 kg e 7.0 kg, caracterizando umainterpolação (não extrapolação), o que garante maior confiabilidade do resultado, pois o ponto está dentro do intervalo dos dados conhecidos.

#### (c) Comparação e Conclusões

**Comparação dos Resultados:**

| Método                     | Resultado      | Diferença |
| --------------------------- | -------------- | ---------- |
| Interpolação implementada | 178.09 minutos | -          |
| ChatGPT                     | 178.09 minutos | 0.00 min   |

**Observações Importantes:**

**Validação Perfeita:** A concordância **exata** (diferença zero) entre nosso resultado e o do ChatGPT confirma definitivamente a correção da implementação

**Método Apropriado:** A interpolação polinomial foi a escolha correta, pois:

O ponto está dentro do intervalo dos dados conhecidos

A função parece ser suave e contínua

Não há indicação de comportamento não-polinomial

## 4. Conclusão

    Este trabalho demonstrou a aplicação prática de métodos de interpolação numérica para resolver um problema real. Através da interpolação de Lagrange e Newton, conseguimos estimar com precisão o tempo necessário para assar um peru de peso intermediário aos dados conhecidos.

    A comparação com o ChatGPT validou nossos resultados de forma perfeita - ambos os métodos produziram resultadosidênticos (178.09 minutos), confirmando definitivamente a correção de nossa implementação. O ChatGPT também forneceu o polinômio interpolador completo, permitindo verificar que ele realmente calculou o polinômio de grau 3 correto. Isso mostra que ferramentas de IA podem ser muito útesis para verificação, mas o entendimento matemático profundo continua sendo essencial para resolver problemas de métodos numéricos.

Resultado Final:

    Para um peru de 6.22 kg, o tempo de cozimento é de 2h 58min (178.09 minutos) a 230°C.
