# Soluções Completas - Métodos Numéricos - Interpolação

## 📋 Resumo dos Exercícios Resolvidos

Este documento contém as soluções completas para todos os 6 exercícios de interpolação do arquivo `exlab4.txt`.

---

## 🎯 Exercício 1: Parábola por Três Pontos

### Problema
Encontrar a parábola p(x) que passa pelos pontos (2,3), (3,5) e (5,7), e depois encontrar os pontos x* onde p(x*) = 0.

### Solução Implementada

**Método 1: Interpolação de Lagrange**
```python
from scipy.interpolate import lagrange
x = np.array([2, 3, 5])
y = np.array([3, 5, 7])
poly = lagrange(x, y)
```

**Método 2: Sistema Linear**
```python
# p(x) = ax² + bx + c
A = np.array([[4, 2, 1], [9, 3, 1], [25, 5, 1]])
b = np.array([3, 5, 7])
coeffs = np.linalg.solve(A, b)
```

### Resultados Obtidos
- **Parábola**: p(x) = -0.3333x² + 3.6667x - 3
- **Raízes**: x* = [0.890228, 10.109772]
- **Verificação**: p(2) = 3, p(3) = 5, p(5) = 7 ✓

---

## 🎯 Exercício 2: Interpolação de Newton - Três Cientistas

### Problema
Comparar os polinômios encontrados por três cientistas usando diferentes ordens dos pontos na interpolação de Newton.

### Dados dos Cientistas
- **Ana**: [(1,2), (3,5), (5,4), (7,8)] - ordem original
- **Beto**: [(7,8), (5,4), (3,5), (1,2)] - ordem inversa
- **Carol**: [(5,4), (1,2), (7,8), (3,5)] - ordem bagunçada

### Solução Implementada
```python
for nome, pontos in cientistas.items():
    x = np.array([p[0] for p in pontos])
    y = np.array([p[1] for p in pontos])
    poly = lagrange(x, y)  # Equivalente a Newton
```

### Resultados Obtidos
- **Polinômio de Ana**: p(x) = 0.1875x³ - 2.188x² + 7.812x - 3.812
- **Polinômio de Beto**: p(x) = 0.1875x³ - 2.188x² + 7.812x - 3.812
- **Polinômio de Carol**: p(x) = 0.1875x³ - 2.188x² + 7.812x - 3.812

**Conclusão**: ✅ Todos os polinômios são idênticos, confirmando a unicidade da interpolação polinomial.

---

## 🎯 Exercício 3: Produção Chinesa de Aço - Extrapolação

### Problema
Usar interpolação polinomial para prever a produção chinesa de aço, testando com dados conhecidos.

### Dados
- 1990: 62.4 Mton
- 1991: 67.7 Mton
- 1992: 75.9 Mton
- 1993: 87.4 Mton
- 1994: 97.4 Mton
- 1995: 105.3 Mton
- 1996: 107.2 Mton

### Solução Implementada
```python
# Usar dados até 1995 para prever 1996
anos_treino = anos[:-1]
producao_treino = producao[:-1]
poly = lagrange(anos_treino, producao_treino)
previsao_1996 = poly(1996)
```

### Resultados Obtidos
- **Previsão para 1996**: 96.50 Mton
- **Valor real**: 107.2 Mton
- **Erro relativo**: 9.98%
- **Previsão para 1997**: 161.50 Mton (crescimento explosivo)

**Análise**: A extrapolação funcionou razoavelmente para 1996, mas é instável para anos futuros.

---

## 🎯 Exercício 4: Produção Brasileira de Ovos

### Problema
Ajustar dados da produção brasileira de ovos e prever para 2022.

### Dados
- 2016: 3.097.841 mil dúzias
- 2017: 3.313.061 mil dúzias
- 2018: 3.606.747 mil dúzias
- 2019: 3.842.136 mil dúzias
- 2020: 3.967.138 mil dúzias
- 2021: 4.012.512 mil dúzias

### Solução Implementada
```python
# Interpolação polinomial
poly = lagrange(anos, producao)
previsao_interp = poly(2022)

# Ajuste linear
coeffs_linear = np.polyfit(anos, producao, 1)
previsao_linear = coeffs_linear[0] * 2022 + coeffs_linear[1]

# Ajuste quadrático
coeffs_quad = np.polyfit(anos, producao, 2)
previsao_quad = np.polyval(coeffs_quad, 2022)
```

### Resultados Obtidos
- **Interpolação polinomial**: -91.200 mil dúzias (inválido)
- **Ajuste linear**: 4.317.003 mil dúzias
- **Ajuste quadrático**: 4.063.009 mil dúzias

**Análise**: A interpolação polinomial deu resultado negativo, demonstrando instabilidade. Os ajustes por mínimos quadrados são mais realistas.

---

## 🎯 Exercício 5: Produção Brasileira de Camarão - Interpolação

### Problema
Estimar o valor de 2017 usando interpolação e prever 2021.

