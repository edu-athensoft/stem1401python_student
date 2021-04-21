"""
score
missing main function        (-10)
missing docstring of comment (-5)
improper file name (-1)

"""

import tkinter as tk
root = tk.Tk()
root.title("python GUI")
# root.iconbitmap("pkcoddomdv.ico")

root.configure(bg='#ddddff')

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

ww = 800
wh = 450

posx = int(sw/2 - ww/2)
posy = int(sh/2 - wh/2)

root.geometry(f"{ww}x{wh}+{posx}+{posy}")

root.mainloop()
