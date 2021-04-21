"""
create a Label widget
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Label')

winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# create a Label
label1 = tk.Label(root, text='My Text Label')

label1.pack()

root.mainloop()