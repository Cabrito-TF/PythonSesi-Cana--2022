from tkinter import *
import webbrowser
def callback():
    webbrowser.open_new(r"https://www.youtube.com/watch?v=M4eQ5H2hOQM")
janela = Tk()#cria o objeto janela
janela.title('Cainho')#nome da janela  aberta
janela.geometry('500x500')#fixa a resolução da janela em px
janela.configure(bg="#000")#Coloca a cor do fundo como preto
label = Label(janela, text='Beijos Selvagens',
                        font=("arial bold", 20),bg='#512888',fg="#fff")#Configura a caixa com texto
button = Button(janela, text="clica aqui uai",bg="#6C3082",fg="#fff", command=callback
                        ,width='30',height='1')#configura o botão e coloca uma função no botão
button.grid(column=1,row=1)#Determina a posição do botão
label.grid(column=1,row=2)#Determina a posição da caixa de texto
janela.mainloop()#mamtém a janela aberta