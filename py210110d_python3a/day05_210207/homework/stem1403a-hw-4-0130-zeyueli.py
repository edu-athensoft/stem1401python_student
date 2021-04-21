"""
[Homework]
Date: 2021-01-30
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create a text Label
set dimension, font, fg, bg, font and any other options which are necessary you think.
"""

"""
score
invalid char in file name (-1)

"""

import tkinter as tk

# window
root = tk.Tk()
root.title('Python GUI - Homework')

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry("{}x{}+{}+{}".format(winw, winh, posx, posy))
# root.iconbitmap("IMG_2408.icns")
root.config(bg="gold")
root.maxsize()
root.minsize(300, 200)
root.attributes('-topmost', True)
root.resizable(1, 1)

# label
label1 = tk.Label(root, text='Label 1', height=7, width=20, anchor=tk.CENTER, bg="red", fg="yellow", wraplength=80)
label1.pack()

root.mainloop()