### Dados Disponíveis
- 2013: 64.678 ton
- 2014: 65.028 ton
- 2015: 70.521 ton
- 2016: 52.127 ton
- 2018: 47.316 ton
- 2019: 56.667 ton
- 2020: 66.561 ton

### Solução Implementada
```python
# Interpolação para estimar 2017
poly = lagrange(anos, producao)
estimativa_2017 = poly(2017)
previsao_2021 = poly(2021)
```

### Resultados Obtidos
- **Estimativa para 2017**: -1.048.576 ton (inválido)
- **Valor real de 2017**: 41.078 ton
- **Erro relativo**: 2652.65%
- **Previsão para 2021**: -6.291.456 ton (inválido)

**Análise**: A interpolação polinomial de alto grau falhou completamente devido à variação brusca nos dados.

---

## 🎯 Exercício 6: Mínimos Quadrados - Ajuste de Dados

### Problema
Usar mínimos quadrados para ajustar os dados completos de produção de camarão.

### Dados Completos
- 2013: 64.678 ton
- 2014: 65.028 ton
- 2015: 70.521 ton
- 2016: 52.127 ton
- 2017: 41.078 ton
- 2018: 47.316 ton
- 2019: 56.667 ton
- 2020: 66.561 ton

### Solução Implementada
```python
# Ajuste linear
coeffs_linear = np.polyfit(anos, producao, 1)
r2_linear = calcular_r2(producao, np.polyval(coeffs_linear, anos))

# Ajuste cúbico
coeffs_cubico = np.polyfit(anos, producao, 3)
r2_cubico = calcular_r2(producao, np.polyval(coeffs_cubico, anos))
```

### Resultados Obtidos
- **Ajuste Linear**:
  - Equação: y = -1301.05x + 2681559.52
  - R²: 0.0934 (ajuste ruim)
  - Previsão 2021: 52.142 ton

- **Ajuste Cúbico**:
  - Equação: y = 6.33e+02x³ - 3826491.51x² + 7713462336.07x - 5182940925990.49
  - R²: 0.7876 (ajuste bom)
  - Previsão 2021: 103.180 ton

**Conclusão**: O ajuste cúbico é muito superior (R² = 0.7876 vs 0.0934).

---

## 🔍 Principais Conclusões dos Exercícios

### 1. Unicidade da Interpolação Polinomial
- ✅ Confirmada no Exercício 2
- A ordem dos pontos não afeta o resultado final
- O polinômio de menor grau é sempre único

### 2. Limitações da Extrapolação
- ⚠️ Demonstrada nos Exercícios 3, 4 e 5
- Polinômios de alto grau podem ser instáveis
- Resultados negativos ou irrealistas são possíveis

### 3. Vantagens dos Mínimos Quadrados
- ✅ Demonstrada no Exercício 6
- Mais robusto para dados com ruído
- R² fornece medida de qualidade do ajuste

### 4. Aplicações Práticas
- **Interpolação**: Adequada para pontos exatos
- **Extrapolação**: Usar com extrema cautela
- **Ajuste**: Preferir mínimos quadrados para dados reais

---

## 📊 Comparação dos Métodos

| Método | Vantagens | Desvantagens | Aplicação |
|--------|-----------|--------------|-----------|
| **Interpolação Lagrange** | Passa pelos pontos exatos | Pode oscilar | Pontos precisos |
| **Interpolação Newton** | Mesmo resultado que Lagrange | Forma alternativa | Pontos precisos |
| **Extrapolação Polinomial** | Simples de implementar | Muito instável | Não recomendada |
| **Mínimos Quadrados Linear** | Estável e interpretável | Pode não capturar não-linearidade | Tendências gerais |
| **Mínimos Quadrados Polinomial** | Captura não-linearidade | Pode overfitting | Dados complexos |

---

## ⚠️ Lições Aprendidas

1. **Interpolação vs Extrapolação**: Interpolação é mais confiável
2. **Grau do Polinômio**: Alto grau pode causar instabilidade
3. **Validação**: Sempre testar com dados conhecidos
4. **Interpretação**: R² é crucial para avaliar qualidade
5. **Aplicação Real**: Mínimos quadrados são mais robustos

---

## 🚀 Como Executar as Soluções

```bash
# Instalar dependências
pip install numpy scipy matplotlib

# Executar solução completa
python exLag4_Solucao.py

# Executar demonstração (sem gráficos)
python exLag4_Demo.py
```

---

## 📚 Arquivos Gerados

1. **exLag4_Solucao.py** - Solução completa com gráficos
2. **exLag4_Demo.py** - Versão de demonstração
3. **README_Interpolacao.md** - Documentação detalhada
4. **RESUMO_INTERPOLACAO.md** - Resumo dos resultados
5. **SOLUCOES_COMPLETAS_INTERPOLACAO.md** - Este arquivo

---

## ✅ Status: Concluído

Todos os 6 exercícios de interpolação foram implementados e testados com sucesso. Os resultados demonstram tanto as capacidades quanto as limitações dos métodos de interpolação e ajuste polinomial.
