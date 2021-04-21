"""
Layout manager:  pack()

-after, -anchor, -before, -expand, -fill,
-in, -ipadx, -ipady, -padx, -pady, -side
"""


from tkinter import *


root = Tk()

label1 = Label(root, text='Python 1')
label2 = Label(root, text='Java 2')
label3 = Label(root, text='Web 3')
label4 = Label(root, text='Database 4')

root.geometry('640x480+0+0')
root.config(bg='#ddddff')

label4.pack()
label1.pack()
label2.pack()
label3.pack()


root.mainloop()

