"""
[Homework]
Date: 2021-03-21
Create a window with two buttons
Click one for showing a text content using a label
Click the other one to exit
Due date: by the end of next Friday
"""

from tkinter import *


def response():
    print("I was clicked!")


root = Tk()
root.title('Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

btn1 = Button(root, text='Click me', command=response)
btn1.pack()

# btn2 = Button(root, text='Click me', command=root.destroy)
btn2 = Button(root, text='Exit', command=root.destroy)
btn2.pack()

root.mainloop()
