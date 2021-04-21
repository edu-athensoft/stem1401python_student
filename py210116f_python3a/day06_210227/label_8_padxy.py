"""
padx and pady in a label

padx = a
pady = b
"""

import tkinter as tk
# from tkinter import *

root = tk.Tk()
root.title('Python GUI - label')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')

# create a label
mytext = 'My Text Label font'
label1 = tk.Label(root, text=mytext,
                  # width=30, height=3,
                  bg='red', fg='#ffffff',
                  font = 'Helvetica 20',
                  padx = 40, pady= 20)
label1.pack()


label2 = tk.Label(root, text=mytext,
                  # width=30, height=3,
                  bg='blue', fg='#ffffff',
                  font = 'Helvetica 10',
                  padx = 40, pady= 20)
label2.pack()

root.mainloop()



