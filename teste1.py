from tkinter import *

wd=Tk()
wd.title('teste')
wd.geometry('300x200')

users = []

nameL = Label(wd, text='Nome completo')
cpfL = Label(wd, text='cpf')
phoneL = Label(wd, text='Telefone')
emailL = Label(wd, text='Email')
passwordL = Label(wd, text='Senha')

nameE = Entry(wd, width=30)
cpfE = Entry(wd, width=30)
phoneE = Entry(wd, width=30)
emailE = Entry(wd, width=30)
passwordE = Entry(wd, width=30)

def createUser():
    name = nameE.get()
    cpf = cpfE.get()
    phone = phoneE.get()
    email = emailE.get()
    password = passwordE.get()
    users.append([name,cpf,phone,email,password])
    print(users)

def showUsers():
    count = 0
    alen = len(users)    
    while count <= alen:
        uFrame = Frame(wd)
        namec = Label(uFrame,text="nome: ".__add__(users[count][0]))
        namec.grid(row=1,column=1)
        cpfc = Label(uFrame,text="cpf: ".__add__(users[count][1]))
        cpfc.grid(row=2,column=1)
        phonec = Label(uFrame,text="phone: ".__add__(users[count][2]))
        phonec.grid(row=3,column=1)
        emailc = Label(uFrame,text="email: ".__add__(users[count][3]))
        emailc.grid(row=4,column=1)
        if count%3 == 0 :
            rowsum = count/2
        count += 1
    # for us in users:
    #     user = Label(wd,text=us)
    #     user.grid(row=2,column=3)



newUser = Button(wd,height='1',width='10',text='Create User', command=createUser)
show = Button(wd,height='1',width='10',text='Show users', command=showUsers)



nameL.grid(row=1,column=1)
cpfL.grid(row=2,column=1)
phoneL.grid(row=3,column=1)
emailL.grid(row=4,column=1)
passwordL.grid(row=5,column=1)
nameE.grid(row=1,column=2)
cpfE.grid(row=2,column=2)
phoneE.grid(row=3,column=2)
emailE.grid(row=4,column=2)
passwordE.grid(row=5,column=2)

newUser.grid(row=6,column=1)
show.grid(row=6,column=2)

wd.mainloop()