import tkinter as tk
from tkinter import ttk
win=tk.Tk()
#win.resizeable(0,0)
win.title("First GUI")

label1=ttk.Label(win,text="Label")
label1.grid(column=0,row=0)
def clicked():
    action.configure(text="Clicked")
    label1.configure(foreground="blue")
    label1.configure(text="hello" +name.get() )

name=tk.StringVar()
nameEntered=ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()                #places cursor int text entry box

chVarDis=tk.IntVar()               #holds state of checkbutton
check1=tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=2)

chVarUn=tk.IntVar()               #holds state of checkbutton
check2=tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=2)

chVarEn=tk.IntVar()               #holds state of checkbutton
check3=tk.Checkbutton(win, text="Checked", variable=chVarEn)
check3.select()
check3.grid(column=2, row=2)

action=ttk.Button(win,text="Click Me",command=clicked)
action.grid(column=1,row=1)
action.configure(state="disabled")  #disables the widget


win.mainloop()
