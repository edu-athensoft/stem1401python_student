"""
set max size for a window

maxsize != maximize

"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - subtopic')

winw= 800
winh= 450
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')

# case 1.
root.maxsize()

# case 2.
root.maxsize(1000,600)

root.mainloop()