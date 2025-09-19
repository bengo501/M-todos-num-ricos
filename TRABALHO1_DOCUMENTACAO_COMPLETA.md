# TRABALHO 1 - MÉTODOS NUMÉRICOS
## Documentação Completa do Desenvolvimento

---

## 📋 **RESUMO EXECUTIVO**

Este trabalho implementa e demonstra conceitos fundamentais de **Métodos Numéricos** baseado nas referências fornecidas sobre:
- **Padrão IEEE 754** e precisão de ponto flutuante
- **Sistemas Lineares** e métodos de solução
- **Solução de Equações** não-lineares
- **Interpolação** e ajuste de dados

### ✅ **Resultados Principais Obtidos:**
- **Epsilon da máquina**: 2.22e-16 (precisão dupla IEEE 754)
- **Sistema linear**: Resolvido com condicionamento 2.09 (bem condicionado)
- **Equação não-linear**: Raiz encontrada em 2.094551 (Newton) vs 2.094552 (Bissecção)
- **Interpolação**: R² = 0.8171 (ajuste quadrático superior ao linear)

---

## 🎯 **PARTE I: PRECISÃO DA MÁQUINA E PADRÃO IEEE 754**

### **Conceito Teórico**
O **padrão IEEE 754** define como números de ponto flutuante são representados em computadores. A **precisão da máquina** (ε) é o menor número positivo tal que `1 + ε > 1` em aritmética de ponto flutuante.

### **Implementação do Algoritmo**
```python
def parte1_precisao_maquina():
    aux = 1.0
    iteracoes = 0
    
    while 1 + aux > 1:
        aux = aux / 2
        iteracoes += 1
    
    epsilon_maquina = aux * 2
    return epsilon_maquina
```

### **Resultados Obtidos**
- **Algoritmo terminou**: Após 53 iterações
- **Epsilon calculado**: 2.22e-16
- **Epsilon do NumPy**: 2.22e-16 ✓ (confirmação)
- **Verificação**: `1 + ε = 1.0000000000000002` (diferente de 1)

### **Significado Prático**
- Representa a **menor diferença** detectável pela máquina
- Define **tolerâncias** para métodos iterativos
- Fundamental para **análise de erros** numéricos

---

## 🔢 **PARTE II: SISTEMAS LINEARES**

### **Sistema Implementado**
```
Ax = b onde:
A = [[ 4, -1,  0,  1],     b = [15]
     [-1,  4, -1,  0],         [10]
     [ 0, -1,  4, -1],         [10]
     [ 1,  0, -1,  4]]         [20]
```

### **Métodos Aplicados**

#### **1. Eliminação Gaussiana**
- **Solução**: x = [3.571, 4.643, 5.000, 5.357]
- **Resíduo**: ||Ax - b|| = 3.55e-15 (excelente precisão)

#### **2. Fatoração LU**
```
A = PLU onde:
L = matriz triangular inferior
U = matriz triangular superior  
P = matriz de permutação
```

#### **3. Análise de Condicionamento**
- **Número de condição**: 2.09
- **Determinante**: 196.00
- **Classificação**: Sistema **bem condicionado** (κ < 100)

### **Importância do Condicionamento**
- κ < 100: **Bem condicionado** (estável)
- 100 ≤ κ < 10⁴: **Moderadamente condicionado**
- κ ≥ 10⁴: **Mal condicionado** (instável)

---

## 📊 **PARTE III: SOLUÇÃO DE EQUAÇÕES NÃO-LINEARES**

### **Função Exemplo**
```
f(x) = x³ - 2x - 5
f'(x) = 3x² - 2
```
**Raiz exata**: x ≈ 2.094551481542327

### **Métodos Implementados**

#### **1. Método da Bissecção**
- **Princípio**: Teorema do Valor Intermediário
- **Intervalo**: [2, 3] (f(2) < 0, f(3) > 0)
- **Convergência**: Linear (ordem 1)
- **Resultado**: x = 2.094552 (21 iterações)
- **Erro**: 9.12e-07

