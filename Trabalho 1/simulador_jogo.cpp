// Trabalho 1 - Simulador de Jogo Coreano
// Bernardo Klein Heitz 
// Lucas Langer Lantmann

//# para compilar:
//      g++ -o simulador simulador_jogo.cpp

//# executar com diferentes numeros de salas (sempre numeros inteiros impares!)
//      ./simulador 3
//      ./simulador 5
//      ./simulador 7
//      ./simulador 23
//  ou  simulador.exe 3


#include <iostream> // biblioteca para entrada e saída de dados
#include <vector> // uso de vetores
#include <iomanip> // formatação de saída
#include <cmath> 
#include <algorithm> // usar algoritmos

using namespace std; 


class SimuladorJogo { // classe para simular o jogo

private: 
    int n;  // numero de salas
    vector<vector<double>> P;  // matriz de transição
    vector<double> x;  // populacao por sala


    void criarMatrizTransicao() { // função para criar a matriz de transição
        cout << "\n======CRIANDO MATRIZ DE TRANSICAO PARA " << n << " SALAS======\n";
        
        double prob_ficar = 1.0 / n; // prob de ficar na mesma sala
        double prob_mover = 1.0 - prob_ficar; // prob de mover para uma sala vizinha
        
        cout << fixed << setprecision(4); // formata a saida para 4 casas decimais
        cout << "prob de ficar na mesma sala: " << prob_ficar << "\n";
        cout << "prob total de movimento: " << prob_mover << "\n";
        
        // Inicializar matriz com zeros
        P.assign(n, vector<double>(n, 0.0));
        
        for (int i = 0; i < n; i++) { // percorre as salas
            int sala_atual = i + 1; // indice da sala atual
            cout << "\nsala " << sala_atual << ":\n"; // mostra a sala atual
            
            // prob de ficar na mesma sala
            P[i][i] = prob_ficar;
            cout << " ficar na sala " << sala_atual << ": " << prob_ficar << "\n"; // mostra a prob de ficar na sala atual
            
            // Identificar salas vizinhas
            vector<int> vizinhas;
            if (i > 0) vizinhas.push_back(i - 1); // adiciona a sala anterior
            if (i < n - 1) vizinhas.push_back(i + 1); // adiciona a sala posterior
            
            cout << "  salas vizinhas: [";
            for (size_t j = 0; j < vizinhas.size(); j++) {
                cout << (vizinhas[j] + 1); // mostra a sala vizinha
                if (j < vizinhas.size() - 1) cout << ", "; // mostra a sala vizinha
            }
            cout << "]\n"; 
            
            // Distribuir prob de movimento
            if (!vizinhas.empty()) { // se a sala tiver vizinhas
                double prob_por_vizinha; 
                double prob_morte = 0.0;
                
                if (vizinhas.size() == 1) {  // sala da ponta
                    prob_por_vizinha = prob_mover / 2.0; // prob de mover para a vizinha
                    prob_morte = prob_mover / 2.0; // prob de morrer
                    cout << "  prob para vizinha: " << prob_por_vizinha << "\n"; // mostra a prob de mover para a vizinha
                    cout << "  prob de morte: " << prob_morte << "\n"; // mostra a prob de morrer
                } else {  // Sala interna
                    prob_por_vizinha = prob_mover / 2.0; // prob de mover para a vizinha
                    cout << "  prob por vizinha: " << prob_por_vizinha << "\n"; // mostra a prob de mover para a vizinha
                }
                
                for (int j : vizinhas) { // percorre as salas vizinhas
                    P[i][j] = prob_por_vizinha;
                    cout << "  ir para sala " << (j + 1) << ": " << prob_por_vizinha << "\n";
                }
                
                if (vizinhas.size() == 1) { // se a sala tiver apenas uma vizinha
                    cout << "  morte! (sair do jogo): " << prob_morte << "\n";
                }
            }
        }
    }
    

    void resolverSistemaLinear() { // funcao para resolver o sistema linear (Ax = b)
        cout << "\n=====RESOLVENDO SISTEMA LINEAR=====\n";
        
        // criar matriz A = I - P^T
        vector<vector<double>> A(n, vector<double>(n, 0.0)); // matriz A (n x n) 
        for (int i = 0; i < n; i++) { // percorre as linhas
            for (int j = 0; j < n; j++) { // percorre as colunas
                A[i][j] = (i == j ? 1.0 : 0.0) - P[j][i];  // P^T (matriz transposta) 
            }
        }
        
            // criar vetor b (chegadas)
        vector<double> b(n, 0.0); // vetor b (n x 1)
        int sala_central = (n + 1) / 2 - 1;  // indice base 0
        b[sala_central] = 1.0;  // taxa de chegada

        cout << "sala central: " << (sala_central + 1) << " (indice " << sala_central << ")\n"; // indice base 0
        
        // resolver Ax = b usando eliminacao gaussiana
        x = resolverGaussiana(A, b); // chama a funcao resolverGaussiana
    }
    
