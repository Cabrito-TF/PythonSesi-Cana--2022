from tkinter import *
from tkinter import messagebox

wd = Tk()
wd.title('Calculadora')
wd.geometry("350x200")
wd.configure(bg="#000")
wd.resizable(False,False)

title = Label(wd, text='Super calculadora 3000', fg="#fff",bg="#000", font=("Arial",18))
title.place(relx=0.5,y=10,anchor='c')

calc = Frame(wd,width=500,height=500,bg="#ddd")
calc.place(relx=0.5,y=50,anchor="n")

num1 = Entry(calc,width=50,state="normal",justify="right",textvariable=IntVar)
num1.grid(column=0,columnspan=4,row=0)
num2 = Entry(calc,width=50,state="normal",justify="right",textvariable=IntVar)
num2.grid(column=0,columnspan=4,row=1)


def soma():
  try:
    a = int(num1.get())
    b = int(num2.get())
    c = a+b
    messagebox.showinfo("result", "Resultado:".__add__(str(c)))
  except:
    messagebox.showerror("inválido", "porfavor insira um número válido")

def sub():
  try:
    a = int(num1.get())
    b = int(num2.get())
    c = a-b
    messagebox.showinfo("result", "Resultado:".__add__(str(c)))
  except:
    messagebox.showerror("inválido", "porfavor insira um número válido")

def mult():
  try:
    a = int(num1.get())
    b = int(num2.get())
    c = a*b
    messagebox.showinfo("result", "Resultado:".__add__(str(c)))
  except:
    messagebox.showerror("inválido", "porfavor insira um número válido")

def div():
  try:
    a = int(num1.get())
    b = int(num2.get())
    c = a/b
    messagebox.showinfo("result", "Resultado:".__add__(str(c)))
  except:
    messagebox.showerror("inválido", "porfavor insira um número válido")

nplus = Button(calc,width=10,height=1,text="+",command=soma)
nminus = Button(calc,width=10,height=1,text="-",command=sub)
ntimes = Button(calc,width=10,height=1,text="*",command=mult)
ndiv = Button(calc,width=10,height=1,text="/",command=div)

nplus.grid(column=0,row=2)
nminus.grid(column=1,row=2)
ntimes.grid(column=2,row=2)
ndiv.grid(column=3,row=2)

wd.mainloop()