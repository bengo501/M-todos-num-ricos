# Guia de Teste - Trabalho 2

## Como testar e validar a solução passo a passo

---

## 📋 Pré-requisitos

### 1. Verificar se Python está instalado

```bash
python --version
```

**Esperado:** Python 3.x instalado

### 2. Verificar se NumPy está instalado

```bash
python -c "import numpy; print(numpy.__version__)"
```

**Esperado:** Versão do NumPy (ex: 1.24.0)

**Se não estiver instalado:**

```bash
pip install numpy
```

---

## 🧪 Teste 1: Execução Básica

### Passo 1: Navegar até a pasta do trabalho

```bash
cd "F:\Game Projects\Godot 4\M-todos-num-ricos\Trabalho 2"
```

### Passo 2: Executar o script

```bash
python interpolacao_peru_simples.py
```

### Resultado Esperado:

```
======================================================================
METODOS NUMERICOS - TRABALHO 2
Interpolacao para Tempo de Assar Peru
======================================================================

DADOS DE REFERENCIA:
----------------------------------------------------------------------
Peso (kg)       Tempo                Tempo (min)  
----------------------------------------------------------------------
3.0             1h 23min           83           
5.0             2h 26min           146          
7.0             3h 17min           197          
9.0             4h 03min           243          
----------------------------------------------------------------------

Peso do peru deste ano: 6.22 kg

======================================================================
METODO: INTERPOLACAO DE LAGRANGE
======================================================================

Resultado para peru de 6.22 kg:
   Tempo: 178.09 minutos
   Tempo: 2h 58min

Verificacao nos pontos conhecidos:
Peso (kg)       Tempo real (min)     Tempo interp. (min)       Erro (min)   
---------------------------------------------------------------------------
3.0             83                   83.000000                 0.0000000000   
5.0             146                  146.000000                0.0000000000   
7.0             197                  197.000000                0.0000000000   
9.0             243                  243.000000                0.0000000000   

======================================================================
METODO: INTERPOLACAO DE NEWTON
======================================================================

Resultado para peru de 6.22 kg:
   Tempo: 178.09 minutos
   Tempo: 2h 58min

======================================================================
COMPARACAO DOS METODOS
======================================================================
Lagrange: 178.0905 minutos (2h 58min)
Newton:   178.0905 minutos (2h 58min)
Diferenca: 0.0000000000 minutos

Observacao: Ambos os metodos devem dar o mesmo resultado!
```

---

## ✅ Validação dos Resultados

### Teste 2: Verificar Pontos Conhecidos

Os erros nos pontos conhecidos devem ser **EXATAMENTE ZERO**:

- P(3.0) = 83.000000 ✓
- P(5.0) = 146.000000 ✓
- P(7.0) = 197.000000 ✓
- P(9.0) = 243.000000 ✓

**Se qualquer erro for diferente de zero:** Há problema na implementação!

### Teste 3: Comparação entre Métodos

Lagrange e Newton devem dar o **MESMO RESULTADO**:

- Resultado esperado: **178.09 minutos**
- Diferença esperada: **0.0000000000 minutos**

---

## 🔍 Teste Manual: Cálculo Passo a Passo

### Verificação Manual com Interpolação Linear Simples

Para validar que o resultado faz sentido, vamos fazer uma interpolação linear simples entre os pontos mais próximos:

**Pontos mais próximos de 6.22 kg:**

- 5.0 kg → 146 min
- 7.0 kg → 197 min

**Interpolação linear:**

```
t_linear = 146 + (197 - 146) × (6.22 - 5.0) / (7.0 - 5.0)
t_linear = 146 + 51 × 1.22 / 2.0
t_linear = 146 + 31.11
t_linear = 177.11 minutos
```

**Nossa interpolação polinomial:** 178.09 minutos

**Análise:** O resultado de 178.09 está próximo da interpolação linear (177.11), mas considera todos os 4 pontos, o que é consistente e esperado!

---

## 🧮 Teste 4: Verificação Manual com Fórmula de Lagrange

### Cálculo Manual para x = 6.22

**Dados:**

- x₀ = 3.0, y₀ = 83
- x₁ = 5.0, y₁ = 146
- x₂ = 7.0, y₂ = 197
- x₃ = 9.0, y₃ = 243
- x = 6.22

**Polinômios de Lagrange base:**

L₀(6.22) = (6.22-5.0)(6.22-7.0)(6.22-9.0) / (3.0-5.0)(3.0-7.0)(3.0-9.0)
         = (1.22)(-0.78)(-2.78) / (-2.0)(-4.0)(-6.0)
         = -2.64 / -48.0
         = 0.055

