"""
[Homework]
Date: 2021-02-14
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create at least 2 text Labels
set dimension, font, fg, bg, font and any other options you know.
create at least 3 image Labels
one for gif, one for png, another one for jpg
set dimension, fg, bg, font and any other options you know.
"""

"""
score:
perfect

"""

import tkinter as tk
from PIL import Image, ImageTk


# window
root = tk.Tk()
root.title('Python GUI - Homework')

winw = 1440
winh = 1080
posx = 300
posy = 200
root.geometry("{}x{}+{}+{}".format(winw, winh, posx, posy))
# root.iconbitmap("IMG_2408.icns")
root.config(bg="white")
root.maxsize()
root.minsize(300, 200)
root.attributes('-topmost', True)
root.resizable(1, 1)

# label
label1 = tk.Label(root, text='Label 1', height=7, width=20, anchor=tk.CENTER, bg="red", fg="yellow", wraplength=80)
label1.pack()

label2 = tk.Label(root, text='Label 2', height=2, width=30, anchor=tk.NW, bg="blue", fg="green", wraplength=70)
label2.pack()

photo_obj = tk.PhotoImage(file= "img/gif.gif")
label3 = tk.Label(root, image=photo_obj, height=200, width=400, bg="gold", fg="white")
label3.pack()

photo_obj = tk.PhotoImage(file= "img/png.png")
label4 = tk.Label(root, image=photo_obj, height=200, width=400, bg="gold", fg="white")
label4.pack()

img_obj = Image.open('./img/jpg.jpg')

bgimg = ImageTk.PhotoImage(img_obj)

label5 = tk.Label(root, image=bgimg, height=200, width=400, bg="gold", fg="white")
label5.pack()

root.mainloop()