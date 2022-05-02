from tkinter import RAISED

from tkinter import *
import tkinter

top = tkinter.Tk()

B1 = tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="sizing")
B2 = tkinter.Button(top, text ="plus", relief=RAISED,\
                         cursor="plus")
B1.pack()
B2.pack()
top.mainloop()