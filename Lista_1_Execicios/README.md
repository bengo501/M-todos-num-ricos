# Métodos Numéricos - Lista 1 Geral

## 📋 Descrição

Este projeto contém a solução completa de todos os exercícios da Lista 1 de Métodos Numéricos, organizados em uma estrutura modular e bem documentada.

**Professor:** João B. Oliveira

## 🗂️ Estrutura do Projeto

```
Lista_1_Execicios/
├── README.md                           # Este arquivo
├── listaExec1_Solucao.py              # Script principal com menu interativo
├── listaExec1_Demo.py                 # Script de demonstração automática
├── requirements.txt                   # Dependências Python
├── Sistemas_Ponto_Flutuante/
│   └── sistemas_ponto_flutuante.py    # Exercícios 1-4: Sistemas de Ponto Flutuante
├── Resolucao_Equacoes/
│   └── resolucao_equacoes.py          # Exercícios 1-8: Resolução de Equações
├── Sistemas_Lineares/
│   └── sistemas_lineares.py           # Exercícios 1-6: Sistemas Lineares
├── Cadeias_Markov/
│   └── cadeias_markov.py              # Exercícios 1-9: Cadeias de Markov
├── Interpolacao/
│   └── interpolacao.py                # Exercícios 1-6: Interpolação
├── Diferenciacao_Automatica/
│   └── diferenciacao_automatica.py    # Exercício 1: Diferenciação Automática
└── Sistemas_Dinamicos/
    └── sistemas_dinamicos.py          # Exercícios 1-3: Sistemas Dinâmicos
```

## 🚀 Como Executar

### Pré-requisitos

```bash
pip install numpy scipy matplotlib
```

### Opção 1: Menu Interativo

Execute o script principal para acessar um menu interativo:

```bash
python listaExec1_Solucao.py
```

O menu permite escolher qual seção executar ou executar todas de uma vez.

### Opção 2: Demonstração Automática

Execute o script de demonstração para executar todos os exercícios automaticamente:

```bash
python listaExec1_Demo.py
```

### Opção 3: Executar Seções Individuais

Você também pode executar cada seção individualmente:

```bash
# Sistemas de Ponto Flutuante
python Sistemas_Ponto_Flutuante/sistemas_ponto_flutuante.py

# Resolução de Equações
python Resolucao_Equacoes/resolucao_equacoes.py

# Sistemas Lineares
python Sistemas_Lineares/sistemas_lineares.py

# Cadeias de Markov
python Cadeias_Markov/cadeias_markov.py

# Interpolação
python Interpolacao/interpolacao.py

# Diferenciação Automática
python Diferenciacao_Automatica/diferenciacao_automatica.py

# Sistemas Dinâmicos
python Sistemas_Dinamicos/sistemas_dinamicos.py
```

## 📚 Seções e Exercícios

### 1. Sistemas de Ponto Flutuante
- **Exercício 1:** Algoritmo de precisão da máquina
- **Exercício 2:** Calculadora com exceções IEEE-754
- **Exercício 3:** Plotagem de funções próximas a x = 1
- **Exercício 4:** Série de Taylor para exp(x)

### 2. Resolução de Equações
- **Exercício 1:** Comparação de funções próximas a zero
- **Exercício 2:** Plotagem de f(1/x) para contornar restrição
- **Exercício 3:** Método de Heron para raiz quadrada
- **Exercício 4:** Polinômio com raízes 2, 3, 4 e método da bissecção
- **Exercício 5:** Polinômio com raízes 2, 3, 4, 5
- **Exercício 6:** Avaliação de polinômio usando método de Horner
- **Exercício 7:** Método da secante
- **Exercício 8:** Algoritmo modificado (derivada)

### 3. Sistemas Lineares
- **Exercício 1:** Problema do parquinho
- **Exercício 2:** Métodos de Gauss-Jacobi e Gauss-Seidel
- **Exercício 3:** Polinômio de terceiro grau por sistema linear
- **Exercício 4:** Análise química - composição de substâncias
- **Exercício 5:** Análise química - versão mais realista
- **Exercício 6:** Análise química - versão ainda mais realista

### 4. Cadeias de Markov
- **Exercício 1:** Sorveteria - pesquisa de satisfação
- **Exercício 2:** Times de futebol - migração de torcedores
- **Exercício 3:** Lobo guará - regiões de caça
- **Exercício 4:** Mobilidade social - Ricos, Médios e Pobres
- **Exercício 5:** Jogo de dados - Guilherme vs Christian
- **Exercício 6:** Letras A-F em fila
- **Exercício 7:** Distribuição de probabilidades
- **Exercício 8:** Modificação com vogais
- **Exercício 9:** Nova distribuição de probabilidades

### 5. Interpolação
- **Exercício 1:** Parábola por três pontos
- **Exercício 2:** Interpolação de Newton - três cientistas
- **Exercício 3:** Produção chinesa de aço - extrapolação
- **Exercício 4:** Produção brasileira de ovos
- **Exercício 5:** Produção brasileira de camarão
- **Exercício 6:** Mínimos quadrados - ajuste de dados

### 6. Diferenciação Automática
- **Exercício 1:** Decomposição e diferenciação de função multivariável

### 7. Sistemas Dinâmicos
- **Exercício 1:** Aproximação de funções usando derivadas
- **Exercício 2:** Decaimento radioativo - método de Euler
- **Exercício 3:** Pêndulo - simulação com método de Euler

## 🔧 Dependências

- **numpy**: Operações numéricas e álgebra linear
- **scipy**: Otimização e interpolação
- **matplotlib**: Visualização de dados (opcional)

## 📊 Características dos Scripts

### Scripts Principais
- **listaExec1_Solucao.py**: Menu interativo completo
- **listaExec1_Demo.py**: Execução automática para demonstrações

### Scripts de Seção
- Cada seção tem seu próprio script independente
- Funções bem documentadas para cada exercício
- Resultados detalhados com explicações
- Tratamento de erros robusto

## 🎯 Funcionalidades

- ✅ **Modular**: Cada seção é independente
- ✅ **Documentado**: Código bem comentado e explicado
- ✅ **Robusto**: Tratamento de erros e validações
- ✅ **Flexível**: Menu interativo ou execução automática
- ✅ **Educativo**: Explicações detalhadas dos métodos
- ✅ **Prático**: Resultados numéricos e análises

## 📈 Exemplos de Saída

Cada exercício produz:
- Enunciado do problema
- Implementação do método
- Resultados numéricos
- Análise e interpretação
- Comparações quando aplicável

## ⚠️ Observações

1. **Gráficos**: Alguns exercícios podem gerar gráficos (matplotlib)
2. **Precisão**: Resultados são calculados com alta precisão
3. **Validação**: Métodos são validados com exemplos conhecidos
4. **Performance**: Algoritmos otimizados para eficiência

## 🤝 Contribuições

Este projeto foi desenvolvido como solução completa para a Lista 1 de Métodos Numéricos. Todas as implementações seguem as melhores práticas de programação científica.

## 📄 Licença

Este projeto é destinado ao uso educacional e acadêmico.

---

**Desenvolvido para:** Métodos Numéricos - Lista 1 Geral  
**Professor:** João B. Oliveira  
**Status:** ✅ Completo e Funcional
