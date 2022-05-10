from tkinter import *
from turtle import right

janela = Tk();#declara uma instância da função TK()

a = Button(janela, text='red',fg='#8A39E1')#atribui um bot]ao a variável
a.pack(side=LEFT)
b = Button(janela,text='green',fg='#9C51E0')
b.pack(side=TOP)
c=Button(janela, text='blue',fg='#B667F1')
c.pack(side=BOTTOM)
d = Button(janela, text='key',fg='#ECC488')
d.pack(side=RIGHT)

#pack não há uma sobreposição dos elementos
janela.mainloop()