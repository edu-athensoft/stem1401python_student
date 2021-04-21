"""
center your window
"""


import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Centering window')

winwidth = 800
winheight = 450

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = int(screenwidth/2 - winwidth/2)
y = int(screenheight/2 - winheight/2)

root.geometry(f"{winwidth}x{winheight}+{x}+{y}")

root.mainloop()
