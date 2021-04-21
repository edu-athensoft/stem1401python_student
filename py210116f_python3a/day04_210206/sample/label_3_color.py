"""
create a label
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - label')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')
# create a label

mytext = 'My Text Label 3'
label1 = tk.Label(root, text=mytext, width=30, height=7, bg='red', fg='#ffffff')
label1.pack()

root.mainloop()
