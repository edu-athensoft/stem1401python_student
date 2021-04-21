#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Tkinter
Button &  MessageBox
click and response

lambda
"""


from tkinter import *
from tkinter import messagebox as msg


def helloCallBack():
   msg.showinfo( "Hello Python", "Hello Athensoft!")


root = Tk()
root.title('Python GUI - Button and Response')
root.geometry('300x200')

# option 1. lambda
btn1 = Button(root, text='Confirm', command=lambda:helloCallBack())
btn1.pack()

# option 2. function name
btn2 = Button(root, text='OK', command=helloCallBack)
btn2.pack()

root.mainloop()
