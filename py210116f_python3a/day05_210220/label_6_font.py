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
                  width=40, height=3,
                  bg="yellow",
                  anchor='w',
                  font="Helvetica 20 bold italic")
label1.pack()

# create a Label
label2 = tk.Label(root, text='My Text Label 2',
                  width=40, height=3,
                  bg="red", fg="white",
                  anchor='e',
                  font='"Courier New" 16 underline')
label2.pack()

# create a Label
label3 = tk.Label(root, text='My Text Label 3',
                  width=40, height=3,
                  bg="pink",
                  anchor='nw',
                  font = ("Times", 24, "normal", "roman","overstrike"))
label3.pack()

# create a Label
label4 = tk.Label(root, text='My Text Label 4',
                  width=40, height=3,
                  bg="blue", fg="yellow",
                  anchor=tk.SW,
                  font = ("Courier New", 24, "normal", "roman"))
label4.pack()


root.mainloop()
