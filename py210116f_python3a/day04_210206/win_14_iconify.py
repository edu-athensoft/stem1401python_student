"""
iconify
"""

import tkinter as tk
import time


root = tk.Tk()
root.title('Python GUI - subtopic')

winw=800
winh=450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# refreshing
root.update()

time.sleep(3)

root.iconify()

root.mainloop()
