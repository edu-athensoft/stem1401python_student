"""
bitmap label
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
label1 = tk.Label(root,bg='yellow',text=mytext, bitmap = 'error',padx = 20, pady= 10, fg='blue', font='40')
label1.pack()



root.mainloop()



