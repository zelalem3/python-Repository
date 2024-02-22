from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import time
tkinter = Tk()
frm = ttk.Frame(tkinter, padding=10)
frm.grid()
ttk.Label(frm, text="this is the text to write down").grid(column=0, row=0)
ttk.Button(frm, text="Finished", command=tkinter.destroy).grid(column=1, row=0)




name = simpledialog.askstring("Enter the text", "Type here")

print("Your name:", name)

tkinter.mainloop()