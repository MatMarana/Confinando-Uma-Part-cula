from tkinter import *
from tkinter import messagebox
from ProjetoFisicaParticula import *


# saída de valores / formatar
# Calculadora 2 / Xp e saída de texto
# arrumar probabilidade e ver se tudo ta dando certo / +/-
# gravar vídeo

def onclick():
    global ladoCaixa
    global nInicial
    global nFinal
    global valorA
    global valorB

    ladoCaixa = str(entradaLado.get())
    nInicial = str(entradaNInicial.get())
    nFinal = str(entradaNFinal.get())
    valorA = str(entradaValorA.get())
    valorB = str(entradaValorB.get())

# is.numeric()

    if ladoCaixa == '' or nInicial == '' or nFinal == '':
        messagebox.showinfo('ERRO', "Preencha todos os valores")
    else:
        ladoCaixa = float(ladoCaixa)
        nInicial = float(nInicial)
        nFinal = float(nFinal)  
        valorA = float(ladoCaixa)
        valorB = float(nInicial)

    calculaValores()

    rotulo3['text'] = ['Função de onda no nível inicial: ', funcaoInicial[0], ' * sen(', funcaoInicial[1], ')', 
                    '\nFunção de onda no nível final: ', funcaoFinal[0], ' * sen(', funcaoFinal[1], ')', 
                    '\nEnergia do ' + particula + ' no nível inicial: ' , energiaInicial[0] , 'J/s',
                    '\nEnergia do '+ particula +' no nível inicial: ' , energiaInicial[1], 'eV',
                    '\nEnergia do '+ particula +' no nível final: ', energiaFinal[0], 'J/s',
                    '\nEnergia do '+ particula +' no nível final: ', energiaFinal[1], 'eV',
                    '\nComprimento de onda do fóton: ', valoresFoton[0],
                    '\nFrequencia do fóton: ', valoresFoton[1],
                    '\nEnergia inicial do fóton: ', valoresFoton[2], 
                    '\nEnergia final do fóton: ', valoresFoton[3], 
                    '\nVelocidade do ' + particula + ' no nível inicial: ', velocidade[0], 'm/s',
                    '\nVelocidade do ' + particula + ' no nível final: ', velocidade[1], 'm/s',
                    '\nComprimento de onda de DeBroglie do ' + particula + ' no nível inicial: ',
                    comprimentoDeBrglie[0],
                    '\nComprimento de onda de DeBroglie do '+ particula +' no nível final: ',
                    comprimentoDeBrglie[1],
                    '\nProbabilidade: ', valorProbabilidade[0]]  

def onclick2():
    global Amplitude
    global k
    global Xp

    Amplitude = str(entradaA.get())
    k = str(entradaK.get())
    Xp = str(entradaXp.get())

# is.numeric()

    if Amplitude == '' or k == '' or Xp == '':
        messagebox.showinfo('ERRO', "Preencha todos os valores")
    else:
        Amplitude = float(Amplitude)
        k = float(k) 
        Xp = float(Xp)

    rotulo3['text'] = []

def eletron():
    global particula
    particula = 'Eletron'

def proton():
    global particula
    particula = 'Proton'
    
def calculaValores():
    global funcaoInicial
    global funcaoFinal
    global energiaInicial
    global energiaFinal
    global valoresFoton
    global velocidade
    global comprimentoDeBrglie
    global valorProbabilidade


    # Funções de Onda
    funcaoInicial = funcaoOnda(ladoCaixa,nInicial) 
    funcaoFinal = funcaoOnda(ladoCaixa,nFinal)

    #Energia Nivel Quantico
    energiaInicial = energiaNivelQuantico(ladoCaixa,nInicial,particula)
    energiaFinal = energiaNivelQuantico(ladoCaixa,nFinal,particula)

    #Foton
    valoresFoton = foton(nInicial,nFinal)

    #Velocidade
    velocidade = velocidadeParticula(ladoCaixa,nInicial,nFinal,particula)

    #Comprimento De Broglie
    comprimentoDeBrglie = comprimentoOndaDeBroglie(ladoCaixa,nInicial,nFinal,particula)

    #Probabilidade
    valorProbabilidade = probabilidade(ladoCaixa,nInicial,nFinal,valorA,valorB)


