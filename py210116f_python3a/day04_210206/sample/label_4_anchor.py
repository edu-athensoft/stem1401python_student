"""
create a label

anchor = 'nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se'
anchor = tk.N, tk.W, ....
"""

import tkinter as tk
# from tkinter import *

root = tk.Tk()
root.title('Python GUI - label')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')

# create a label
mytext = 'My Text Label 4'
label1 = tk.Label(root, text=mytext,
                  width=30, height=7,
                  bg='red', fg='#ffffff',
                  anchor='s')
label1.pack()

# create a label
mytext = 'My Text Label 4'
label2 = tk.Label(root, text=mytext,
                  width=30, height=7,
                  bg='blue', fg='#ffffff',
                  anchor=tk.W)
label2.pack()

root.mainloop()
