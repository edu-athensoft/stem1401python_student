"""
label anchor
anchor = {'w','e','s','n','nw','ne','sw','se','center'}
anchor = {W, E, S, ...}
"""

import tkinter as tk

# from tkinter import *


root = tk.Tk()
root.title('Python GUI - Label anchor')

winw=800
winh=450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddddff')

# create a Label
label1 = tk.Label(root, text='My Text Label 1',
                  width=40, height=7,
                  bg="yellow",
                  anchor='w')
label1.pack()

# create a Label
label2 = tk.Label(root, text='My Text Label 2',
                  width=40, height=5,
                  bg="red", fg="white",
                  anchor='e')
label2.pack()

# create a Label
label3 = tk.Label(root, text='My Text Label 3',
                  width=40, height=5,
                  bg="pink",
                  anchor='nw')
label3.pack()

# create a Label
label4 = tk.Label(root, text='My Text Label 4',
                  width=40, height=5,
                  bg="blue", fg="yellow",
                  anchor=tk.SW)
label4.pack()


root.mainloop()