def gerarGraficos():
    plotGraphicFunctionInicial(ladoCaixa,nInicial)
    plotGraphicFunctionFinal(ladoCaixa,nFinal)
    

janela = Tk()
janela.title("Confinando uma Partícula")
janela.geometry('800x800')
janela.resizable(False,False)

rotulo = Label(janela, text="Calculadora 1", font=("Arial Bold", 14))
rotulo.place(x=80,y=10, anchor=N)

rotulo2 = Label(janela, text="Calculadora 2", font=("Arial Bold", 14))
rotulo2.place(x=450,y=10, anchor=N)

lado = Label(janela, text="Lado da Caixa", font=("Arial Bold", 14))
lado.place(x=250,y=50, anchor=N)
entradaLado = Entry(janela,width=14,font=('Arial Bold', 14))
entradaLado.place(x=90, y=50, anchor=N)

LnInicial = Label(janela, text="N Inicial", font=("Arial Bold", 14))
LnInicial.place(x=250,y=90, anchor=N)
entradaNInicial = Entry(janela,width=14,font=('Arial Bold', 14))
entradaNInicial.place(x=90, y=90, anchor=N)

LnFinal = Label(janela, text="N Final", font=("Arial Bold", 14))
LnFinal.place(x=250,y=130, anchor=N)
entradaNFinal = Entry(janela,width=14,font=('Arial Bold', 14))
entradaNFinal.place(x=90, y=130, anchor=N)

LvalorA = Label(janela, text="Valor de A", font=('Arial Bold', 14))
LvalorA.place(x=250,y=170, anchor=N)
entradaValorA = Entry(janela,width=14,font=('Arial Bold', 14))
entradaValorA.place(x=90, y=170, anchor=N)

LvalorB = Label(janela, text="Valor de B", font=('Arial Bold', 14))
LvalorB.place(x=250,y=210, anchor=N)
entradaValorB = Entry(janela,width=14,font=('Arial Bold', 14))
entradaValorB.place(x=90, y=210, anchor=N)

LentradaA = Label(janela, text="A", font=('Arial Bold', 14))
LentradaA.place(x=600, y=50, anchor=N)
entradaA = Entry(janela,width=14,font=('Arial Bold', 14))
entradaA.place(x=470, y=50, anchor=N)

LentradaK = Label(janela, text="K", font=('Arial Bold', 14))
LentradaK.place(x=600, y=90, anchor=N)
entradaK = Entry(janela,width=14,font=('Arial Bold', 14))
entradaK.place(x=470, y=90, anchor=N)

LentradaXp = Label(janela, text="Xp", font=('Arial Bold', 14))
LentradaXp.place(x=600, y=130, anchor=N)
entradaXp = Entry(janela,width=14,font=('Arial Bold', 14))
entradaXp.place(x=470, y=130, anchor=N)

btnEletron = Button(janela, text="Eletron", command=eletron)
btnEletron.place(x=50, y=270,anchor=N)

btnProton = Button(janela, text="Proton", command=proton)
btnProton.place(x=130, y=270,anchor=N)

btnEnviaValores1 = Button(janela, text="Enviar valores", command=onclick)
btnEnviaValores1.place(x=90, y=320,anchor=N)

btnGerador = Button(janela, text="Gerar Gráficos", command=gerarGraficos)
btnGerador.place(x=90, y=350,anchor=N)

btnEnviaValores2 = Button(janela, text="Enviar valores", command=onclick2)
btnEnviaValores2.place(x=500, y=320,anchor=N)

rotulo3 = Label(janela, text="", font=("Arial", 12), background='#FFFFFF',
                highlightbackground='#000000', highlightthickness=3)
rotulo3.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.46)



janela.mainloop()