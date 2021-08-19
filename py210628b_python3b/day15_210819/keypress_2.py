"""
KeyPress
special key

<Escape>
<Control>
<Shift>

event.char

"""

from tkinter import *
from tkinter import messagebox


def press(event):
    flag = messagebox.askyesno('Exit', 'Do you really want to exit?')

    # flag == True
    if flag:
        root.destroy()
    else:
        return


root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# root
root.bind("<Escape>", press)

label1 = Label(root, text="test ESC key")
label1.pack(pady=50)

root.mainloop()
