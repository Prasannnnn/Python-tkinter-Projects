from tkinter import *
import random
#assign tk values
root=Tk()
root.geometry("5000x600")
root.title("Number Generator")

#frame work
tops = Frame(root,height=50,relief=SUNKEN)
tops.pack(side=TOP, fill=X)
#label
labelinfo = Label(tops, font=('verdana',30,"bold"),text="Number Generator",fg="black",bd=10,anchor="w")
labelinfo.pack(pady=10)
#framework in the windows
l1=Frame(root,width=900,height=700,relief=SUNKEN)
l1.pack(padx=5)
#label Framework 
labell=Label(root,font=('verdana',30,"bold"),text="Number Gen",fg="brown",bd=20,anchor="w")
labell.pack(pady=5)

rand = StringVar()
textid=Entry(l1,font=("verdana",30,"bold"),textvariable=rand,bd=6,insertwidth=6,bg="yellow",justify="right")
textid.pack(padx=10)
#reference for number generating
def ref():
    x=random.randint(0,10)
    randomref=x
    randomref=x*randomref
    rand.set(randomref)

button = Button(l1,pady=0,bd=0,fg="black",font=("verdana",30,"bold"),width=10,text="generate",bg="blue",command=ref)
button.pack(padx=10,pady=20)

root.mainloop()