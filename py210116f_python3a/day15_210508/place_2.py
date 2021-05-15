"""
layout manager

place(width=a, height=b)

width and height can be both integer and floating number
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Python GUI - Layout place")
root.geometry("640x480+300+300")
root.config(bg="#ddddff")

# pictures
dog = ImageTk.PhotoImage(Image.open("img/dog.jpg"))
dog2 = ImageTk.PhotoImage(Image.open("img/dog2.jpg"))

# label1
label1 = Label(root, image=dog)
label1.place(x=20, y=20, width = 200, height = 200)

# label2
label2 = Label(root, image=dog2)
label2.place(x=300, y=200, width = 150, height = 150)


root.mainloop()


