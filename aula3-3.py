from tkinter import *
from turtle import right

janela = Tk();#declara uma instância da função TK()

a = Button(janela, text='red',fg='#8A39E1')#atribui um bot]ao a variável
a.grid(row=0,column=1)
b = Button(janela,text='green',fg='#9C51E0')
b.grid(row=5,column=4)
c=Button(janela, text='blue',fg='#B667F1')
c.grid(row=6,column=3)
d = Button(janela, text='key',fg='#ECC488')
d.grid(row=2,column=2)

#pack não há uma sobreposição dos elementos
janela.mainloop()