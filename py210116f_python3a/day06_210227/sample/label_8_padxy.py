"""
font in a label

padx = a
pady = b


"""

import tkinter as tk
# from tkinter import *

root = tk.Tk()
root.title('Python GUI - label')

winw= 800
winh= 600
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')

# create a label
mytext = 'My Text Label font'
label1 = tk.Label(root, text=mytext,
                  # width=30, height=3,
                  bg='red', fg='#ffffff',
                  font = 'Helvetica 20 italic underline',
                  padx = 20, pady= 10)
label1.pack()



root.mainloop()



