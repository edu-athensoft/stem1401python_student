"""
[Homework]
Date: 2021-04-17
Please make a layout for the labels as above.
Due date: by the end of next Friday
"""
from tkinter import *

root = Tk()
root.title('Python GUI - pack anchor')
root.geometry('640x480+0+0')
root.config(bg='brown')

label1 = Label(root, text='Label 0,0',bg='yellow', font=('Arial', 20))
label2 = Label(root, text='Label 0,1', font=('Arial', 20))
label3 = Label(root, text='Label 1,0', font=('Arial', 20))
label4 = Label(root, text='Label 1,1',bg='yellow', font=('Arial', 20))

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

root.mainloop()