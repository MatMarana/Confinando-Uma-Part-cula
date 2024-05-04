from math import sqrt, sin
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

ladoCaixa = float(input("Digite o largura da caixa"))
nInicial = int(input("Digite o n Inicial"))
nFinal = int(input("Digite o n Final"))

a = int(input("Digite o valor de a"))
b = int(input("Digite o valor de b"))

MASSAELETRON = 9.11e-31
MASSAPROTON = 1.67E-27
PLANCKEV = 4.136e-15
PLANCKJS = 6.26e-34
PI = 3.14
LUZ = 3e8

def funcaoOnda(ladoCaixa,n): # Funciona
    raiz = sqrt(2/ladoCaixa)
    seno = (n * PI) / ladoCaixa
    
    return raiz,seno

def energiaNivelQuantico(ladoCaixa, n, particula):
    if particula == 'Eletron':
        energia = ((PLANCKJS**2) / 8 * MASSAELETRON * (ladoCaixa**2)) * (n**2)
    elif particula == 'Proton':
        energia = ((PLANCKJS**2) / 8 * MASSAPROTON * (ladoCaixa**2)) * (n**2)

    energiaConvertida = conversor(energia,'Js')
    return energia, energiaConvertida

def conversor(energia, medida):
    if medida == 'Ev':
        energia = energia * 1.602e-19
    elif medida == 'Js':
        energia = energia / 1.602e-19

    return energia

def energiaFoton(n):
    energiaFoton = -13.6 / (n**2)
    return energiaFoton

def foton():
    energiaInicial = energiaFoton(nInicial)
    energiaFinal = energiaFoton(nFinal)
    energiaAbsoluta = abs(energiaFinal - energiaInicial)

    comprimentoOnda = (PLANCKEV * LUZ) / energiaAbsoluta
    frequenciaFoton = energiaAbsoluta / PLANCKEV

    return comprimentoOnda,frequenciaFoton,energiaInicial,energiaFinal


def velocidadeParticula(particula):
    if particula == 'Eletron':
        energiaInicial = energiaNivelQuantico(ladoCaixa,nInicial,"Eletron")
        energiaFinal = energiaNivelQuantico(ladoCaixa,nFinal,"Eletron")
        velocidadeInicial = sqrt((2 * energiaInicial[0]) / MASSAELETRON)
        velocidadeFinal = sqrt((2 * energiaFinal[0]) / MASSAELETRON)
    elif particula == 'Proton':
        energiaInicial = energiaNivelQuantico(ladoCaixa,nInicial,"Proton")
        energiaFinal = energiaNivelQuantico(ladoCaixa,nFinal,"Proton")
        velocidadeInicial = sqrt((2 * energiaInicial[0]) / MASSAPROTON)
        velocidadeFinal = sqrt((2 * energiaFinal[0]) / MASSAPROTON)

    return velocidadeInicial, velocidadeFinal

def comprimentoOndaDeBroglie(particula):
    if particula == 'Eletron':
        velocidade = velocidadeParticula("Eletron")
        comprimentoInicial = PLANCKJS / (MASSAELETRON * velocidade[0])
        comprimentoFinal = PLANCKJS / (MASSAELETRON * velocidade[1])
    elif particula == 'Proton':
        velocidade = velocidadeParticula("Proton")
        comprimentoInicial = PLANCKJS / (MASSAPROTON * velocidade[0])
        comprimentoFinal = PLANCKJS / (MASSAPROTON * velocidade[1])

    return comprimentoInicial, comprimentoFinal
    
def probabilidade():
    valoresInicial = funcaoOnda(ladoCaixa, nInicial)
    valoresFinal = funcaoOnda(ladoCaixa, nFinal)
    x = sp.simblos('x')

    funcaoInicial = valoresInicial[0] * sin(valoresInicial[1] * x) 
    funcaoFinal = valoresFinal[0] * sin(valoresInicial[1] * x)

    probabilidadeInicial = sp.integrate((funcaoInicial**2),(x,a,b)) 
    probabilidadeFinal = sp.integrate((funcaoFinal**2),(x,a,b))

    return probabilidadeInicial, probabilidadeFinal


L = 1.0  # Lado da caixa (comprimento)
n = 3    # Nível quântico
A = 1.0  # Amplitude

# Função de onda
def wave_function(x):
    return A * np.sin(n * np.pi * x / L)

# Valores de x (posição)
x_values = np.linspace(0, L, 1000)

# Calcula os valores da função de onda
psi_values = wave_function(x_values)

