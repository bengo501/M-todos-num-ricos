
import numpy as np
import matplotlib.pyplot as plt

def exemplo_dois_tanques():
    print("=== SISTEMAS DINÂMICOS: OS DOIS TANQUES ===")
    
    # Problema:
    # Tanque A: Volume Va, recebe água pura a uma taxa F, e troca líquido com Tanque B.
    # Tanque B: Volume Vb, troca líquido com Tanque A.
    # x(t): Quantidade de sal no Tanque A
    # y(t): Quantidade de sal no Tanque B
    
    # Equações (exemplo simplificado):
    # dx/dt = -k1*x + k2*y
    # dy/dt = k1*x - k2*y
    
    # Parâmetros
    k1 = 0.1  # Taxa de transferência A -> B
    k2 = 0.05 # Taxa de transferência B -> A
    
    # Condições iniciais
    x0 = 100.0 # 100kg de sal em A
    y0 = 0.0   # 0kg de sal em B
    
    dt = 0.1
    t_max = 50
    steps = int(t_max / dt)
    
    t = np.linspace(0, t_max, steps)
    x = np.zeros(steps)
    y = np.zeros(steps)
    
    x[0] = x0
    y[0] = y0
    
    print(f"Parâmetros: k1={k1}, k2={k2}")
    print(f"Início: Tanque A={x0}, Tanque B={y0}")
    
    # Método de Euler
    for i in range(steps - 1):
        dxdt = -k1 * x[i] + k2 * y[i]
        dydt = k1 * x[i] - k2 * y[i]
        
        x[i+1] = x[i] + dxdt * dt
        y[i+1] = y[i] + dydt * dt
        
    print(f"Final (t={t_max}): Tanque A={x[-1]:.2f}, Tanque B={y[-1]:.2f}")
    print(f"Total de sal: {x[-1] + y[-1]:.2f} (Conservação de massa)")

def exemplo_epidemias_sir():
    print("\n=== SISTEMAS DINÂMICOS: EPIDEMIAS (MODELO SIR) ===")
    
    # Modelo SIR:
    # S: Suscetíveis
    # I: Infectados
    # R: Recuperados
    
    # Equações:
    # dS/dt = -beta * S * I
    # dI/dt = beta * S * I - gamma * I
    # dR/dt = gamma * I
    
    # Parâmetros
    beta = 0.001  # Taxa de infecção
    gamma = 0.1   # Taxa de recuperação
    
    # Condições iniciais
    S0 = 990
    I0 = 10
    R0 = 0
    
    dt = 0.1
    t_max = 100
    steps = int(t_max / dt)
    
    t = np.linspace(0, t_max, steps)
    S = np.zeros(steps)
    I = np.zeros(steps)
    R = np.zeros(steps)
    
    S[0] = S0
    I[0] = I0
    R[0] = R0
    
    print(f"População Total: {S0+I0+R0}")
    print(f"Parâmetros: beta={beta}, gamma={gamma}")
    print(f"Início: S={S0}, I={I0}, R={R0}")
    
    # Método de Euler
    for i in range(steps - 1):
        dSdt = -beta * S[i] * I[i]
        dIdt = beta * S[i] * I[i] - gamma * I[i]
        dRdt = gamma * I[i]
        
        S[i+1] = S[i] + dSdt * dt
        I[i+1] = I[i] + dIdt * dt
        R[i+1] = R[i] + dRdt * dt
        
    idx_pico = np.argmax(I)
    print(f"Pico de infecção: {I[idx_pico]:.0f} pessoas em t={t[idx_pico]:.1f}")
    print(f"Final (t={t_max}): S={S[-1]:.0f}, I={I[-1]:.0f}, R={R[-1]:.0f}")

if __name__ == "__main__":
    exemplo_dois_tanques()
    exemplo_epidemias_sir()