    vector<double> resolverGaussiana(vector<vector<double>> A, vector<double> b) { // funcao para resolver o sistema linear
        int n = A.size(); // tamanho da matriz A
    
        // eliminacao para frente
        for (int i = 0; i < n; i++) {
            // encontrar pivô
            int max_row = i; // indice da linha com o maior valor absoluto
            for (int k = i + 1; k < n; k++) { // percorre as linhas abaixo da linha i
                if (abs(A[k][i]) > abs(A[max_row][i])) { // abs = valor absoluto
                    max_row = k; // atualiza o indice da linha com o maior valor absoluto
                }
            }
            
            // trocar linhas
            swap(A[i], A[max_row]); // troca as linhas i e max_row
            swap(b[i], b[max_row]); // troca os elementos i e max_row
            
            // tornar diagonal principal 1
            double pivot = A[i][i]; // elemento da diagonal principal
            if (abs(pivot) < 1e-10) { // abs = valor absoluto
                throw runtime_error("matriz singular (o sistema nao pode ser resolvido)"); // matriz singular
            }
            
            for (int k = i; k < n; k++) { // percorre as colunas
                A[i][k] /= pivot; // divide a linha i pelo elemento da diagonal principal
            }
            b[i] /= pivot; // divide o elemento i pelo elemento da diagonal principal
            
            // eliminacao
            for (int k = i + 1; k < n; k++) { // percorre as linhas abaixo da linha i
                double factor = A[k][i]; // elemento da linha k e coluna i
                for (int j = i; j < n; j++) { // percorre as colunas
                    A[k][j] -= factor * A[i][j]; // subtrai o produto do elemento da linha k e coluna j pelo elemento da linha i e coluna j
                }
                b[k] -= factor * b[i]; // subtrai o produto do elemento da linha k pelo elemento da linha i
            }
        }
        
        // substituicao para tras
        vector<double> x(n); // vetor x (n x 1)
        for (int i = n - 1; i >= 0; i--) { // percorre as linhas de baixo para cima
            x[i] = b[i]; // atribui o valor de b[i] para x[i]
            for (int j = i + 1; j < n; j++) { 
                x[i] -= A[i][j] * x[j]; // subtrai o produto do elemento da linha i e coluna j pelo elemento da linha i e coluna j
            }
        }
        
        return x; // retorna o vetor x (solucao do sistema linear)
    }


public: 
    SimuladorJogo(int num_salas) : n(num_salas) { // construtor da classe SimuladorJogo (parametro num_salas) 
        if (n <= 0 || n % 2 == 0) { // se o numero de salas for menor ou igual a 0 ou for par
            throw invalid_argument("n de salas deve ser um inteiro positivo impar!"); // lanca uma excecao
        }
    }
    
    void executar() { // funcao para executar o programa
        cout << "==================================\n";
        cout << "SIMULADOR DE JOGO COREANO\n";
        cout << "==================================\n";
        cout << "simulacao para " << n << " salas\n";
        
        try {
            criarMatrizTransicao(); // chama a funcao criarMatrizTransicao
            resolverSistemaLinear(); // chama a funcao resolverSistemaLinear
            mostrarResultados(); // chama a funcao mostrarResultados
        } catch (const exception& e) {
            cout << "erro: " << e.what() << "\n"; 
        }
    }
    

    void mostrarResultados() { // funcao para mostrar os resultados
        cout << "\n===RESULT FINAL=== :\n";
        
        double populacao_total = 0.0; // populacao total
        for (double pop : x) {
            populacao_total += pop; // soma a populacao de cada sala
        }
        
        cout << fixed << setprecision(0); // formata a saida para 0 casas decimais
        cout << "populacao para " << n << " salas: " << round(populacao_total) << " atores\n";
        
        cout << fixed << setprecision(6); // formata a saida para 6 casas decimais
        cout << "populacao total exata: " << populacao_total << "\n";
        
        cout << "\ndistribuicao por sala:\n";
        cout << fixed << setprecision(4); // formata a saida para 4 casas decimais
        for (int i = 0; i < n; i++) { // percorre as salas
            double percentual = (x[i] / populacao_total) * 100.0; // calcula o percentual de atores em cada sala
            cout << "  sala " << setw(2) << (i + 1) << ": " 
                 << setw(8) << x[i] << " atores (" 
                 << setw(5) << setprecision(1) << percentual << "%)\n";
        }
        
        // analise
        cout << "\nanalise:\n";
        int sala_central = (n + 1) / 2; // indice da sala central
        cout << "  sala central (" << sala_central << "): " 
             << fixed << setprecision(4) << x[sala_central - 1] << " atores\n";
        
        auto max_it = max_element(x.begin(), x.end()); // encontra o maior elemento do vetor x
        auto min_it = min_element(x.begin(), x.end()); // encontra o menor elemento do vetor x
        
        cout << "  sala com + atores: sala numero "  // sala com mais atores
             << (max_it - x.begin() + 1) << " (" << *max_it << ")\n";
        cout << "  sala com - atores: sala numero "  // sala com menos atores
             << (min_it - x.begin() + 1) << " (" << *min_it << ")\n";
    }
};


int main(int argc, char* argv[]) { // funcao principal (argc = numero de argumentos, argv = vetor de argumentos)
    if (argc != 2) { // se o numero de argumentos for diferente de 2
        cout << "uso: " << argv[0] << " <numero_de_salas>\n"; // mostra o uso do programa
        cout << "exemplo: " << argv[0] << " 23\n"; // mostra um exemplo de uso do programa
        return 1; // retorna 1 se o programa for executado com erro
    }
    
    try { // try = tenta executar o codigo
        int n = stoi(argv[1]); // converte o primeiro argumento para um inteiro
        SimuladorJogo simulador(n); // cria um objeto da classe SimuladorJogo
        simulador.executar(); // chama a funcao executar
    } catch (const exception& e) {
        cout << "erro: " << e.what() << "\n"; 
        return 1; // retorna 1 se o programa for executado com erro
    }
    
    return 0; // retorna 0 se o programa for executado com sucesso
}
