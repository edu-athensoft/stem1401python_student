"""
[Homework]
Date: 2021-03-21
Create a window with two buttons
Click one for showing a text content using a label
Click the other one to exit
Due date: by the end of next Friday
"""
from tkinter import *
### import datetime


def myresponse():
    label_text = Label(root, text='i was clicked!')
    label_text.pack()


root = Tk()
root.title('button homework')
root.geometry('640x480+200+200')
root.config(bg='#ddddff')

btn1 = Button(root,text='CLICK ME!', command=myresponse)
btn2 = Button(root,text='close', command=root.destroy)

btn1.pack()
btn2.pack()

root.mainloop()
