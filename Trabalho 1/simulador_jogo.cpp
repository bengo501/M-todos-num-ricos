#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <string>

using namespace std;

class SimuladorJogo {
private:
    int n;  // número de salas
    vector<vector<double>> P;  // matriz de transição
    vector<double> x;  // população por sala

    void criarMatrizTransicao() {
        cout << "\n=== CRIANDO MATRIZ DE TRANSIÇÃO PARA " << n << " SALAS ===\n";
        
        double prob_ficar = 1.0 / n;
        double prob_mover = 1.0 - prob_ficar;
        
        cout << fixed << setprecision(4);
        cout << "Probabilidade de ficar na mesma sala: " << prob_ficar << "\n";
        cout << "Probabilidade total de movimento: " << prob_mover << "\n";
        
        // Inicializar matriz com zeros
        P.assign(n, vector<double>(n, 0.0));
        
        for (int i = 0; i < n; i++) {
            int sala_atual = i + 1;
            cout << "\nSala " << sala_atual << ":\n";
            
            // Probabilidade de ficar na mesma sala
            P[i][i] = prob_ficar;
            cout << "  Ficar na sala " << sala_atual << ": " << prob_ficar << "\n";
            
            // Identificar salas vizinhas
            vector<int> vizinhas;
            if (i > 0) vizinhas.push_back(i - 1);
            if (i < n - 1) vizinhas.push_back(i + 1);
            
            cout << "  Salas vizinhas: [";
            for (size_t j = 0; j < vizinhas.size(); j++) {
                cout << (vizinhas[j] + 1);
                if (j < vizinhas.size() - 1) cout << ", ";
            }
            cout << "]\n";
            
            // Distribuir probabilidade de movimento
            if (!vizinhas.empty()) {
                double prob_por_vizinha;
                double prob_morte = 0.0;
                
                if (vizinhas.size() == 1) {  // Sala da ponta
                    prob_por_vizinha = prob_mover / 2.0;
                    prob_morte = prob_mover / 2.0;
                    cout << "  Probabilidade para vizinha: " << prob_por_vizinha << "\n";
                    cout << "  Probabilidade de morte: " << prob_morte << "\n";
                } else {  // Sala interna
                    prob_por_vizinha = prob_mover / 2.0;
                    cout << "  Probabilidade por vizinha: " << prob_por_vizinha << "\n";
                }
                
                for (int j : vizinhas) {
                    P[i][j] = prob_por_vizinha;
                    cout << "  Ir para sala " << (j + 1) << ": " << prob_por_vizinha << "\n";
                }
                
                if (vizinhas.size() == 1) {
                    cout << "  💀 Morte (sair do jogo): " << prob_morte << "\n";
                }
            }
        }
    }
    
    void resolverSistemaLinear() {
        cout << "\n=== RESOLVENDO SISTEMA LINEAR ===\n";
        
        // Criar matriz A = I - P^T
        vector<vector<double>> A(n, vector<double>(n, 0.0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = (i == j ? 1.0 : 0.0) - P[j][i];  // P^T
            }
        }
        
        // Criar vetor b (chegadas)
        vector<double> b(n, 0.0);
        int sala_central = (n + 1) / 2 - 1;  // índice base 0
        b[sala_central] = 1.0;  // taxa de chegada
        
        cout << "Sala central: " << (sala_central + 1) << " (índice " << sala_central << ")\n";
        
        // Resolver Ax = b usando eliminação gaussiana
        x = resolverGaussiana(A, b);
    }
    
    vector<double> resolverGaussiana(vector<vector<double>> A, vector<double> b) {
        int n = A.size();
        
        // Eliminação para frente
        for (int i = 0; i < n; i++) {
            // Encontrar pivô
            int max_row = i;
            for (int k = i + 1; k < n; k++) {
                if (abs(A[k][i]) > abs(A[max_row][i])) {
                    max_row = k;
                }
            }
            
            // Trocar linhas
            swap(A[i], A[max_row]);
            swap(b[i], b[max_row]);
            
            // Tornar diagonal principal 1
            double pivot = A[i][i];
            if (abs(pivot) < 1e-10) {
                throw runtime_error("Matriz singular - não é possível resolver o sistema");
            }
            
            for (int k = i; k < n; k++) {
                A[i][k] /= pivot;
            }
            b[i] /= pivot;
            
            // Eliminação
            for (int k = i + 1; k < n; k++) {
                double factor = A[k][i];
                for (int j = i; j < n; j++) {
                    A[k][j] -= factor * A[i][j];
                }
                b[k] -= factor * b[i];
            }
        }
        
        // Substituição para trás
        vector<double> x(n);
        for (int i = n - 1; i >= 0; i--) {
            x[i] = b[i];
            for (int j = i + 1; j < n; j++) {
                x[i] -= A[i][j] * x[j];
            }
        }
        
        return x;
    }

public:
    SimuladorJogo(int num_salas) : n(num_salas) {
        if (n <= 0 || n % 2 == 0) {
            throw invalid_argument("Número de salas deve ser um inteiro positivo ímpar!");
        }
    }
    
    void executar() {
        cout << "============================================================\n";
        cout << "SIMULADOR DE JOGO COREANO - VERSÃO C++\n";
        cout << "============================================================\n";
        cout << "Simulação para " << n << " salas\n";
        
        try {
            criarMatrizTransicao();
            resolverSistemaLinear();
            mostrarResultados();
        } catch (const exception& e) {
            cout << "Erro: " << e.what() << "\n";
        }
    }
    
    void mostrarResultados() {
        cout << "\n🎯 RESULTADO FINAL:\n";
        
        double populacao_total = 0.0;
        for (double pop : x) {
            populacao_total += pop;
        }
        
        cout << fixed << setprecision(0);
        cout << "População para " << n << " salas: " << round(populacao_total) << " atores\n";
        
        cout << fixed << setprecision(6);
        cout << "População total exata: " << populacao_total << "\n";
        
        cout << "\nDistribuição por sala:\n";
        cout << fixed << setprecision(4);
        for (int i = 0; i < n; i++) {
            double percentual = (x[i] / populacao_total) * 100.0;
            cout << "  Sala " << setw(2) << (i + 1) << ": " 
                 << setw(8) << x[i] << " atores (" 
                 << setw(5) << setprecision(1) << percentual << "%)\n";
        }
        
        // Análise
        cout << "\nAnálise:\n";
        int sala_central = (n + 1) / 2;
        cout << "  - Sala central (" << sala_central << "): " 
             << fixed << setprecision(4) << x[sala_central - 1] << " atores\n";
        
        auto max_it = max_element(x.begin(), x.end());
        auto min_it = min_element(x.begin(), x.end());
        
        cout << "  - Sala com mais atores: Sala " 
             << (max_it - x.begin() + 1) << " (" << *max_it << ")\n";
        cout << "  - Sala com menos atores: Sala " 
             << (min_it - x.begin() + 1) << " (" << *min_it << ")\n";
    }
};

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "Uso: " << argv[0] << " <número_de_salas>\n";
        cout << "Exemplo: " << argv[0] << " 23\n";
        return 1;
    }
    
    try {
        int n = stoi(argv[1]);
        SimuladorJogo simulador(n);
        simulador.executar();
    } catch (const exception& e) {
        cout << "Erro: " << e.what() << "\n";
        return 1;
    }
    
    return 0;
}