#### **2. Método de Newton-Raphson**
- **Fórmula**: x_{n+1} = x_n - f(x_n)/f'(x_n)
- **Chute inicial**: x₀ = 2.0
- **Convergência**: Quadrática (ordem 2)
- **Resultado**: x = 2.094551 (4 iterações)
- **Erro**: 8.88e-16

### **Comparação dos Métodos**
| Método | Raiz | Iterações | Erro | Vantagens |
|--------|------|-----------|------|-----------|
| Bissecção | 2.094552 | 21 | 9.12e-07 | Robusto, sempre converge |
| Newton-Raphson | 2.094551 | 4 | 8.88e-16 | Rápido, alta precisão |

---

## 📈 **PARTE IV: INTERPOLAÇÃO E AJUSTE DE DADOS**

### **Dados de Exemplo**
Pontos: [(1,2), (2,3), (3,5), (4,4), (5,6)]

### **Métodos Implementados**

#### **1. Interpolação de Lagrange**
- **Polinômio resultante** (grau 4):
  ```
  p(x) = 0.417x⁴ - 4.833x³ + 19.083x² - 28.667x + 16.000
  ```
- **Característica**: Passa **exatamente** por todos os pontos
- **Verificação**: p(xᵢ) = yᵢ para todos os pontos ✓

#### **2. Ajuste por Mínimos Quadrados**

**Ajuste Linear:**
- **Equação**: y = 0.900x + 1.300
- **R²**: 0.8100

**Ajuste Quadrático:**
- **Equação**: y = -0.071x² + 1.329x + 0.800
- **R²**: 0.8171 (melhor ajuste)

### **Análise dos Resultados**
- **Interpolação**: Perfeita para os pontos dados, mas pode oscilar
- **Ajuste Linear**: Simples, mas pode não capturar não-linearidades
- **Ajuste Quadrático**: Melhor compromisso (R² mais alto)

---

## 🔗 **PARTE V: ANÁLISE INTEGRADA**

### **Conexões Entre os Métodos**

#### **1. Precisão da Máquina**
- Afeta **TODOS** os cálculos numéricos
- Define **tolerâncias** para critérios de parada
- Fundamental para **análise de erros**

#### **2. Sistemas Lineares Aparecem Em:**
- **Interpolação polinomial**: Sistema de Vandermonde
- **Método de Newton**: Sistemas jacobianos
- **Mínimos quadrados**: Equações normais

#### **3. Condicionamento**
- Afeta **estabilidade** de todos os métodos
- Sistemas mal condicionados amplificam erros
- Crucial para **escolha de métodos**

### **Considerações Práticas**

#### **✅ Boas Práticas:**
- Sempre verificar **condicionamento** de sistemas
- Usar **tolerâncias apropriadas** baseadas em ε
- Preferir métodos **estáveis numericamente**
- **Validar resultados** com dados conhecidos
- **Documentar limitações** e suposições

#### **⚠️ Cuidados:**
- **Cancelamento catastrófico**: Evitar subtrações de números próximos
- **Overflow/Underflow**: Monitorar crescimento de valores
- **Extrapolação**: Usar com extrema cautela
- **Alto grau**: Polinômios podem ser instáveis

---

## 📊 **RESULTADOS NUMÉRICOS DETALHADOS**

### **Resumo Quantitativo**
```
PRECISÃO DA MÁQUINA
├── Epsilon calculado: 2.22e-16
├── Iterações: 53
└── Verificação: ✓ Correto

SISTEMAS LINEARES  
├── Solução: [3.571, 4.643, 5.000, 5.357]
├── Resíduo: 3.55e-15
├── Condicionamento: 2.09 (bem condicionado)
└── Determinante: 196.00

EQUAÇÕES NÃO-LINEARES
├── Bissecção: 2.094552 (21 iter, erro 9.12e-07)
├── Newton: 2.094551 (4 iter, erro 8.88e-16)
└── Diferença: 1.00e-06

INTERPOLAÇÃO
├── Lagrange: Grau 4, passa exatamente pelos pontos
├── Linear: R² = 0.8100
└── Quadrático: R² = 0.8171 (melhor)
```

