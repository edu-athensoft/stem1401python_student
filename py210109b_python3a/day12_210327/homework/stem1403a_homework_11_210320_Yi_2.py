"""
Homework 10
"""

from tkinter import *


def response():
    print("Hallo welcome!")


def close():
    root.destroy()


root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+200+200')
# root.geometry('+400+300')
# root.config(bg='#ddddff')


btn1 = Button(root, text='Click me', command=response)
btn1.pack()

btn2 = Button(root, text='Exit', command=close)
btn2.pack()

root.mainloop()