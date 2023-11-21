from tkinter import *
import os
def restart():
    os.system("shutdown -r -t 1")

def restarttime():
    os.system("shutdown -r -t 20")

def shotdown():
    os.system("shutdown -s -t 1")


shawon = Tk()
shawon.title("Shut down app")
shawon.geometry("500x500")
shawon.config(bg="blue")

batton = Button(shawon,text="Restart",font=("arial",20,"bold",),bg="red",fg="black",cursor="plus",command=restart)
batton.place(x=150,y=60,width=200,height=50)

batton = Button(shawon,text="Restart time",font=("arial",20,"bold",),bg="red",fg="black",cursor="plus",command=restarttime)
batton.place(x=150,y=160,width=200,height=50)

batton = Button(shawon,text="Shut down",font=("arial",20,"bold",),bg="red",fg="black",cursor="plus",command=shotdown)
batton.place(x=150,y=260,width=200,height=50)

batton = Button(shawon,text="Close",font=("arial",20,"bold",),bg="red",fg="black",cursor="plus",command=shawon.destroy)
batton.place(x=150,y=360,width=200,height=50)

shawon.mainloop()