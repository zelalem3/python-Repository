from tkinter import *
windows = Tk()
windows.title("my first gui program")
windows.minsize(width=500, height=300)

my_label = Label(text="this is old text",font=("arial", 24, "bold"))
my_label.pack()
my_label.config(text="new text")

def action():
    print("do something")


button = Button(text="click me", command=action)
button.pack()
entry = Entry(width=30)
ntry.insert(END, string= "@gmail.com "e)
print(entry.get())
entry.pack()

text = Text(height=5, width=30)
text.focus()

text.insert(END, "example of multi-line text entry. ")


button.pack()

windows.mainloop()