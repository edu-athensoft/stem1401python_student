"""
set max size for a window

"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - set max size for a window')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# case 1.
w,h = root.maxsize()
print(w,h)

# case 2.
root.maxsize(900,600)


root.mainloop()