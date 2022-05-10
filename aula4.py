from tkinter import *

janela = Tk()
janela.title('Aulas sobre entry')
janela.geometry('300x300')

entrada1 = Entry(janela,width=20, state='disabled')
valor = entrada1.get()
txt1 = Label(janela,text='nome')
entrada1.grid(row=1,column=1)
txt1.grid(row=2,column=1)

entrada2 = Entry(janela,width=20)
valor = entrada2.get()
txt2 = Label(janela,text='idade')
entrada2.grid(row=3,column=1)
txt2.grid(row=4,column=1)

entrada3 = Entry(janela,width=20,)
valor = entrada3.get()
txt3 = Label(janela,text='pais')
entrada3.grid(row=5,column=1)
txt3.grid(row=6,column=1)
def click():
    v1 = entrada1.get()
    v2 = entrada2.get()
    v3 = entrada3.get()
    txt4 = Label(janela,text=(v1,v2,v3))
    txt4.grid(row=2,column=2)
    print('\n',v1, '\n', v2, '\n', v3)

button = Button(janela, text='clica me',command=click)
button.grid(row=1,column=2)

janela.mainloop()