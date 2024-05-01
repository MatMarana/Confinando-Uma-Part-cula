from math import sqrt, sin

ladoCaixa = float(input("Digite o largura da caixa"))
nInicial = int(input("Digite o n Inicial"))
nFinal = int(input("Digite o n Final"))

MASSAELETRON = 9.11e-31
MASSAPROTON = 1.67E-27
PLANCKEV = 4.136e-15
PLANCKJS = 6.26e-34
PI = 3.14
LUZ = 3e8

def funcaoOnda(ladoCaixa,n):
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

    return comprimentoOnda,frequenciaFoton


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
        comprimentoInicial = PLANCKJS / (MASSAELETRON * velocidade[0])
        comprimentoFinal = PLANCKJS / (MASSAELETRON * velocidade[1])

    return comprimentoInicial, comprimentoFinal
    


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
