"""
to set image icon

ico - special image format
.ico

.jpg
.png
.bmp
.gif

get an image file (in gif, png, jpg)
convert image to ico

"""


import tkinter as tk
# from tkinter import *

root = tk.Tk()

root.title('Python GUI - Position')

# set position
# root.geometry('800x450')
# root.geometry('800x450+300+200')
root.geometry('800x450-300+200')
# root.geometry('800x450-300-200')

root.iconbitmap('img/IMG_2408.ico')

root.mainloop()
