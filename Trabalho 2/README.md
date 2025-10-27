# Trabalho 2 - Métodos Numéricos
## Interpolação para Tempo de Assar Peru

Este trabalho resolve o problema de Dona Selma sobre o tempo necessário para assar um peru de 6.22 kg utilizando métodos de interpolação polinomial.

## 📋 Enunciado

Dona Selma precisa calcular o tempo para assar um peru de 6.22 kg a 230°C. Ela possui uma tabela de referência:

- 3.0 kg = 1h 23min
- 5.0 kg = 2h 26min  
- 7.0 kg = 3h 17min
- 9.0 kg = 4h 03min

## ✅ Resultado

**t(6.22) = 178.09 minutos = 2h 58min**

## 📁 Arquivos

- `enunciadoTrab2.txt` - Enunciado completo do trabalho
- `interpolacao_peru_simples.py` - Código Python com implementação manual de Lagrange e Newton
- `RELATORIO_TRABALHO_2.md` - Relatório completo com todas as análises solicitadas
- `resultado.txt` - Saída do programa Python

## 🚀 Como Executar

```bash
cd "Trabalho 2"
python interpolacao_peru_simples.py
```

## 📊 Métodos Utilizados

1. **Interpolação de Lagrange** - Implementação manual
2. **Interpolação de Newton** - Validação usando diferenças divididas

Ambos os métodos produziram o mesmo resultado: **178.09 minutos**

## 📝 Relatório

O relatório completo (`RELATORIO_TRABALHO_2.md`) contém:

1. ✅ Obtenção do resultado usando interpolação de Newton/Lagrange
2. ✅ Comparação com resultado do ChatGPT  
3. ✅ Análise detalhada das três partes solicitadas:
   - (a) Experiência de extrair informação do ChatGPT
   - (b) Como obtivemos nosso resultado
   - (c) Comparação e conclusões

## 🔍 Verificação

O polinômio interpolador foi verificado nos pontos conhecidos:
- P(3.0) = 83.00 min ✓
- P(5.0) = 146.00 min ✓
- P(7.0) = 197.00 min ✓
- P(9.0) = 243.00 min ✓

Todos os pontos foram reproduzidos com erro zero, confirmando a correção da implementação.

## 📚 Referências

- Métodos de Interpolação Polinomial
- Interpolação de Lagrange
- Interpolação de Newton (Diferenças Divididas)