# Plota o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_values, psi_values, label=f"n = {n}")
plt.xlabel("Posição (x)")
plt.ylabel("Função de Onda (Ψ(x))")
plt.title("Gráfico da Função de Onda")
plt.grid(True)
plt.legend()
plt.show()


prob_values = psi_values**2

plt.plot(x_values, prob_values, label="Probabilidade")
plt.xlabel("Posição (x)")
plt.ylabel("Probabilidade")
plt.title("Gráfico de Probabilidade da Função de Onda")
plt.legend()
plt.grid(True)
plt.show()


while(True):
    print("Escolha uma opção:")
    print("1 - Calcular a função da onda")
    print("2 - Calcular a Energia no nível quantico")
    print("3 - Calcular os atributos do Fóton")
    print("4 - Calcular a velocidade da particula")
    print("5 - Calcular o comprimento da onda de De Broglie")
    print("6 - Calcular a probabilidade")
    escolha = int(input())

    if escolha == 1:
        funcaoInicial = funcaoOnda(ladoCaixa, nInicial)
        funcaoFinal = funcaoOnda(ladoCaixa, nFinal)
        print("O valor da função no nivel inicial: ")
        print(funcaoInicial[0], " ( ", funcaoInicial[1], "x)")
        print("O valor da função no nivel final: ")
        print(funcaoFinal[0], " ( ", funcaoFinal[1], "x)")
    elif escolha == 2:
        print("Escolha a particula desejada: ")
        print("1 - Para Eletron")
        print("2 - para Proton")
        escolhaParticula = int(input())
        if escolhaParticula == 1:
            energiaInicial = energiaNivelQuantico(ladoCaixa, nInicial, "Eletron")
            energiaFinal = energiaNivelQuantico(ladoCaixa, nFinal, "Eletron")
        elif escolhaParticula == 2:
            energiaInicial = energiaNivelQuantico(ladoCaixa, nInicial, "Proton")
            energiaFinal = energiaNivelQuantico(ladoCaixa, nFinal, "Proton")
        
        print("A energia da particula desejada em J/s, no nivel inicial:")
        print(energiaInicial[0])
        print("A energia da particula desejada em eV, no nivel inicial:")
        print(energiaInicial[1])
        print("A energia da particula desejada em J/s, no nivel final:")
        print(energiaFinal[0])
        print("A energia da particula desejada em eV, no nivel final:")
        print(energiaFinal[1])
    elif escolha == 3:
        fotonMedidas = foton()
        print("compirmento de onda", fotonMedidas[0])
        print("frequencia", fotonMedidas[1])
    elif escolha == 4:
        print("Escolha a particula desejada: ")
        print("1 - Para Eletron")
        print("2 - para Proton")
        escolhaParticula = int(input())
        if escolhaParticula == 1:
            velocidade = velocidadeParticula("Eletron")
        elif escolhaParticula == 2:
            velocidade = velocidadeParticula("Proton")

        print("A energia da particula desejada  no nivel inicial:")
        print(velocidade[0])
        print("A energia da particula desejada  no nivel inicial:")
        print(velocidade[1])
    elif escolha == 5:
        print("Escolha a particula desejada: ")
        print("1 - Para Eletron")
        print("2 - para Proton")
        escolhaParticula = int(input())
        if escolhaParticula == 1:
            compirmentoDeBroglie = comprimentoOndaDeBroglie("Eletron")
        elif escolhaParticula == 2:
            compirmentoDeBroglie = comprimentoOndaDeBroglie("Proton")
    elif escolha == 6:
        prob = probabilidade()
    elif escolha == 0:
        break
    
    

# 1 / lambda = R(1/nf^2 - 1/ni^2)
# Energia de um fóton = hf (planck e frequencia)
# Energia = (hc) / lambda (c = constante da luz (3e8))
# se dado em joules dividir por 1.602e-19
# se dado em eV multiplicar pelo valor acima
# momento linear da particula (p) = massa(m) * velocidade (v)
# momento linear do fóton (p) = planck(h) / lambda
# comprimento de onda de De Broglie de uma particula lambda = h/p = h/(m*v) = h/sqrt(2mE)
# energia de uma particula = E = 1/2(m*v²) = p²/2m
# comprimento de onda do fóton = h * c / (|Ef - Ei|)
# En = -13,6/n² eV
# absorção  ef > ei
# emissão ef < ei
# função = sqrt(2/Lado) sen((n*Pi)/L * x)
# energia n = ((h^2)/ 8m(L^2)) * n^2  
# massa eletron = 9.11 * 10e-31
# h = 6.626 * 10e-34 em J*s 
# massa proton = 1.67 * 10e-27 
# integral a - b (função de onda)^2 dx
