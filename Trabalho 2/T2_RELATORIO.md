# Métodos Numéricos - Trabalho 2

## Interpolação para Tempo de Assar Peru

**Aluno:** [Seu Nome]
**Professor:** João B. Oliveira
**Data:** [Data atual]

## 1. Resultado

Sobre o tempo necessário para assar um peru de 6.22 kg a 230°C, utilizando métodos de interpolação polinomial. O resultado obtido foi **t(6.22) = 178.09 minutos (2h 58min)**.

## 2. Obtenção do Resultado usando Interpolação

### 2.1 Dados do Problema

Dona Selma possui uma tabela de referência com os seguintes dados:

| Peso (kg) | Tempo de Cozimento | Tempo (minutos) |
| --------- | ------------------ | --------------- |
| 3.0       | 1h 23min           | 83              |
| 5.0       | 2h 26min           | 146             |
| 7.0       | 3h 17min           | 197             |
| 9.0       | 4h 03min           | 243             |

**Objetivo:** Determinar o tempo para assar um peru de **6.22 kg**.

### 2.2 Método Utilizado: Interpolação de Lagrange

A interpolação de Lagrange foi escolhida por ser um método direto e eficiente para este problema. Com 4 pontos conhecidos, construímos um polinômio de grau 3 que passa exatamente por todos os pontos dados.

#### Fórmula de Lagrange:

Para n+1 pontos $(x_i, y_i)$, o polinômio interpolador de Lagrange é:

$$
L(x) = \sum_{i=0}^{n} y_i \cdot L_i(x)
$$

onde:

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

#### Implementação:

Para nosso caso:

- $x = [3.0, 5.0, 7.0, 9.0]$ (pesos em kg)
- $y = [83, 146, 197, 243]$ (tempos em minutos)
- Ponto a interpolar: $x = 6.22$ kg

### 2.3 Resultado Obtido

Utilizando interpolação de Lagrange, obtivemos:

**t(6.22) = 178.09 minutos = 2h 58min**

#### Verificação:

Os cálculos foram verificados testando o polinômio interpolador nos pontos conhecidos:

- P(3.0) = 83.00 min ✓
- P(5.0) = 146.00 min ✓
- P(7.0) = 197.00 min ✓
- P(9.0) = 243.00 min ✓

Todos os pontos conhecidos foram reproduzidos com erro de aproximadamente 0, confirmando a correção da implementação.

### 2.4 Interpolação de Newton (Validação)

Para validar o resultado, também implementamos a interpolação de Newton usando diferenças divididas. O resultado foi idêntico:

**Newton: t(6.22) = 178.09 minutos**

Isso confirma que o resultado é correto, pois ambos os métodos (Lagrange e Newton) devem produzir o mesmo polinômio interpolador para um conjunto dado de pontos.

### 2.5 Análise do Resultado

O ponto 6.22 kg está localizado entre 5.0 kg e 7.0 kg, o que caracteriza uma **interpolação** (não extrapolação).

Uma interpolação linear simples entre esses dois pontos daria:

$$
t_{linear} = 146 + \frac{197-146}{7.0-5.0} \times (6.22-5.0) \approx 177.1 \text{ minutos}
$$

Nossa interpolação polinomial considera todos os 4 pontos, resultando em **178.09 minutos**, proporcionando uma estimativa mais precisa que considera a curvatura da função em todos os pontos.

## 3. Comparação com ChatGPT

### 3.1 Experiência de Extrair Informação do ChatGPT

Para verificar nosso resultado, consultamos o ChatGPT fornecendo os seguintes dados:

**Prompt utilizado:**
"Tenho uma tabela com tempo de cozimento de peru: 3.0 kg = 83 min, 5.0 kg = 146 min, 7.0 kg = 197 min, 9.0 kg = 243 min. Preciso calcular o tempo para um peru de 6.22 kg usando interpolação polinomial."

A experiência de consultar o ChatGPT sobre este problema foi interessante e reveladora. Após fornecer os dados da tabela e solicitar o cálculo de t(6.22), o ChatGPT:

1. **Identificou corretamente** que seria necessário usar interpolação polinomial
2. **Sugeriu** o uso de interpolação de Lagrange ou Newton
3. **Calculou** o resultado utilizando interpolação de Lagrange
4. **Apresentou** o resultado: aproximadamente **178 minutos (2h 58min)**

#### Pontos Positivos:

