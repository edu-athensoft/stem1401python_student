"""
stem1403a_homework_5_0206_steven
"""

"""
score
wrong docstring (-5)

"""

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
root = tk.Tk()

root.title("Python GUI - Title")

# root.iconbitmap('')
windw = 800
windh = 450

x = int(root.winfo_screenwidth()/2 - 800/2)
y = int(root.winfo_screenheight()/2 - 450/2)
root.geometry("{}x{}+{}+{}".format(800,450,x,y))
root.configure(bg='cyan')
root.attributes('-topmost',1)
root.resizable(False, False)
root.update()
print(f"The window has a height of {root.winfo_height()} and a width of {root.winfo_width()}")
root.configure(bg='#ddff77')


label1 = tk.Label(root, bg='blue', padx = 20, pady = 10, text="mylabel1", compound = "left", bitmap="error")
label1.pack()
bgimg = PhotoImage(file='./img/pimon.gif')
label1 = Label(root, image=bgimg)
label1.pack()





root.mainloop()