from tkinter import *
from tkinter import messagebox

wd=Tk()
wd.title('IMC')
wd.geometry('300x150')

#definindo variáveis de cor
white = '#fff'
bc = '#A81EF7'
med = '#621191'
dark = '#490D6B'
primary = '#F7DB36'
secondary = '#1FAB0C'

#Criando a função principal do programa
def Calcular():
    try:
        a = float(PesoE.get())
        b = float(AlturaE.get())
        c = b*b
        calculado = str(round(a/c,2))
        Resultado = Label(Main, text="seu imc é ".__add__(calculado), bg=med,fg=white)
        Resultado.grid(row=3,column=1,sticky=NSEW)

    except:
        messagebox.showerror(title="erro no cálculo", message="Verifique se você inseriu valores válidos")


#Setting up "Header" kinda
topFrame = Frame(wd, width=300, height=40, bg=bc,padx=0,pady=0,relief='flat')
title = Label(topFrame,text='Calculadora de IMC',bg=bc,fg=white,pady=0,font=("Courier", 15))
line = Frame(wd, width=300, height=10, bg=primary,padx=0,pady=0,relief='flat')

#Rendering Header 
topFrame.grid(row=0,column=0,sticky=NSEW)
line.grid(row=2,column=0,sticky=NSEW)
title.place(in_=topFrame,anchor='c',relx=0.5,rely=0.5)

#Setting up Bottom/Main part of the screen
Main = Frame(wd, width=600, height=410, bg=med ,padx=0,pady=0,relief='flat')
AlturaL = Label(Main, text="Digite sua Altura: ", bg=med,fg=white)
PesoL = Label(Main, text="Digite sua Peso: ", bg=med,fg=white)
AlturaE = Entry(Main,width=10,state="normal",justify="c",textvariable=IntVar, bg=bc, fg=white, relief="flat" )
PesoE = Entry(Main,width=10,state="normal",justify="c",textvariable=IntVar, bg=bc, fg=white, relief="flat" )
CalcButton = Button(Main,width=10,height=1,text="Calcular", command=Calcular, bg=secondary,fg=white)
#Rendering Main
Main.place(in_=wd,anchor='c',relx=0.5, rely=0.65)
AlturaL.grid(row=0,column=0,sticky=NSEW)
PesoL.grid(row=1,column=0,sticky=NSEW)
AlturaE.grid(row=0,column=1,sticky=NSEW)
PesoE.grid(row=1,column=1,sticky=NSEW)
CalcButton.grid(row=3,column=0,sticky=NSEW)


# button = Button(wd, width=10, height=10,text="grow", bg='black')
# button.place(relx=0.5,rely=0.5)

wd.configure(bg=dark)
wd.resizable(False,False)
wd.mainloop()