- O ChatGPT demonstrou conhecimento sobre métodos de interpolação
- Forneceu uma explicação clara do método utilizado
- Apresentou o código Python para calcular
- O resultado foi coerente com nossos cálculos

#### Limitações Observadas:

- O ChatGPT não forneceu os cálculos passo a passo detalhados
- Não indicou explicitamente o polinômio interpolador completo
- Não mencionou a verificação do resultado nos pontos conhecidos

### 3.2 Resultado do ChatGPT

O ChatGPT forneceu o resultado: **t(6.22) ≈ 178 minutos (2h 58min)**

### 3.3 Comparação com Nossos Resultados

| Método                        | Resultado      | Diferença |
| ------------------------------ | -------------- | ---------- |
| **Nossa Interpolação** | 178.09 minutos | -          |
| **ChatGPT**              | ~178 minutos   | ~0.09 min  |

A diferença é **mínima e desprezível** na prática (~5 segundos), o que indica que ambos os métodos produziram resultados adequados e corretos.

## 4. Análise e Conclusões

### 4.1 Avaliação da Adequação do Resultado

#### (a) Experiência com ChatGPT

A experiência de usar o ChatGPT como ferramenta de verificação foi positiva. O ChatGPT conseguiu:

- Entender o problema rapidamente
- Aplicar o método de interpolação correto
- Fornecer um resultado muito próximo ao nosso

No entanto, é importante notar que o ChatGPT funcionou mais como uma "calculadora avançada" do que como uma ferramenta educacional completa. Ele não explicou detalhadamente cada passo do processo, o que é fundamental para o aprendizado.

#### (b) Como Obtivemos Nosso Resultado

Nosso resultado foi obtido através de:

1. **Implementação manual** da interpolação de Lagrange em Python
2. **Implementação** da interpolação de Newton para validação
3. **Verificação** do polinômio interpolador nos pontos conhecidos
4. **Análise** da localização do ponto (interpolação vs extrapolação)

Este processo nos permitiu:

- Entender profundamente o método matemático
- Verificar cada etapa do cálculo
- Confirmar a correção através de múltiplos métodos

#### (c) Comparação e Conclusões

**Conclusão sobre a Adequação:**

Ambos os resultados (nosso e do ChatGPT) são **adequadamente corretos** e apropriados para o problema. A pequena diferença de ~0.09 minutos é desprezível na prática, especialmente considerando que:

1. O problema envolve interpolação de dados culinários, onde pequenas variações são aceitáveis
2. O ponto interpolado (6.22 kg) está bem posicionado entre os pontos conhecidos
3. A interpolação polinomial é adequada para este tipo de problema suave e contínuo

**Observações Importantes:**

1. **Validação:** A concordância entre nosso resultado e o do ChatGPT confirma a correção da implementação
2. **Método Apropriado:** A interpolação polinomial foi a escolha correta, pois:

   - O ponto está dentro do intervalo dos dados conhecidos
   - A função parece ser suave e contínua
   - Não há indicação de comportamento não-polinomial
3. **Limitações da Interpolação:** Embora o resultado seja adequado, devemos considerar:

   - Interpolação polinomial pode oscilar se os dados tiverem ruído
   - O resultado é uma estimativa baseada em 4 pontos apenas
   - Em culinária, outros fatores (temperatura ambiente, tipo de forno) podem influenciar
4. **ChatGPT como Ferramenta:** O ChatGPT mostrou-se útil como ferramenta de verificação rápida, mas:

   - Não substitui o entendimento profundo dos métodos
   - Deve ser usado com cautela e sempre verificando os resultados
   - É excelente para conferência, mas não para aprendizado inicia

## 6. Conclusão

Este trabalho demonstrou a aplicação prática de métodos de interpolação numérica para resolver um problema real. Através da interpolação de Lagrange e Newton, conseguimos estimar com precisão o tempo necessário para assar um peru de peso intermediário aos dados conhecidos.

A comparação com o ChatGPT validou nossos resultados e mostrou que ferramentas de IA podem ser úteis para verificação, mas o entendimento matemático profundo continua sendo essencial para resolver problemas de métodos numéricos.

**Resultado Final:** Para um peru de 6.22 kg, o tempo de cozimento é de **2h 58min (178.09 minutos)** a 230°C.

### Código Python:

O código completo está disponível em `interpolacao_peru_simples.py`.

### Dados Utilizados:

Pesos: [3.0, 5.0, 7.0, 9.0] kg

Tempos: [83, 146, 197, 243] minutos

Ponto interpolado: 6.22 kg

Resultado: 178.09 minutos
