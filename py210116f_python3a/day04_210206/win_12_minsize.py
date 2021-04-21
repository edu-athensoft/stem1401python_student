"""
set max size for a window

"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - set min size for a window')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# case 1.
# w,h = root.minsize()
# print(w,h)

# case 2.
root.minsize(400,300)


root.mainloop()