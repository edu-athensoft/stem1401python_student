"""
place a window to topmost

"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - place a window to topmost')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

root.attributes('-topmost',1)
root.attributes('-topmost',True)

root.mainloop()