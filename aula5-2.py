from tkinter import *
from tkinter.ttk import *

wd=Tk()
wd.title('aula 5')
wd.geometry('300x200')
wd.configure(bg='#b1d8ff')

estado = StringVar()

def test():
    print('uai zé tô', estado.get())

check = Checkbutton(wd,text='eae zé?bão ou não?',var=estado,
                            onvalue="bão",offvalue="não",command=test)
check.grid(row=1,column=1)



wd.mainloop()