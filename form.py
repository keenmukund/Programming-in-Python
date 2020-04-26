from tkinter import *
from tkinter import ttk

class xyz:
   def __init__():
      
      root=Tk()
      lab1=ttk.Label(root,text="Username")
      lab1.pack()
      e1=ttk.Entry(root)
      e1.pack()
      lab2=ttk.Label(root,text="Password")
      lab2.pack()
      e2=ttk.Entry(root)
      e2.pack()

      s1=StringVar()
      s1=e1.get()
      button1=ttk.Button(root,text="Submit")
      button1.pack()

   def callback(self):
      print(s1)
        

