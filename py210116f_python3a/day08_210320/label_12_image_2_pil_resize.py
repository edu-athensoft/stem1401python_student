"""
how to resize an image

"""
from tkinter import *
from PIL import Image, ImageTk
# import tkinter as tk


def resize(w, h, image):
    factor = 0.3
    width = int(w * factor)
    height = int(h * factor)
    return image.resize((width, height), Image.ANTIALIAS)


# main program
root = Tk()

root.title("Python GUI - Homework images")

window_width = 1200
window_height = 675

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = int(screenwidth/2 - window_width/2)
y = int(screenheight/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.config(bg="#ddddff")

# get image
# img1 = PhotoImage(file='./Samoyed.png')
img1 = Image.open(r'./img/dog.jpg')
w, h = img1.size
print(w,h)

# image size
img1 = resize(w, h, img1)

# convert image type
myimg = ImageTk.PhotoImage(img1)
label1 = Label(root, width=1100, height=600, bg="red4", image=myimg)
label1.pack()

root.mainloop()

