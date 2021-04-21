"""
[Homework]
Date: 2021-03-21
Create a window with two buttons
Click one for showing a text content using a label
Click the other one to exit
Due date: by the end of next Friday
"""

from tkinter import *


def btn1_clicked():
    label.pack()


root = Tk()
root.title('Python GUI - Button')
root.geometry("800x450")
root.configure(bg='#ddddff')

label = Label(text="Button 1 was clicked")

#
btn1 = Button(root, text='Click me!', command=btn1_clicked)
btn1.pack(padx=20, pady=40)

#
btn2 = Button(root, text='Close', command=root.destroy)
btn2.pack(padx=20, pady=40)

root.mainloop()
