"""
set max size for a window
maxsize()
"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - set max size')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# mw,mh = root.maxsize()
# print(mw, mh)

root.maxsize(900,600)
# print()

root.mainloop()
