"""
Tkinter
place a label widget
image label with .jpg

pillow - PIL

"""


from tkinter import *
from PIL import Image, ImageTk


root = Tk()

root.title('Python GUI - Label image')

# root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image in .jpg
myjpg = Image.open("./img/dog.jpg")
bgimg = ImageTk.PhotoImage(myjpg)

label1 = Label(root, image=bgimg)
label1.pack()


root.mainloop()
