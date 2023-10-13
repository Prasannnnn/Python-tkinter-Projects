from tkinter import *
import qrcode
#assign tk
root=Tk()
root.title("QR Code Generator")
root.geometry("1000x550")
root.config(bg="light blue")
root.resizable(False,False)
#image icon in the windows
image_icon=PhotoImage(file="Robomatiic.PNG")
root.iconphoto(False,image_icon)
#generate a QR code
def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("qrcode/"+str(name)+".png")
#it will show the QR Code
    global Image
    Image=PhotoImage(file="qrcode/"+str(name)+".png")
    image_view.config(image=Image)
#its view of image Layout in the Label
image_view=Label(root,bg="yellow")
image_view.pack(padx=50,pady=10,side=RIGHT)
#title of the mentioned
Label(root,text="Title",fg="white",bg="black",font=15).place(x=50,y=170)
#entry field
title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)
#entry what you want to show in QR code
entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=250)
#generate Button
Button(root,text="Generate ",width=20,height=2,bg="blue",fg="white",command=generate).place(x=50,y=300)


mainloop()