from tkinter import *
#install the libraries pillow
from PIL import Image,ImageTk
#assign tk 
root=Tk()
root.title("Toggle Switch")
#assign Geometry
root.geometry("400x600")
root.config(bg="white")
#button 
button_mode=True

def customize():
    global button_mode

    if button_mode:
        button.config(image=off,bg="black",activebackground="black")
        root.config(bg="black")
        button_mode=False
    else:
        button.config(image=on,bg="white",activebackground="white")
        root.config(bg="white")
        button_mode=True      


on=ImageTk.PhotoImage(file="light.jpg")
off=ImageTk.PhotoImage(file="dark.jpg")

button=Button(root,image=on,bd=0,bg="white",activebackground="white",command=customize)
button.pack(padx=50,pady=50)


root.mainloop()