"""
window iconify
"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - iconify')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

root.update()

time.sleep(2)

# set iconify
root.iconify()

root.mainloop()