---

## 🚀 **IMPLEMENTAÇÃO TÉCNICA**

### **Estrutura do Código**
```python
trabalho1_solucao_completa.py
├── parte1_precisao_maquina()      # IEEE 754
├── parte2_sistemas_lineares()     # Ax = b  
├── parte3_equacoes_nao_lineares() # f(x) = 0
├── parte4_interpolacao()          # Ajuste de dados
└── parte5_analise_integrada()     # Conclusões
```

### **Bibliotecas Utilizadas**
- **NumPy**: Operações matriciais e vetoriais
- **SciPy**: Métodos numéricos avançados
- **Matplotlib**: Visualização de resultados

### **Arquivos Gerados**
1. `trabalho1_solucao_completa.py` - Código principal
2. `trabalho1_interpolacao.png` - Gráficos comparativos
3. `TRABALHO1_DOCUMENTACAO_COMPLETA.md` - Esta documentação

---

## 📚 **BASE TEÓRICA**

### **Referências Utilizadas**

#### **1. Padrão IEEE 754**
- Representação de ponto flutuante
- Precisão simples vs dupla
- Epsilon da máquina
- Erros de arredondamento

#### **2. Sistemas Lineares**
- Eliminação gaussiana
- Fatoração LU
- Análise de condicionamento
- Estabilidade numérica

#### **3. Solução de Equações**
- Método da bissecção
- Método de Newton-Raphson
- Análise de convergência
- Critérios de parada

#### **4. Interpolação**
- Polinômios de Lagrange
- Diferenças divididas
- Mínimos quadrados
- Coeficiente de determinação (R²)

---

## 🎓 **APRENDIZADOS E CONCLUSÕES**

### **Principais Lições**

#### **1. Precisão Numérica é Fundamental**
- Todo cálculo computacional tem **limitações**
- Epsilon da máquina define **tolerâncias realistas**
- Erros se **propagam** através dos cálculos

#### **2. Condicionamento Determina Estabilidade**
- Sistemas bem condicionados são **estáveis**
- Mal condicionamento amplifica **pequenos erros**
- Sempre **verificar** antes de resolver

#### **3. Diferentes Métodos, Diferentes Trade-offs**
- **Bissecção**: Robusto mas lento
- **Newton**: Rápido mas requer derivada
- **Interpolação**: Exata mas pode oscilar
- **Ajuste**: Robusto para dados com ruído

#### **4. Validação é Essencial**
- Sempre **verificar** resultados
- Usar **múltiplos métodos** quando possível
- **Documentar** limitações e suposições

### **Aplicações Práticas**
Este trabalho demonstra conceitos que são **fundamentais** em:
- **Engenharia**: Simulações numéricas
- **Física**: Modelagem de fenômenos
- **Economia**: Análise de dados
- **Computação Científica**: Algoritmos robustos

---

## ✅ **STATUS FINAL**

### **Objetivos Alcançados**
- [x] Implementação do algoritmo de precisão da máquina
- [x] Solução de sistemas lineares com análise de condicionamento
- [x] Comparação de métodos para equações não-lineares
- [x] Interpolação e ajuste de dados com visualização
- [x] Análise integrada dos métodos
- [x] Documentação completa

### **Resultados Validados**
- [x] Epsilon da máquina coincide com NumPy
- [x] Sistema linear resolvido com alta precisão
- [x] Métodos convergem para mesma raiz
- [x] Interpolação passa exatamente pelos pontos
- [x] Ajustes apresentam R² consistentes

### **Código Executável**
```bash
# Para executar o trabalho completo:
python trabalho1_solucao_completa.py

# Saída esperada:
# ✅ Todos os métodos executados com sucesso!
```

---

**Desenvolvido por:** Assistente IA  
**Data:** 2025  
**Baseado em:** Referências de Métodos Numéricos fornecidas  
**Status:** ✅ **CONCLUÍDO COM SUCESSO**
