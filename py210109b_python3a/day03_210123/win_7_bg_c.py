"""
set background color

color value
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - background color')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

root.configure(bg='tomato')

root.mainloop()