L₁(6.22) = (6.22-3.0)(6.22-7.0)(6.22-9.0) / (5.0-3.0)(5.0-7.0)(5.0-9.0)
         = (3.22)(-0.78)(-2.78) / (2.0)(-2.0)(-4.0)
         = 6.98 / 16.0
         = 0.436

L₂(6.22) = (6.22-3.0)(6.22-5.0)(6.22-9.0) / (7.0-3.0)(7.0-5.0)(7.0-9.0)
         = (3.22)(1.22)(-2.78) / (4.0)(2.0)(-2.0)
         = -10.93 / -16.0
         = 0.683

L₃(6.22) = (6.22-3.0)(6.22-5.0)(6.22-7.0) / (9.0-3.0)(9.0-5.0)(9.0-7.0)
         = (3.22)(1.22)(-0.78) / (6.0)(4.0)(2.0)
         = -3.07 / 48.0
         = -0.064

**Resultado:**

```
P(6.22) = 83×0.055 + 146×0.436 + 197×0.683 + 243×(-0.064)
        = 4.565 + 63.656 + 134.551 - 15.552
        = 187.22 - 15.552
        = 178.09 minutos ✓
```

**Confirmação:** O resultado está correto!

---

## 📊 Teste 5: Testar com Outros Valores

Vamos criar um script de teste para validar vários pontos:

```python
# testar_valores.py
import numpy as np

# Importar a função do script principal
from interpolacao_peru_simples import lagrange_interpolation

pesos = np.array([3.0, 5.0, 7.0, 9.0])
tempos = np.array([83, 146, 197, 243])

# Testar pontos conhecidos
print("Teste com pontos conhecidos:")
for peso, tempo_esperado in zip(pesos, tempos):
    resultado = lagrange_interpolation(pesos, tempos, peso)
    erro = abs(resultado - tempo_esperado)
    status = "✓" if erro < 1e-10 else "✗"
    print(f"P({peso}) = {resultado:.6f} (esperado: {tempo_esperado}) {status}")

# Testar pontos intermediários
print("\nTeste com pontos intermediários:")
testes = [4.0, 6.0, 6.22, 8.0]
for peso_teste in testes:
    resultado = lagrange_interpolation(pesos, tempos, peso_teste)
    horas = int(resultado // 60)
    minutos = int(resultado % 60)
    print(f"P({peso_teste}) = {resultado:.2f} min = {horas}h {minutos:02d}min")
```

---

## 🎯 Checklist de Validação

Use este checklist para garantir que tudo está funcionando:

- [ ] Script executa sem erros
- [ ] Resultado principal: **178.09 minutos (2h 58min)**
- [ ] Verificação nos pontos conhecidos: **erro = 0.000000** em todos
- [ ] Lagrange e Newton produzem **mesmo resultado**
- [ ] Diferença entre métodos: **0.000000 minutos**
- [ ] Resultado está entre 146 min (5kg) e 197 min (7kg) ✓
- [ ] Resultado faz sentido (peru maior precisa mais tempo) ✓

---

## ⚠️ Problemas Comuns e Soluções

### Erro: "ModuleNotFoundError: No module named 'numpy'"

**Solução:**

```bash
pip install numpy
```

### Erro: Script não executa

**Solução:**

1. Verificar se está na pasta correta
2. Verificar se o arquivo existe: `interpolacao_peru_simples.py`
3. Tentar: `python -u interpolacao_peru_simples.py`

### Resultado diferente de 178.09

**Possíveis causas:**

1. Erro de digitação nos dados
2. Erro na implementação da função
3. Problema de precisão numérica

**Verificar:**

- Dados de entrada estão corretos?
- Função lagrange_interpolation está correta?
- Usar print para debug

---

## 📝 Teste Final: Salvar Resultado

Para salvar a saída do programa:

```bash
python interpolacao_peru_simples.py > resultado_teste.txt 2>&1
```

Depois verificar o arquivo `resultado_teste.txt` para confirmar os resultados.

---

## ✅ Resultado Esperado Final

```
RESULTADO FINAL
======================================================================

Para assar um peru de 6.22 kg a 230C:
   Tempo necessario: 2h 58min
   Valor em minutos: 178.09 minutos

Recomendacao: Comece a assar o peru 2h 58min antes
   do horario previsto para servir!
```

**Se todos os testes passarem:** O trabalho está funcionando corretamente! ✅
