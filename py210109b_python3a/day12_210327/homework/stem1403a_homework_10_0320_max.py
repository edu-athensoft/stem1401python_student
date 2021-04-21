"""
Homework 10
"""

from tkinter import *


def response():
    print("I was clicked!")


root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

btn1 = Button(root, text='Click me', command=response)
btn1.pack()

btn2 = Button(root, text='Click me', command=root.destroy)
btn2.pack()

root.mainloop()
