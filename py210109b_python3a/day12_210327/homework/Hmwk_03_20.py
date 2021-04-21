from tkinter import *

from PIL import Image, ImageTk


def response():
    print("I was clicked!")

root = Tk()
root.title('Python GUI - Button')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')


class ImageTk():
    pass

label1 = Label(root, text='Label 1')


img = ImageTk.PhotoImage(Image.open("img/IMG1.jpg"))

btn1 = Button(root, text='Click me', command=response)

btn1.pack

label1.grid(row=2)
p2 = Label(root,image = img)


p2.place(x=300, y=200, width=150, height = 150)

btn2 = Button(root, text='Exit', command=root.destroy)

btn2.pack

mainloop()