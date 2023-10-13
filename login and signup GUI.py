from tkinter import *
import os

creds='tempfile.temp'

def signup():
    global pwordE
    global nameE
    global roots

    roots = Tk()
    roots.title('Sign up')
    roots.geometry('500x500')
    instruction = Label(roots,text='Please Enter a new details\n',font=("Times New Roman",16))
    instruction.grid(row=0, column=125, sticky=NSEW)

    nameL = Label(roots, text='New username:',font=("Times New Roman",12))
    pwordl = Label(roots, text="New password:",font=("Times New Roman",12))
    nameL.grid(row=1,column=125,sticky=NSEW)
    pwordl.grid(row=2,column=125,sticky=NSEW)

    nameE = Entry(roots)
    pwordE= Entry(roots,show='*')
    nameE.grid(row=1,column=135)
    pwordE.grid(row=2, column=135)

    signupbutton = Button(roots, text='signup',font=("verdana",12),fg='black',bg='red', command= firstsignup)
    signupbutton.grid(columnspan=10, sticky=NSEW)
    roots.mainloop()

def firstsignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()

def Login():
    global pwordEL
    global nameEL
    global rootA 

    rootA = Tk()
    rootA.title('login')
    rootA.geometry('600x600')

    instruction = Label(rootA, text='please Login rasa\n',font=("Times New Roman",16))
    instruction.grid(sticky=E)

    nameL = Label(rootA, text='Username: ',font=("verdana",12))
    pwordL = Label(rootA, text='Password: ',font=("verdana",12))
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2,sticky=W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=2)
    pwordEL.grid(row=2,column=2)

    loginB = Button(rootA, text='Login',font=("verdana",12),fg="green", command=CheckLogin)
    loginB.grid(columnspan=2,sticky=NSEW)

    rmuser = Button(rootA, text='delete user',font=("verdana",12), fg='red', command=deluser)
    rmuser.grid(columnspan=2,sticky=NSEW)
    rootA.mainloop()

def CheckLogin():
    with open (creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.title(':datas')
        r.geometry('600x600')
        rlbl = Label(r, text='\n vaa arunachalam nee varuvenu teriyum!!',font=("Times New Roman",16),fg='brown',bg='White')
        rlbl.pack()
        r.mainloop()

def deluser():
    os.remove(creds)
    rootA.destroy()
    signup()

if os.path.isfile(creds):
    Login()
else:
    signup()

