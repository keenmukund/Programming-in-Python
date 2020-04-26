from tkinter import *
from tkinter import ttk
root=Tk()
Label(root,text="Name",relief=SOLID).pack()
Button(root,text="click me",relief=SOLID).pack()
def callback():
   print("click me")
Button(command=callback)
Label(root,text="label 1",relief=GROOVE).pack()
Label(root,text="label 2",relief=FLAT).pack()
s=StringVar()
Entry(root,textvariable=s).pack()
s.set("hello")
Text(root,height=20,width=20).pack()
canvas=Canvas(root,width=300,height=400,background="blue")
canvas.create_oval(10,10,100,100,fill="red")
canvas.pack()
