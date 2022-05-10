from tkinter import *
from tkinter.ttk import *

wd=Tk()
wd.title('aula 5')
wd.geometry('300x200')
wd.configure(bg='#b1d8ff')

combo = Combobox(wd)
combo['values'] = ['GO','RS','TO','MA']
combo.grid(row=1,column=1)



wd.mainloop()