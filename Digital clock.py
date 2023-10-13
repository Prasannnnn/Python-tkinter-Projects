from tkinter import *
from time import *
#download the pillow libraries
from PIL import ImageTk,Image
#Assign the tk Values in w
w=Tk()
w.title("Digital clock")
w.geometry("420x150")
w.resizable(1,1)
#give a correct path of image or else doesn’t work
img=ImageTk.PhotoImage(Image.open("Text.png"))
label=Label(image=img)
label.pack(padx=10)
#its an current time and date will work in the GUI
l= Label(w,font=("Times New roman",50,"bold"),bg="red",fg="black")
l.pack(padx=10)
#its an quotes 
l1=Label(w,font=("Times New Roman",50,"bold"),bg="black",fg="green")
l1.pack(padx=10)
log=Label(w,text="""Today is an New day,
                    Even if you were wrong yesterday,
                    you can get it right
                    today.""",font=("Times New Roman",35,"italic"),bg="brown",fg="white")
log.pack(pady=10)
#its updates the current date and time zones
def update():
    t=strftime("%H:%M:%S:%p")
    l.config(text=t)
    t1=strftime("%c")
    l1.config(text=t1)
    w.after(1000,update)
#call the main functions
update()
mainloop()
