"""
grid layout manager
"""

from tkinter import *


root = Tk()
root.geometry('640x480+200+200')
root.config(bg='#ddddff')

# create label widgets
label1 = Label(root, text='Label 1')
label2 = Label(root, text='Label 2')
label3 = Label(root, text='Label 3')
label4 = Label(root, text='Label 4')
label5 = Label(root, text='Label 5')


# show on screen
# column number is 0 by default
label1.grid()
label2.grid(row=1)
label3.grid(row=2)
label4.grid(row=3)
label5.grid(row=4)


root.mainloop()