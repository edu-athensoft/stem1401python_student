"""
set resizable for a window

"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - Resizable')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# root.resizable(True, True)
# root.resizable(True, False)
# root.resizable(False, True)
root.resizable(False, False)


root.mainloop()