from tkinter import *
from tkinter import messagebox
from ProjetoFisicaParticula import *

def onclick():
    global ladoCaixa
    global nInicial
    global nFinal
    global valorA
    global valorB

    ladoCaixa = str(entradaLado.get())
    nInicial = str(entradaNInicial.get())
    nFinal = str(entradaNFinal.get())
    valorA = str(entrada4.get())
    valorB = str(entrada5.get())

    if ladoCaixa == '' or nInicial == '' or nFinal == '':
        messagebox.showinfo('ERRO', "Preencha todos os valores")
    else:
        ladoCaixa = float(ladoCaixa)
        nInicial = int(nInicial)
        nFinal = int(nFinal)  
        valorA = int(ladoCaixa)
        valorB = int(nInicial)
           
    calculaValores()

def eletron():
    global particula
    particula = 'Eletron'

def proton():
    global particula
    particula = 'Proton'
    
def calculaValores():
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
    comprimentoDeBrglie = comprimentoOndaDeBroglie(particula)

    #Probabilidade
    valorProbabilidade = probabilidade(ladoCaixa,nInicial,nFinal,valorA,valorB)






janela = Tk()
janela.title("Confinando uma Partícula")
janela.geometry('800x800')

rotulo = Label(janela, text="Calculadora 1", font=("Arial Bold", 14))
rotulo.place(x=80,y=10, anchor=N)

lado = Label(janela, text="Lado da Caixa", font=("Arial Bold", 14))
lado.place(x=250,y=50, anchor=N)
entradaLado = Entry(janela,width=14,font=('Arial Bold', 14))
entradaLado.place(x=90, y=50, anchor=N)

nInicial = Label(janela, text="N Inicial", font=("Arial Bold", 14))
nInicial.place(x=250,y=90, anchor=N)
entradaNInicial = Entry(janela,width=14,font=('Arial Bold', 14))
entradaNInicial.place(x=90, y=90, anchor=N)

nFinal = Label(janela, text="N Final", font=("Arial Bold", 14))
nFinal.place(x=250,y=130, anchor=N)
entradaNFinal = Entry(janela,width=14,font=('Arial Bold', 14))
entradaNFinal.place(x=90, y=130, anchor=N)

entrada4 = Entry(janela,width=14,font=('Arial Bold', 14))
entrada4.place(x=90, y=170, anchor=N)

entrada5 = Entry(janela,width=14,font=('Arial Bold', 14))
entrada5.place(x=90, y=210, anchor=N)

btn2 = Button(janela, text="Eletron", command=eletron)
btn2.place(x=170, y=270,anchor=CENTER)

btn3 = Button(janela, text="Proton", command=proton)
btn3.place(x=230, y=270,anchor=CENTER)

btn1 = Button(janela, text="Enviar valores", command=onclick)
btn1.place(x=200, y=300,anchor=CENTER)

janela.mainloop()