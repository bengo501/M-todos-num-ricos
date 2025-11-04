import numpy as np
pesos, tempos = np.array([3.0, 5.0, 7.0, 9.0]), np.array([83, 146, 197, 243])   # pesos e tempos em kg e minutos
pesoDoPeru = 6.22#em kg

def metodoLagrange(x, y, pontoDesejado): 
    tamanho, resultado = len(x), 0.0 #   tamanho é o numero de pontos e resultado é o resultado do metodo de lagrange
    for i in range(tamanho):             #percorre todos os pontos 
        polinomioBase = 1.0              # polinomioBase é o produto dos polinomios de lagrange
        for j in range(tamanho):
            if i != j:   #se i for diferente de j
                polinomioBase *= (pontoDesejado - x[j]) / (x[i] - x[j])
        resultado += y[i] * polinomioBase    #resultado do metodo de lagrange
    return resultado 

def metodoNewton(x, y, pontoDesejado):#x e y são os pesos e tempos, pontoDesejado é o peso do peru (ponto que desejamos interpolar)
    tamanho = len(x)
    F = np.zeros((tamanho, tamanho))#F é a matriz de diferenças divididas (tamanho x tamanho) 
    F[:, 0] = y                     #primeira coluna da matriz F é o vetor y (tempos) 
    for j in range(1, tamanho):   
        for i in range(tamanho - j): 
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x[i+j] - x[i]) # F[i, j] é a diferença dividida de ordem j em x[i]
    resultado, produto = F[0, 0], 1.0 
    for i in range(1, tamanho):  
        produto *= (pontoDesejado - x[i-1])    #produto dos polinomios de newton
        resultado += F[0, i] * produto #       resultado do metodo de newton
    return resultado 

# resultado do metodo de lagrange e newton
resultadoLagrange, resultadoNewton = metodoLagrange(pesos, tempos, pesoDoPeru), metodoNewton(pesos, tempos, pesoDoPeru) 
#resultadoLagrange dividido por 60 para obter as horas e o resto para os minutos
horas, minutos = int(resultadoLagrange // 60), int(resultadoLagrange % 60) 

print(" ================================================ ")
print(" metodos numericos - t2 ")
print(f" tempo para assar: peru com peso de {pesoDoPeru} kg ") 
print(" ================================================ ")
print(f"\n metodo lagrange: {resultadoLagrange:.2f} min = {horas}h {minutos:02d}min ") 
print(f" metodo newton:   {resultadoNewton:.2f} min = {horas}h {minutos:02d}min ")
print(f" diferenca: {abs(resultadoLagrange - resultadoNewton):.10f} min ") 
print(" \nverificacao: \n")
for p, t in zip(pesos, tempos):                # p é o peso e t é o tempo
    calc = metodoLagrange(pesos, tempos, p)                   #  calc é o resultado do metodo de lagrange
    print(f" p({p}) = {calc:.2f} (esperado: {t}) {'ok' if abs(calc-t) < 1e-10 else 'erro'} ")
print(f"\n resultado: {horas}h {minutos:02d}min ({resultadoLagrange:.2f} minutos) ")
print(" ================================================ ")