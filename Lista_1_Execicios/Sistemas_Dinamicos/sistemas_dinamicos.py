"""
Métodos Numéricos - Sistemas Dinâmicos
Solução dos exercícios da Lista 1
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# ============================================================================
# EXERCÍCIO 1: Decaimento radioativo - Comparação exato vs Euler
# ============================================================================

def exercicio1():
    """
    Implementa simulação de decaimento radioativo
    """
    print("=== EXERCÍCIO 1: DECAIMENTO RADIOATIVO ===")
    
    def N_exato(t, N0, tau):
        """
        Solução exata: N(t) = N0 * e^(-t/tau)
        
        FÓRMULA EXPLICADA:
        - N(t): número de átomos no tempo t
        - N0: número inicial de átomos
        - tau (τ): tempo de meia-vida (tempo para metade dos átomos decaírem)
        - e^(-t/tau): fator de decaimento exponencial
        
        Esta é a solução analítica da equação diferencial:
        dN/dt = -N/tau
        """
        return N0 * math.exp(-t / tau)
    
    def N_euler(t, N0, tau, delta_t):
        """
        Aproximação de Euler: N(t + Δt) ≈ N(t) - (N(t)/τ) * Δt
        
        FÓRMULA EXPLICADA:
        - Método de Euler para resolver a EDO: dN/dt = -N/tau
        - N(t + Δt) ≈ N(t) + dN/dt * Δt
        - Como dN/dt = -N/tau, temos: N(t + Δt) ≈ N(t) - (N(t)/tau) * Δt
        - Esta é uma aproximação de primeira ordem (erro proporcional a Δt)
        """
        n_steps = int(t / delta_t)
        N = N0
        
        for i in range(n_steps):
            dN_dt = -N / tau  # Taxa de decaimento
            N = N + dN_dt * delta_t
        
        return N
    
    # Parâmetros
    N0 = 1000  # Número inicial de átomos
    tau = 1.0  # Tempo de meia-vida (em unidades de tempo)
    t_max = 5.0  # Tempo máximo de simulação
    delta_t = 0.1  # Passo de tempo para Euler
    
    print(f"Parâmetros da simulação:")
    print(f"N0 = {N0} átomos (quantidade inicial)")
    print(f"τ = {tau} unidades de tempo (tempo de meia-vida)")
    print(f"Tempo máximo = {t_max} unidades de tempo")
    print(f"Passo de tempo (Euler) = {delta_t} unidades de tempo")
    
    print(f"\nFÓRMULAS UTILIZADAS:")
    print(f"Solução exata: N(t) = N0 * e^(-t/τ) = {N0} * e^(-t/{tau})")
    print(f"Método de Euler: N(t + Δt) ≈ N(t) - (N(t)/τ) * Δt")
    print(f"Taxa de decaimento: dN/dt = -N/τ")
    
    # Calcular valores
    print(f"\n--- RESULTADOS DA SIMULAÇÃO ---")
    print("Tempo\tN(t) exato\tN(t) Euler\tErro\tErro relativo (%)")
    print("-" * 70)
    
    tempos = []
    valores_exatos = []
    valores_euler = []
    erros = []
    erros_relativos = []
    
    for t in np.arange(0, t_max + delta_t, delta_t):
        N_exato_val = N_exato(t, N0, tau)
        N_euler_val = N_euler(t, N0, tau, delta_t)
        
        erro = abs(N_exato_val - N_euler_val)
        erro_relativo = (erro / N_exato_val) * 100 if N_exato_val > 0 else 0
        
        tempos.append(t)
        valores_exatos.append(N_exato_val)
        valores_euler.append(N_euler_val)
        erros.append(erro)
        erros_relativos.append(erro_relativo)
        
        print(f"{t:.1f}\t{N_exato_val:.2f}\t\t{N_euler_val:.2f}\t\t{erro:.2f}\t{erro_relativo:.2f}")
    
    # Análise dos resultados
    print(f"\n--- ANÁLISE DOS RESULTADOS ---")
    
    erro_max = max(erros)
    erro_medio = np.mean(erros)
    erro_relativo_max = max(erros_relativos)
    erro_relativo_medio = np.mean(erros_relativos)
    
    print(f"Erro máximo absoluto: {erro_max:.4f} átomos")
    print(f"Erro médio absoluto: {erro_medio:.4f} átomos")
    print(f"Erro relativo máximo: {erro_relativo_max:.4f}%")
    print(f"Erro relativo médio: {erro_relativo_medio:.4f}%")
    
    # Verificar tempo de meia-vida
    t_meia_vida = tau * math.log(2)
    N_meia_vida_exato = N_exato(t_meia_vida, N0, tau)
    N_meia_vida_euler = N_euler(t_meia_vida, N0, tau, delta_t)
    
    print(f"\nVerificação do tempo de meia-vida:")
    print(f"Tempo de meia-vida teórico: t = τ * ln(2) = {t_meia_vida:.4f}")
    print(f"N(t) exato na meia-vida: {N_meia_vida_exato:.2f} (deveria ser {N0/2:.2f})")
    print(f"N(t) Euler na meia-vida: {N_meia_vida_euler:.2f}")
    print(f"Erro na meia-vida: {abs(N_meia_vida_exato - N_meia_vida_euler):.4f}")
    
    # Gráfico comparativo
    print(f"\nGerando gráfico comparativo...")
    
    plt.figure(figsize=(12, 8))
    
    # Plotar solução exata
    plt.plot(tempos, valores_exatos, 'b-', linewidth=2, label='Solução exata: N(t) = N0 * e^(-t/τ)')
    
    # Plotar aproximação de Euler
    plt.plot(tempos, valores_euler, 'r--', linewidth=2, label='Aproximação de Euler')
    
    # Marcar pontos importantes
    plt.plot(0, N0, 'go', markersize=8, label=f'Condição inicial: N(0) = {N0}')
    plt.plot(t_meia_vida, N0/2, 'mo', markersize=8, label=f'Meia-vida: t = {t_meia_vida:.3f}')
    
    # Configurações do gráfico
    plt.xlabel('Tempo (unidades de tempo)')
    plt.ylabel('Número de átomos N(t)')
    plt.title('Decaimento Radioativo: Solução Exata vs Método de Euler')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')  # Escala logarítmica para melhor visualização
    
    plt.tight_layout()
    plt.show()
    
    # Gráfico do erro
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(tempos, erros, 'r-', linewidth=2)
    plt.xlabel('Tempo')
    plt.ylabel('Erro absoluto')
    plt.title('Erro Absoluto vs Tempo')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(tempos, erros_relativos, 'g-', linewidth=2)
    plt.xlabel('Tempo')
    plt.ylabel('Erro relativo (%)')
    plt.title('Erro Relativo vs Tempo')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nOBSERVAÇÕES:")
    print("- O método de Euler aproxima bem a solução exata")
    print("- O erro aumenta com o tempo, mas permanece controlado")
    print("- A aproximação é melhor para passos de tempo menores")
    print("- O decaimento exponencial é bem modelado pelo método de Euler")
    print("- O erro é proporcional ao passo de tempo Δt (método de primeira ordem)")

# ============================================================================
# EXERCÍCIO 2: Pêndulo simples - Simulação numérica
# ============================================================================

def exercicio2():
    """
    Implementa simulação de pêndulo simples
    """
    print("=== EXERCÍCIO 2: PÊNDULO SIMPLES ===")
    
    def simular_pendulo(theta0, omega0, L, g, t_max, delta_t):
        """
        Simula pêndulo simples usando método de Euler
        
        FÓRMULAS EXPLICADAS:
        
        Equações diferenciais do pêndulo:
        dθ/dt = ω(t)                    # Velocidade angular
        dω/dt = -(g/L) * sin(θ(t))      # Aceleração angular
        
        Método de Euler:
        θ(t + Δt) ≈ θ(t) + ω(t) * Δt
        ω(t + Δt) ≈ ω(t) - (g/L) * sin(θ(t)) * Δt
        
        Coordenadas cartesianas:
        x(t) = L * sin(θ(t))            # Posição horizontal
        y(t) = L * (1 - cos(θ(t)))      # Posição vertical (referência no topo)
        """
        # Condições iniciais
        theta = theta0  # Ângulo inicial
        omega = omega0  # Velocidade angular inicial
        
        # Listas para armazenar resultados
        tempos = []
        angulos = []
        velocidades = []
        posicoes_x = []
        posicoes_y = []
        
        # Simulação
        t = 0
        while t <= t_max:
            tempos.append(t)
            angulos.append(theta)
            velocidades.append(omega)
            
            # Calcular posições cartesianas
            x = L * math.sin(theta)
            y = L * (1 - math.cos(theta))
            posicoes_x.append(x)
            posicoes_y.append(y)
            
            # Método de Euler
            # θ(t + Δt) ≈ θ(t) + ω(t) * Δt
            # ω(t + Δt) ≈ ω(t) - (g/L) * sin(θ(t)) * Δt
            
            theta_novo = theta + omega * delta_t
            omega_novo = omega - (g / L) * math.sin(theta) * delta_t
            
            theta = theta_novo
            omega = omega_novo
            t += delta_t
        
        return tempos, angulos, velocidades, posicoes_x, posicoes_y
    
    # Parâmetros
    theta0 = math.pi / 4  # 45 graus
    omega0 = 0  # Velocidade inicial zero
    L = 1.0  # Comprimento do pêndulo (metros)
    g = 9.81  # Aceleração da gravidade (m/s²)
    t_max = 10.0  # Tempo máximo de simulação (segundos)
    delta_t = 0.01  # Passo de tempo (segundos)
    
    print(f"Parâmetros da simulação:")
    print(f"Ângulo inicial: θ₀ = {theta0:.4f} rad = {math.degrees(theta0):.1f}°")
    print(f"Velocidade angular inicial: ω₀ = {omega0} rad/s")
    print(f"Comprimento do pêndulo: L = {L} m")
    print(f"Aceleração da gravidade: g = {g} m/s²")
    print(f"Tempo de simulação: {t_max} s")
    print(f"Passo de tempo: Δt = {delta_t} s")
    
    print(f"\nFÓRMULAS UTILIZADAS:")
    print(f"Equações diferenciais:")
    print(f"  dθ/dt = ω(t)")
    print(f"  dω/dt = -(g/L) * sin(θ(t)) = -({g}/{L}) * sin(θ(t)) = -{g/L:.2f} * sin(θ(t))")
    print(f"Método de Euler:")
    print(f"  θ(t + Δt) ≈ θ(t) + ω(t) * Δt")
    print(f"  ω(t + Δt) ≈ ω(t) - (g/L) * sin(θ(t)) * Δt")
    print(f"Coordenadas cartesianas:")
    print(f"  x(t) = L * sin(θ(t)) = {L} * sin(θ(t))")
    print(f"  y(t) = L * (1 - cos(θ(t))) = {L} * (1 - cos(θ(t)))")
    
    # Simular pêndulo
    tempos, angulos, velocidades, posicoes_x, posicoes_y = simular_pendulo(theta0, omega0, L, g, t_max, delta_t)
    
    # Calcular período teórico (aproximação para pequenos ângulos)
    T_teorico = 2 * math.pi * math.sqrt(L / g)
    print(f"\nPeríodo teórico (pequenos ângulos): T = 2π√(L/g) = 2π√({L}/{g}) = {T_teorico:.4f} s")
    
    # Encontrar período da simulação
    def encontrar_periodo(tempos, angulos):
        """Encontra o período da oscilação"""
        # Procurar por cruzamentos com zero
        cruzamentos = []
        for i in range(1, len(angulos)):
            if angulos[i-1] * angulos[i] < 0:  # Mudança de sinal
                # Interpolação linear para encontrar tempo exato
                t1, t2 = tempos[i-1], tempos[i]
                a1, a2 = angulos[i-1], angulos[i]
                t_cruzamento = t1 - a1 * (t2 - t1) / (a2 - a1)
                cruzamentos.append(t_cruzamento)
        
        if len(cruzamentos) >= 2:
            periodos = []
            for i in range(1, len(cruzamentos)):
                periodos.append(2 * (cruzamentos[i] - cruzamentos[i-1]))
            return np.mean(periodos)
        else:
            return None
    
    T_simulado = encontrar_periodo(tempos, angulos)
    if T_simulado:
        print(f"Período da simulação: T = {T_simulado:.4f} s")
        print(f"Diferença: {abs(T_simulado - T_teorico):.4f} s")
        print(f"Erro relativo: {abs(T_simulado - T_teorico)/T_teorico*100:.2f}%")
    
    # Análise da energia
    def calcular_energia(theta, omega, m=1.0):
        """
        Calcula energia total do pêndulo
        
        FÓRMULAS EXPLICADAS:
        Energia cinética: E_c = (1/2) * m * L² * ω²
        Energia potencial: E_p = m * g * L * (1 - cos(θ))
        Energia total: E = E_c + E_p
        
        Para m = 1 kg, L = 1 m:
        E_c = (1/2) * ω²
        E_p = g * (1 - cos(θ))
        """
        # Energia cinética: E_c = (1/2) * m * L² * ω²
        E_c = 0.5 * m * L**2 * omega**2
        
        # Energia potencial: E_p = m * g * L * (1 - cos(θ))
        E_p = m * g * L * (1 - math.cos(theta))
        
        return E_c + E_p
    
    energias = [calcular_energia(theta, omega) for theta, omega in zip(angulos, velocidades)]
    energia_inicial = energias[0]
    
    print(f"\nAnálise da energia:")
    print(f"Energia inicial: {energia_inicial:.6f} J")
    print(f"Energia final: {energias[-1]:.6f} J")
    print(f"Variação da energia: {abs(energias[-1] - energia_inicial):.6f} J")
    print(f"Variação relativa: {abs(energias[-1] - energia_inicial)/energia_inicial*100:.4f}%")
    
    # Mostrar alguns valores da simulação
    print(f"\n--- VALORES DA SIMULAÇÃO ---")
    print("Tempo\tθ (rad)\tω (rad/s)\tx (m)\ty (m)\tEnergia (J)")
    print("-" * 70)
    
    for i in range(0, len(tempos), len(tempos)//10):  # Mostrar 10 pontos
        t = tempos[i]
        theta = angulos[i]
        omega = velocidades[i]
        x = posicoes_x[i]
        y = posicoes_y[i]
        energia = energias[i]
        print(f"{t:.2f}\t{theta:.4f}\t{omega:.4f}\t\t{x:.4f}\t{y:.4f}\t{energia:.4f}")
    
    # Gráficos
    print(f"\nGerando gráficos da simulação...")
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # Gráfico 1: Ângulo vs tempo
    axes[0, 0].plot(tempos, angulos, 'b-', linewidth=2)
    axes[0, 0].set_xlabel('Tempo (s)')
    axes[0, 0].set_ylabel('Ângulo θ (rad)')
    axes[0, 0].set_title('Ângulo vs Tempo')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Gráfico 2: Velocidade angular vs tempo
    axes[0, 1].plot(tempos, velocidades, 'r-', linewidth=2)
    axes[0, 1].set_xlabel('Tempo (s)')
    axes[0, 1].set_ylabel('Velocidade angular ω (rad/s)')
    axes[0, 1].set_title('Velocidade Angular vs Tempo')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Gráfico 3: Energia vs tempo
    axes[0, 2].plot(tempos, energias, 'g-', linewidth=2)
    axes[0, 2].set_xlabel('Tempo (s)')
    axes[0, 2].set_ylabel('Energia total (J)')
    axes[0, 2].set_title('Energia Total vs Tempo')
    axes[0, 2].grid(True, alpha=0.3)
    
    # Gráfico 4: Diagrama de fase (θ vs ω)
    axes[1, 0].plot(angulos, velocidades, 'm-', linewidth=2)
    axes[1, 0].set_xlabel('Ângulo θ (rad)')
    axes[1, 0].set_ylabel('Velocidade angular ω (rad/s)')
    axes[1, 0].set_title('Diagrama de Fase: θ vs ω')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Gráfico 5: Trajetória no espaço (x vs y)
    axes[1, 1].plot(posicoes_x, posicoes_y, 'c-', linewidth=2)
    axes[1, 1].set_xlabel('Posição x (m)')
    axes[1, 1].set_ylabel('Posição y (m)')
    axes[1, 1].set_title('Trajetória no Espaço: x vs y')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_aspect('equal')  # Manter proporção 1:1
    
    # Gráfico 6: Posições x e y vs tempo
    axes[1, 2].plot(tempos, posicoes_x, 'b-', linewidth=2, label='x(t)')
    axes[1, 2].plot(tempos, posicoes_y, 'r-', linewidth=2, label='y(t)')
    axes[1, 2].set_xlabel('Tempo (s)')
    axes[1, 2].set_ylabel('Posição (m)')
    axes[1, 2].set_title('Posições x e y vs Tempo')
    axes[1, 2].legend()
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nOBSERVAÇÕES:")
    print("- O pêndulo oscila com período aproximadamente constante")
    print("- A energia total deveria ser conservada (mas há pequenas variações)")
    print("- O diagrama de fase mostra uma trajetória elíptica")
    print("- O método de Euler introduz pequenos erros que se acumulam")
    print("- Para simulações mais precisas, usar métodos de ordem superior")
    print("- A trajetória no espaço mostra o movimento circular do pêndulo")

# ============================================================================
# EXERCÍCIO 3: Comparação de diferentes métodos numéricos
# ============================================================================

def exercicio3():
    """
    Compara diferentes métodos numéricos para o pêndulo
    """
    print("=== EXERCÍCIO 3: COMPARAÇÃO DE MÉTODOS NUMÉRICOS ===")
    
    def euler(theta0, omega0, L, g, t_max, delta_t):
        """Método de Euler explícito"""
        theta = theta0
        omega = omega0
        tempos = []
        angulos = []
        velocidades = []
        
        t = 0
        while t <= t_max:
            tempos.append(t)
            angulos.append(theta)
            velocidades.append(omega)
            
            # Euler explícito
            theta_novo = theta + omega * delta_t
            omega_novo = omega - (g / L) * math.sin(theta) * delta_t
            
            theta = theta_novo
            omega = omega_novo
            t += delta_t
        
        return tempos, angulos, velocidades
    
    def euler_cromer(theta0, omega0, L, g, t_max, delta_t):
        """
        Método de Euler-Cromer (Euler semi-implícito)
        
        FÓRMULA EXPLICADA:
        θ(t + Δt) = θ(t) + ω(t + Δt) * Δt
        ω(t + Δt) = ω(t) - (g/L) * sin(θ(t)) * Δt
        
        Note que ω(t + Δt) é calculado primeiro, depois usado para θ(t + Δt)
        """
        theta = theta0
        omega = omega0
        tempos = []
        angulos = []
        velocidades = []
        
        t = 0
        while t <= t_max:
            tempos.append(t)
            angulos.append(theta)
            velocidades.append(omega)
            
            # Euler-Cromer
            omega_novo = omega - (g / L) * math.sin(theta) * delta_t
            theta_novo = theta + omega_novo * delta_t
            
            theta = theta_novo
            omega = omega_novo
            t += delta_t
        
        return tempos, angulos, velocidades
    
    def verlet(theta0, omega0, L, g, t_max, delta_t):
        """
        Método de Verlet para o pêndulo
        
        FÓRMULA EXPLICADA:
        Para um sistema com aceleração a(θ) = -(g/L) * sin(θ):
        
        θ(t + Δt) = 2θ(t) - θ(t - Δt) + a(θ(t)) * Δt²
        ω(t) = (θ(t + Δt) - θ(t - Δt)) / (2Δt)
        
        Este método é de segunda ordem e conserva melhor a energia
        """
        # Inicialização: precisamos de dois pontos iniciais
        theta_prev = theta0 - omega0 * delta_t  # Aproximação para θ(t - Δt)
        theta = theta0
        tempos = []
        angulos = []
        velocidades = []
        
        t = 0
        while t <= t_max:
            tempos.append(t)
            angulos.append(theta)
            
            # Calcular velocidade
            omega = (theta - theta_prev) / (2 * delta_t)
            velocidades.append(omega)
            
            # Verlet
            a = -(g / L) * math.sin(theta)  # Aceleração
            theta_novo = 2 * theta - theta_prev + a * delta_t**2
            
            theta_prev = theta
            theta = theta_novo
            t += delta_t
        
        return tempos, angulos, velocidades
    
    # Parâmetros
    theta0 = math.pi / 6  # 30 graus
    omega0 = 0
    L = 1.0
    g = 9.81
    t_max = 5.0
    delta_t = 0.01
    
    print(f"Comparação de métodos numéricos para o pêndulo:")
    print(f"Ângulo inicial: θ₀ = {theta0:.4f} rad = {math.degrees(theta0):.1f}°")
    print(f"Velocidade inicial: ω₀ = {omega0} rad/s")
    print(f"Tempo de simulação: {t_max} s")
    print(f"Passo de tempo: Δt = {delta_t} s")
    
    # Simular com diferentes métodos
    print(f"\nSimulando com diferentes métodos...")
    
    t_euler, theta_euler, omega_euler = euler(theta0, omega0, L, g, t_max, delta_t)
    t_cromer, theta_cromer, omega_cromer = euler_cromer(theta0, omega0, L, g, t_max, delta_t)
    t_verlet, theta_verlet, omega_verlet = verlet(theta0, omega0, L, g, t_max, delta_t)
    
    # Calcular energia para cada método
    def energia_media(angulos, velocidades):
        """Calcula energia média ao longo da simulação"""
        energias = []
        for theta, omega in zip(angulos, velocidades):
            E_c = 0.5 * L**2 * omega**2
            E_p = g * L * (1 - math.cos(theta))
            energias.append(E_c + E_p)
        return np.mean(energias), np.std(energias)
    
    E_med_euler, E_std_euler = energia_media(theta_euler, omega_euler)
    E_med_cromer, E_std_cromer = energia_media(theta_cromer, omega_cromer)
    E_med_verlet, E_std_verlet = energia_media(theta_verlet, omega_verlet)
    
    # Energia inicial
    E_inicial = g * L * (1 - math.cos(theta0))
    
    print(f"\n--- ANÁLISE DE CONSERVAÇÃO DE ENERGIA ---")
    print(f"Energia inicial: {E_inicial:.6f} J")
    print(f"\nMétodo\t\tEnergia Média\tDesvio Padrão\tVariação (%)")
    print("-" * 60)
    print(f"Euler\t\t{E_med_euler:.6f}\t{E_std_euler:.6f}\t{abs(E_med_euler-E_inicial)/E_inicial*100:.2f}%")
    print(f"Euler-Cromer\t{E_med_cromer:.6f}\t{E_std_cromer:.6f}\t{abs(E_med_cromer-E_inicial)/E_inicial*100:.2f}%")
    print(f"Verlet\t\t{E_med_verlet:.6f}\t{E_std_verlet:.6f}\t{abs(E_med_verlet-E_inicial)/E_inicial*100:.2f}%")
    
    # Gráfico comparativo
    plt.figure(figsize=(15, 10))
    
    # Gráfico 1: Ângulos
    plt.subplot(2, 2, 1)
    plt.plot(t_euler, theta_euler, 'b-', linewidth=2, label='Euler')
    plt.plot(t_cromer, theta_cromer, 'r-', linewidth=2, label='Euler-Cromer')
    plt.plot(t_verlet, theta_verlet, 'g-', linewidth=2, label='Verlet')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Ângulo θ (rad)')
    plt.title('Comparação: Ângulo vs Tempo')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfico 2: Velocidades
    plt.subplot(2, 2, 2)
    plt.plot(t_euler, omega_euler, 'b-', linewidth=2, label='Euler')
    plt.plot(t_cromer, omega_cromer, 'r-', linewidth=2, label='Euler-Cromer')
    plt.plot(t_verlet, omega_verlet, 'g-', linewidth=2, label='Verlet')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade angular ω (rad/s)')
    plt.title('Comparação: Velocidade vs Tempo')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfico 3: Diagramas de fase
    plt.subplot(2, 2, 3)
    plt.plot(theta_euler, omega_euler, 'b-', linewidth=2, label='Euler')
    plt.plot(theta_cromer, omega_cromer, 'r-', linewidth=2, label='Euler-Cromer')
    plt.plot(theta_verlet, omega_verlet, 'g-', linewidth=2, label='Verlet')
    plt.xlabel('Ângulo θ (rad)')
    plt.ylabel('Velocidade angular ω (rad/s)')
    plt.title('Comparação: Diagramas de Fase')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfico 4: Energia ao longo do tempo
    plt.subplot(2, 2, 4)
    
    # Calcular energia para cada método
    def energia_tempo(angulos, velocidades):
        energias = []
        for theta, omega in zip(angulos, velocidades):
            E_c = 0.5 * L**2 * omega**2
            E_p = g * L * (1 - math.cos(theta))
            energias.append(E_c + E_p)
        return energias
    
    E_euler = energia_tempo(theta_euler, omega_euler)
    E_cromer = energia_tempo(theta_cromer, omega_cromer)
    E_verlet = energia_tempo(theta_verlet, omega_verlet)
    
    plt.plot(t_euler, E_euler, 'b-', linewidth=2, label='Euler')
    plt.plot(t_cromer, E_cromer, 'r-', linewidth=2, label='Euler-Cromer')
    plt.plot(t_verlet, E_verlet, 'g-', linewidth=2, label='Verlet')
    plt.axhline(y=E_inicial, color='k', linestyle='--', alpha=0.5, label='Energia inicial')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Energia total (J)')
    plt.title('Comparação: Energia vs Tempo')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nOBSERVAÇÕES:")
    print("- O método de Verlet conserva melhor a energia")
    print("- Euler-Cromer é uma melhoria sobre Euler explícito")
    print("- Euler explícito tende a ganhar energia (instabilidade)")
    print("- Verlet é um método de segunda ordem mais preciso")
    print("- A escolha do método depende da aplicação e requisitos")

# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todos os exercícios de Sistemas Dinâmicos
    """
    print("MÉTODOS NUMÉRICOS - SISTEMAS DINÂMICOS")
    print("=" * 60)
    
    # Executar exercícios
    print("\n" + "="*60)
    exercicio1()
    
    print("\n" + "="*60)
    exercicio2()
    
    print("\n" + "="*60)
    exercicio3()
    
    print("\n" + "="*60)
    print("EXECUÇÃO CONCLUÍDA!")
    print("Todos os exercícios de Sistemas Dinâmicos foram resolvidos.")

if __name__ == "__main__":
    main()
