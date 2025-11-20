# Guia Visual Interativo - Documentação Completa

## Visão Geral
O **Guia Visual Interativo** foi expandido para cobrir todos os tópicos de métodos numéricos do curso. Esta aplicação web permite visualizar e interagir com os algoritmos em tempo real.

**Localização:** `Visualizacao_Web/index.html`

## Módulos Disponíveis

### 1. Sistemas Lineares (Decomposição LU)
- **O que faz:** Resolve sistemas lineares $Ax=b$ visualizando a decomposição da matriz $A$ em $L$ (Lower) e $U$ (Upper).
- **Interação:**
    - Edite os valores da matriz $A$ (padrão: Problema do Parquinho).
    - Clique em "Resolver LU" para ver as matrizes resultantes.

### 2. Mínimos Quadrados
- **O que faz:** Encontra a melhor reta que se ajusta a um conjunto de pontos (Regressão Linear).
- **Interação:**
    - Clique no gráfico para adicionar pontos dispersos.
    - A reta de regressão e o erro (MSE) são recalculados instantaneamente.

### 3. Interpolação Polinomial
- **O que faz:** Constrói o Polinômio de Lagrange que passa exatamente por todos os pontos dados.
- **Interação:**
    - Adicione pontos clicando no gráfico.
    - Observe o fenômeno de Runge (oscilação) ao adicionar muitos pontos equidistantes.

### 4. Otimização (Gradiente Descendente)
- **O que faz:** Simula o algoritmo de Gradiente Descendente encontrando o mínimo da função $f(x) = x^2 - 4x + 4$.
- **Interação:**
    - Ajuste a **Taxa de Aprendizado** (Learning Rate).
    - Inicie a simulação para ver a "bolinha" descendo a curva passo a passo.

### 5. Cadeias de Markov
- **Sorveteria (Estado Estacionário):**
    - Visualiza a transição de probabilidades entre dois estados (Chocolate vs Baunilha).
    - Clique em "Próximo Dia" para ver as probabilidades convergirem para o equilíbrio.
- **Jogo de Dados (Estados Absorventes):**
    - (Conceitual) Representa o caminho até a vitória ou derrota.

### 6. Diferenciação Automática
- **O que faz:** Demonstra o cálculo de gradientes em um grafo computacional para $f(x) = x^2 + \sin(x)$.
- **Interação:**
    - Mova o slider para alterar o valor de entrada $x$.
    - Veja os valores e gradientes ($\nabla$) serem propagados por cada nó do grafo.

### 7. Sistemas Dinâmicos
- **Epidemias (Modelo SIR):**
    - Simula a propagação de um vírus (Suscetíveis, Infectados, Recuperados).
    - Sliders para Taxa de Infecção ($\beta$) e Recuperação ($\gamma$).
- **Dois Tanques (Mistura):**
    - Simula a troca de fluidos e concentrações entre dois tanques conectados.
    - Visualiza a mudança de cor (concentração) até o equilíbrio.

## Como Executar
Basta abrir o arquivo `Visualizacao_Web/index.html` em qualquer navegador moderno (Chrome, Edge, Firefox). Não é necessário instalação de servidor.
