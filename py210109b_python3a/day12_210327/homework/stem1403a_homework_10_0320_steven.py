"""
Create a window with two buttons
Click one for showing a text content using a label
Click the other one to exit
Due date: by the end of next Friday

"""

from tkinter import *


def response():
    a = Label(root, text = "I was clicked", bg="yellow", font="Helvetica 10")
    a.pack(pady=2)


# main program
root = Tk()
root.geometry("640x480+300+300")
root.title("Python Buttons")
root.config(bg="#dddfff")

btn1 = Button(root, text="Click me",font="Helvetica 20 bold", bg="cyan", command=response, width=10, height=1)
btn1.pack()

btn2 = Button(root, text="Exit", font="Helvetica 13 bold", bg ="cyan", command=root.destroy)
btn2.pack(pady=10)

root.mainloop()

