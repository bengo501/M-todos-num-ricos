# Simulador de Jogo Coreano - Trabalho de Métodos Numéricos

## Descrição do Problema

Este projeto implementa um simulador para um jogo inspirado em séries como Squid Game, onde personagens se movem entre `n` salas conectadas linearmente, com probabilidades específicas de movimento e possibilidade de "morte" nas extremidades.

### Regras do Jogo

1. **Salas**: `n` salas dispostas linearmente (sempre ímpar)
2. **Início**: Personagens começam na sala central: `⌊(n+1)/2⌋`
3. **Probabilidades por episódio**:
   - Ficar na mesma sala: `1/n`
   - Mover-se: `(n-1)/n`
4. **Movimento**:
   - **Salas internas (2 a n-1)**: divide movimento igualmente entre esquerda e direita
   - **Salas das pontas (1 e n)**: metade da probabilidade resulta em "morte"

### Objetivo

Calcular a população estacionária total de atores quando o sistema estabilizar, usando **sistema linear** (não simulação).

## Implementações Disponíveis

### 1. Python (Recomendado)
```bash
python simulador_jogo.py <número_de_salas>
```

**Exemplos:**
```bash
python simulador_jogo.py 23    # Exemplo do enunciado
python simulador_jogo.py 5     # Exemplo pequeno
python simulador_jogo.py       # Executa exemplos padrão (3,5,7,23)
```

### 2. C++ (Para Estúdios Coreanos)
```bash
# Compilação (Linux/Mac):
g++ -o simulador_jogo simulador_jogo.cpp -std=c++11

# Compilação (Windows com Visual Studio):
cl simulador_jogo.cpp /EHsc

# Execução:
./simulador_jogo 23
```

## Modelo Matemático

### Matriz de Transição
Para `n` salas, criamos uma matriz `P` onde `P[i,j]` é a probabilidade de ir da sala `i` para a sala `j`.

**Exemplo para n=5:**
```
Probabilidades:
- Ficar: s = 1/5 = 0.2
- Mover: 1-s = 4/5 = 0.8

Sala 1 (ponta): ficar=0.2, ir_para_2=0.4, morrer=0.4
Sala 2 (interna): ficar=0.2, ir_para_1=0.4, ir_para_3=0.4
Sala 3 (central): ficar=0.2, ir_para_2=0.4, ir_para_4=0.4
Sala 4 (interna): ficar=0.2, ir_para_3=0.4, ir_para_5=0.4
Sala 5 (ponta): ficar=0.2, ir_para_4=0.4, morrer=0.4
```

### Sistema Linear
No equilíbrio: `x = P^T × x + b`

Rearranjando: `(I - P^T) × x = b`

Onde:
- `x[i]` = população média na sala i
- `b[i]` = taxa de chegada na sala i (1.0 na sala central, 0 nas demais)

## Resultados de Exemplo

| Salas (n) | População Total | Sala Central | Padrão |
|-----------|-----------------|--------------|---------|
| 3         | 6.00            | 3.00         | Simétrico |
| 5         | 11.25           | 3.75         | Simétrico |
| 7         | 18.67           | 4.67         | Simétrico |
| 23        | 150.55          | 12.55        | Simétrico |

### Padrões Observados
- **Simetria**: Distribuição simétrica em relação à sala central
- **Máximo no centro**: Sala central sempre tem maior população
- **Decrescimento linear**: População decresce linearmente conforme se afasta do centro
- **Mortalidade**: Salas das pontas têm menor população devido à mortalidade

## Dependências

### Python
```bash
pip install numpy
```

### C++
- Compilador compatível com C++11 ou superior
- Nenhuma biblioteca externa necessária

## Estrutura do Código

### Python (`simulador_jogo.py`)
- `criar_matriz_transicao(n)`: Cria matriz de probabilidades de transição
- `calcular_populacao_estacionaria(n, taxa_chegada)`: Resolve sistema linear
- `main()`: Interface de linha de comando e exemplos

### C++ (`simulador_jogo.cpp`)
- `class SimuladorJogo`: Encapsula toda a lógica
- `criarMatrizTransicao()`: Cria matriz de transição
- `resolverGaussiana()`: Implementa eliminação gaussiana
- `mostrarResultados()`: Exibe análise detalhada

## Métodos Numéricos Utilizados

1. **Modelagem de Cadeias de Markov**: Matriz de transição
2. **Sistemas Lineares**: Resolução de `(I-P^T)x = b`
3. **Eliminação Gaussiana**: Algoritmo de resolução (C++)
4. **NumPy.linalg.solve**: Resolução otimizada (Python)

## Validação

O programa inclui verificações automáticas:
- Soma das probabilidades por linha ≤ 1.0
- Detecção de matrizes singulares
- Validação de entrada (n ímpar e positivo)

## Autor

Implementação baseada no enunciado do Trabalho II de Métodos Numéricos
Professor: João B. Oliveira
