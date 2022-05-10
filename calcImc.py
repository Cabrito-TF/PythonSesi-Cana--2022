from tkinter import *

wd=Tk()
wd.title('IMC')
wd.geometry('600x450')

#definindo variáveis de cor
white = '#fff'
bc = '#A81EF7'
med = '#621191'
dark = '#490D6B'
primary = '#F7DB36'
secondary = '#1FAB0C'

#dividindo a tela em frames
topFrame = Frame(wd, width=600, height=40, bg=bc,padx=0,pady=0,relief='flat')
topFrame.grid(row=0,column=0,sticky=NSEW)

title = Label(topFrame,text='Calculadora de IMC',bg=bc,fg=white,padx=250,pady=0)
title.place(in_=topFrame,anchor='c',relx=0.5,rely=0.5)

line = Frame(wd, width=600, height=20, bg=primary,padx=0,pady=0,relief='flat')
line.grid(row=2,column=0,sticky=NSEW)

bottomFrame = Frame(wd, width=600, height=410, bg=med,padx=0,pady=0,relief='flat')
bottomFrame.grid(row=5,column=0,sticky=NSEW)

line = Frame(wd, width=10, height=10, bg="black",padx=0,pady=0,relief='flat')
line.grid(row=4,column=0,sticky=NSEW)

button = Button(wd, width=10, height=10,text="grow", bg='black')
button.place(relx=0.5,rely=0.5)

wd.configure(bg=dark)
wd.resizable(False,False)
wd.mainloop()