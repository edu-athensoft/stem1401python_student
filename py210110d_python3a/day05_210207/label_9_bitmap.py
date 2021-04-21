"""
bitmap label
"""

import tkinter as tk
# from tkinter import *

root = tk.Tk()
root.title('Python GUI - label bitmap')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddddff')

# create a label
mytext = 'My Text Label bitmap'
label1 = tk.Label(root,
                  bg='red', fg='#ffffff',
                  bitmap='question',
                  padx = 20, pady= 15)
label1.pack()

mytext = 'My Text Label bitmap'
label1 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  bitmap='error',
                  padx = 20, pady= 15)
label1.pack()




root.mainloop()



