# Métodos Numéricos - Interpolação

Este projeto contém a solução completa dos exercícios de interpolação do arquivo `exlab4.txt`.

## 📋 Exercícios Implementados

### Exercício 1: Parábola por Três Pontos
- **Objetivo**: Encontrar a parábola que passa pelos pontos (2,3), (3,5) e (5,7)
- **Métodos utilizados**:
  - Interpolação de Lagrange
  - Resolução de sistema linear
- **Resultado**: Encontrar os pontos x* onde p(x*) = 0 (raízes da parábola)

### Exercício 2: Interpolação de Newton - Três Cientistas
- **Objetivo**: Comparar polinômios encontrados por três cientistas usando diferentes ordens dos pontos
- **Cientistas**:
  - Ana: ordem original [(1,2), (3,5), (5,4), (7,8)]
  - Beto: ordem inversa [(7,8), (5,4), (3,5), (1,2)]
  - Carol: ordem bagunçada [(5,4), (1,2), (7,8), (3,5)]
- **Resultado**: Verificar se os polinômios são iguais e explicar o porquê

### Exercício 3: Produção Chinesa de Aço - Extrapolação
- **Objetivo**: Usar interpolação polinomial para prever produção futura
- **Dados**: Produção de aço na China (1990-1996)
- **Método**: Usar dados até 1995 para prever 1996 e comparar com valor real
- **Extrapolação**: Prever produção para 1997

### Exercício 4: Produção Brasileira de Ovos
- **Objetivo**: Ajustar dados e prever produção para 2022
- **Dados**: Produção brasileira de ovos (2016-2021)
- **Métodos**:
  - Interpolação polinomial
  - Ajuste linear por mínimos quadrados
  - Ajuste polinomial de grau 2

### Exercício 5: Produção Brasileira de Camarão - Interpolação
- **Objetivo**: Estimar valor faltante (2017) e prever 2021
- **Dados**: Produção de camarão (2013-2020, exceto 2017)
- **Método**: Interpolação polinomial para estimar 2017 e comparar com valor real

### Exercício 6: Mínimos Quadrados - Ajuste de Dados
- **Objetivo**: Usar mínimos quadrados para ajustar dados de produção de camarão
- **Métodos**:
  - Ajuste linear (reta)
  - Ajuste polinomial de grau 3
- **Análise**: Comparar R² dos ajustes e fazer previsões para 2021

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install numpy scipy matplotlib
```

### Execução
```bash
# Versão completa (com gráficos)
python exLag4_Solucao.py

# Versão de demonstração (sem gráficos)
python exLag4_Demo.py
```

## 📊 Conceitos Matemáticos

### Interpolação Polinomial
- **Lagrange**: Polinômio que passa exatamente pelos pontos dados
- **Newton**: Forma alternativa de interpolação polinomial
- **Unicidade**: Para n+1 pontos, existe um único polinômio de grau ≤ n

### Extrapolação
- **Definição**: Estender o polinômio além dos pontos dados
- **Risco**: Pode ser instável e imprecisa
- **Aplicação**: Previsão de valores futuros

### Mínimos Quadrados
- **Objetivo**: Minimizar a soma dos quadrados dos resíduos
- **Vantagem**: Mais robusto que interpolação para dados com ruído
- **Métrica**: R² (coeficiente de determinação)

## 📈 Resultados Principais

### Exercício 1
- Parábola encontrada: p(x) = ax² + bx + c
- Raízes: x* = [valor1, valor2]

### Exercício 2
- **Conclusão**: Todos os polinômios são iguais
- **Explicação**: A interpolação polinomial é única para um conjunto de pontos

### Exercício 3
- Erro de extrapolação para 1996: [valor]%
- Previsão para 1997: [valor] Mton

### Exercício 4
- Previsões para 2022:
  - Interpolação: [valor] mil dúzias
  - Ajuste linear: [valor] mil dúzias
  - Ajuste grau 2: [valor] mil dúzias

### Exercício 5
- Estimativa para 2017: [valor] ton
- Erro relativo: [valor]%
- Previsão para 2021: [valor] ton

### Exercício 6
- R² linear: [valor]
- R² cúbico: [valor]
- Melhor ajuste: [linear/cúbico]

## ⚠️ Observações Importantes

1. **Extrapolação**: Sempre arriscada, especialmente com polinômios de alto grau
2. **Overfitting**: Polinômios de alto grau podem oscilar entre pontos
3. **Dados reais**: Valores do IBGE podem diferir das previsões
4. **Interpretação**: R² próximo a 1 indica bom ajuste

## 📁 Estrutura de Arquivos

```
├── exlab4.txt                    # Exercícios originais
├── exLag4_Solucao.py            # Solução completa
├── exLag4_Demo.py               # Versão de demonstração
├── README_Interpolacao.md       # Este arquivo
└── requirements.txt             # Dependências
```

## 🔧 Dependências

- `numpy`: Operações numéricas e álgebra linear
- `scipy`: Interpolação e otimização
- `matplotlib`: Visualização (opcional)

## 📚 Referências

- Métodos Numéricos para Engenharia
- Interpolação Polinomial de Lagrange
- Método dos Mínimos Quadrados
- Extrapolação e suas limitações
