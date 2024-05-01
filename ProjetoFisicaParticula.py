from math import sqrt, sin

ladoCaixa = float(input("Digite o largura da caixa"))
nInicial = int(input("Digite o n Inicial"))
nFinal = int(input("Digite o n Final"))
massaParticula = 9.11 * (10 ** -31)
PLANCK = 4.136 #E-15 em eV

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

EnergiaFinal = -13.6 / nFinal**2
EnergiaInicial = -13.6 / nInicial**2
EnergiaFoton = EnergiaFinal - EnergiaInicial
comprimentoOndaFoton = ((PLANCK*(10**-15)) * (3*(10**8))) / (abs(EnergiaFoton))
FrequenciaFoton = EnergiaFoton / (PLANCK*10**-15)
velocidadeInicial = sqrt(2 * EnergiaInicial) / massaParticula
velocidadeFinal = sqrt(2 * EnergiaFinal) / massaParticula
comprimentoDeBroglieI = (PLANCK * (10 **-15)) / massaParticula * velocidadeInicial
comprimentoDeBroglieF = (PLANCK * (10 **-15)) / massaParticula * velocidadeFinal



