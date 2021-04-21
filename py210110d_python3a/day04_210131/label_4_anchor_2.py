"""
anchor of Label widget

anchor = n, s, w, e, ne, nw, se, sw, center

anchor= tk.N,tk.S,W,E,NE,NW,SE,SW,CENTER
"""

# import tkinter as tk

from tkinter import *

root = Tk()
root.title('Python GUI - Label')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddddff')

# create a Label
label1 = Label(root, text='My Text Label', width=50, height=3, anchor='nw')
label1.pack()

# create a Label
label2 = Label(root, text='My Text Label 2',width=30, height=5, anchor=NW)
label2.pack()

root.mainloop()