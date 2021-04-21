"""
create a label
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - subtopic')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')
# create a label

mytext = 'My Text Label 2'
label1 = tk.Label(root, text=mytext, width=30, height=7)

# label1 = tk.Label(root, text='My Text Label')
label1.pack()

root.mainloop()